cmake_minimum_required(VERSION 3.0)
project(cmake_wrapper)

include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
conan_basic_setup()

set(TEST_PROBE_DIRS ${CMAKE_RUNTIME_OUTPUT_DIRECTORY})
message("1) TEST_PROBE_DIRS:${TEST_PROBE_DIRS}")
include(CMakeListsOriginal.txt)
