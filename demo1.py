import sys
import gym
import environments
from train.utils import solve_argv_conflict
from train.arguments import get_parser
import pyrobotdesign as rd

args_list = ['--env-name', 'RobotLocomotion-v0',
                '--task', 'RidgedTerrainTask',
                '--grammar-file', 'data/designs/grammar_apr30.dot',
                '--algo', 'ppo',
                '--use-gae',
                '--log-interval', '5',
                '--num-steps', '1024',
                '--num-processes', '8',
                '--lr', '3e-4',
                '--entropy-coef', '0',
                '--value-loss-coef', '0.5',
                '--ppo-epoch', '10',
                '--num-mini-batch', '32',
                '--gamma', '0.995',
                '--gae-lambda', '0.95',
                '--num-env-steps', '30000000',
                '--use-linear-lr-decay',
                '--use-proper-time-limits',
                '--save-interval', '100',
                '--seed', '2',
                '--save-dir', './tmp/trained_models/RobotLocomotion-v0/test/',
                '--render-interval', '80',
                '--rule-sequence', '0,7,1,13,1,2,16,12,13,6,4,19,4,17,5,3,2,16,4,5,18,9,8,9,9,8']

solve_argv_conflict(args_list)
parser = get_parser()
args = parser.parse_args(args_list + sys.argv[1:])

env = gym.make("RobotLocomotion-v0", args=args)
env.reset()
# viewer = rd.GLFWViewer()

while True:
    a = env.action_space.sample() * 100
    obs, reward, done, info = env.step(a)
    print(obs)
    
    # viewer.render(env.sim)
