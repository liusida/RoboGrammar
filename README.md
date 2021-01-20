# Compile without OpenGL

HPC clusters usually don't have OpenGL support, so this repository shows how to install pyrobotdesign without OpenGL.

First, make sure you have a new version of GCC/G++. Most HPC servers have a very old version (such as 4.8 in my case) of GCC. You need to compile from source to get a new version (such as 8.3) if you don't have the root priviledge.

Second, pick a virtual environment, software authors suggest `virtualenv`, but `conda` works perfectly fine for me.

```
(venv) /path/to/RoboGrammar $ export CC=/path/to/your/gcc CXX=/path/to/your/g++
(venv) /path/to/RoboGrammar $ mkdir build; cd build; cmake -DCMAKE_BUILD_TYPE=Release ..; make -j8; cd ..
(venv) /path/to/RoboGrammar $ python3 examples/design_search/setup.py develop
(venv) /path/to/RoboGrammar $ python3 build/examples/python_bindings/setup.py develop
(venv) /path/to/RoboGrammar $ python demo0.py
```

# RL package

This repo also demostrates how to make use of the RL package in the `examples` folder.

```shell
(venv) /path/to/RoboGrammar $ cd examples/rl
(venv) /path/to/RoboGrammar/examples/rl $ pip install -e .
(venv) /path/to/RoboGrammar/examples/rl $ cd ..
(venv) /path/to/RoboGrammar $ python demo1.py
```
