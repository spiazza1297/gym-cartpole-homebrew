from gym.envs.registration import register

register(
    id='CartpoleHomebrew-v0',
    entry_point='gym-cartpole-homebrew.gym_cartpole_homebrew.envs:CartpoleHomebrewEnv',
)
#register(
#    id='foo-extrahard-v0',
#    entry_point='gym_foo.envs:FooExtraHardEnv',
#)
