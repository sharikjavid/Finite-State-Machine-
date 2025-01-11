import unittest
from fsm.core.transition_event import TransitionEvent

class TestTransitionEvent(unittest.TestCase):
    def setUp(self):
        self.event = TransitionEvent(
            entered_state="state_2",
            exited_state="state_1",
            token="token_a",
            is_terminal=True,
            feed_count=5,
            transition_count=3,
            payload={"key": "value"}
        )

    def test_properties(self):
        self.assertEqual(self.event.entered_state, "state_2")
        self.assertEqual(self.event.exited_state, "state_1")
        self.assertEqual(self.event.token, "token_a")
        self.assertTrue(self.event.entered_state_is_terminal)
        self.assertEqual(self.event.feed_count, 5)
        self.assertEqual(self.event.transition_count, 3)
        self.assertEqual(self.event.payload, {"key": "value"})

if __name__ == "__main__":
    unittest.main()