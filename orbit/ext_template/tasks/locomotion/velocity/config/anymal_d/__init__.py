import gymnasium as gym

from . import agents, flat_env_cfg, rough_env_cfg

##
# Register Gym environments.
##

gym.register(
    id="Template-Velocity-Flat-Anymal-D-v0",
    entry_point="omni.isaac.orbit.envs:RLTaskEnv",
    disable_env_checker=True,
    kwargs={
        "env_cfg_entry_point": flat_env_cfg.AnymalDFlatEnvCfg,
        "rsl_rl_cfg_entry_point": agents.rsl_rl_cfg.AnymalDFlatPPORunnerCfg,
    },
)

gym.register(
    id="Template-Velocity-Flat-Anymal-D-Play-v0",
    entry_point="omni.isaac.orbit.envs:RLTaskEnv",
    disable_env_checker=True,
    kwargs={
        "env_cfg_entry_point": flat_env_cfg.AnymalDFlatEnvCfg_PLAY,
        "rsl_rl_cfg_entry_point": agents.rsl_rl_cfg.AnymalDFlatPPORunnerCfg,
    },
)

gym.register(
    id="Template-Velocity-Rough-Anymal-D-v0",
    entry_point="omni.isaac.orbit.envs:RLTaskEnv",
    disable_env_checker=True,
    kwargs={
        "env_cfg_entry_point": rough_env_cfg.AnymalDRoughEnvCfg,
        "rsl_rl_cfg_entry_point": agents.rsl_rl_cfg.AnymalDRoughPPORunnerCfg,
    },
)

gym.register(
    id="Template-Velocity-Rough-Anymal-D-Play-v0",
    entry_point="omni.isaac.orbit.envs:RLTaskEnv",
    disable_env_checker=True,
    kwargs={
        "env_cfg_entry_point": rough_env_cfg.AnymalDRoughEnvCfg_PLAY,
        "rsl_rl_cfg_entry_point": agents.rsl_rl_cfg.AnymalDRoughPPORunnerCfg,
    },
)
