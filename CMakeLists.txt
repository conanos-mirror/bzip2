cmake_minimum_required(VERSION 3.0)
project(cmake_wrapper)

include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
conan_basic_setup()

set(TEST_SEARCH_FOLDERS "${CMAKE_BINARY_DIR}/bin")
include(CMakeListsOriginal.txt)
