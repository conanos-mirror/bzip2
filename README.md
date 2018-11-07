| Windows | Linux |
|:------:|:------:|
| [![Windows Build Status](https://ci.appveyor.com/api/projects/status/github/conanos/bzip2?svg=true)](https://ci.appveyor.com/project/Mingyiz/bzip2-qo8a3) |[![Linux Build Status](https://api.travis-ci.org/conanos/bzip2.svg)](https://travis-ci.org/conanos/bzip2)|
# conan-bzip2

Conan package for BZip2 library. http://www.bzip.org/

The packages generated with this **conanfile** can be found in [Bintray](https://bintray.com/conan-community/conan/bzip2%3Aconan).

## Basic setup

    $ conan install bzip2/1.0.6@conanos/stable

## Project setup

If you handle multiple dependencies in your project is better to add a *conanfile.txt*

    [requires]
    bzip2/1.0.6@conanos/stable

    [options]
    bzip2:shared=true # false

    [generators]
    cmake

Complete the installation of requirements for your project running:</small></span>

    conan install . 

Project setup installs the library (and all his dependencies) and generates the files *conanbuildinfo.cmake* with all the 
paths and variables that you need to link with your dependencies.
