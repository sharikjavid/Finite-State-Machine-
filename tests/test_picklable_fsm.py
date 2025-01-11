import unittest
import os
from fsm.core.picklable_fsm import _PicklableDeterministicFiniteStateMachine
from fsm.core.fsm import DeterministicFiniteStateMachine

class TestPicklableDeterministicFiniteStateMachine(unittest.TestCase):
    def setUp(self):
        self.fsm = DeterministicFiniteStateMachine()
        self.fsm.add_state("state_1")
        self.fsm.add_state("state_2", is_terminal=True)
        self.fsm.set_initial_state("state_1")
        self.fsm.add_transition("state_1", "state_2", "token_a")

    def test_pickling(self):
        picklable_fsm = _PicklableDeterministicFiniteStateMachine.from_state_machine(self.fsm)
        picklable_fsm.pickle_to_file("test_fsm.pkl")
        self.assertTrue(os.path.exists("test_fsm.pkl"))

        unpickled_fsm = _PicklableDeterministicFiniteStateMachine.unpickle_from_file("test_fsm.pkl")
        reconstructed_fsm = unpickled_fsm.to_state_machine()

        self.assertEqual(reconstructed_fsm.current_state, "state_1")
        os.remove("test_fsm.pkl")

if __name__ == "__main__":
    unittest.main()