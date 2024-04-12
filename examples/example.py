#!/usr/bin/env python3

# Copyright (c) Meta Platforms, Inc. and its affiliates.
# This source code is licensed under the MIT license found in the
# LICENSE file in the root directory of this source tree.

import gym

import habitat.gym  # noqa: F401


def example():
    # Note: Use with for the example testing, doesn't need to be like this on the README

    env = gym.make("HabitatRenderPick-v0")#env is a RLTaskEnv
    #methods = [method for method in dir(env) if callable(getattr(env, method))]
    #print(methods) -> step
    #input(",h")

    #env = gym.make("HabitatRenderTidyHouse-v0") 
    print("Environment creation successful")
    observations = env.reset()  # noqa: F841
    print("Agent acting inside environment.")
    count_steps = 0
    terminal = False
    
    while count_steps < 10000:

        env.render()
        if terminal:
            env.reset()
            print(env.action_space)
            print(env.action_space.shape)

        action = env.action_space.sample()
        action[-1] = 0
        action[-2] = 0

        observations, reward, terminal, info = env.step(action
        )  # noqa: F841
        count_steps += 1
    print("Episode finished after {} steps.".format(count_steps))


if __name__ == "__main__":
    #for e in gym.envs.registry.all():
    #    print(e)
    #input("ops")
    import habitat_sim
    import importlib

# Get the module information
    module_info = importlib.util.find_spec('habitat_sim')

# Print the location of the module
    print(module_info.origin)
    #example()
