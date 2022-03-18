# -------------------------------------------------------
# Diseño de Lenguajes de Programación
# Automatas Finitos
# Francisco Rosal - 18676
# -------------------------------------------------------

from afn import AFN
from afd import AFD
from retree import RETree
from thompson import Thompson
from subconjuntos import Subconjuntos

"""
42 - *
43 - +
46 - .
63 - ?
69 - E
97 - a
98 - b
99 - c
100 - d
101 - e
102 - f
103 - g
104 - h
124 - |
"""

re = "abcd"
re = "(a|b)c"
re = "(b|b)ac"
re = "(b|b)abc"
re = "a|b"
re = "ab|c"
re = "(ab)|c"
re = "abc|d"
re = "(abc)|d"
re = "a*"
re = "a*|c"
re = "(a)*|b"
re = "ab*|c"
re = "(ab)*|c"
re = "(ab)+|c"
re = "(ab)?|c"
re = "(abcd)|e"
re = "(abcd)*|e"
re = "a|b*"
re = "(a|b)*"
re = "(a|b)*|c"
re = "(a|b)*c"
re = "(a|b)*abb"
re = "a|bc"
re = "a|(bc)"
re = "ab|cd"
re = "a|bcd"
re = "a|bcde"
re = "abc|def"
re = "a|(b|c)"
re = "a|(b|cd)"
re = "(c|(d|e))*abb"
re = "(c|(d|(e|f)))*abc"
re = "(c|(d|(e|f)))*abb|h"
re = "(c|(d|(e|f)))abb|h"
re = "(c|(d|e))*abb|(a|b)"
re = "(a|b)*abb|(c|(d|e))"
re = "(c|(d|e))*abb(a|b)"
re = "(c|(d|e))*(a|b)"
re = "((c|(d|e))*)(a|b)"
re = "(a|b)*abb(c|(d|e))"
re = "((b|b)*abb(a|b)*)(a|b)*"
re = "((a|b)*((a|(bb))*))e"

# - EXAMEN
re = "(a|b)*"
re = "((a|(bb))*)"
re = "(a|b)*((a|(bb))*)"
re = "((a|b)*((a|(bb))*))E"
re = "((a|b)*((a|(bb))*))E#"

# - EXAMPLE
re = "(b|b)*abb(a|b)*" # La del ejemplo de las instrucciones
w = "babbaaaaa"

# - EXEC THIS
re = "(b|b)*abb(a|b)*" # La del ejemplo de las instrucciones
w = "babbaaaaa"

ret = RETree(re)
tree = ret.get_tree()
print(tree)

thompson = Thompson(tree)
thompson.draw()

final_state = thompson.cantidad_estados
alfabeto = thompson.alfabeto
transiciones = thompson.transiciones

input()

if AFN.simulacion(w, alfabeto, transiciones, "S" + str(final_state-1)):
    print("Si pertenece")
else:
    print("No pertenece")

subconjuntos = Subconjuntos(transiciones, alfabeto, final_state)
subconjuntos.run()
subconjuntos.draw()

input()

re = "(" + re + ")#"
ret = RETree(re)
tree = ret.get_tree()
print(tree)

afd = AFD(tree)
afd.get_transiciones()
afd.draw()

if afd.simulacion(w):
    print("Si pertenece")
else:
    print("No pertenece")
