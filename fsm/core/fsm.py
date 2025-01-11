from typing import Any, Callable, Dict, Hashable, Iterable, List, Tuple
from itertools import chain
from fsm.core.transition_event import TransitionEvent
import logging

# Set up logging for FSM
logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)

class DeterministicFiniteStateMachine:
    """
    Represents a deterministic finite state machine (FSM) with support for transitions,
    callbacks, and event tracking.
    """

    def __init__(self, raise_on_invalid_token: bool = False):
        """
        Initializes the FSM with optional invalid token behavior.

        Args:
            raise_on_invalid_token (bool): If True, raises an exception for invalid tokens.
        """
        self._is_terminal: Dict[Hashable, bool] = {}
        self._transitions: Dict[Tuple[Hashable, Hashable], Hashable] = {}
        self._current_state: Hashable = None
        self._initial_state: Hashable = None
        self._feed_count = 0
        self._transition_count = 0
        self._callbacks: Dict[Tuple[Hashable, Hashable], Callable[[TransitionEvent], None]] = {}
        self._raise_on_invalid_token = raise_on_invalid_token
        logger.info("FSM initialized.")

    def add_state(self, state: Hashable, is_terminal: bool = False):
        """
        Adds a state to the FSM.

        Args:
            state (Hashable): The state identifier.
            is_terminal (bool): Whether the state is terminal.
        """
        if state in self._is_terminal:
            raise ValueError(f"State '{state}' already exists!")
        self._is_terminal[state] = is_terminal
        logger.info(f"State '{state}' added. Terminal: {is_terminal}")

    def set_initial_state(self, state: Hashable):
        """
        Sets the initial state of the FSM.

        Args:
            state (Hashable): The state identifier.
        """
        if state not in self._is_terminal:
            raise ValueError(f"State '{state}' does not exist!")
        self._initial_state = state
        self._current_state = state
        logger.info(f"Initial state set to '{state}'.")

    def add_transition(self, from_state: Hashable, to_state: Hashable, token: Hashable):
        """
        Adds a transition between states.

        Args:
            from_state (Hashable): State to transition from.
            to_state (Hashable): State to transition to.
            token (Hashable): Token triggering the transition.
        """
        if from_state not in self._is_terminal or to_state not in self._is_terminal:
            raise ValueError("Both states must exist before adding a transition.")
        if (from_state, token) in self._transitions:
            raise ValueError(f"Transition for token '{token}' from state '{from_state}' already exists!")
        self._transitions[(from_state, token)] = to_state
        logger.info(f"Transition added: {from_state} --({token})--> {to_state}")

    def feed(self, token: Hashable, payload: Any = None) -> bool:
        """
        Processes a token and triggers a state transition if valid.

        Args:
            token (Hashable): The token to process.
            payload (Any): Optional payload to pass with the transition event.

        Returns:
            bool: True if the token triggered a valid transition, False otherwise.
        """
        if self._current_state is None:
            raise RuntimeError("Initial state is not set.")

        logger.info(f"Current state: {self._current_state}, Token received: {token}")

        key = (self._current_state, token)
        if key not in self._transitions:
            if self._raise_on_invalid_token:
                raise ValueError(f"Invalid token '{token}' from state '{self._current_state}'.")
            logger.warning(f"No transition for token '{token}' from state '{self._current_state}'.")
            return False

        next_state = self._transitions[key]
        event = TransitionEvent(
            entered_state=next_state,
            exited_state=self._current_state,
            token=token,
            is_terminal=self._is_terminal[next_state],
            feed_count=self._feed_count,
            transition_count=self._transition_count,
            payload=payload
        )

        logger.info(f"Transitioning from {self._current_state} to {next_state} on token '{token}'")
        if key in self._callbacks:
            logger.info(f"Executing callback for transition {key}.")
            self._callbacks[key](event)

        self._current_state = next_state
        self._feed_count += 1
        self._transition_count += 1

        return True

    def reset(self):
        """
        Resets the FSM to the initial state.
        """
        self._current_state = self._initial_state
        self._feed_count = 0
        self._transition_count = 0
        logger.info("FSM reset to initial state.")

    def bind_callback(self, from_state: Hashable, token: Hashable, callback: Callable[[TransitionEvent], None]):
        """
        Binds a callback to a specific transition.

        Args:
            from_state (Hashable): State to transition from.
            token (Hashable): Token triggering the transition.
            callback (Callable): Callback to execute on transition.
        """
        if (from_state, token) not in self._transitions:
            raise ValueError(f"No transition exists for token '{token}' from state '{from_state}'.")
        self._callbacks[(from_state, token)] = callback
        logger.info(f"Callback bound to transition {from_state} --({token})-->.")

    @property
    def current_state(self) -> Hashable:
        """Returns the current state."""
        return self._current_state

    @property
    def is_terminal(self) -> bool:
        """Returns True if the current state is terminal."""
        return self._is_terminal.get(self._current_state, False)
