#include <pybind11/pybind11.h>

namespace py = pybind11;

void initEigenGeometry(py::module &m);
void initGraph(py::module &m);
void initOptim(py::module &m);
void initProp(py::module &m);
#ifdef USE_OPENGL
  void initRender(py::module &m);
#endif
void initRobot(py::module &m);
void initSim(py::module &m);
void initValue(py::module &m);

PYBIND11_MODULE(pyrobotdesign, m) {
  initEigenGeometry(m);
  initGraph(m);
  initOptim(m);
  initProp(m);
#ifdef USE_OPENGL
  initRender(m);
#endif
  initRobot(m);
  initSim(m);
  initValue(m);
}
