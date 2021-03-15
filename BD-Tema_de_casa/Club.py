import tkinter
from tkinter import *
from tkinter import ttk
import re
from tkinter import messagebox

import cx_Oracle

connection = cx_Oracle.connect("alexm", "alexm", "localhost/xe")


class Club:
    def __init__(self, window, color, uoi):
        self.window = window
        self.NumeEchipa = StringVar()
        self.Oras = StringVar()
        self.NumarJucatori = StringVar()
        self.AntrenorPrincipal = StringVar()
        self.ID_Liga_FK = StringVar()

        self.uoi = uoi

        self.labelNumeEchipa = Label(self.window, font=('Times New Roman', 12, 'bold'), text='Nume echipa', padx=2,
                                     pady=2, bg=color)
        self.labelNumeEchipa.grid(row=0, column=0, sticky=W)
        self.txtNumeEchipa = Entry(self.window, font=('Times New Roman', 12, 'bold'), textvariable=self.NumeEchipa,
                                   width=32)
        self.txtNumeEchipa.grid(row=0, column=1, sticky=W)

        self.labelOras = Label(self.window, font=('Times New Roman', 12, 'bold'), text='Oras', padx=2,
                               pady=2, bg=color)
        self.labelOras.grid(row=1, column=0, sticky=W)
        self.txtOras = Entry(self.window, font=('Times New Roman', 12, 'bold'), textvariable=self.Oras,
                             width=32)
        self.txtOras.grid(row=1, column=1, sticky=W)

        self.labelNumarJucatori = Label(self.window, font=('Times New Roman', 12, 'bold'), text='Numar jucatori ',
                                        padx=2,
                                        pady=2, bg=color)
        self.labelNumarJucatori.grid(row=2, column=0, sticky=W)
        self.txtNumarJucatori = Entry(self.window, font=('Times New Roman', 12, 'bold'),
                                      textvariable=self.NumarJucatori,
                                      width=32)
        self.txtNumarJucatori.grid(row=2, column=1, sticky=W)

        self.labelAntrenorPrincipal = Label(self.window, font=('Times New Roman', 12, 'bold'),
                                            text='Antrenor principal', padx=2,
                                            pady=2, bg=color)
        self.labelAntrenorPrincipal.grid(row=3, column=0, sticky=W)
        self.txtAntrenorPrincipal = Entry(self.window, font=('Times New Roman', 12, 'bold'),
                                          textvariable=self.AntrenorPrincipal,
                                          width=32)
        self.txtAntrenorPrincipal.grid(row=3, column=1, sticky=W)

        self.labelID_Liga = Label(self.window, font=('Times New Roman', 12, 'bold'), text='ID_Liga', padx=2,
                                  pady=2, bg=color)
        self.labelID_Liga.grid(row=4, column=0, sticky=W)
        self.txtID_Liga_FK = ttk.Combobox(self.window, width=40, textvariable=self.ID_Liga_FK, state='readonly')
        results = connection.cursor()
        query = "SELECT id_liga FROM liga_de_fotbal"
        results.execute(query)
        for i in results:
            print(i)
            self.txtID_Liga_FK['values'] = (*self.txtID_Liga_FK['values'], i)
        self.txtID_Liga_FK.grid(row=4, column=1)
        self.txtID_Liga_FK.current()

        self.buttonOK = Button(self.window, text="Ok", font=('Times New Roman', 14, 'bold'), relief=RAISED, height=1,
                               width=10, padx=50, pady=0, bd=4, bg='lavender', command=self.UpdateorInsert)
        self.buttonOK.grid(row=5, column=0)
        self.buttonClear = Button(self.window, text="Clear", font=('Times New Roman', 14, 'bold'), relief=RAISED,
                                  height=1,
                                  width=10, padx=50, pady=0, bd=4, bg='lavender', command=self.clearClub)
        self.buttonClear.grid(row=5, column=1)

    def clearClub(self):
        self.txtNumeEchipa.delete(0, END)
        self.txtOras.delete(0, END)
        self.txtNumarJucatori.delete(0, END)
        self.txtAntrenorPrincipal.delete(0, END)
        self.txtID_Liga_FK.set("")

    def verifyConstraints(self):
        return (len(self.NumeEchipa.get()) > 8 and re.match("^[A-Za-z0-9 ]+$", self.NumeEchipa.get()) and (
                len(self.Oras.get()) > 3) and re.match("^[A-Za-z ]+$", self.Oras.get()) and
                (int(self.NumarJucatori.get()) >= 11 and int(self.NumarJucatori.get()) <= 38) and len(
                    self.AntrenorPrincipal.get()) > 5 and re.match("^[A-Za-z ]+$",
                                                                   self.AntrenorPrincipal.get()) and self.txtID_Liga_FK.get() != "")

    def addClub(self):
        results = connection.cursor()
        command = "INSERT INTO echipa_de_club VALUES(NULL, '%s', '%s', %s, '%s', %s)" % (
            self.NumeEchipa.get(), self.Oras.get(), self.NumarJucatori.get(), self.AntrenorPrincipal.get(),
            self.txtID_Liga_FK.get())
        if self.verifyConstraints():
            results.execute(command)
            tkinter.messagebox.showinfo("Confirmare INSERT", "S-a adaugat!")
        else:
            tkinter.messagebox.showerror("Eroare INSERT", "Reintroduceti date valide!")
        connection.commit()

    def updateClub(self):
        results = connection.cursor()
        command = "UPDATE echipa_de_club SET oras='%s', numar_jucatori=%s, antrenor_principal='%s', id_liga=%s WHERE nume_echipa='%s'" % (
        self.Oras.get(), self.NumarJucatori.get(), self.AntrenorPrincipal.get(), self.txtID_Liga_FK.get(),
        self.NumeEchipa.get())
        if self.verifyConstraints():
            results.execute(command)
            tkinter.messagebox.showinfo("Confirmare", "S-a modificat inregistrarea!")
        else:
            tkinter.messagebox.showerror("Eroare UPDATE", "Reintroduceti date valide!")
        connection.commit()

    def UpdateorInsert(self):
        if self.uoi == 1:
            return self.addClub()
        if self.uoi == 2:
            return self.updateClub()
