from tkinter import Tk
import vista


class Controlador:
    def __init__(self, root):
        self.root_controlador = root
        self.vista_obj = vista.Ventana(self.root_controlador)


if __name__ == "__main__":
    root_tk = Tk()
    app = Controlador(root_tk)

    root_tk.mainloop()
