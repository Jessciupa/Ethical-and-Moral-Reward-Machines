from gym.envs.registration import register

# ----------------------------------------- DRIVING ACT DEONTOLOGY
register(
    id='Driving-v0',
    entry_point='envs.grids.grid_environment:DrivingRMEnv',
    max_episode_steps=1000
)

register(
    id='Driving-single-v0',
    entry_point='envs.grids.grid_environment:DrivingRM3Env',
    max_episode_steps=1000
)

# ----------------------------------------- DRIVING UTILITARIAN
register(
    id='DrivingUtil-v0',
    entry_point='envs.grids.grid_environment:DrivingUtilRMEnv',
    max_episode_steps=1000
)

register(
    id='DrivingUtil-single-v0',
    entry_point='envs.grids.grid_environment:DrivingUtilRM3Env',
    max_episode_steps=1000
)

# ----------------------------------------- DILEMMA ACT DEONTOLOGY
register(
    id='Dilemma-v0',
    entry_point='envs.grids.grid_environment:DilemmaRMEnv',
    max_episode_steps=1000
)

# ----------------------------------------- DILEMMA UTILITARIAN
register(
    id='DilemmaRM2-v0',
    entry_point='envs.grids.grid_environment:DilemmaRM2Env',
    max_episode_steps=1000
)

# ----------------------------------------- MORAL MACHINE WESTERN (AGE PREFERENCE)
register(
    id='MoralWestern-v0',
    entry_point='envs.grids.grid_environment:MoralWestern',
    max_episode_steps=1000
)

# ----------------------------------------- MORAL MACHINE SOUTHERN (AGE PREFERENCE)
register(
    id='MoralSouthern-v0',
    entry_point='envs.grids.grid_environment:MoralSouthern',
    max_episode_steps=1000
)

# ----------------------------------------- MORAL MACHINE EASTERN (AGE PREFERENCE)
register(
    id='MoralEastern-v0',
    entry_point='envs.grids.grid_environment:MoralEastern',
    max_episode_steps=1000
)