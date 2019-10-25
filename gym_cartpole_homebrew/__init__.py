from gym.envs.registration import register

register(
    id='cartpole-homebrew',
    entry_point='gym_cartpole_homebrew.envs:CartpoleHomebrewEnv',
)
#register(
#    id='foo-extrahard-v0',
#    entry_point='gym_foo.envs:FooExtraHardEnv',
#)
