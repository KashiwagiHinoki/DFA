from functools import lru_cache
from _regex import _Regex
from _regex import empty_set

class DFA:
    #transitions: map transitions["state", "letter"] -> "state"
    def __init__(self, states, alp, init_state, transitions, accepting_states):
        self.states = states
        self.alp = alp
        self.init_state = init_state
        self.transitions = transitions
        self.accepting_states = accepting_states

        self.accepting_states_index = [i for i in range(len(self.states)) if self.states[i] in accepting_states]
        for i in range(len(self.states)):
            if states[i] == init_state:
                self.init_state_index = i

    @lru_cache(maxsize=10000)
    def toRegexRecursion(self, i, j, k):
        if i == j and k <= 0:
            _l = '+'.join([t[1] for t, q_j in self.transitions.items() if t[0] == self.states[i] and q_j == self.states[j]])
            _l = "(" + _l + '+' + "{e})"
            return _Regex(_l).rep()

        if k <= 0:
            _l = '+'.join([t[1] for t, q_j in self.transitions.items() if t[0] == self.states[i] and q_j == self.states[j]])
            return self.toRegexRecursion(i, i, k) * _Regex("("+_l+")")* self.toRegexRecursion(j, j, k)
        
        ret = self.toRegexRecursion(i, j, k - 1) + self.toRegexRecursion(i, k, k - 1) * self.toRegexRecursion(k, k, k - 1).rep() * self.toRegexRecursion(k, j, k - 1)
        if i == j: 
            return ret.rep()
        return ret

    def toRegex(self):
        _regs = [self.toRegexRecursion(self.init_state_index, ac_index, len(self.states) - 1) for ac_index  in self.accepting_states_index]
        ret = empty_set
        for _reg in _regs:
            ret = ret + _reg
        return ret
    
    def is_accept(self, input_string):
        current_state = self.init_state
        for letter in input_string:
            current_state = self.transitions[current_state, letter]
        
        return current_state in self.accepting_states
