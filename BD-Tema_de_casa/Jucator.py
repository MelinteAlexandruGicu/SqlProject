import tkinter
from tkinter import *
from tkinter import ttk
import re
import cx_Oracle
from tkinter import messagebox
from datetime import date

connection = cx_Oracle.connect("alexm", "alexm", "localhost/xe")


class Jucator:
    def __init__(self, window, color, uoi):
        self.window = window
        self.NumeJucator = StringVar()
        self.DataNasterii = StringVar()
        self.Inaltime = StringVar()
        self.Greutate = StringVar()
        self.Pozitie = StringVar()
        self.NumarGoluri = StringVar()
        self.NumarMeciuri = StringVar()
        self.NumarTricou = StringVar()
        self.Convocare = StringVar()
        self.Retras = StringVar()
        self.Atuu = StringVar()
        self.ID_Club_FK = StringVar()
        self.Tara_FK = StringVar()
        self.ID_Liga_FK = StringVar()

        self.uoi = uoi

        self.labelNumeJucator = Label(self.window, font=('Times New Roman', 12, 'bold'), text='Nume jucator', padx=2,
                                      pady=2, bg=color)
        self.labelNumeJucator.grid(row=0, column=0, sticky=W)
        self.txtNumeJucator = Entry(self.window, font=('Times New Roman', 12, 'bold'), textvariable=self.NumeJucator,
                                    width=32)
        self.txtNumeJucator.grid(row=0, column=1, sticky=W)

        self.labelDataNasterii = Label(self.window, font=('Times New Roman', 12, 'bold'), text='Data nasterii', padx=2,
                                       pady=2, bg=color)
        self.labelDataNasterii.grid(row=1, column=0, sticky=W)
        self.txtDataNasterii = Entry(self.window, font=('Times New Roman', 12, 'bold'), textvariable=self.DataNasterii,
                                     width=32)
        self.txtDataNasterii.grid(row=1, column=1, sticky=W)

        self.labelInaltime = Label(self.window, font=('Times New Roman', 12, 'bold'), text='Inaltime', padx=2,
                                   pady=2, bg=color)
        self.labelInaltime.grid(row=2, column=0, sticky=W)
        self.txtInaltime = Entry(self.window, font=('Times New Roman', 12, 'bold'), textvariable=self.Inaltime,
                                 width=32)
        self.txtInaltime.grid(row=2, column=1, sticky=W)

        self.labelGreutate = Label(self.window, font=('Times New Roman', 12, 'bold'), text='Greutate', padx=2,
                                   pady=2, bg=color)
        self.labelGreutate.grid(row=3, column=0, sticky=W)
        self.txtGreutate = Entry(self.window, font=('Times New Roman', 12, 'bold'), textvariable=self.Greutate,
                                 width=32)
        self.txtGreutate.grid(row=3, column=1, sticky=W)

        self.labelPozitie = Label(self.window, font=('Times New Roman', 12, 'bold'), text='Pozitie', padx=2,
                                  pady=2, bg=color)
        self.labelPozitie.grid(row=4, column=0, sticky=W)
        self.txtPozitie = Entry(self.window, font=('Times New Roman', 12, 'bold'), textvariable=self.Pozitie,
                                width=32)
        self.txtPozitie.grid(row=4, column=1, sticky=W)

        self.labelNumarGoluri = Label(self.window, font=('Times New Roman', 12, 'bold'), text='Numar goluri', padx=2,
                                      pady=2, bg=color)
        self.labelNumarGoluri.grid(row=5, column=0, sticky=W)
        self.txtNumarGoluri = Entry(self.window, font=('Times New Roman', 12, 'bold'), textvariable=self.NumarGoluri,
                                    width=32)
        self.txtNumarGoluri.grid(row=5, column=1, sticky=W)

        self.labelNumarMeciuri = Label(self.window, font=('Times New Roman', 12, 'bold'), text='Numar meciuri', padx=2,
                                       pady=2, bg=color)
        self.labelNumarMeciuri.grid(row=6, column=0, sticky=W)
        self.txtNumarMeciuri = Entry(self.window, font=('Times New Roman', 12, 'bold'), textvariable=self.NumarMeciuri,
                                     width=32)
        self.txtNumarMeciuri.grid(row=6, column=1, sticky=W)

        self.labelNumarTricou = Label(self.window, font=('Times New Roman', 12, 'bold'), text='Numar tricou', padx=2,
                                      pady=2, bg=color)
        self.labelNumarTricou.grid(row=7, column=0, sticky=W)
        self.txtNumarTricou = Entry(self.window, font=('Times New Roman', 12, 'bold'), textvariable=self.NumarTricou,
                                    width=32)
        self.txtNumarTricou.grid(row=7, column=1, sticky=W)

        self.labelConvocare = Label(self.window, font=('Times New Roman', 12, 'bold'), text='Convocare', padx=2,
                                    pady=2, bg=color)
        self.labelConvocare.grid(row=8, column=0, sticky=W)
        self.txtConvocare = Entry(self.window, font=('Times New Roman', 12, 'bold'), textvariable=self.Convocare,
                                  width=32)
        self.txtConvocare.grid(row=8, column=1, sticky=W)

        self.labelRetras = Label(self.window, font=('Times New Roman', 12, 'bold'), text='Retras', padx=2,
                                 pady=2, bg=color)
        self.labelRetras.grid(row=9, column=0, sticky=W)
        self.txtRetras = Entry(self.window, font=('Times New Roman', 12, 'bold'), textvariable=self.Retras,
                               width=32)
        self.txtRetras.grid(row=9, column=1, sticky=W)

        self.labelAtuu = Label(self.window, font=('Times New Roman', 12, 'bold'), text='Atuu', padx=2,
                               pady=2, bg=color)
        self.labelAtuu.grid(row=10, column=0, sticky=W)
        self.txtAtuu = Entry(self.window, font=('Times New Roman', 12, 'bold'), textvariable=self.Atuu,
                             width=32)
        self.txtAtuu.grid(row=10, column=1, sticky=W)

        self.labelID_Club_FK = Label(self.window, font=('Times New Roman', 12, 'bold'), text='ID_Club', padx=2,
                                     pady=2, bg=color)
        self.labelID_Club_FK.grid(row=11, column=0, sticky=W)
        self.txtID_Club_FK = ttk.Combobox(self.window, width=40, textvariable=self.ID_Club_FK, state='readonly')
        results = connection.cursor()
        query = "SELECT id_club FROM echipa_de_club"
        results.execute(query)
        for i in results:
            print(i)
            self.txtID_Club_FK['values'] = (*self.txtID_Club_FK['values'], i)
        self.txtID_Club_FK.grid(row=11, column=1)
        self.txtID_Club_FK.current()

        self.labelTara_FK = Label(self.window, font=('Times New Roman', 12, 'bold'), text='Tara', padx=2,
                                  pady=2, bg=color)
        self.labelTara_FK.grid(row=12, column=0, sticky=W)
        self.txtTara_FK = ttk.Combobox(self.window, width=40, textvariable=self.Tara_FK, state='readonly')
        results = connection.cursor()
        query = "SELECT tara FROM echipa_nationala"
        results.execute(query)
        for i in results:
            print(i)
            self.txtTara_FK['values'] = (*self.txtTara_FK['values'], i)
        self.txtTara_FK.grid(row=12, column=1)
        self.txtTara_FK.current()

        self.labelID_Liga_FK = Label(self.window, font=('Times New Roman', 12, 'bold'), text='ID_Liga', padx=2,
                                     pady=2, bg=color)
        self.labelID_Liga_FK.grid(row=13, column=0, sticky=W)
        self.txtID_Liga_FK = ttk.Combobox(self.window, width=40, textvariable=self.ID_Liga_FK, state='readonly')
        results = connection.cursor()
        query = "SELECT id_liga FROM liga_de_fotbal"
        results.execute(query)
        for i in results:
            print(i)
            self.txtID_Liga_FK['values'] = (*self.txtID_Liga_FK['values'], i)
        self.txtID_Liga_FK.grid(row=13, column=1)
        self.txtID_Liga_FK.current()

        self.buttonOK = Button(self.window, text="Ok", font=('Times New Roman', 14, 'bold'), relief=RAISED, height=1,
                               width=10, padx=50, pady=0, bd=4, bg='lavender', command=self.UpdateorInsert)

        self.buttonOK.grid(row=14, column=0)
        self.buttonClear = Button(self.window, text="Clear", font=('Times New Roman', 14, 'bold'), relief=RAISED,
                                  height=1,
                                  width=10, padx=50, pady=0, bd=4, bg='lavender', command=self.clearJucator)
        self.buttonClear.grid(row=14, column=1)

    def clearJucator(self):
        self.txtNumeJucator.delete(0, END)
        self.txtDataNasterii.delete(0, END)
        self.txtInaltime.delete(0, END)
        self.txtGreutate.delete(0, END)
        self.txtPozitie.delete(0, END)
        self.txtNumarGoluri.delete(0, END)
        self.txtNumarMeciuri.delete(0, END)
        self.txtNumarTricou.delete(0, END)
        self.txtConvocare.delete(0, END)
        self.txtRetras.delete(0, END)
        self.txtAtuu.delete(0, END)
        self.txtID_Club_FK.set("")
        self.txtTara_FK.set("")
        self.txtID_Liga_FK.set("")

    def verifyConstraints(self):
        results = connection.cursor()
        numeJucator_ck = 1
        convocare_ck = 1
        retras_ck = 1
        if len(self.NumeJucator.get()) > 0:
            numeJucator = results.execute("SELECT nume_jucator FROM jucator_de_fotbal")
            for i in numeJucator:
                print(i)
                if i:
                    numeJucator_ck = 0
        if len(self.Convocare.get()) > 0:
            numeJucator = results.execute("SELECT convocare FROM jucator_de_fotbal")
            for i in numeJucator:
                print(i)
                if i:
                    convocare_ck = 0
        if len(self.Retras.get()) > 0:
            numeJucator = results.execute("SELECT retras FROM jucator_de_fotbal")
            for i in numeJucator:
                print(i)
                if i:
                    retras_ck = 0
        return (len(self.NumeJucator.get()) > 5 and re.match("^[A-Za-z ]+$", self.NumeJucator.get()) and int(
            self.Inaltime.get()) > 150 and int(self.Greutate.get()) > 50 and (
                        self.Pozitie.get() == "atacant" or self.Pozitie.get() == "portar" or self.Pozitie.get() == "mijlocas" or self.Pozitie.get() == "fundas")
                and int(self.NumarGoluri.get()) >= 0 and int(self.NumarMeciuri.get()) >= 0 and int(
                    self.NumarTricou.get()) >= 1 and int(self.NumarTricou.get()) <= 99 and (
                        self.Convocare.get() == "convocat" or self.Convocare.get() == "neconvocat") and (
                        self.Retras.get() == "da" or self.Retras.get() == "nu") and self.txtID_Club_FK.get() != "" and self.txtTara_FK.get() != "" and self.txtID_Liga_FK.get() != "" and numeJucator_ck == 0 and convocare_ck == 0 and retras_ck == 0)

    def addJucator(self):
        date1 = str(self.DataNasterii.get()).split('-')
        print(date1)
        print("Ziua")
        print(date1[0])
        print("Luna")
        print(int(date1[1]))
        print("Anul")
        print(date1[2])
        systemDate = date.today().strftime("%d-%m-%Y")
        print(systemDate)
        results = connection.cursor()
        command = "INSERT INTO jucator_de_fotbal VALUES(NULL, '%s', TO_DATE('%s', ' DD-MM-YYYY'), %s, %s, '%s', " \
                  "%s, %s, %s, '%s','%s','%s', %s," \
                  "'%s', %s)" % (
                      self.NumeJucator.get(), self.DataNasterii.get(), self.Inaltime.get(), self.Greutate.get(),
                      self.Pozitie.get(), self.NumarGoluri.get(), self.NumarMeciuri.get(), self.NumarTricou.get(),
                      self.Convocare.get(), self.Retras.get(), self.Atuu.get(),
                      self.txtID_Club_FK.get(), self.txtTara_FK.get(), self.txtID_Liga_FK.get())
        if self.verifyConstraints():
            print(command)
            results.execute(command)
            tkinter.messagebox.showinfo("Confirmare INSERT", "S-a adaugat!")
        else:
            tkinter.messagebox.showerror("Eroare INSERT", "Reintroduceti date valide!")
        connection.commit()

    def updateJucator(self):
        date1 = str(self.DataNasterii.get()).split('-')
        print(date1)
        print("Ziua")
        print(date1[0])
        print("Luna")
        print(date1[1])
        print("Anul")
        print(date1[2])
        systemDate = date.today().strftime("%d-%m-%Y")
        print(systemDate)
        results = connection.cursor()
        command = "UPDATE jucator_de_fotbal SET data_nasterii=TO_DATE('%s-%s-%s', ' DD-MM-YYYY'), inaltime=%s, " \
                  "greutate=%s, pozitie='%s', numar_goluri=%s, numar_meciuri=%s, numar_tricou=%s, atuu='%s', " \
                  "id_club=%s, tara='%s', id_liga='%s' WHERE nume_jucator='%s' and convocare='%s' and retras='%s'" % (
                      date1[0], date1[1], date1[2], self.Inaltime.get(), self.Greutate.get(),
                      self.Pozitie.get(), self.NumarGoluri.get(), self.NumarMeciuri.get(), self.NumarTricou.get(),
                      self.Atuu.get(),
                      self.txtID_Club_FK.get(), self.txtTara_FK.get(), self.txtID_Liga_FK.get(), self.NumeJucator.get(),
                      self.Convocare.get(), self.Retras.get())
        if self.verifyConstraints():
            results.execute(command)
            tkinter.messagebox.showinfo("Confirmare", "S-a modificat inregistrarea!")
        else:
            tkinter.messagebox.showerror("Eroare UPDATE", "Reintroduceti date valide!")
        connection.commit()

    def UpdateorInsert(self):
        if self.uoi == 1:
            return self.addJucator()
        if self.uoi == 2:
            return self.updateJucator()
