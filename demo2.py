# require stable-baselines3
# pip install stable-baselines3
import gym
import pyrobotdesign as rd
import pyrobotdesign_env

from stable_baselines3 import PPO
from stable_baselines3.common.vec_env import DummyVecEnv, VecNormalize

def make_env():
    def _init():
        env = gym.make("RobotLocomotion-v0")
        return env

    return _init

env = DummyVecEnv([make_env()])
# env.render()

model = PPO("MlpPolicy", env, tensorboard_log="tb", verbose=True)

model.learn(total_timesteps=1e6)

model.save("default")