import tkinter
from tkinter import *
from tkinter import ttk
from tkinter import messagebox

import cx_Oracle

connection = cx_Oracle.connect("alexm", "alexm", "localhost/xe")


class Trofee:
    def __init__(self, window, color, uoi):
        self.window = window
        self.Individuale = StringVar()
        self.Colective = StringVar()
        self.NumeCompetitie_FK = StringVar()
        self.AnulTrofeului = StringVar()

        self.uoi = uoi

        self.buttonOK = Button(self.window, text="Ok", font=('Times New Roman', 14, 'bold'), relief=RAISED, height=1,
                               width=10, padx=50, pady=0, bd=4, bg='lavender', command=self.UpdateorInsert)
        self.buttonOK.grid(row=4, column=0)
        self.buttonClear = Button(self.window, text="Clear", font=('Times New Roman', 14, 'bold'), relief=RAISED,
                                  height=1,
                                  width=10, padx=50, pady=0, bd=4, bg='lavender', command=self.clearTrofee)
        self.buttonClear.grid(row=4, column=1)

        self.labelIndividuale = Label(self.window, font=('Times New Roman', 12, 'bold'), text='Individuale', padx=2,
                                      pady=2, bg=color)
        self.labelIndividuale.grid(row=0, column=0, sticky=W)
        self.txtIndividuale = Entry(self.window, font=('Times New Roman', 12, 'bold'), textvariable=self.Individuale,
                                    width=32)
        self.txtIndividuale.grid(row=0, column=1, sticky=W)

        self.labelColective = Label(self.window, font=('Times New Roman', 12, 'bold'),
                                    text='Colective', padx=2,
                                    pady=2, bg=color)
        self.labelColective.grid(row=1, column=0, sticky=W)
        self.txtColective = Entry(self.window, font=('Times New Roman', 12, 'bold'),
                                  textvariable=self.Colective,
                                  width=32)
        self.txtColective.grid(row=1, column=1, sticky=W)

        self.labelNumeCompetitie_FK = Label(self.window, font=('Times New Roman', 12, 'bold'), text='Nume competitie',
                                            padx=2,
                                            pady=2, bg=color)
        self.labelNumeCompetitie_FK.grid(row=2, column=0, sticky=W)
        self.txtNumeCompetitie_FK = ttk.Combobox(self.window, width=40, textvariable=self.NumeCompetitie_FK,
                                                 state='readonly')
        self.txtNumeCompetitie_FK['values'] = (
            'CAMPIONAT ASIATIC',
            'CAMPIONAT AUSTRALIA',
            'CAMPIONAT BRAZIL',
            'CAMPIONAT CAMEROON',
            'CAMPIONAT EGIPT',
            'CAMPIONAT ENGLAND',
            'CAMPIONAT EUROPEAN',
            'CAMPIONAT FRANCE',
            'CAMPIONAT GERMANY',
            'CAMPIONAT ROMANIA',
            'CAMPIONAT SPAIN')
        self.txtNumeCompetitie_FK.grid(row=2, column=1)
        self.txtNumeCompetitie_FK.current()

        self.labelAnulTrofeului = Label(self.window, font=('Times New Roman', 12, 'bold'), text='Anul trofeului',
                                        padx=2,
                                        pady=2, bg=color)
        self.labelAnulTrofeului.grid(row=3, column=0, sticky=W)
        self.txtAnulTrofeului = Entry(self.window, font=('Times New Roman', 12, 'bold'),
                                      textvariable=self.AnulTrofeului,
                                      width=32)
        self.txtAnulTrofeului.grid(row=3, column=1, sticky=W)

    def clearTrofee(self):
        self.txtIndividuale.delete(0, END)
        self.txtColective.delete(0, END)
        self.txtNumeCompetitie_FK.set("")
        self.txtAnulTrofeului.delete(0, END)

    def verifyConstraints(self):
        return (int(self.Individuale.get()) > 0 and int(
            self.Colective.get()) > 0 and self.txtNumeCompetitie_FK.get() != "" and int(
            self.AnulTrofeului.get()) >= 2000 and int(self.AnulTrofeului.get()) <= 2020)

    def addTrofee(self):
        results = connection.cursor()
        command = "INSERT INTO trofee VALUES(%s, %s, '%s', NULL, %s)" % (
            self.Individuale.get(), self.Colective.get(), self.txtNumeCompetitie_FK.get(), self.AnulTrofeului.get())
        if self.verifyConstraints():
            results.execute(command)
            tkinter.messagebox.showinfo("Confirmare INSERT", "S-a adaugat")
        else:
            tkinter.messagebox.showerror("Eroare INSERT", "Reintroduceti date valide!")
        connection.commit()

    def updateTrofee(self):
        results = connection.cursor()
        command = "UPDATE trofee SET individuale=%s, colective=%s, nume_competitie=%s WHERE anul_trofeului=%s" % (
        self.Individuale.get(), self.Colective.get(), self.txtNumeCompetitie_FK.get(), self.AnulTrofeului.get())
        if self.verifyConstraints():
            results.execute(command)
            tkinter.messagebox.showinfo("Confirmare", "S-a modificat inregistrarea!")
        else:
            tkinter.messagebox.showerror("Eroare UPDATE", "Reintroduceti date valide!")
        connection.commit()

    def UpdateorInsert(self):
        if self.uoi == 1:
            return self.addTrofee()
        if self.uoi == 2:
            return self.updateTrofee()
