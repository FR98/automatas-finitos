# -------------------------------------------------------
# Diseño de Lenguajes de Programación
# Subconjuntos
# Francisco Rosal - 18676
# -------------------------------------------------------

import graphviz
from afn import AFN

class Subconjuntos:
    def __init__(self, transiciones, alfabeto, final_state):
        self.transiciones = transiciones
        self.data = {}
        self.alfabeto = alfabeto
        self.final_state = final_state

    def run(self):
        cont = 0
        self.alfabeto.remove("E")
        cerradura = AFN.cerraduraEpsilon("S0", self.transiciones, [])
        cerradura.sort()

        # Se genera la tabla de transicion del AFD
        self.data[str(cerradura)] = {
            "name": str(cont),
        }

        for letra in self.alfabeto:
            self.data[str(cerradura)][letra] = None

        cont += 1
        continuar = True
        while (continuar):
            initial_size = len(self.data)
            keys = list(self.data.keys())

            # Se llena la tabla de transicion del AFD
            for key in keys:
                for letra in self.alfabeto:
                    if self.data[key][letra] is None:
                        new_state = []
                        st = key
                        for specialChar in ["[", "]", " "]:
                            st = st.replace(specialChar, "")
                        st = st.split(",")
                        state = []

                        for i in st:
                            i = i.replace("'",'')
                            state.append(i)

                        new_state = AFN.cerraduraEpsilonS(AFN.mover(state, letra, self.transiciones), self.transiciones)

                        # Se verifica si hay un estado y se valida si existe en la tabla de transiciones o se agrega
                        if len(new_state) > 0:
                            if str(new_state) not in self.data:
                                self.data[str(new_state)] = {
                                    "name": str(cont)
                                }

                                for letter in self.alfabeto:
                                    self.data[str(new_state)][letter] = None

                                cont += 1
                                # Se agrega el estado nuevo a la transicion evaluada
                                self.data[key][letra] = self.data[str(new_state)]["name"]
                            else:
                                self.data[key][letra] = self.data[str(new_state)]["name"]

            final_size = len(self.data)

            if initial_size == final_size:
                continuar = not all(self.data.values())

        return self.data

    def draw(self):
        canvas = graphviz.Digraph(comment="AFD")
        canvas.attr(rankdir="LR")

        # Se dibujan los nodos
        for key in self.data.keys():
            states = key
            for specialChar in ["[", "]", " "]:
                states = states.replace(specialChar, "")
            states = states.split(",")
            st = []

            for i in states:
                i = i.replace("'", '')
                st.append(i)

            if ("S" + str(self.final_state-1)) in st:
                canvas.node(self.data[key]["name"], self.data[key]["name"], shape="doublecircle")
            else:
                canvas.node(self.data[key]["name"], self.data[key]["name"])

        # Se dibujan las transiciones
        for key, value in self.data.items():
            for letra in self.alfabeto:
                if value["name"] is not None and value[letra] is not None:
                    states = key
                    for specialChar in ["[", "]", " "]:
                        states = states.replace(specialChar, "")
                    states = states.split(",")

                    if ("S" + str(self.final_state-1)) in states:
                        canvas.node(value["name"], value["name"], shape="doublecircle")
                    else:
                        canvas.node(value["name"], value["name"])

                    canvas.node(value[letra], value[letra])
                    canvas.edge(value["name"], value[letra], letra)

        canvas.view()
