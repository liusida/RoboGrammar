# Origin

This repository is forked from [allanzhao/RoboGrammar](https://github.com/allanzhao/RoboGrammar)

# Compile without OpenGL

HPC clusters usually don't have OpenGL support, so this repository shows how to install pyrobotdesign without OpenGL.

First, make sure you have a new version of GCC/G++. Most HPC servers have a very old version (such as 4.8 in my case) of GCC. You need to compile from source to get a new version (such as 8.3) if you don't have the root priviledge.

Second, pick a virtual environment, software authors suggest `virtualenv`, but `conda` works perfectly fine for me.

```
(venv) /path/to/RoboGrammar $ export CC=/path/to/your/gcc CXX=/path/to/your/g++
(venv) /path/to/RoboGrammar $ mkdir build; cd build
(venv) /path/to/RoboGrammar/build $ cmake -DCMAKE_BUILD_TYPE=Release ..
(venv) /path/to/RoboGrammar/build $ make -j8
(venv) /path/to/RoboGrammar/build $ cd ..
(venv) /path/to/RoboGrammar $ python3 examples/design_search/setup.py develop
(venv) /path/to/RoboGrammar $ python3 build/examples/python_bindings/setup.py develop
(venv) /path/to/RoboGrammar $ python demo0.py
```

Of course you can bring back OpenGL support by changing the third command above to 
```
cmake -DOPENGL=1 -DCMAKE_BUILD_TYPE=Release ..
```

We love visual clues!

# RL package

This repo also demostrates how to make use of the RL package in the `examples` folder.

```shell
(venv) /path/to/RoboGrammar $ cd examples/rl
(venv) /path/to/RoboGrammar/examples/rl $ pip install -e .
(venv) /path/to/RoboGrammar/examples/rl $ cd ..
(venv) /path/to/RoboGrammar $ python demo1.py
```

If you compile with OpenGL support, you can enable `env.render()` to see the training robot.
