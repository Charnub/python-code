from tkinter import *
class Mastermind(Frame):
    def red(self):
        print("Red")
    def green(self):
        print("Green")
    def yellow(self):
        print("Yellow")
    def blue(self):
        print("Blue")
    def brown(self):
        print("Brown")
    def indigo(self):
        print("Indigo")
    def purple(self):
        print("Purple")

    def createColours(self):
        self.Red = Button(self)
        self.Red["text"] = "Red"
        self.Red["fg"]   = "red"
        self.Red["command"] =  self.red
        self.Red.pack({"side": "left"})

        self.Green = Button(self)
        self.Green["text"] = "Green"
        self.Green["fg"]   = "green"
        self.Green["command"] =  self.green
        self.Green.pack({"side": "left"})

        self.Yellow = Button(self)
        self.Yellow["text"] = "Yellow"
        self.Yellow["fg"]   = "yellow"
        self.Yellow["command"] =  self.yellow
        self.Yellow.pack({"side": "left"})

        self.Blue = Button(self)
        self.Blue["text"] = "Blue"
        self.Blue["fg"]   = "blue"
        self.Blue["command"] =  self.blue
        self.Blue.pack({"side": "left"})

        self.Brown = Button(self)
        self.Brown["text"] = "Brown"
        self.Brown["fg"]   = "brown"
        self.Brown["command"] =  self.brown
        self.Brown.pack({"side": "left"})

        self.Indigo = Button(self)
        self.Indigo["text"] = "Indigo"
        self.Indigo["fg"]   = "indigo"
        self.Indigo["command"] =  self.indigo
        self.Indigo.pack({"side": "left"})

        self.Purple = Button(self)
        self.Purple["text"] = "Purple"
        self.Purple["fg"]   = "purple"
        self.Purple["command"] =  self.purple
        self.Purple.pack({"side": "left"})

    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.createColours()

root = Tk()
app = Mastermind(master=root)
app.mainloop()
