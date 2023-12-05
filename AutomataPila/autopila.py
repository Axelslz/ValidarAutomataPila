import tkinter as tk
from tkinter import messagebox

class Automata:
    def __init__(self):
        self.transitions = {
           ('S', 'X0'): ('A1', 'O'),
           ('A1', 'O'): ('A4', 'L'),
           ('A4', 'L'): ('A7', 'G'),
           ('A7', 'G'): ('A10', 'N'),
           ('A10', 'N'): ('AF', 'W'),
           ('AF', 'W'): ('AFF', 'AAA'),
           ('S', 'X1'): ('A2', 'O'),
           ('A2', 'O'): ('A5', 'L'),
           ('A5', 'L'): ('A8', 'G'),
           ('A8', 'G'): ('A11', 'T'),
           ('A11', 'T'): ('AU', 'W'),
           ('AU', 'EE'): ('AUU', 'EEE')
           
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
            elif dato == 'X1':
                self.current_state = 'S'
            #elif dato == 'X2':
                #self.current_state = ''
            else:
                raise ValueError("Cima de la pila invalida")

        while self.stack:
            print(f'Estado actual: [{self.current_state}] Lyra: {self.stack}')
            text_area.insert(tk.END, f"Lyra: {self.stack}\n")
            input_type = self.stack.pop()
            transition_key = (self.current_state, input_type)
            transition = self.transitions.get(transition_key)
            if transition is None:
                messagebox.showerror("ERROR", f"Transición no encontrada para: {transition_key}")
            next_state, action = transition
            self.current_state = next_state

        if self.current_state == 'AFF' 'AU':
            print(f'Estado actual: [{self.current_state}] Lyra: {self.stack}')
            text_area.insert(tk.END, f"Lyra: {self.stack}\n")
            messagebox.showinfo('Logix', 'Cadena Válida')
        else:
            messagebox.showerror("ERROR", f"No se puede terminar en: {self.current_state}")

        return next_state, action

    def procesar_entrada(self, entrada):
        tokens = {
            'O': ["$"],
            'Y': ['L', 'RY'],
            'RY': ['L', 'RY', '£'],
            'V': ['"'],
            'G': ['='],
            'Q': ['L', 'Q', '£'],
            'T': ['V', 'Q', 'V'],
            'Z': ['true', 'false'],
            'W': [";"],
            'X0': ['int'],
            'X1': ['string'],
            'X2': ['bool'],
            'N': list("0123456789"),
            'L': list("abcdefghijklmnñopqrstuvwxyz"),
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

