from setuptools import setup, find_packages

setup(name='gym_cartpole_homebrew',
      packages=find_packages(),
      version='0.0.1',
      install_requires=['gym','numpy>=1.10.4']  # And any other dependencies cartpole_homebrew needs
)
