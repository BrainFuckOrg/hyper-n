cmake_minimum_required(VERSION 3.24)
project(hyper_n C)

set(CMAKE_C_STANDARD 11)

add_executable(hyper_n main.c hyperLibMax.c hyperLibMax.h cmake-build-debug/hyperLibSanya.c cmake-build-debug/hyperLibSanya.h)
