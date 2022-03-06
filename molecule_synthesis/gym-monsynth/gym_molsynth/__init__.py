from gym.envs.registration import register

register(
    id='molsynth-v0', 
    entry_points='gym_molsynth.envs.molsynth_env:MolsynthEnv',
    )
