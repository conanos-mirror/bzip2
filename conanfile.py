import os
import shutil

from conans import CMake, tools
from conans import ConanFile
from conanos.build import config_scheme


class Bzip2Conan(ConanFile):
    name = "bzip2"
    version = "1.0.6"
    branch = "master"
    generators = "cmake"
    settings = "os", "compiler", "arch", "build_type"
    options = {"shared": [True, False]}
    default_options = "shared=True"
    exports = ["LICENSE"]
    exports_sources = ["CMakeLists.txt"]
    url = "https://github.com/lasote/conan-bzip2"
    license = "BSD-style license"
    description = "bzip2 is a freely available, patent free (see below), high-quality data " \
                  "compressor. It typically compresses files to within 10% to 15% of the best" \
                  " available techniques (the PPM family of statistical compressors), whilst " \
                  "being around twice as fast at compression and six times faster at decompression."

    source_subfolder = "source_subfolder"

    @property
    def zip_folder_name(self):
        return "bzip2-master"

    def configure(self):
        del self.settings.compiler.libcxx
        config_scheme(self)

    def source(self):
        RC = 'rc4'
        url = "https://github.com/mingyiz/bzip2/archive/%s-%s.tar.gz"%(self.version,RC)
        tools.get(url)
        os.rename("bzip2-%s-%s"%(self.version,RC) ,self.source_subfolder)

        os.rename(os.path.join(self.source_subfolder, "CMakeLists.txt"),
                  os.path.join(self.source_subfolder, "CMakeListsOriginal.txt"))
        shutil.copy("CMakeLists.txt",
                    os.path.join(self.source_subfolder, "CMakeLists.txt"))

    def build(self):
        cmake = CMake(self)
        cmake.configure(source_folder=self.source_subfolder)
        cmake.build()
        cmake.test()
        cmake.install()

    def package(self):
        # remove binaries
        for bin_program in ['bzip2', 'bzip2recover']:
            for ext in ['', '.exe','.js']:
                try:
                    os.remove(os.path.join(self.package_folder, 'bin', bin_program+ext))
                except:
                    pass

        #self.copy("bzlib.h", "include", "%s" % self.zip_folder_name, keep_path=False)
        #self.copy("*bzip2", dst="bin", src=self.zip_folder_name, keep_path=False)
        #self.copy(pattern="*.so*", dst="lib", src=self.zip_folder_name, keep_path=False)
        #self.copy(pattern="*.dylib", dst="lib", src=self.zip_folder_name, keep_path=False)
        #self.copy(pattern="*.a", dst="lib", src="%s/_build" % self.zip_folder_name, keep_path=False)
        #self.copy(pattern="*.lib", dst="lib", src="%s/_build" % self.zip_folder_name, keep_path=False)
        #self.copy(pattern="*.dll", dst="bin", src="%s/_build" % self.zip_folder_name, keep_path=False)

        pc_content ='''
        prefix={prefix}
        exec_prefix=${{prefix}}
        libdir=${{prefix}}/lib
        toolexeclibdir=${{prefix}}/lib
        includedir=${{prefix}}/include
        
        Name: {name}
        Description: {description}
        Version: {version}
        Libs: -L${{toolexeclibdir}} -lbz2
        Cflags: -I${{includedir}}
        '''
        
        tools.save('%s/lib/pkgconfig/%s.pc'%(self.package_folder, self.name),
        pc_content.format(prefix=self.package_folder, name=self.name, version=self.version, description=self.description))

        tools.save('%s/lib/pkgconfig/bz2.pc'%(self.package_folder),
        pc_content.format(prefix=self.package_folder, name=self.name, version=self.version, description=self.description))

    def package_info(self):
        self.cpp_info.libs = ['bz2']
