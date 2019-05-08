from DFA import DFA
from _regex import _Regex
from _regex import empty_set


state_num = 20
states = list([str(i) for i in range(state_num)])
alp = list([str(i) for i in range(10)])
init_state = str(0)

transitions = dict()
for state in states:
    for letter in alp:
        transitions[(state, letter)] = str((int(state) * 10 + int(letter)) % len(states))

accepting_states = {str(0)}

dfa = DFA(states, alp, init_state, transitions, accepting_states)

#in_number = input()
#input_string = [str(s) for s in in_number]

#print(dfa.is_accept(input_string))
print(dfa.toRegex())
