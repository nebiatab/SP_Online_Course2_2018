"""
Module tests for the water-regulation module
"""

import unittest
from unittest.mock import MagicMock

from pump import Pump
from sensor import Sensor

from .controller import Controller
from .decider import Decider


class ModuleTests(unittest.TestCase):
    """
    Module tests for the water-regulation module
    """

    # TODO: write an integration test that combines controller and decider,
    #       using a MOCKED sensor and pump.
    '''
        def test_dummy(self):
            """
            Just some example syntax that you might use
            """

            pump = Pump('127.0.0.1', 8000)
            pump.set_state = MagicMock(return_value=True)

            self.fail("Remove this test.")

    '''
    def setUp(self):
        self.sensor = Sensor('127.0.0.1', 8000)
        self.pump = Pump('127.0.0.1', 8000)
        self.decider = Decider(10, .1)
        
        self.controller = Controller(self.sensor, self.pump, self.decider)
       
    def test_module(self):
        self.sensor.measure = MagicMock(return_value=8)
        self.pump.get_state = MagicMock(return_value='PUMP_IN')

        self.pump.set_state = MagicMock(return_value=1)

        result = self.controller.tick()

        self.assertEqual(result, 1)


        
