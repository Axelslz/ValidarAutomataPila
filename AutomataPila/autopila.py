import tkinter as tk
from tkinter import messagebox

class Automata:
    def __init__(self):
        self.transitions = {
          # Parte 1
        ('S', 'X0'): ('A1', 'O'),
        ('A1', 'O'): ('A4', 'L'),
        ('A4', 'L'): ('A7', 'G'),
        ('A7', 'G'): ('A10', 'N'),
        ('A10', 'N'): ('EE', 'W'),
        ('EE', 'W'): ('EEP', 'ZZZ'),

        # Parte 2
        ('S', 'X1'): ('A2', 'O'),
        ('A2', 'O'): ('A5', 'L'),
        ('A5', 'L'): ('A8', 'G'),
        ('A8', 'G'): ('A11', 'V'),
        ('A11', 'V'): ('A13', 'L'),
        ('A13', 'L'): ('A14', 'F'),
        ('A14', 'F'): ('EEE', 'W'),
        ('EEE', 'W'): ('EEEB', 'ÑÑÑ'),

        # Parte 3 (Agregada)
        ('S', 'X2'): ('A3', 'O'),
        ('A3', 'O'): ('A6', 'L'),
        ('A6', 'L'): ('A9', 'G'),
        ('A9', 'G'): ('A12', 'X9'),
        ('A12', 'X9'): ('AZ', 'W'),
        ('AZ', 'W'): ('AZZ', 'AAAA'),

    
           ('S', 'X4'): ('R1', 'X10'),
           ('R1', 'X10'): ('R2', 'P'),
           ('R2', 'P'): ('R3', 'X1'),
           ('R3', 'X1'): ('R4', 'O'),
           ('R4', 'O'): ('R5', 'J'),
           ('R5', 'J'): ('R6', 'C'),
           ('R6', 'C'): ('R7', 'X1'),
           ('R7', 'X1'): ('R8', 'O'),
           ('R8', 'O'): ('R9', 'J'),
           ('R9', 'J'): ('R10', 'U'),
           ('R10', 'U'): ('R11', 'H'),
           ('R11', 'H'): ('R12', 'X1'),
           ('R12', 'X1'): ('R13', 'Y'),
           ('R13', 'Y'): ('R14', 'X7'),
           ('R14', 'X7'): ('R15', 'O'),
           ('R15', 'O'): ('R16', 'J'),
           ('R16', 'J'): ('R17', 'M'),
           ('R17', 'M'): ('R18', 'O'),
           ('R18', 'O'): ('R19', 'J'),
           ('R19', 'J'): ('R20', 'W'),
           ('R20', 'W'): ('AA', 'XXX'),
    
           ('S', 'X6'): ('S1', 'P'),
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
           ('S23', 'W'): ('AA', 'XXX'),
    
           ('S', 'X4'): ('Z1', 'X5'),
           ('Z1', 'X5'): ('Z2', 'P'),
           ('Z2', 'P'): ('Z3', 'U'),
           ('Z3', 'U'): ('Z4', 'Y'),
           ('Z4', 'Y'): ('Z5', 'X8'),
           ('Z5', 'X8'): ('Z6', 'P'),
           ('Z6', 'P'): ('Z7', 'V'),
           ('Z7', 'V'): ('Z8', 'L'),
           ('Z8', 'L'): ('Z9', 'F'),
           ('Z9', 'F'): ('Z10', 'U'),
           ('Z10', 'U'): ('Z11', 'W'),
           ('Z11', 'W'): ('AA', 'XXX'),
           ('AA', 'XXX'): ('AAA', 'XXXX'),
           
        }

        self.stack = []

    def next_state(self):
        text_area.delete('1.0', tk.END)
        if not self.stack:
            raise ValueError("La pila está vacía")
        else:
            dato = self.stack[-1]
            if dato == 'X0':
                self.current_state = 'S'
            #elif dato == 'X1':
                #self.current_state = 'S'
            #elif dato == 'X2':
                #self.current_state = ''
            else:
                raise ValueError("Cima de la pila invalida")

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

        if self.current_state == ['EEP', 'EEE']:
            print(f'Estado actual: [{self.current_state}] Lyra: {self.stack}')
            text_area.insert(tk.END, f"Lyra: {self.stack}\n")
            messagebox.showinfo('Logix', 'Cadena Válida')
        else:
            messagebox.showerror("ERROR", f"No se puede terminar en: {self.current_state}")

        return next_state, action

    def procesar_entrada(self, entrada):
        tokens = {
            'O': ["$"],
            'G': ["="],
            'V': ['"'],
            'F': ['"'],
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
            'X0': ['int'],
            'X1': ['string'],
            'X2': ['bool'],
            'X3': ['func'],
            'X4': ['main'],
            'X5': ['repeat'],
            'X6': ['retornar'],
            'X7': ['echo'],
            'X8': ['true', 'false'],
            'X9': ['suma'],
            'N': list("0123456789"),
            'L': list("abcdefghijklmnopqrstuvwxyz"),

        }

        palabras = entrada.split()
        palabras.reverse()

        for palabra in palabras:
            simbolo_encontrado = False
            for tipo, valores in tokens.items():
                if palabra in valores or (tipo == 'L' and palabra.isalpha()) or (tipo == 'N' and palabra.isdigit()):
                    self.stack.append(tipo)  # Guarda el tipo en la pila
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

