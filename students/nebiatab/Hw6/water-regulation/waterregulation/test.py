"""
Unit tests for the water-regulation module
"""

import unittest
from unittest.mock import MagicMock

from pump import Pump
from sensor import Sensor

from .controller import Controller
from .decider import Decider


class DeciderTests(unittest.TestCase):
    """
    Unit tests for the Decider class
    """

    # TODO: write a test or tests for each of the behaviors defined for
    #       Decider.decide

    def test_decide(self):
        ''' Tests for decider behaviors '''
        decider = Decider(100, .1)
        '''
            target_height is 100, and margin is .1
            lower margin = 90  upper margin = 110
        '''

        actions = {
            'PUMP_IN': 10,
            'PUMP_OUT': -10,
            'PUMP_OFF': 0
        }
        # decide takes current_height, current_action, and dict actions
        
        self.assertEqual(decider.decide(80, 'PUMP_OFF', actions), 10)
        self.assertEqual(decider.decide(120, 'PUMP_OFF', actions), -10)
        self.assertEqual(decider.decide(100, 'PUMP_OFF', actions), 0)

        self.assertEqual(decider.decide(105, 'PUMP_IN', actions), 0)
        self.assertEqual(decider.decide(85, 'PUMP_IN', actions), 10)

        self.assertEqual(decider.decide(85, 'PUMP_OUT', actions), 10)
        self.assertEqual(decider.decide(85, 'PUMP_OUT', actions), 10)
        
        


class ControllerTests(unittest.TestCase):
    """
    Unit tests for the Controller class
    """

    # TODO: write a test or tests for each of the behaviors defined for
    #       Controller.tick

    pass
