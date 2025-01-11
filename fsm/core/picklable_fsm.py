from dataclasses import dataclass
from typing import Any, Dict, Hashable, Tuple
import pickle
from fsm.core.fsm import DeterministicFiniteStateMachine
import logging

# Set up logging for pickling operations
logger = logging.getLogger(__name__)

@dataclass
class _PicklableDeterministicFiniteStateMachine:
    """
    Facilitates pickling of a DeterministicFiniteStateMachine instance for persistence.
    """

    _is_terminal: Dict[Hashable, bool]
    _transitions: Dict[Tuple[Hashable, Hashable], Hashable]
    _initial_state: Hashable
    _current_state: Hashable
    _feed_count: int
    _transition_count: int
    _raise_on_invalid_token: bool

    @classmethod
    def from_state_machine(
        cls, state_machine: DeterministicFiniteStateMachine
    ) -> "_PicklableDeterministicFiniteStateMachine":
        """Converts an FSM instance into a picklable representation."""
        logger.info("Creating picklable FSM instance.")
        return cls(
            state_machine._is_terminal,
            state_machine._transitions,
            state_machine._initial_state,
            state_machine._current_state,
            state_machine._feed_count,
            state_machine._transition_count,
            state_machine._raise_on_invalid_token
        )

    def pickle_to_file(self, filename: str, protocol: int = None):
        """Serializes the FSM instance to a file."""
        logger.info(f"Pickling FSM to file: {filename}")
        with open(filename, "wb") as file:
            pickle.dump(self, file, protocol)

    @classmethod
    def unpickle_from_file(
        cls, filename: str
    ) -> "_PicklableDeterministicFiniteStateMachine":
        """Deserializes an FSM instance from a file."""
        logger.info(f"Unpickling FSM from file: {filename}")
        with open(filename, "rb") as file:
            return pickle.load(file)

    def to_state_machine(self) -> DeterministicFiniteStateMachine:
        """Reconstructs the FSM instance from its pickled representation."""
        logger.info("Reconstructing FSM from pickled representation.")
        state_machine = DeterministicFiniteStateMachine()
        state_machine._is_terminal = self._is_terminal
        state_machine._transitions = self._transitions
        state_machine._initial_state = self._initial_state
        state_machine._current_state = self._current_state
        state_machine._feed_count = self._feed_count
        state_machine._transition_count = self._transition_count
        state_machine._raise_on_invalid_token = self._raise_on_invalid_token
        return state_machine