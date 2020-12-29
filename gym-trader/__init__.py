from gym.envs.registration import register

register(
    id='single-discrete-v0',
    entry_point='gym_foo.envs:SingleDiscreteEnv',
)
register(
    id='single-continuous-v0',
    entry_point='gym_foo.envs:SingleContinuousEnv',
)
