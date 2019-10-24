import gym
from gym import error, spaces, utils
from gym.utils import seeding

class CartpoleHomebrewEnv(gym.Env):
  metadata = {'render.modes': ['human']}

  def __init__(self):
    self.gravity = 9.8
    
  def step(self, action):
    print("You took action: {:d}".format(action))
    
  def reset(self):
    print("You've reset")
    
  def render(self, mode='human'):
    print("We can't render yet")
    
  def close(self):
    print("Nothing to close")
    
