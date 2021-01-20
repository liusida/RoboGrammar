cmake_minimum_required(VERSION 3.0)

project(RobotDesign)

if (DEFINED OPENGL)
else()
    set(OPENGL 0)
endif()

# Use double precision in Bullet
add_compile_options(-DBT_USE_DOUBLE_PRECISION)

add_subdirectory(core)
add_subdirectory(examples/python_bindings)
if (${OPENGL})
    message("\nCompile with OpenGL\n")
    add_subdirectory(examples/rule_viewer)
endif()

file(COPY ${PROJECT_SOURCE_DIR}/data DESTINATION ${CMAKE_BINARY_DIR})
