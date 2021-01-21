from setuptools import setup, find_packages

setup(
    name='pyrobotdesign-env',
    version='0.1.0',
    packages=[
        'pyrobotdesign_env', 
        'pyrobotdesign_env.environments',
        'pyrobotdesign_env.common',
        'pyrobotdesign_env.simulation',
        ],
)
