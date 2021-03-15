import tkinter
from tkinter import *
from tkinter import ttk
from tkinter import messagebox

import cx_Oracle

connection = cx_Oracle.connect("alexm", "alexm", "localhost/xe")


class Palmares:
    def __init__(self, window, color, uoi):
        self.window = window
        self.premii_individuale = StringVar()
        self.numar_cupe = StringVar()
        self.id_player_FK = StringVar()

        self.uoi = uoi

        self.buttonOK = Button(self.window, text="Ok", font=('Times New Roman', 14, 'bold'), relief=RAISED, height=1,
                               width=10, padx=50, pady=0, bd=4, bg='lavender', command=self.UpdateorInsert)
        self.buttonOK.grid(row=7, column=0)
        self.buttonClear = Button(self.window, text="Clear", font=('Times New Roman', 14, 'bold'), relief=RAISED,
                                  height=1,
                                  width=10, padx=50, pady=0, bd=4, bg='lavender', command=self.clearPalmares)
        self.buttonClear.grid(row=7, column=1)

        self.labelpremii_individuale = Label(self.window, font=('Times New Roman', 12, 'bold'),
                                             text='Premii individuale',
                                             padx=2,
                                             pady=2, bg=color)
        self.labelpremii_individuale.grid(row=0, column=0, sticky=W)
        self.txtpremii_individuale = Entry(self.window, font=('Times New Roman', 12, 'bold'),
                                           textvariable=self.premii_individuale,
                                           width=32)
        self.txtpremii_individuale.grid(row=0, column=1, sticky=W)

        self.labelnumar_cupe = Label(self.window, font=('Times New Roman', 12, 'bold'), text='Numar cupe', padx=2,
                                     pady=2, bg=color)
        self.labelnumar_cupe.grid(row=1, column=0, sticky=W)
        self.txtnumar_cupe = Entry(self.window, font=('Times New Roman', 12, 'bold'), textvariable=self.numar_cupe,
                                   width=32)
        self.txtnumar_cupe.grid(row=1, column=1, sticky=W)

        self.labelid_player_FK = Label(self.window, font=('Times New Roman', 12, 'bold'), text='Id_player',
                                       padx=2,
                                       pady=2, bg=color)
        self.labelid_player_FK.grid(row=2, column=0, sticky=W)
        self.txtid_player_FK = ttk.Combobox(self.window, width=40, textvariable=self.id_player_FK,
                                            state='readonly')
        self.txtid_player_FK['values'] = (
            '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19',
            '20',
            '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31', '32', '33', '34', '35', '36', '37', '38')
        self.txtid_player_FK.grid(row=2, column=1)
        self.txtid_player_FK.current()

    def clearPalmares(self):
        self.txtpremii_individuale.delete(0, END)
        self.txtnumar_cupe.delete(0, END)
        self.txtid_player_FK.set("")

    def verifyConstraints(self):
        return (int(self.premii_individuale.get()) >= 0 and int(
            self.numar_cupe.get()) >= 0 and self.txtid_player_FK.get() != "")

    def addPalmares(self):
        results = connection.cursor()
        command = "INSERT INTO Palmares VALUES(%s, %s, %s, NULL)" % (
            self.premii_individuale.get(), self.numar_cupe.get(), self.txtid_player_FK.get())
        if self.verifyConstraints():
            results.execute(command)
            tkinter.messagebox.showinfo("Confirmare INSERT", "S-a adaugat")
        else:
            tkinter.messagebox.showerror("Eroare INSERT", "Reintroduceti date valide")
        connection.commit()

    def updatePalmares(self):
        results = connection.cursor()
        command = "UPDATE Palmares SET numar_cupe=%s, id_player=%s WHERE premii_individuale=%s" % (
        self.numar_cupe.get(), self.txtid_player_FK.get(), self.premii_individuale.get())
        if self.verifyConstraints():
            results.execute(command)
            tkinter.messagebox.showinfo("Confirmare UPDATE", "S-a modificat inregistrarea!")
        else:
            tkinter.messagebox.showerror("Eroare UPDATE", "Reintroduceti date valide!")
        connection.commit()

    def UpdateorInsert(self):
        if self.uoi == 1:
            return self.addPalmares()
        if self.uoi == 2:
            return self.updatePalmares()
