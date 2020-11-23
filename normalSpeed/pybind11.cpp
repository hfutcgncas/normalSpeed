#include <pybind11/pybind11.h>
#include <pybind11/stl.h>
#include "np2mat/ndarray_converter.h"
#include "normal.hpp"
namespace py = pybind11;

PYBIND11_MODULE(normalSpeed, m) {
    NDArrayConverter::init_numpy();
    m.def("depth_normal", &depthNormals, "A function get normal of depth");
}
