import tkinter as tk
from tkinter import ttk
from tkinter.constants import W, E, N, S
from tkinter import StringVar, DoubleVar
import math

class PuntoFijoApp:

    def __init__(self, root):
        self.root = root
        self.root.title("Método Punto Fijo") 
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)

        # Crear estilo
        self.estilos = ttk.Style()
        self.estilos.theme_use('clam')
        self.estilos.configure('mainframe.TFrame', background="#DBDBDB")

        # Crear el marco principal
        self.mainframe = ttk.Frame(root, style="mainframe.TFrame")
        self.mainframe.grid(column=0, row=0, sticky=(W, N, E, S))

        # Configuración de la cuadrícula del marco principal
        for i in range(4):
            self.mainframe.columnconfigure(i, weight=1)
        for i in range(11):
            self.mainframe.rowconfigure(i, weight=1)

        estilos_label1 = ttk.Style()
        estilos_label1.configure('Label1.TLabel', font="arial 15", anchor="e")

        estilos_label2 = ttk.Style()
        estilos_label2.configure('Label2.TLabel', font="arial 15", anchor="e")

        # Variables para el método de punto fijo
        self.gx = StringVar()
        self.x0 = StringVar()
        self.tolerancia = StringVar()
        self.resultado = StringVar()

        # Entradas para el método de punto fijo
        ttk.Label(self.mainframe, text="g(x) = ", style="Label1.TLabel").grid(column=0, row=0, sticky=E)
        ttk.Entry(self.mainframe, textvariable=self.gx, width=30).grid(column=1, row=0, columnspan=3, sticky=(W, E))

        ttk.Label(self.mainframe, text="x0 = ", style="Label1.TLabel").grid(column=0, row=1, sticky=E)
        ttk.Entry(self.mainframe, textvariable=self.x0, width=10).grid(column=1, row=1, sticky=(W, E))

        ttk.Label(self.mainframe, text="Tolerancia = ", style="Label1.TLabel").grid(column=2, row=1, sticky=E)
        ttk.Entry(self.mainframe, textvariable=self.tolerancia, width=10).grid(column=3, row=1, sticky=(W, E))

        # Botón para calcular
        ttk.Button(self.mainframe, text="Calcular", style="botones_restantes.TButton", command=self.calcular_punto_fijo).grid(column=0, row=2, columnspan=4, sticky=(W, E))

        # Área para mostrar el resultado
        label_resultado = ttk.Label(self.mainframe, textvariable=self.resultado, style="Label2.TLabel", wraplength=300)
        label_resultado.grid(column=0, row=3, columnspan=4, sticky=(W, N, E, S))

        # Configuración de estilos para botones
        self.estilos.configure('botones_numericos.TButton', font="arial 22", width=5, background="#FFFFFF", relief="flat")
        self.estilos.map('botones_numericos.TButton', background=[('active', '#B9B9B9')])

        self.estilos.configure('botones_borrar.TButton', font="arial 22", width=5, relief="flat", background="#CECECE")
        self.estilos.map('botones_borrar.TButton', foreground=[('active', '#FF0000')], background=[('active', '#858585')])

        self.estilos.configure('botones_restantes.TButton', font="arial 22", width=5, relief="flat", background="#CECECE")
        self.estilos.map('botones_restantes.TButton', background=[('active', '#858585')])

        # Crear botones
        self.crear_botones()

    def crear_botones(self):
        # Definición de los botones
        boton0 = ttk.Button(self.mainframe, text="0", style="botones_numericos.TButton", command=lambda: self.ingresar_valores('0'))
        boton1 = ttk.Button(self.mainframe, text="1", style="botones_numericos.TButton", command=lambda: self.ingresar_valores('1'))
        boton2 = ttk.Button(self.mainframe, text="2", style="botones_numericos.TButton", command=lambda: self.ingresar_valores('2'))
        boton3 = ttk.Button(self.mainframe, text="3", style="botones_numericos.TButton", command=lambda: self.ingresar_valores('3'))
        boton4 = ttk.Button(self.mainframe, text="4", style="botones_numericos.TButton", command=lambda: self.ingresar_valores('4'))
        boton5 = ttk.Button(self.mainframe, text="5", style="botones_numericos.TButton", command=lambda: self.ingresar_valores('5'))
        boton6 = ttk.Button(self.mainframe, text="6", style="botones_numericos.TButton", command=lambda: self.ingresar_valores('6'))
        boton7 = ttk.Button(self.mainframe, text="7", style="botones_numericos.TButton", command=lambda: self.ingresar_valores('7'))
        boton8 = ttk.Button(self.mainframe, text="8", style="botones_numericos.TButton", command=lambda: self.ingresar_valores('8'))
        boton9 = ttk.Button(self.mainframe, text="9", style="botones_numericos.TButton", command=lambda: self.ingresar_valores('9'))
        boton_borrar = ttk.Button(self.mainframe, text=chr(9003), style="botones_borrar.TButton", command=self.borrar)  
        boton_euler = ttk.Button(self.mainframe, text="e", style="botones_restantes.TButton", command=lambda: self.ingresar_valores('e'))
        boton_punto = ttk.Button(self.mainframe, text=".", style="botones_restantes.TButton", command=lambda: self.ingresar_valores('.'))
        boton_abrir_parentesis = ttk.Button(self.mainframe, text="(", style="botones_restantes.TButton", command=lambda: self.ingresar_valores('('))
        boton_cerrar_parentesis = ttk.Button(self.mainframe, text=")", style="botones_restantes.TButton", command=lambda: self.ingresar_valores(')'))
        boton_division = ttk.Button(self.mainframe, text=chr(247), style="botones_restantes.TButton", command=lambda: self.ingresar_valores('/'))
        boton_multiplicar = ttk.Button(self.mainframe, text="*", style="botones_restantes.TButton", command=lambda: self.ingresar_valores('*'))
        boton_suma = ttk.Button(self.mainframe, text="+", style="botones_restantes.TButton", command=lambda: self.ingresar_valores('+'))
        boton_menos = ttk.Button(self.mainframe, text="-", style="botones_restantes.TButton", command=lambda: self.ingresar_valores('-'))
        boton_raizcuadrada = ttk.Button(self.mainframe, text="√", style="botones_restantes.TButton", command=lambda: self.ingresar_valores('sqrt('))
        boton_potencia = ttk.Button(self.mainframe, text="^", style="botones_restantes.TButton", command=lambda: self.ingresar_valores('**'))

        # Botones de funciones trigonométricas
        boton_sin = ttk.Button(self.mainframe, text="sin", style="botones_restantes.TButton", command=lambda: self.ingresar_valores('sin('))
        boton_cos = ttk.Button(self.mainframe, text="cos", style="botones_restantes.TButton", command=lambda: self.ingresar_valores('cos('))
        boton_tan = ttk.Button(self.mainframe, text="tan", style="botones_restantes.TButton", command=lambda: self.ingresar_valores('tan('))

        # Colocar los botones en la pantalla
        boton_abrir_parentesis.grid(column=0, row=4, sticky=W + N + E + S)
        boton_cerrar_parentesis.grid(column=1, row=4, sticky=W + N + E + S)
        boton_euler.grid(column=2, row=4, sticky=W + N + E + S)
        boton_borrar.grid(column=3, row=4, sticky=W + N + E + S)
        boton7.grid(column=0, row=5, sticky=W + N + E + S)
        boton8.grid(column=1, row=5, sticky=W + N + E + S)
        boton9.grid(column=2, row=5, sticky=W + N + E + S)
        boton_division.grid(column=3, row=5, sticky=W + N + E + S)
        boton4.grid(column=0, row=6, sticky=W + N + E + S)
        boton5.grid(column=1, row=6, sticky=W + N + E + S)
        boton6.grid(column=2, row=6, sticky=W + N + E + S)
        boton_multiplicar.grid(column=3, row=6, sticky=W + N + E + S)
        boton1.grid(column=0, row=7, sticky=W + N + E + S)
        boton2.grid(column=1, row=7, sticky=W + N + E + S)
        boton3.grid(column=2, row=7, sticky=W + N + E + S)
        boton_suma.grid(column=3, row=7, sticky=W + N + E + S)
        boton0.grid(column=0, row=8, sticky=W + N + E + S)
        boton_punto.grid(column=1, row=8, sticky=W + N + E + S)
        boton_menos.grid(column=2, row=8, sticky=W + N + E + S)
        boton_raizcuadrada.grid(column=3, row=8, sticky=W + N + E + S)
        boton_sin.grid(column=0, row=9, sticky=W + N + E + S)
        boton_cos.grid(column=1, row=9, sticky=W + N + E + S)
        boton_tan.grid(column=2, row=9, sticky=W + N + E + S)
        boton_potencia.grid(column=3, row=9, sticky=W + N + E + S)

        # Configuración de estilo de los botones
        for child in self.mainframe.winfo_children():
            child.grid_configure(ipady=10, padx=1, pady=1)

    # Ingresar valores en el campo de entrada
    def ingresar_valores(self, tecla):
        current = self.gx.get()
        self.gx.set(current + tecla)

    def borrar(self):
        current = self.gx.get()
        self.gx.set(current[:-1])

    def calcular_punto_fijo(self):
        try:
            # Reemplazar 'e' con 'math.e' para la evaluación
            gx_expr = self.gx.get().replace('e', 'math.e')
            # Reemplazar funciones trigonométricas con sus equivalentes de math
            for func in ['sin', 'cos', 'tan', 'sqrt']:
                gx_expr = gx_expr.replace(func, f'math.{func}')
            
            g = lambda x: eval(gx_expr)
            x0 = float(self.x0.get())
            tol = float(self.tolerancia.get())
            max_iter = 100
            
            for i in range(max_iter):
                x1 = g(x0)
                if abs(x1 - x0) < tol:
                    self.resultado.set(f"La solución es x = {x1:.6f} después de {i+1} iteraciones.")
                    return
                x0 = x1
            
            self.resultado.set("El método no convergió después de 100 iteraciones.")
        except ValueError:
            self.resultado.set("Error: Asegúrese de ingresar valores numéricos válidos para x0 y tolerancia.")
        except ZeroDivisionError:
            self.resultado.set("Error: División por cero en la función g(x).")
        except OverflowError:
            self.resultado.set("Error: Desbordamiento numérico. La función puede estar divergiendo.")
        except Exception as e:
            self.resultado.set(f"Error: {str(e)}")

# Crear la raíz y ejecutar la app
root = tk.Tk()
app = PuntoFijoApp(root)
root.mainloop()