from setuptools import setup

setup(name='gym-cartpole-homebrew',
      packages=['gym_cartpole_homebrew', 'envs'],
      version='0.0.1',
      install_requires=['gym']  # And any other dependencies cartpole_homebrew needs
)
