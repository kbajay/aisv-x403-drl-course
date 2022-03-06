from importlib.metadata import metadata
import gym

class MolsynthEnv(gym.Env):
  metadata = {'render.modes': ['human']}

  def __init__(self):
    # TODO

  def reset(self):
    # TODO
  
  def render(self, mode='human'):
    if mode == 'human':
      #
  def close(self):
    # TODO
