# -------------------------------------------------------
# Diseño de Lenguajes de Programación
# Automatas Finitos No Deterministas
# Francisco Rosal - 18676
# -------------------------------------------------------


class AFN:
    def __init__(self):
        pass

    @classmethod
    def simulacion(cls, cadena, alfabeto, trans, final_state):
        for i in cadena:
            if i not in alfabeto: return False

        states = cls.cerraduraEpsilon("S0", trans, [])
        cont = 1
        cadena += "#"
        c = cadena[0]

        while c != "#":
            states = cls.cerraduraEpsilonS(cls.mover(states, c, trans), trans)
            c = cadena[cont]
            cont += 1

        return True if final_state in states else False

    @classmethod
    def cerraduraEpsilon(cls, state, trans, states = []):
        # Hasta donde puedo llegar desde un estado con E
        if state not in states: states.append(state)

        if (len(trans[state]["E"]) > 0):
            for state in trans[state]["E"]:
                if state not in states: states.append(state)
                cls.cerraduraEpsilon(state, trans, states)

        return states

    @classmethod
    def cerraduraEpsilonS(cls, all_states, trans):
        final_states = []

        for state in all_states:
            new_states = []
            new_states = cls.cerraduraEpsilon(state, trans, [])
            final_states.append(new_states)

        final_states = [item for sublist in final_states for item in sublist]
        final_states = list(set(final_states))
        final_states.sort()

        return final_states

    @classmethod
    def mover(cls, states, caracter, trans):
        # Hasta donde podes llegar con un caracter
        moved_states = []

        for state in states:
            for key, value in trans.items():
                if key == state and len(value[caracter]) > 0:
                    for st in value[caracter]:
                        if st not in moved_states:
                            moved_states.append(st)

        return moved_states

