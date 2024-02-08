from tkinter import *

window = Tk()

class Application():
    def __init__(self):
        self.window = window
        self.tela()
        self.frames()
        window.mainloop()
    def tela(self):
        self.window.title("Cotação RPA")
        self.window.configure(background='black')
        self.window.geometry("800x600")
        #self.window.resizable() #RESPONSIVIDADE
        #self.window.maxsize()
        #self.window.minsize()
    def frames(self):
        self.frame_1 = Frame(self.window, border=4, bg='orange')
        self.frame_1.place(relx=0.05, rely=0.05, relwidth=0.90, relheight=0.90)
        self.frame_1.grid()
    # def botoes():
    #     self.bt_registar = Button(self.frame_1)
    #     self.bt_registar.place

Application()
