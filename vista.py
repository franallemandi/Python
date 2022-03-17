from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from PIL import ImageTk, Image
import os
from modelo import Bbdd


class Ventana:
    def __init__(self, window):
        # Llamo a función de inicio
        con = self.llamada()
        # Líneas para la imagen de fondo
        self.BASE_DIR = os.path.dirname((os.path.abspath(__file__)))
        self.ruta = os.path.join(self.BASE_DIR, "img", "futbol.jpg")
        # Defino la ventana principal de la aplicación con su fondo
        self.root = window
        self.image2 = Image.open(self.ruta)
        self.image1 = ImageTk.PhotoImage(self.image2)
        self.background_label = ttk.Label(self.root, image=self.image1)
        self.background_label.place(x=0, y=0, relwidth=1, relheight=0.4)
        # Fijo el tamaño de la ventana y el título
        self.root.resizable(width=False, height=False)
        self.root.title("Centro de Estadísticas del Fútbol Argentino")
        # Defino las variables que voy a usar
        self.id = StringVar()
        self.cat = ["A", "B"]
        self.eq_a = [
            "Boca Juniors",
            "River Plate",
            "Independiente",
            "Racing",
            "San Lorenzo",
            "Estudiantes LP",
            "Gimnasia LP",
            "Newell's",
            "Rosario Central",
            "Talleres",
            "Banfield",
            "Lanús",
            "Arsenal",
            "Central Córdoba",
            "Defensa y Justicia",
            "Platense",
            "Patronato",
            "Unión",
            "Atl. Tucumán",
            "Argentinos Jrs.",
            "Colón",
            "Sarmiento",
            "Vélez",
            "Aldosivi",
            "Godoy Cruz",
            "Huracán",
        ]
        self.l = StringVar()
        self.v = StringVar()
        self.gl = StringVar()
        self.gv = StringVar()
        self.al = StringVar()
        self.av = StringVar()
        self.rl = StringVar()
        self.rv = StringVar()
        # Creo las etiquetas, las entradas y los botones
        self.l_cat = ttk.Label(self.root, text="Categoría: ")
        self.l_l = ttk.Label(self.root, text="Equipo Local: ")
        self.l_v = ttk.Label(self.root, text="Equipo Visitante: ")
        self.l_gl = ttk.Label(self.root, text="Goles Local: ")
        self.l_gv = ttk.Label(self.root, text="Goles Visitante: ")
        self.l_al = ttk.Label(self.root, text="Amarillas Local: ")
        self.l_av = ttk.Label(self.root, text="Amarillas Visitante: ")
        self.l_rl = ttk.Label(self.root, text="Rojas Local: ")
        self.l_rv = ttk.Label(self.root, text="Rojas Visitante: ")
        self.l_x = ttk.Label(self.root, text="Buscar por equipo: ")

        self.e1 = ttk.Combobox(self.root, values=self.cat, width=2)
        self.e1.current(0)

        self.e2 = ttk.Combobox(self.root, values=self.eq_a, width=15)
        self.e3 = ttk.Combobox(self.root, values=self.eq_a, width=15)
        self.e4 = ttk.Entry(self.root, textvariable=self.gl, width=2)
        self.e5 = ttk.Entry(self.root, textvariable=self.gv, width=2)
        self.e6 = ttk.Entry(self.root, textvariable=self.al, width=15)
        self.e7 = ttk.Entry(self.root, textvariable=self.av, width=15)
        self.e8 = ttk.Entry(self.root, textvariable=self.rl, width=15)
        self.e9 = ttk.Entry(self.root, textvariable=self.rv, width=15)

        self.ex = ttk.Combobox(self.root, values=self.eq_a, width=15)

        self.b_agregar = ttk.Button(
            self.root,
            text="Insertar",
            command=lambda: self.fc_insertar(
                con,
                self.e1.get(),
                self.e2.get(),
                self.e3.get(),
                self.gl.get(),
                self.gv.get(),
                self.al.get(),
                self.av.get(),
                self.rl.get(),
                self.rv.get(),
            ),
        )
        self.b_borrar = ttk.Button(
            self.root, text="Borrar", command=lambda: self.fc_borrar(con)
        )
        self.b_consulta_a = ttk.Button(
            self.root,
            text="Datos Cat. A",
            command=lambda: self.fc_consultar(con, self.cat[0]),
        )
        self.b_consulta_b = ttk.Button(
            self.root,
            text="Datos Cat. B",
            command=lambda: self.fc_consultar(con, self.cat[1]),
        )
        self.b_editar = ttk.Button(
            self.root,
            text="Editar",
            command=lambda: self.fc_editar(
                con,
                self.e1.get(),
                self.e2.get(),
                self.e3.get(),
                self.gl.get(),
                self.gv.get(),
                self.al.get(),
                self.av.get(),
                self.rl.get(),
                self.rv.get(),
            ),
        )
        self.b_filtrar = ttk.Button(
            self.root,
            text="Buscar",
            command=lambda: self.fc_filtrar(con, self.ex.get()),
        )
        self.b_salir = ttk.Button(self.root, text="Salir", command=self.salir)
        # Creo el treeview
        self.style = ttk.Style(self.root)
        self.style.theme_use("clam")
        self.style.configure(
            "Treeview",
            background="#267830",
            fieldbackground="#5FE884",
            foreground="white",
        )
        self.style.configure(
            "Treeview.Heading",
            background="#215227",
            fieldbackground="#5FE884",
            foreground="white",
            font=("Calibri", 10, "bold"),
        )
        self.style.configure(
            "Treeview.Heading.#3",
            background="yellow",
            fieldbackground="yellow",
            foreground="black",
        )
        self.tree = ttk.Treeview(self.root)
        self.tree["columns"] = (
            "id",
            "cat",
            "l",
            "v",
            "gl",
            "gv",
            "al",
            "av",
            "rl",
            "rv",
        )
        self.tree.column("#0", width=1, minwidth=1, anchor=W)
        self.tree.column("id", width=30, minwidth=30)
        self.tree.column("cat", width=80, minwidth=80, anchor=CENTER)
        self.tree.column("l", width=120, minwidth=120, anchor=CENTER)
        self.tree.column("v", width=120, minwidth=120, anchor=CENTER)
        self.tree.column("gl", width=80, minwidth=80, anchor=CENTER)
        self.tree.column("gv", width=100, minwidth=100, anchor=CENTER)
        self.tree.column("al", width=100, minwidth=100, anchor=CENTER)
        self.tree.column("av", width=100, minwidth=100, anchor=CENTER)
        self.tree.column("rl", width=80, minwidth=80, anchor=CENTER)
        self.tree.column("rv", width=100, minwidth=100, anchor=CENTER)

        self.tree.heading("id", text="ID")
        self.tree.heading("cat", text="Categoría")
        self.tree.heading("l", text="Local")
        self.tree.heading("v", text="Visitante")
        self.tree.heading("gl", text="Goles Local")
        self.tree.heading("gv", text="Goles Visita")
        self.tree.heading("al", text="Amarillas Local")
        self.tree.heading("av", text="Amarillas Visita")
        self.tree.heading("rl", text="Rojas Local")
        self.tree.heading("rv", text="Rojas Visita")

        self.tree.bind("<ButtonRelease-1>", self.selectItem)

        # Posiciono etiquetas, botones y controles
        self.l_cat.grid(column=1, row=1)
        self.l_l.grid(column=3, row=1)
        self.l_v.grid(column=5, row=1)
        self.l_gl.grid(column=3, row=2)
        self.l_gv.grid(column=5, row=2)
        self.l_al.grid(column=3, row=3)
        self.l_av.grid(column=5, row=3)
        self.l_rl.grid(column=3, row=4)
        self.l_rv.grid(column=5, row=4)
        self.l_x.grid(column=7, row=7)

        self.e1.grid(column=2, row=1)
        self.e2.grid(column=4, row=1)
        self.e3.grid(column=6, row=1)
        self.e4.grid(column=4, row=2)
        self.e5.grid(column=6, row=2)
        self.e6.grid(column=4, row=3)
        self.e7.grid(column=6, row=3)
        self.e8.grid(column=4, row=4)
        self.e9.grid(column=6, row=4)
        self.ex.grid(column=8, row=7)

        self.tree.grid(column=0, row=9, columnspan=15)
        self.b_agregar.grid(column=2, row=5, pady=10)
        self.b_borrar.grid(column=3, row=5)
        self.b_editar.grid(column=4, row=5)
        self.b_consulta_a.grid(column=2, row=7)
        self.b_consulta_b.grid(column=4, row=7)
        self.b_filtrar.grid(column=9, row=7)
        self.b_salir.grid(column=9, row=11)

    # Defino función para salir del programa
    def salir(
        self,
    ):
        self.root.destroy()

    # Defino función para agregar partido
    def fc_insertar(self, con, cat, l, v, gl, gv, al, av, rl, rv):
        ret, msg = self.objeto_bbdd.insertar(con, cat, l, v, gl, gv, al, av, rl, rv)
        if ret:
            self.fc_consultar(con, cat)
        self.mensaje(msg)

    # Defino función para mostrar los partidos cargados de cada categoría
    def fc_consultar(self, con, cat):
        resultado = self.objeto_bbdd.consultar(con, cat)
        for i in self.tree.get_children():
            self.tree.delete(i)
        for x in resultado:
            self.tree.insert(
                "",
                "end",
                values=(x[0], x[1], x[2], x[3], x[4], x[5], x[6], x[7], x[8], x[9]),
            )

    # Defino función para borrar registros
    def fc_borrar(self, con):
        item_2 = self.tree.focus()
        item_3 = self.tree.item(item_2)
        if item_2:
            self.objeto_bbdd.borrar(con, item_3["values"][0])
            self.tree.delete(item_2)
            self.mensaje("Partido borrado!")
        else:
            self.mensaje("No se seleccionó registro.")

    # Defino función para editar partidos
    def fc_editar(self, con, cat, l, v, gl, gv, al, av, rl, rv):
        item_2 = self.tree.focus()
        item_3 = self.tree.item(item_2)
        cadena1 = gl
        cadena2 = gv
        if self.objeto_bbdd.validar_num(cadena1):
            if self.objeto_bbdd.validar_num(cadena2):
                try:
                    self.objeto_bbdd.editar(
                        con,
                        cat,
                        l,
                        v,
                        gl,
                        gv,
                        al,
                        av,
                        rl,
                        rv,
                        item_3["values"][0],
                    )
                    self.fc_consultar(con, cat)
                    self.mensaje("Partido editado!")
                except IndexError:
                    self.mensaje("No se seleccionó registro.")
            else:
                self.mensaje("Ingrese un número en el campo de goles visitante")
        else:
            self.mensaje("Ingrese un número en el campo de goles local")

    # Defino función para filtrar búsqueda por equipo
    def fc_filtrar(self, con, equipo_seleccionado):
        resultado = self.objeto_bbdd.filtrar(con, equipo_seleccionado)
        for i in self.tree.get_children():
            self.tree.delete(i)
        if resultado:
            for x in resultado:
                self.tree.insert(
                    "",
                    "end",
                    values=(x[0], x[1], x[2], x[3], x[4], x[5], x[6], x[7], x[8], x[9]),
                )
        else:
            self.mensaje("No hay regsitros de este equipo.")

    # Defino función para cuando selecciono un item
    def selectItem(self, a):
        item_2 = self.tree.focus()
        if item_2:
            item_3 = self.tree.item(item_2)
            self.e1.delete(0, END)
            self.e1.insert(0, item_3["values"][1])
            self.e2.delete(0, END)
            self.e2.insert(0, item_3["values"][2])
            self.e3.delete(0, END)
            self.e3.insert(0, item_3["values"][3])
            self.e4.delete(0, END)
            self.e4.insert(0, item_3["values"][4])
            self.e5.delete(0, END)
            self.e5.insert(0, item_3["values"][5])
            self.e6.delete(0, END)
            self.e6.insert(0, item_3["values"][6])
            self.e7.delete(0, END)
            self.e7.insert(0, item_3["values"][7])
            self.e8.delete(0, END)
            self.e8.insert(0, item_3["values"][8])
            self.e9.delete(0, END)
            self.e9.insert(0, item_3["values"][9])

    # Defino función para notificaciones
    def mensaje(self, texto):
        messagebox.showinfo("Atención!", texto)

    # Defino función para llamar a las funciones iniciales en modelo e instanciar sus clasess
    def llamada(
        self,
    ):
        self.objeto_bbdd = Bbdd()
        self.objeto_bbdd.crear_bbdd()
        con = self.objeto_bbdd.conectar()
        self.objeto_bbdd.crear_tabla(con)
        return con
