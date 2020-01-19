from gym.envs.registration import register

register(
    id='CartpoleNoisy-v0',
    entry_point='gym_cartpole_noisy.envs:CartPoleNoisyEnv',
)
#register(
#    id='foo-extrahard-v0',
#    entry_point='gym_foo.envs:FooExtraHardEnv',
#)
