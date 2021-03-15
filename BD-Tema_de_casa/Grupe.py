import tkinter
from tkinter import *
from tkinter import messagebox

import cx_Oracle

connection = cx_Oracle.connect("alexm", "alexm", "localhost/xe")


class Grupe:
    def __init__(self, window, color, uoi):
        self.window = window

        self.numar_echipe_nationale = StringVar()
        self.continent = StringVar()

        self.uoi = uoi

        self.buttonOK = Button(self.window, text="Ok", font=('Times New Roman', 14, 'bold'), relief=RAISED, height=1,
                               width=10, padx=50, pady=0, bd=4, bg='lavender', command=self.UpdateorInsert)
        self.buttonOK.grid(row=7, column=0)
        self.buttonClear = Button(self.window, text="Clear", font=('Times New Roman', 14, 'bold'), relief=RAISED,
                                  height=1,
                                  width=10, padx=50, pady=0, bd=4, bg='lavender', command=self.clearGrupe)
        self.buttonClear.grid(row=7, column=1)

        self.labelnumar_echipe_nationale = Label(self.window, font=('Times New Roman', 12, 'bold'),
                                                 text='Numar echipe nationale',
                                                 padx=2,
                                                 pady=2, bg=color)
        self.labelnumar_echipe_nationale.grid(row=0, column=0, sticky=W)
        self.txtnumar_echipe_nationale = Entry(self.window, font=('Times New Roman', 12, 'bold'),
                                               textvariable=self.numar_echipe_nationale,
                                               width=32)
        self.txtnumar_echipe_nationale.grid(row=0, column=1, sticky=W)

        self.labelcontinent = Label(self.window, font=('Times New Roman', 12, 'bold'), text='Continent', padx=2,
                                    pady=2, bg=color)
        self.labelcontinent.grid(row=1, column=0, sticky=W)
        self.txtcontinent = Entry(self.window, font=('Times New Roman', 12, 'bold'), textvariable=self.continent,
                                  width=32)
        self.txtcontinent.grid(row=1, column=1, sticky=W)

    def clearGrupe(self):
        self.txtnumar_echipe_nationale.delete(0, END)
        self.txtcontinent.delete(0, END)

    def verifyConstraints(self):
        return (
                self.continent.get() == "Europa" or self.continent.get() == "Asia" or
                self.continent.get() == "Africa" or self.continent.get() == "Oceania" or
                self.continent.get() == "America" and len(self.numar_echipe_nationale.get()) > 0)

    def addGrupe(self):
        results = connection.cursor()
        if self.verifyConstraints():
            results.execute("INSERT INTO Grupe_nationale VALUES(NULL, '%s', '%s')" % (
                self.numar_echipe_nationale.get(), self.continent.get()))
            tkinter.messagebox.showinfo("Confirmare INSERT", "S-a adaugat!")
        else:
            tkinter.messagebox.showerror("Eroare INSERT",
                                         "Nu ai introdus un continent existent!\nHint: Europa, America, Asia, Africa, "
                                         "Oceania_si_Australia")
        connection.commit()

    def updateGrupe(self):
        results = connection.cursor()
        command = "UPDATE Grupe_nationale SET numar_echipe_nationale=%s WHERE continent='%s'" % (
        self.numar_echipe_nationale.get(), self.continent.get())
        if self.verifyConstraints():
            results.execute(command)
            tkinter.messagebox.showinfo("Confirmare UPDATE", "S-a modificat inregistrarea!")
        else:
            tkinter.messagebox.showerror("Eroare UPDATE", "Reintroduceti date valide!")
        connection.commit()

    def UpdateorInsert(self):
        if self.uoi == 1:
            return self.addGrupe()
        if self.uoi == 2:
            return self.updateGrupe()
