from gym.envs.registration import register

register(
    id='CartpoleHomebrew-v0',
    entry_point='gym.gym_cartpole_homebrew.envs.cartpole_homebrew_env:CartpoleHomebrewEnv',
)
#register(
#    id='foo-extrahard-v0',
#    entry_point='gym_foo.envs:FooExtraHardEnv',
#)
