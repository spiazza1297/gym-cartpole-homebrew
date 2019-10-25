from gym.envs.registration import register

register(
    id='cartpole_homebrew-v0',
    entry_point='envs:CartpoleHomebrewEnv',
)
#register(
#    id='foo-extrahard-v0',
#    entry_point='gym_foo.envs:FooExtraHardEnv',
#)
