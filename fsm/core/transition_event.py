from typing import Any, Hashable
import logging

# Set up logging for TransitionEvent
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class TransitionEvent:
    """
    Represents an event triggered during a state transition in the FSM.
    """

    def __init__(
        self, entered_state: Hashable, exited_state: Hashable, token: Hashable,
        is_terminal: bool, feed_count: int, transition_count: int,
        payload: Any
    ):
        self._entered_state = entered_state
        self._exited_state = exited_state
        self._entered_state_is_terminal = is_terminal
        self._token = token
        self._feed_count = feed_count
        self._transition_count = transition_count
        self._payload = payload
        logger.info(f"TransitionEvent created: {self}")

    @property
    def entered_state(self) -> Hashable:
        """Returns the state entered after the transition."""
        return self._entered_state

    @property
    def exited_state(self) -> Hashable:
        """Returns the state exited during the transition."""
        return self._exited_state

    @property
    def entered_state_is_terminal(self) -> bool:
        """Checks if the entered state is terminal."""
        return self._entered_state_is_terminal

    @property
    def token(self) -> Hashable:
        """Returns the token that caused the transition."""
        return self._token

    @property
    def feed_count(self) -> int:
        """Returns the total number of feeds processed."""
        return self._feed_count

    @property
    def transition_count(self) -> int:
        """Returns the total number of transitions performed."""
        return self._transition_count

    @property
    def payload(self) -> Any:
        """Returns the payload associated with the transition."""
        return self._payload

    def __repr__(self):
        return (f"TransitionEvent(entered_state={self._entered_state}, "
                f"exited_state={self._exited_state}, token={self._token}, "
                f"is_terminal={self._entered_state_is_terminal}, "
                f"feed_count={self._feed_count}, "
                f"transition_count={self._transition_count}, "
                f"payload={self._payload})")
