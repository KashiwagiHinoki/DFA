from DFA import DFA
from _regex import _Regex

states = ["q_1", "q_2"]
alp = ["0", "1"]
init_state = "q_1"

transitions = dict()
transitions["q_1", "0"] = "q_2"
transitions["q_1", "1"] = "q_1"
transitions["q_2", "0"] = "q_1"
transitions["q_2", "1"] = "q_2"

accepting_states = ["q_1"]
dfa = DFA(states, alp, init_state, transitions, accepting_states)
print(dfa.toRegex())

print(dfa.is_accept("0101"))