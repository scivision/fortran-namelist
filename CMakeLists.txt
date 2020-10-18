cmake_minimum_required(VERSION 3.12)
project(nml LANGUAGES Fortran)

include(CTest)

add_executable(read read.f90)
add_test(NAME NamelistRead COMMAND $<TARGET_FILE:read>
WORKING_DIRECTORY ${CMAKE_CURRENT_SOURCE_DIR})

find_package(Matlab COMPONENTS MAIN_PROGRAM)
if(Matlab_FOUND)
add_test(NAME Matlab COMMAND ${Matlab_MAIN_PROGRAM} -batch "r = runtests('.'); assertSuccess(r)"
WORKING_DIRECTORY ${CMAKE_CURRENT_SOURCE_DIR})
endif()

find_package(Python3 COMPONENTS Interpreter)
if(Python3_FOUND)
add_test(NAME Python COMMAND ${Python3_EXECUTABLE} -m pytest
WORKING_DIRECTORY ${CMAKE_CURRENT_SOURCE_DIR})
endif()
