import unittest
from fsm.examples.mod_three import mod_three_fsm

class TestModThreeFSM(unittest.TestCase):
    def setUp(self):
        # Initialize FSM with error-raising behavior for invalid tokens
        self.fsm = mod_three_fsm(raise_on_invalid_token=True)

    def test_initial_state(self):
        # Test that the FSM starts in the correct initial state
        self.assertEqual(self.fsm.current_state, 0)

    def test_happy_path(self):
        # Test a valid sequence of inputs
        inputs = [1, 1, 0]
        for token in inputs:
            self.fsm.feed(token)
        self.assertEqual(self.fsm.current_state, 0)

    def test_invalid_token(self):
        # Test feeding an invalid token
        with self.assertRaises(ValueError):
            self.fsm.feed("invalid")

    def test_reset(self):
        # Test resetting the FSM to its initial state
        self.fsm.feed(1)
        self.fsm.reset()
        self.assertEqual(self.fsm.current_state, 0)

if __name__ == "__main__":
    unittest.main()
