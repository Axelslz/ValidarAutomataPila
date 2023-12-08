import tkinter as tk
from tkinter import messagebox

class Automata:
    def __init__(self):
        self.transitions = {
          # Para int
          ('S', 'X1'): ('A1', 'O'),
          ('A1', 'O'): ('A4', 'L'),
          ('A4', 'L'): ('A7', 'G'),
          ('A7', 'G'): ('A10', 'N'),
          ('A10', 'N'): ('EE', 'W'),
          ('EE', 'W'): ('EE', 'ZZZ'),

        # Para string
           ('S', 'X2'): ('A2', 'O'),
           ('A2', 'O'): ('A5', 'L'),
           ('A5', 'L'): ('A8', 'G'),
           ('A8', 'G'): ('A13', 'L'),
           ('A13', 'L'): ('EEE', 'W'),
           ('EEE', 'W'): ('EEE', 'ZZZ'),
           

        # Para bool
           ('S', 'X3'): ('A3', 'O'),
           ('A3', 'O'): ('A6', 'X11'),
           ('A6', 'X11'): ('A9', 'G'),
           ('A9', 'G'): ('A12', 'X9'),
           ('A12', 'X9'): ('BT', 'W'),
           ('BT', 'W'): ('BTB', 'ZZZ'),

        # Para funciones
           ('D', 'X4'): ('D1', 'S'),
           ('D1', 'S'): ('D2', 'P'),
           ('D2', 'P'): ('D3', 'X1'),
           ('D3', 'X1'): ('D4', 'O'),
           ('D4', 'O'): ('D5', 'J'),
           ('D5', 'J'): ('D6', 'C'),
           ('D6', 'C'): ('D7', 'X1'),
           ('D7', 'X1'): ('D8', 'O'),
           ('D8', 'O'): ('D9', 'J'),
           ('D9', 'J'): ('D10', 'U'),
           ('D10', 'U'): ('D11', 'H'),
           ('D11', 'H'): ('D12', 'X1'),
           ('D12', 'X1'): ('D13', 'Y'),
           ('D13', 'Y'): ('D14', 'X7'),
           ('D14', 'X7'): ('D15', 'O'),
           ('D15', 'O'): ('D16', 'J'),
           ('D16', 'J'): ('D17', 'M'),
           ('D17', 'M'): ('D18', 'O'),
           ('D18', 'O'): ('D19', 'J'),
           ('D19', 'J'): ('D20', 'W'),
           ('D20', 'W'): ('TT', 'K'),
           ('TT', 'K'): ('BBB', 'K'),
        # Para ciclos
           ('R', 'X6'): ('S1', 'P'),
           ('S1', 'P'): ('S2', 'X1'),
           ('S2', 'X1'): ('S3', 'O'),
           ('S3', 'O'): ('S4', 'Q'),
           ('S4', 'Q'): ('S5', 'G'),
           ('S5', 'G'): ('S6', 'N'),
           ('S6', 'N'): ('S7', 'W'),
           ('S7', 'W'): ('S8', 'O'),
           ('S8', 'O'): ('S9', 'Q'),
           ('S9', 'Q'): ('S10', 'D'),
           ('S10', 'D'): ('S11', 'N'),
           ('S11', 'N'): ('S12', 'W'),
           ('S12', 'W'): ('S13', 'O'),
           ('S13', 'O'): ('S14', 'Q'),
           ('S14', 'Q'): ('S15', 'M'),
           ('S15', 'M'): ('S16', 'U'),
           ('S16', 'U'): ('S17', 'Y'),
           ('S17', 'Y'): ('S18', 'X8'),
           ('S18', 'X8'): ('S19', 'P'),
           ('S19', 'P'): ('S20', 'O'),
           ('S20', 'O'): ('S21', 'Q'),
           ('S21', 'Q'): ('S22', 'U'),
           ('S22', 'U'): ('S23', 'W'),
           ('S23', 'W'): ('AA', 'K'),
           ('AA', 'K'): ('AA', 'ZZZ'),
        #Para Condicional
           ('W', 'X12'): ('T1', 'P'),
           ('T1', 'P'): ('T2', 'O'),
           ('T2', 'O'): ('T3', 'L'),
           ('T3', 'L'): ('T4', 'D'),
           ('T4', 'D'): ('T5', 'N'),
           ('T5', 'N'): ('T6', 'U'),
           ('T6', 'U'): ('T7', 'Y'),
           ('T7', 'Y'): ('T8', 'X8'),
           ('T8', 'X8'): ('T9', 'P'),
           ('T9', 'P'): ('T10', 'L'),
           ('T10', 'L'): ('T11', 'U'),
           ('T11', 'U'): ('T12', 'W'),
           ('T12', 'W'): ('T13', 'K'),
           ('T13', 'K'): ('T14', 'X13'),
           ('T14', 'X13'): ('T15', 'Y'),
           ('T15', 'Y'): ('T16', 'X8'),
           ('T16', 'X8'): ('T17', 'P'),
           ('T17', 'P'): ('T18', 'L'),
           ('T18', 'L'): ('T19', 'U'),
           ('T19', 'U'): ('T20', 'W'),
           ('T20', 'W'): ('AE', 'K'),
           ('AE', 'K'): ('AE', 'ZZZ'),
        # Para main
           ('T', 'X4'): ('Z1', 'X5'),
           ('Z1', 'X5'): ('Z2', 'P'),
           ('Z2', 'P'): ('Z3', 'U'),
           ('Z3', 'U'): ('Z4', 'Y'),
           ('Z4', 'Y'): ('Z5', 'X8'),
           ('Z5', 'X8'): ('Z6', 'P'),
           ('Z6', 'P'): ('Z7', 'L'),
           ('Z7', 'L'): ('Z8', 'U'),
           ('Z8', 'U'): ('Z9', 'W'),
           ('Z9', 'W'): ('TZ', 'K'),
           ('TZ', 'K'): ('TZ', 'ZZZ'),
           
        }

        self.stack = []

    def next_state(self):
        text_area.delete('1.0', tk.END)
        if not self.stack:
            raise ValueError("La pila está vacía")
        else:
            dato = self.stack[-1]
            valores_estados = {'X1': 'S', 'X2': 'S', 'X3': 'S', 'X6': 'R', 'X4': 'B', 'X4': 'T', 'X12' : 'W'}
            if dato in valores_estados:
             self.current_state = valores_estados[dato]
             print(f'Se estableció el estado actual a: {self.current_state}')
            else:
               raise ValueError(f"La cima de la pila con valor {dato} no es válido")


        while self.stack:
            print(f'Estado actual: [{self.current_state}] Logix: {self.stack}')
            text_area.insert(tk.END, f"Logix: {self.stack}\n")
            input_type = self.stack.pop()
            transition_key = (self.current_state, input_type)
            transition = self.transitions.get(transition_key)
            if transition is None:
                messagebox.showerror("ERROR", f"Transición no encontrada para: {transition_key}")
            next_state, action = transition
            self.current_state = next_state

            estados_validos = ['EE', 'EEE', 'BTB', 'BBB', 'AA', 'TZ', 'AE']

        if self.current_state in estados_validos:
            print(f'Estado actual: [{self.current_state}] Lyra: {self.stack}')
            text_area.insert(tk.END, f"Logix: {self.stack}\n")
            messagebox.showinfo('Logix', 'Cadena Válida')
        else:
            messagebox.showerror("ERROR", f"No se puede terminar en: {self.current_state}")

        return next_state, action

    def procesar_entrada(self, entrada):
        tokens = {
            'S': ['suma'],
            'O': ["$"],
            'G': ["="],
            'W': [";"],
            'P': ["("],
            'U': [")"],
            'M': ["+", "++"],
            'Y': ["{"],
            'K': ["}"],
            'D': ["<", ">"],
            'J': ["a", "b"],
            'C': [","],
            'H': [":"],
            'Q': ["i"],
            'X1': ['int'],
            'X2': ['string'],
            'X3': ['bool'],
            'X4': ['func'],
            'X5': ['main'],
            'X6': ['repeat'],
            'X7': ['retornar'],
            'X8': ['echo'],
            'X9': ['true', 'false'],
            'X11': ['verdadero'],
            'X12': ['if'],
            'X13': ['else'],
            'N': list("0123456789"),
            'L': list("abcdefghijklmnopqrstuvwxyz"),
            

        }

        palabras = entrada.split()
        palabras.reverse()

        for palabra in palabras:
            simbolo_encontrado = False
            for tipo, valores in tokens.items():
                if palabra in valores or (tipo == 'L' and palabra.isalpha()) or (tipo == 'N' and palabra.isdigit()):
                    self.stack.append(tipo)  
                    simbolo_encontrado = True
                    break
            if not simbolo_encontrado:
                messagebox.showerror("ERROR", f"Simbolo no encontrado para: {palabra}")
                exit(0)

        if 'DESCONOCIDO' in self.stack:
            messagebox.showerror("ERROR", f"Símbolo desconocido en la entrada: {entrada}")

        return ' '.join(self.stack)


def procesar():
    entrada = entry.get()
    try:
        automata.procesar_entrada(entrada)
        text_area.delete('1.0', tk.END)
    except ValueError as e:
        messagebox.showerror("Error", e)
    automata.next_state()


root = tk.Tk()
root.title("Logix: Automata de pila")

entry = tk.Entry(root, width=100)
entry.pack(padx=10, pady=10)

boton_procesar = tk.Button(root, text="PROCESAR", command=procesar)
boton_procesar.pack(padx=10, pady=10)

text_area = tk.Text(root, height=15, width=150)
text_area.pack(padx=10, pady=10)

automata = Automata()

root.mainloop()

