from fsm.core.fsm import DeterministicFiniteStateMachine
import logging

logger = logging.getLogger(__name__)

def mod_three_fsm(raise_on_invalid_token=False):
    """
    Creates an FSM to solve the modulo-three problem based on the given transition rules.

    States:
        - S0, S1, S2
    Alphabet:
        - 0, 1
    Transitions:
        - δ(S0, 0) = S0, δ(S0, 1) = S1
        - δ(S1, 0) = S2, δ(S1, 1) = S0
        - δ(S2, 0) = S1, δ(S2, 1) = S2
    """
    fsm = DeterministicFiniteStateMachine(raise_on_invalid_token=raise_on_invalid_token)
    
    # Add states
    fsm.add_state(0)  # S0
    fsm.add_state(1)  # S1
    fsm.add_state(2)  # S2
    # Set initial state
    fsm.set_initial_state(0)
    # Add transitions
    fsm.add_transition(0, 0, 0)  # δ(S0, 0) = S0
    fsm.add_transition(0, 1, 1)  # δ(S0, 1) = S1
    fsm.add_transition(1, 2, 0)  # δ(S1, 0) = S2
    fsm.add_transition(1, 0, 1)  # δ(S1, 1) = S0
    fsm.add_transition(2, 1, 0)  # δ(S2, 0) = S1
    fsm.add_transition(2, 2, 1)  # δ(S2, 1) = S2
    
    logger.info("Modulo-three FSM configured.")
    return fsm

if __name__ == "__main__":
    fsm = mod_three_fsm()
    binary_input = input("Enter a binary sequence: ")
    inputs = [int(char) for char in binary_input if char in "01"]
    logger.info(f"Starting FSM with inputs: {inputs}")

    for token in inputs:
        fsm.feed(token)

    print(f"Final state: {fsm.current_state}")
    logger.info(f"Final state: {fsm.current_state}")
