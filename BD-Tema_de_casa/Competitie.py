import tkinter
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import re

import cx_Oracle

connection = cx_Oracle.connect("alexm", "alexm", "localhost/xe")


class Competitie:
    def __init__(self, window, color, uoi):
        self.window = window
        self.NumeCompetitie = StringVar()
        self.Tip = StringVar()
        self.NumarTrofeeIndividuale = StringVar()
        self.NumarTrofeeColective = StringVar()
        self.NumarLigaComp = StringVar()
        self.Grupe_nationale_ID_FKComp = StringVar()
        self.ID_Liga_FKComp = StringVar()

        self.uoi = uoi

        self.buttonOK = Button(self.window, text="Ok", font=('Times New Roman', 14, 'bold'), relief=RAISED, height=1,
                               width=10, padx=50, pady=0, bd=4, bg='lavender', command=self.UpdateorInsert)
        self.buttonOK.grid(row=7, column=0)
        self.buttonClear = Button(self.window, text="Clear", font=('Times New Roman', 14, 'bold'), relief=RAISED,
                                  height=1,
                                  width=10, padx=50, pady=0, bd=4, bg='lavender', command=self.clearCompetitie)
        self.buttonClear.grid(row=7, column=1)

        self.labelNumeCompetitie = Label(self.window, font=('Times New Roman', 12, 'bold'), text='Nume competitie',
                                         padx=2,
                                         pady=2, bg=color)
        self.labelNumeCompetitie.grid(row=0, column=0, sticky=W)
        self.txtNumeCompetitie = Entry(self.window, font=('Times New Roman', 12, 'bold'),
                                       textvariable=self.NumeCompetitie,
                                       width=32)
        self.txtNumeCompetitie.grid(row=0, column=1, sticky=W)

        self.labelTip = Label(self.window, font=('Times New Roman', 12, 'bold'), text='Tip', padx=2,
                              pady=2, bg=color)
        self.labelTip.grid(row=1, column=0, sticky=W)
        self.txtTip = Entry(self.window, font=('Times New Roman', 12, 'bold'), textvariable=self.Tip,
                            width=32)
        self.txtTip.grid(row=1, column=1, sticky=W)

        self.labelNumarTrofeeIndividuale = Label(self.window, font=('Times New Roman', 12, 'bold'),
                                                 text='Numar trofee individuale',
                                                 padx=2,
                                                 pady=2, bg=color)
        self.labelNumarTrofeeIndividuale.grid(row=2, column=0, sticky=W)
        self.txtNumarTrofeeIndividuale = Entry(self.window, font=('Times New Roman', 12, 'bold'),
                                               textvariable=self.NumarTrofeeIndividuale,
                                               width=32)
        self.txtNumarTrofeeIndividuale.grid(row=2, column=1, sticky=W)

        self.labelNumarTrofeeColective = Label(self.window, font=('Times New Roman', 12, 'bold'),
                                               text='Numar trofee colective', padx=2,
                                               pady=2, bg=color)
        self.labelNumarTrofeeColective.grid(row=3, column=0, sticky=W)
        self.txtNumarTrofeeColective = Entry(self.window, font=('Times New Roman', 12, 'bold'),
                                             textvariable=self.NumarTrofeeColective,
                                             width=32)
        self.txtNumarTrofeeColective.grid(row=3, column=1, sticky=W)

        self.labelNumarLigaComp = Label(self.window, font=('Times New Roman', 12, 'bold'),
                                        text='Numar liga', padx=2,
                                        pady=2, bg=color)
        self.labelNumarLigaComp.grid(row=4, column=0, sticky=W)
        self.txtNumarLigaComp = Entry(self.window, font=('Times New Roman', 12, 'bold'),
                                      textvariable=self.NumarLigaComp,
                                      width=32)
        self.txtNumarLigaComp.grid(row=4, column=1, sticky=W)

        self.labelGrupe_nationale_ID_FKComp = Label(self.window, font=('Times New Roman', 12, 'bold'),
                                                    text='Grupe_nationale_ID',
                                                    padx=2,
                                                    pady=2, bg=color)
        self.labelGrupe_nationale_ID_FKComp.grid(row=5, column=0, sticky=W)
        self.txtGrupe_nationale_ID_FKComp = ttk.Combobox(self.window, width=40,
                                                         textvariable=self.Grupe_nationale_ID_FKComp,
                                                         state='readonly')
        results = connection.cursor()
        query = "SELECT Grupe_nationale_ID FROM Grupe_nationale"
        results.execute(query)
        for i in results:
            print(i)
            self.txtGrupe_nationale_ID_FKComp['values'] = (*self.txtGrupe_nationale_ID_FKComp['values'], i)
        self.txtGrupe_nationale_ID_FKComp.grid(row=5, column=1)
        self.txtGrupe_nationale_ID_FKComp.current()

        self.labelID_Liga_FKComp = Label(self.window, font=('Times New Roman', 12, 'bold'),
                                         text='ID_Liga',
                                         padx=2,
                                         pady=2, bg=color)
        self.labelID_Liga_FKComp.grid(row=6, column=0, sticky=W)
        self.txtID_Liga_FKComp = ttk.Combobox(self.window, width=40,
                                              textvariable=self.ID_Liga_FKComp,
                                              state='readonly')
        query = "SELECT id_liga FROM liga_de_fotbal"
        results.execute(query)
        for i in results:
            print(i)
            self.txtID_Liga_FKComp['values'] = (*self.txtID_Liga_FKComp['values'], i)
        self.txtID_Liga_FKComp.grid(row=6, column=1)
        self.txtID_Liga_FKComp.current()

    def clearCompetitie(self):
        self.txtNumeCompetitie.delete(0, END)
        self.txtTip.delete(0, END)
        self.txtNumarTrofeeIndividuale.delete(0, END)
        self.txtNumarTrofeeColective.delete(0, END)
        self.txtNumarLigaComp.delete(0, END)
        self.txtGrupe_nationale_ID_FKComp.set("")
        self.txtID_Liga_FKComp.set("")

    def verifyConstraints(self):
        return (len(self.NumeCompetitie.get()) > 8 and re.match(
            "^[A-Za-z0-9 ]+$",
            self.NumeCompetitie.get()) and
                (self.Tip.get() == "Echipe de club" or self.Tip.get() == "Echipe nationale") and
                len(self.NumarTrofeeColective.get()) > 0 and
                self.txtGrupe_nationale_ID_FKComp.get() != "" and
                self.txtID_Liga_FKComp != "")

    def addCompetitie(self):
        results = connection.cursor()
        command = "INSERT INTO competitie VALUES('%s','%s', %s, %s, '%s', %s, %s)" % (
            self.NumeCompetitie.get(), self.Tip.get(), self.NumarTrofeeIndividuale.get(),
            self.NumarTrofeeColective.get(),
            self.NumarLigaComp.get(), self.txtGrupe_nationale_ID_FKComp.get(), self.txtID_Liga_FKComp.get())
        if self.verifyConstraints():
            results.execute(command)
            tkinter.messagebox.showinfo("Confirmare INSERT", "S-a adaugat!")
        else:
            tkinter.messagebox.showerror("Eroare INSERT", "Reintroduceti date valide!")
        connection.commit()

    def updateCompetitie(self):
        results = connection.cursor()
        command = "UPDATE competitie SET tip='%s', numar_trofee_individuale=%s, numar_trofee_colective=%s, numar_liga='%s', Grupe_nationale_ID=%s, id_liga=%s WHERE nume_competitie= '%s'" % (
            self.Tip.get(), self.NumarTrofeeIndividuale.get(), self.NumarTrofeeColective.get(), self.NumarLigaComp.get(), self.txtGrupe_nationale_ID_FKComp.get(), self.txtID_Liga_FKComp.get(), self.NumeCompetitie)
        if self.verifyConstraints():
            results.execute(command)
            tkinter.messagebox.showinfo("Confirmare", "S-a modificat inregistrarea!")
        else:
            tkinter.messagebox.showerror("Eroare UPDATE", "Reintroduceti date valide!")
        connection.commit()

    def UpdateorInsert(self):
        if self.uoi == 1:
            return self.addCompetitie()
        if self.uoi == 2:
            return self.updateCompetitie()