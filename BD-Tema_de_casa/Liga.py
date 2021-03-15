import tkinter
from tkinter import *
from tkinter import messagebox
import re
import cx_Oracle

connection = cx_Oracle.connect("alexm", "alexm", "localhost/xe")


class Liga:
    def __init__(self, window, color, uoi):
        self.window = window
        self.NumarLiga = StringVar()
        self.NumarEchipe = StringVar()
        self.NumarCompetitii = StringVar()
        self.TaraLiga = StringVar()

        self.uoi = uoi

        self.buttonOK = Button(self.window, text="Ok", font=('Times New Roman', 14, 'bold'), relief=RAISED, height=1,
                               width=10, padx=50, pady=0, bd=4, bg='lavender', command=self.UpdateorInsert)
        self.buttonOK.grid(row=4, column=0)
        self.buttonClear = Button(self.window, text="Clear", font=('Times New Roman', 14, 'bold'), relief=RAISED,
                                  height=1,
                                  width=10, padx=50, pady=0, bd=4, bg='lavender', command=self.clearLiga)
        self.buttonClear.grid(row=4, column=1)

        self.labelNumarLiga = Label(self.window, font=('Times New Roman', 12, 'bold'), text='Numar liga', padx=2,
                                    pady=2, bg=color)
        self.labelNumarLiga.grid(row=0, column=0, sticky=W)
        self.txtNumarLiga = Entry(self.window, font=('Times New Roman', 12, 'bold'), textvariable=self.NumarLiga,
                                  width=32)
        self.txtNumarLiga.grid(row=0, column=1, sticky=W)

        self.labelNumarEchipe = Label(self.window, font=('Times New Roman', 12, 'bold'), text='Numar echipe', padx=2,
                                      pady=2, bg=color)
        self.labelNumarEchipe.grid(row=1, column=0, sticky=W)
        self.txtNumarEchipe = Entry(self.window, font=('Times New Roman', 12, 'bold'), textvariable=self.NumarEchipe,
                                    width=32)
        self.txtNumarEchipe.grid(row=1, column=1, sticky=W)

        self.labelNumarCompetitii = Label(self.window, font=('Times New Roman', 12, 'bold'), text='Numar competitii',
                                          padx=2,
                                          pady=2, bg=color)
        self.labelNumarCompetitii.grid(row=2, column=0, sticky=W)
        self.txtNumarCompetitii = Entry(self.window, font=('Times New Roman', 12, 'bold'),
                                        textvariable=self.NumarCompetitii,
                                        width=32)
        self.txtNumarCompetitii.grid(row=2, column=1, sticky=W)

        self.labelTaraLiga = Label(self.window, font=('Times New Roman', 12, 'bold'), text='Tara', padx=2,
                                   pady=2, bg=color)
        self.labelTaraLiga.grid(row=3, column=0, sticky=W)
        self.txtTaraLiga = Entry(self.window, font=('Times New Roman', 12, 'bold'), textvariable=self.TaraLiga,
                                 width=32)
        self.txtTaraLiga.grid(row=3, column=1, sticky=W)

    def clearLiga(self):
        self.txtNumarLiga.delete(0, END)
        self.txtNumarEchipe.delete(0, END)
        self.txtNumarCompetitii.delete(0, END)
        self.txtTaraLiga.delete(0, END)

    def verifyConstraints(self):
        return (self.NumarLiga.get() == "Liga 1" and (
                int(self.NumarEchipe.get()) >= 16 and int(self.NumarEchipe.get()) <= 20) and (
                        int(self.NumarCompetitii.get()) >= 1 and int(self.NumarCompetitii.get()) <= 3) and len(
            self.TaraLiga.get()) >= 3 and re.match("^[A-Za-z]+[ A-Za-z]+$", self.TaraLiga.get()))

    def addLiga(self):
        results = connection.cursor()
        command = "INSERT INTO liga_de_fotbal VALUES(NULL, '%s', %s, %s, '%s')" % (
            self.NumarLiga.get(), self.NumarEchipe.get(), self.NumarCompetitii.get(), self.TaraLiga.get())
        if self.verifyConstraints():
            results.execute(command)
            tkinter.messagebox.showinfo("Confirmare INSERT", "S-a adaugat!")
        else:
            tkinter.messagebox.showerror("Eroare INSERT", "Reintroduceti date valide!")
        connection.commit()

    def updateLiga(self):
        results = connection.cursor()
        command = "UPDATE liga_de_fotbal SET numar_liga='%s', numar_echipe=%s, numar_competitii=%s WHERE tara='%s'" % (
        self.NumarLiga.get(), self.NumarEchipe.get(), self.NumarCompetitii.get(), self.TaraLiga.get())
        if self.verifyConstraints():
            results.execute(command)
            tkinter.messagebox.showinfo("Confirmare", "S-a modificat inregistrarea!")
        else:
            tkinter.messagebox.showerror("Eroare UPDATE", "Reintroduceti date valide!")
        connection.commit()

    def UpdateorInsert(self):
        if self.uoi == 1:
            return self.addLiga()
        if self.uoi == 2:
            return self.updateLiga()
