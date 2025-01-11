import unittest
from fsm.core.fsm import DeterministicFiniteStateMachine
from fsm.core.transition_event import TransitionEvent

class TestDeterministicFiniteStateMachine(unittest.TestCase):
    def setUp(self):
        self.fsm = DeterministicFiniteStateMachine(raise_on_invalid_token=True)
        self.fsm.add_state("state_1")
        self.fsm.add_state("state_2", is_terminal=True)
        self.fsm.set_initial_state("state_1")
        self.fsm.add_transition("state_1", "state_2", "token_a")

    def test_initial_state(self):
        self.assertEqual(self.fsm.current_state, "state_1")

    def test_transition(self):
        self.assertTrue(self.fsm.feed("token_a"))
        self.assertEqual(self.fsm.current_state, "state_2")
        self.assertTrue(self.fsm.is_terminal)

    def test_invalid_token(self):
        with self.assertRaises(ValueError):
            self.fsm.feed("invalid_token")

    def test_reset(self):
        self.fsm.feed("token_a")
        self.fsm.reset()
        self.assertEqual(self.fsm.current_state, "state_1")

if __name__ == "__main__":
    unittest.main()