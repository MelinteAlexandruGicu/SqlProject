import tkinter
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import re
import cx_Oracle

connection = cx_Oracle.connect("alexm", "alexm", "localhost/xe")


class Nationala:
    def __init__(self, window, color, uoi):
        self.window = window
        self.Tara = StringVar()
        self.NumarJucatoriConvocati = StringVar()
        self.NumeSelectioner = StringVar()
        self.Grupe_nationale_ID_FK = StringVar()
        self.uoi = uoi

        self.buttonOK = Button(self.window, text="Ok", font=('Times New Roman', 14, 'bold'), relief=RAISED, height=1,
                               width=10, padx=50, pady=0, bd=4, bg='lavender',
                               command=self.UpdateorInsert)
        self.buttonOK.grid(row=4, column=0)
        self.buttonClear = Button(self.window, text="Clear", font=('Times New Roman', 14, 'bold'), relief=RAISED,
                                  height=1,
                                  width=10, padx=50, pady=0, bd=4, bg='lavender', command=self.clearNationala)
        self.buttonClear.grid(row=4, column=1)

        self.labelTara = Label(self.window, font=('Times New Roman', 12, 'bold'), text='Tara', padx=2,
                               pady=2, bg=color)
        self.labelTara.grid(row=0, column=0, sticky=W)
        self.txtTara = Entry(self.window, font=('Times New Roman', 12, 'bold'), textvariable=self.Tara,
                             width=32)
        self.txtTara.grid(row=0, column=1, sticky=W)

        self.labelNumarJucatoriConvocati = Label(self.window, font=('Times New Roman', 12, 'bold'),
                                                 text='Numar jucatori convocati', padx=2,
                                                 pady=2, bg=color)
        self.labelNumarJucatoriConvocati.grid(row=1, column=0, sticky=W)
        self.txtNumarJucatoriConvocati = Entry(self.window, font=('Times New Roman', 12, 'bold'),
                                               textvariable=self.NumarJucatoriConvocati,
                                               width=32)
        self.txtNumarJucatoriConvocati.grid(row=1, column=1, sticky=W)

        self.labelNumeSelectioner = Label(self.window, font=('Times New Roman', 12, 'bold'), text='Nume selectioner',
                                          padx=2,
                                          pady=2, bg=color)
        self.labelNumeSelectioner.grid(row=2, column=0, sticky=W)
        self.txtNumeSelectioner = Entry(self.window, font=('Times New Roman', 12, 'bold'),
                                        textvariable=self.NumeSelectioner,
                                        width=32)
        self.txtNumeSelectioner.grid(row=2, column=1, sticky=W)

        self.Grupe_nationale_ID_FK = Label(self.window, font=('Times New Roman', 12, 'bold'), text='Grupe_nationale_ID',
                                           padx=2,
                                           pady=2, bg=color)
        self.Grupe_nationale_ID_FK.grid(row=3, column=0, sticky=W)
        self.txtGrupe_nationale_ID_FK = ttk.Combobox(self.window, width=40, textvariable=self.Grupe_nationale_ID_FK,
                                                     state='readonly')
        results = connection.cursor()
        query = "SELECT Grupe_nationale_ID FROM Grupe_nationale"
        results.execute(query)
        for i in results:
            print(i)
            self.txtGrupe_nationale_ID_FK['values'] = (*self.txtGrupe_nationale_ID_FK['values'], i)

        self.txtGrupe_nationale_ID_FK.grid(row=3, column=1)
        self.txtGrupe_nationale_ID_FK.current()

    def clearNationala(self):
        self.txtTara.delete(0, END)
        self.txtNumarJucatoriConvocati.delete(0, END)
        self.txtNumeSelectioner.delete(0, END)
        self.txtGrupe_nationale_ID_FK.set("")

    def verifyConstraints(self):
        return (len(self.Tara.get()) >= 3 and re.match("^[A-Z]+[ A-Z]+$", self.Tara.get()) and
                int(self.NumarJucatoriConvocati.get()) >= 11 and int(
                    self.NumarJucatoriConvocati.get()) <= 32 and re.match("[A-Z]{1}[A-Za-z-]+ [A-Z]{1}[A-Za-z-]+$",
                                                                          self.NumeSelectioner.get()) and self.txtGrupe_nationale_ID_FK.get() != "")

    def addNationala(self):
        results = connection.cursor()
        command = "INSERT INTO echipa_nationala VALUES('%s', %s, '%s', %s)" % (
            self.Tara.get(), self.NumarJucatoriConvocati.get(), self.NumeSelectioner.get(),
            self.txtGrupe_nationale_ID_FK.get())
        if self.verifyConstraints():
            results.execute(command)
            tkinter.messagebox.showinfo("Confirmare INSERT", "S-a adaugat!")
        else:
            tkinter.messagebox.showerror("Eroare INSERT", "Reintroduceti date valide!")
        connection.commit()

    def updateNationala(self):
        results = connection.cursor()
        command = "UPDATE echipa_nationala SET numar_jucatori_convocati = %s, nume_selectioner = '%s', Grupe_nationale_ID = %s WHERE tara = '%s'" % (
            self.NumarJucatoriConvocati.get(), self.NumeSelectioner.get(),
            self.txtGrupe_nationale_ID_FK.get(), self.Tara.get())
        if self.verifyConstraints():
            results.execute(command)
            tkinter.messagebox.showinfo("Confirmare", "S-a modificat inregistrarea!")
        else:
            tkinter.messagebox.showerror("Eroare UPDATE", "Reintroduceti date valide!")
        connection.commit()

    def UpdateorInsert(self):
        if self.uoi == 1:
            return self.addNationala()
        if self.uoi == 2:
            return self.updateNationala()
