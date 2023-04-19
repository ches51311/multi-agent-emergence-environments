import numpy as np
import gym
import logging
import sys
from copy import deepcopy
from functools import partial
from collections import OrderedDict

class DummyAgentPolicy(object):
    def __init__(self):
        pass
    def reset(self):
        pass
    def act(self, observation):
        action = {}
        # action['action_movement'] = np.array([[0, 0, 0],
        #                                     [5, 0, 7],
        #                                     [3, 3, 3],
        #                                     [3, 2, 3]], dtype=np.int32)
        # action['action_pull'] = np.array([1, 0, 0, 1])
        # action['action_glueall'] = np.array([0, 0, 0, 1])
        action['action_movement'] = np.array([[0, 0, 0],
                                            [0, 0, 0],
                                            [0, 0, 0],
                                            [0, 0, 0]], dtype=np.int32)
        action['action_pull'] = np.array([0, 0, 0, 0])
        action['action_glueall'] = np.array([0, 0, 0, 0])
        return action, None