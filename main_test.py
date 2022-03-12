# -------------------------------------------------------
# Diseño de Lenguajes de Programación
# Automatas Finitos
# Francisco Rosal - 18676
# -------------------------------------------------------

r = "(b|b)*abb(a|b)*"
w = "babbaaaaa"

r = "(a|b)*abb"
w = "baabb"

# # construction of the NFA from the regular expression
# nfa = NFA(r)


# # construction of the DFA from the NFA
# dfa = DFA(nfa)


# # construction of the minimized DFA from the DFA
# min_dfa = MinimizedDFA(dfa)


# # construction of the minimized DFA from the NFA
# min_nfa = MinimizedDFA(nfa)


# # construction of the minimized DFA from the regular expression
# min_r = MinimizedDFA(r)


# # construction of the minimized DFA from the word
# min_w = MinimizedDFA(w)


# class DFA:
#     def __init__(self, nfa):
#         self.nfa = nfa
#         self.states = []
#         self.alphabet = []
#         self.transitions = []
#         self.initial_state = None
#         self.final_states = []

#         self.construct_dfa()

#     def construct_dfa(self):
#         # get the states of the NFA
#         self.states = self.nfa.states

#         # get the alphabet of the NFA
#         self.alphabet = self.nfa.alphabet

#         # get the transitions of the NFA
#         self.transitions = self.nfa.transitions

#         # get the initial state of the NFA
#         self.initial_state = self.nfa.initial_state

#         # get the final states of the NFA
#         self.final_states = self.nfa.final_states

#         # get the initial state of the DFA
#         self.initial_state = self.get_initial_state()

#         # get the final states of the DFA
#         self.final_states = self.get_final_states()

#         # get the transitions of the DFA
#         self.transitions = self.get_transitions()

#     def get_initial_state(self):
#         # get the initial state of the NFA
#         initial_state = self.nfa.initial_state

#         # get the initial state of the DFA
#         initial_state_dfa = self.nfa.get_initial_state_dfa()

#         # return the initial state of the DFA
#         return initial_state_dfa

#     def get_final_states(self):
#         # get the final states of the NFA
#         final_states = self.nfa.final_states

#         # get the final states of the DFA
#         final_states_dfa = []
#         for final_state in final_states:
#             final_states_dfa.append(self.nfa.get_final_state_dfa(final_state))

#         # return the final states of the DFA
#         return final_states_dfa

#     def get_transitions():
#         # get the transitions of the NFA
#         transitions = self.nfa.transitions

#         # get the transitions of the DFA
#         transitions_dfa = []
#         for transition in transitions:
#             transitions_dfa.append(self.nfa.get_transition_dfa(transition))

#         # return the transitions of the DFA
#         return transitions_dfa


# class MinimizedDFA:
#     def __init__(self, dfa):
#         self.dfa = dfa
#         self.states = []
#         self.alphabet = []
#         self.transitions = []
#         self.initial_state = None
#         self.final_states = []

#         self.construct_min_dfa()

#     def construct_min_dfa(self):
#         # get the states of the DFA
#         self.states = self.dfa.states

#         # get the alphabet of the DFA
#         self.alphabet = self.dfa.alphabet

#         # get the transitions of the DFA
#         self.transitions = self.dfa.transitions

#         # get the initial state of the DFA
#         self.initial_state = self.dfa.initial_state

#         # get the final states of the DFA
#         self.final_states = self.dfa.final_states

#         # get the initial state of the minimized DFA
#         self.initial_state = self.get_initial_state()

#         # get the final states of the minimized DFA
#         self.final_states = self.get_final_states()

#         # get the transitions of the minimized DFA
#         self.transitions = self.get_transitions()

#     def get_initial_state(self):
#         # get the initial state of the DFA
#         initial_state = self.dfa.initial_state

#         # get the initial state of the minimized DFA
#         initial_state_min_dfa = self.dfa.get_initial_state_min_dfa()

#         # return the initial state of the minimized DFA
#         return initial_state_min_dfa

#     def get_final_states(self):
#         # get the final states of the DFA
#         final_states = self.dfa.final_states

#         # get the final states of the minimized DFA
#         final_states_min_dfa = []
#         for final_state in final_states:
#             final_states_min_dfa.append(self.dfa.get_final_state_min_dfa(final_state))
