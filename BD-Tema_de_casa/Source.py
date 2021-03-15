import tkinter
import tkinter as tk
from tkinter import *
from tkinter import messagebox
from tkinter import ttk

import cx_Oracle

import Club
import Competitie
import Grupe
import Jucator
import Liga
import Nationala
import Palmares
import Trofee

connection = cx_Oracle.connect("alexm", "alexm", "localhost/xe")


class Interface:
    UpdateorInsert: int = 1
    selectedList: list = []

    def __init__(self, root):
        self.root = root
        self.root.title("Selectia unei echipe nationale de fotbal")
        self.root.geometry("1550x620+250+150")
        self.root.config(bg="lavender")
        self.root.resizable(0, 0)
        # mainFrame
        mainFrame = Frame(self.root, bg='lavender')
        mainFrame.grid()

        # Title Frame
        titleFrame = Frame(mainFrame, bd=4, padx=285, pady=3, bg="Snow", relief=RIDGE)
        titleFrame.pack(side=TOP)

        self.lblTitle = Label(titleFrame, font=('Times New Roman', 34, 'bold'),
                              text='SELECTIA ECHIPEI NATIONALE DE FOTBAL',
                              bg="Snow")
        self.lblTitle.grid()

        # Buttons Frame
        buttonsFrame = Frame(mainFrame, bd=4, width=1550, height=60, padx=30, pady=10, bg="lavender", relief=RIDGE)
        buttonsFrame.pack(side=BOTTOM)

        # Combobox Select Table
        n = tk.StringVar()
        self.entityTable = ttk.Combobox(buttonsFrame, width=26, textvariable=n, state='readonly')
        self.entityTable['values'] = (' JUCATOR DE FOTBAL',
                                      ' ECHIPA DE FOTBAL',
                                      ' LIGA DE FOTBAL',
                                      ' ECHIPA NATIONALA',
                                      ' TROFEE',
                                      ' COMPETITII',
                                      ' PALMARES',
                                      ' GRUPE NATIONALE',
                                      ' DIRECTIONARE')

        self.entityTable.grid(row=0, column=1)
        self.entityTable.current()

        dataFrame = Frame(mainFrame, bd=1, width=1550, height=500, padx=0, pady=0, relief=RIDGE, bg="snow")
        dataFrame.pack(side=BOTTOM)

        # Baza de date
        self.dataFrameOUT = LabelFrame(dataFrame, bd=1, width=1550, height=470, padx=0, pady=0, relief=RIDGE,
                                       bg="lavender",
                                       font=('Times New Roman', 20, 'bold'), text="\tBaza de date\n")
        self.dataFrameOUT.pack(side=RIGHT)

        # Buttons
        self.buttonInsert = Button(buttonsFrame, text="Insert", font=('Times New Roman', 14, 'bold'), height=1,
                                   width=20, pady=0, bd=4, command=self.optiuneInsert)
        self.buttonInsert.grid(row=0, column=2)
        self.buttonUpdate = Button(buttonsFrame, text="Update", font=('Times New Roman', 14, 'bold'), height=1,
                                   width=20, pady=0, bd=4, command=self.optiuneUpdate)
        self.buttonUpdate.grid(row=0, column=3)
        self.buttonDelete = Button(buttonsFrame, text="Delete", font=('Times New Roman', 14, 'bold'), height=1,
                                   width=20, pady=0, bd=4, command=self.optiuneDelete)
        self.buttonDelete.grid(row=0, column=4)
        self.buttonDisplay = Button(buttonsFrame, text="Display", font=('Times New Roman', 14, 'bold'), height=1,
                                    width=20, pady=0, bd=4, command=self.optiuneDisplay)
        self.buttonDisplay.grid(row=0, column=5)
        # self.buttonReset = Button(buttonsFrame, text="Refresh", font=('Times New Roman', 14, 'bold'), height=1,
        #                            width=20, pady=0, bd=4, command=lambda : self.dataFrameOUT.destroy())
        # self.buttonReset.grid(row=0, column=6)
        self.ttk = Label(buttonsFrame, text="SELECT TABLE", font=("Times New Roman", 16, 'bold'), bg='lavender',
                         padx=20).grid(column=0,
                                       row=0)

        # Scrollbar-uri
        self.scrollbar = Scrollbar(self.dataFrameOUT, orient='vertical')

        # scrollbar.grid(row=0, column=1, sticky='ns')
        # scrollbar1.grid(row=1, column=0, sticky='ew')

        # self.recordList = Listbox(dataFrameOUT, width=110, height=20, font=('Times New Roman', 13, 'underline'),
        #                            selectbackground="black", highlightcolor="Black",
        #                            yscrollcommand=scrollbar.set, xscrollcommand=scrollbar1.set)
        # self.recordList.grid(row=0, column=0, padx=10)

        # scrollbar.config(command=self.recordList.yview)
        # scrollbar1.config(command=self.recordList.xview)
        self.recordList = ttk.Treeview(self.dataFrameOUT, height=18, columns="",
                                       yscrollcommand=self.scrollbar.set)

        self.curitem = []

    def displayJucator(self):
        self.recordList.destroy()
        self.recordList = ttk.Treeview(self.dataFrameOUT, height=18, columns=("ID Jucator",
                                                                              "nume", "data nasterii", "inaltime",
                                                                              "greutate", "pozitie", "numar goluri",
                                                                              "numar meciuri", "numar tricou",
                                                                              "convocare", "retras", "atuu", "ID Club",
                                                                              "tara", "ID Liga"),
                                       yscrollcommand=self.scrollbar.set)

        self.scrollbar.pack(side=RIGHT, fill=Y)
        self.recordList.heading("ID Jucator", text="ID jucator")
        self.recordList.heading("nume", text="Nume jucator")
        self.recordList.heading("data nasterii", text="Data nasterii")
        self.recordList.heading("inaltime", text="Inaltime")
        self.recordList.heading("greutate", text="Greutate")
        self.recordList.heading("pozitie", text="Pozitie")
        self.recordList.heading("numar goluri", text="Nr. goluri")
        self.recordList.heading("numar meciuri", text="Nr. meciuri")
        self.recordList.heading("numar tricou", text="Nr. tricou")
        self.recordList.heading("convocare", text="Convocare")
        self.recordList.heading("retras", text="Retras")
        self.recordList.heading("atuu", text="Atuu")
        self.recordList.heading("ID Club", text="ID Club")
        self.recordList.heading("tara", text="Tara")
        self.recordList.heading("ID Liga", text="ID Liga")

        self.recordList['show'] = 'headings'

        self.recordList.column("ID Jucator", width=75)
        self.recordList.column("nume", width=200)
        self.recordList.column("data nasterii", width=100)
        self.recordList.column("inaltime", width=75)
        self.recordList.column("greutate", width=75)
        self.recordList.column("pozitie", width=100)
        self.recordList.column("numar goluri", width=75)
        self.recordList.column("numar meciuri", width=75)
        self.recordList.column("numar tricou", width=75)
        self.recordList.column("convocare", width=75)
        self.recordList.column("retras", width=75)
        self.recordList.column("atuu", width=100)
        self.recordList.column("ID Club", width=50)
        self.recordList.column("tara", width=75)
        self.recordList.column("ID Liga", width=50)

        self.recordList.pack(fill=BOTH, expand=1)

        self.recordList.bind('<ButtonRelease-1>', self.selectItem)

        self.jucatorAfisare()

    def displayClub(self):
        self.recordList.destroy()
        self.recordList = ttk.Treeview(self.dataFrameOUT, height=18, columns=(
            "ID Club", "nume echipa", "oras", "numar jucatori", "antrenor principal", "ID Liga"),
                                       yscrollcommand=self.scrollbar.set)

        self.scrollbar.pack(side=RIGHT, fill=Y)
        self.recordList.heading("ID Club", text="ID Club")
        self.recordList.heading("nume echipa", text="Nume echipa")
        self.recordList.heading("oras", text="Oras")
        self.recordList.heading("numar jucatori", text="Nr. jucatori")
        self.recordList.heading("antrenor principal", text="Antrenor principal")
        self.recordList.heading("ID Liga", text="ID Liga")

        self.recordList['show'] = 'headings'

        self.recordList.column("ID Club", width=75)
        self.recordList.column("nume echipa", width=400)
        self.recordList.column("oras", width=300)
        self.recordList.column("numar jucatori", width=75)
        self.recordList.column("antrenor principal", width=200)
        self.recordList.column("ID Liga", width=75)

        self.recordList.pack(fill=BOTH, expand=1)

        self.recordList.bind('<ButtonRelease-1>', self.selectItem)

        self.clubAfisare()

    def displayNationala(self):
        self.recordList.destroy()
        self.recordList = ttk.Treeview(self.dataFrameOUT, height=18, columns=(
            "tara nat", "numar jucatori convocati", "nume selectioner", "ID Grupe"),
                                       yscrollcommand=self.scrollbar.set)
        self.scrollbar.pack(side=RIGHT, fill=Y)
        self.recordList.heading("tara nat", text="Tara")
        self.recordList.heading("numar jucatori convocati", text="Nr. jucatori convocati")
        self.recordList.heading("nume selectioner", text="Nume selectioner")
        self.recordList.heading("ID Grupe", text="Grupe_nationale_ID")

        self.recordList['show'] = 'headings'

        self.recordList.column("tara nat", width=300)
        self.recordList.column("numar jucatori convocati", width=100)
        self.recordList.column("nume selectioner", width=300)
        self.recordList.column("ID Grupe", width=120)

        self.recordList.pack(fill=BOTH, expand=1)

        self.recordList.bind('<ButtonRelease-1>', self.selectItem)

        self.nationalaAfisare()

    def displayLiga(self):
        self.recordList.destroy()
        self.recordList = ttk.Treeview(self.dataFrameOUT, height=18, columns=(
            "Id Liga", "numar liga", "numar echipe", "numar competitii", "tara"),
                                       yscrollcommand=self.scrollbar.set)

        self.scrollbar.pack(side=RIGHT, fill=Y)
        self.recordList.heading("Id Liga", text="Id Liga")
        self.recordList.heading("numar liga", text="Nr. liga")
        self.recordList.heading("numar echipe", text="Nr. echipe")
        self.recordList.heading("numar competitii", text="Nr.competitii")
        self.recordList.heading("tara", text="Tara")

        self.recordList['show'] = 'headings'

        self.recordList.column("Id Liga", width=100)
        self.recordList.column("numar liga", width=100)
        self.recordList.column("numar echipe", width=100)
        self.recordList.column("numar competitii", width=120)
        self.recordList.column("tara", width=200)

        self.recordList.pack(fill=BOTH, expand=1)

        self.recordList.bind('<ButtonRelease-1>', self.selectItem)

        self.ligaAfisare()

    def displayTrofee(self):
        self.recordList.destroy()
        self.recordList = ttk.Treeview(self.dataFrameOUT, height=18, columns=(
            "ind", "col", "nume comp", "ID Trofee", "an"),
                                       yscrollcommand=self.scrollbar.set)

        self.scrollbar.pack(side=RIGHT, fill=Y)
        self.recordList.heading("ind", text="Trofee individuale")
        self.recordList.heading("col", text="Trofee colective")
        self.recordList.heading("nume comp", text="Nume competitie")
        self.recordList.heading("ID Trofee", text="Id trofeu")
        self.recordList.heading("an", text="Anul trofeului")

        self.recordList['show'] = 'headings'

        self.recordList.column("ind", width=100)
        self.recordList.column("col", width=100)
        self.recordList.column("nume comp", width=200)
        self.recordList.column("ID Trofee", width=120)
        self.recordList.column("an", width=200)

        self.recordList.pack(fill=BOTH, expand=1)

        self.recordList.bind('<ButtonRelease-1>', self.selectItem)

        self.trofeeAfisare()

    def displayCompetitie(self):
        self.recordList.destroy()
        self.recordList = ttk.Treeview(self.dataFrameOUT, height=18, columns=(
            "nume competitie", "tip", "nr trofee ind", "nr trofee col", "numar ligaComp", "ID GrupeComp_FK",
            "ID LigaComp_FK"),
                                       yscrollcommand=self.scrollbar.set)

        self.scrollbar.pack(side=RIGHT, fill=Y)
        self.recordList.heading("nume competitie", text="Nume competitie")
        self.recordList.heading("tip", text="Tip")
        self.recordList.heading("nr trofee ind", text="Nr. trofee individuale")
        self.recordList.heading("nr trofee col", text="Nr. trofee colective")
        self.recordList.heading("numar ligaComp", text="Nr. liga")
        self.recordList.heading("ID GrupeComp_FK", text="Grupe_nationale_ID")
        self.recordList.heading("ID LigaComp_FK", text="ID Liga")

        self.recordList['show'] = 'headings'

        self.recordList.column("nume competitie", width=200)
        self.recordList.column("tip", width=100)
        self.recordList.column("nr trofee ind", width=150)
        self.recordList.column("nr trofee col", width=150)
        self.recordList.column("numar ligaComp", width=100)
        self.recordList.column("ID GrupeComp_FK", width=150)
        self.recordList.column("ID LigaComp_FK", width=100)

        self.recordList.pack(fill=BOTH, expand=1)

        self.recordList.bind('<ButtonRelease-1>', self.selectItem)

        self.competitieAfisare()

    def displayPalmares(self):
        self.recordList.destroy()
        self.recordList = ttk.Treeview(self.dataFrameOUT, height=18, columns=(
            "premii ind", "nr cupe", "ID player_FK", "ID Palmares"),
                                       yscrollcommand=self.scrollbar.set)

        self.scrollbar.pack(side=RIGHT, fill=Y)
        self.recordList.heading("premii ind", text="Nr. premii individuale")
        self.recordList.heading("nr cupe", text="Nr. cupe")
        self.recordList.heading("ID player_FK", text="ID jucator")
        self.recordList.heading("ID Palmares", text="Palmares_ID")

        self.recordList['show'] = 'headings'

        self.recordList.column("premii ind", width=200)
        self.recordList.column("nr cupe", width=100)
        self.recordList.column("ID player_FK", width=150)
        self.recordList.column("ID Palmares", width=150)

        self.recordList.pack(fill=BOTH, expand=1)

        self.recordList.bind('<ButtonRelease-1>', self.selectItem)

        self.palmaresAfisare()

    def displayGrupe(self):
        self.recordList.destroy()
        self.recordList = ttk.Treeview(self.dataFrameOUT, height=18, columns=(
            "ID grupe", "nr echipe nationale", "continent"),
                                       yscrollcommand=self.scrollbar.set)

        self.scrollbar.pack(side=RIGHT, fill=Y)
        self.recordList.heading("ID grupe", text="Grupe nationale ID")
        self.recordList.heading("nr echipe nationale", text="Nr. echipe nationale")
        self.recordList.heading("continent", text="Continent")

        self.recordList['show'] = 'headings'

        self.recordList.column("ID grupe", width=200)
        self.recordList.column("nr echipe nationale", width=200)
        self.recordList.column("continent", width=150)

        self.recordList.pack(fill=BOTH, expand=1)

        self.recordList.bind('<ButtonRelease-1>', self.selectItem)
        self.grupeAfisare()

    def optiuneDelete(self):
        if self.entityTable.get() == ' JUCATOR DE FOTBAL':
            return self.deleteJucator()
        elif self.entityTable.get() == ' ECHIPA DE FOTBAL':
            return self.deleteClub()
        elif self.entityTable.get() == ' ECHIPA NATIONALA':
            return self.deleteNationala()
        elif self.entityTable.get() == ' LIGA DE FOTBAL':
            return self.deleteLiga()
        elif self.entityTable.get() == ' TROFEE':
            return self.deleteTrofee()
        elif self.entityTable.get() == ' COMPETITII':
            return self.deleteCompetitie()
        elif self.entityTable.get() == ' PALMARES':
            return self.deletePalmares()
        elif self.entityTable.get() == ' GRUPE NATIONALE':
            return self.deleteGrupe()
        else:
            return

    def deletePalmares(self):
        results = connection.cursor()
        command = "DELETE FROM Palmares where palmares_id = %s" % self.getCellValue()
        results.execute(command)
        print(command)
        connection.commit()

        self.displayPalmares()
        tkinter.messagebox.showinfo("Informatie",
                                    "S-a efectuat stergerea liniei cu Palmares_Id = %s" % self.getCellValue())

    def deleteTrofee(self):
        results = connection.cursor()
        command = "DELETE FROM trofee where trofee_id = %s" % self.getCellValue()
        results.execute(command)
        print(command)
        connection.commit()
        self.displayTrofee()
        tkinter.messagebox.showinfo("Informatie",
                                    "S-a efectuat stergerea liniei cu trofee_Id = %s" % self.getCellValue())

    def deleteJucator(self):
        results = connection.cursor()
        command = "DELETE FROM jucator_de_fotbal where id_player = %s" % self.getCellValue()
        results.execute(command)
        print(command)
        connection.commit()
        self.displayJucator()
        tkinter.messagebox.showinfo("Informatie",
                                    "S-a efectuat stergerea liniei cu id_player = %s" % self.getCellValue())

    def deleteCompetitie(self):
        results = connection.cursor()
        command = "DELETE FROM competitie where nume_competitie = '%s'" % self.getCellValue()
        results.execute(command)
        print(command)
        connection.commit()
        self.displayCompetitie()
        tkinter.messagebox.showinfo("Informatie",
                                    "S-a efectuat stergerea liniei cu nume_competitie = '%s'" % self.getCellValue())

    def deleteClub(self):
        results = connection.cursor()
        command = "DELETE FROM echipa_de_club where id_club = %s" % self.getCellValue()
        results.execute(command)
        print(command)
        connection.commit()
        self.displayClub()
        tkinter.messagebox.showinfo("Informatie",
                                    "S-a efectuat stergerea liniei cu id_club = %s" % self.getCellValue())

    def deleteLiga(self):
        results = connection.cursor()
        command = "DELETE FROM liga_de_fotbal where id_liga = %s" % self.getCellValue()
        results.execute(command)
        print(command)
        connection.commit()
        self.displayLiga()

        tkinter.messagebox.showinfo("Informatie",
                                    "S-a efectuat stergerea liniei cu id_liga = %s" % self.getCellValue())

    def deleteNationala(self):
        results = connection.cursor()
        command = "DELETE FROM echipa_nationala where tara = '%s'" % self.getCellValue()
        results.execute(command)
        print(command)
        connection.commit()
        self.displayNationala()
        tkinter.messagebox.showinfo("Informatie",
                                    "S-a efectuat stergerea liniei cu tara = '%s'" % self.getCellValue())

    def deleteGrupe(self):
        results = connection.cursor()
        command = "DELETE FROM Grupe_nationale where Grupe_nationale_ID = %s" % self.getCellValue()
        results.execute(command)
        print(command)
        connection.commit()
        tkinter.messagebox.showinfo("Informatie",
                                    "S-a efectuat stergerea liniei cu Grupe_nationale_ID = %s" % self.getCellValue())

    def selectItem(self, event):
        global cell_value
        curItem = self.recordList.item(self.recordList.focus())
        col = self.recordList.identify_column(event.x)
        # print('curItem = ', curItem['values'])
        # print('col = ', col)
        if col == '#0':
            cell_value = curItem['text']
        elif col == '#1':
            cell_value = curItem['values'][0]
        elif col == '#2':
            cell_value = curItem['values'][1]
        elif col == '#3':
            cell_value = curItem['values'][2]
        elif col == '#4':
            cell_value = curItem['values'][3]
        elif col == '#5':
            cell_value = curItem['values'][4]
        elif col == '#6':
            cell_value = curItem['values'][5]
        elif col == '#7':
            cell_value = curItem['values'][6]
        elif col == '#8':
            cell_value = curItem['values'][7]
        elif col == '#9':
            cell_value = curItem['values'][8]
        elif col == '#10':
            cell_value = curItem['values'][9]
        elif col == '#11':
            cell_value = curItem['values'][10]
        elif col == '#12':
            cell_value = curItem['values'][11]
        elif col == '#13':
            cell_value = curItem['values'][12]
        elif col == '#14':
            cell_value = curItem['values'][13]
        print('cell_value = ', cell_value)

    @staticmethod
    def getCellValue():
        print(cell_value)
        return cell_value

    def jucatorAfisare(self):
        results = connection.cursor()
        results.execute("SELECT * FROM jucator_de_fotbal")

        self.recordList.delete(*self.recordList.get_children())
        for row in results:
            self.recordList.insert('', END, values=row)

    def clubAfisare(self):
        results = connection.cursor()
        results.execute("SELECT * FROM echipa_de_club")

        self.recordList.delete(*self.recordList.get_children())
        for row in results:
            self.recordList.insert('', END, values=row)

    def nationalaAfisare(self):
        results = connection.cursor()
        results.execute("SELECT * FROM echipa_nationala")

        self.recordList.delete(*self.recordList.get_children())
        for row in results:
            self.recordList.insert('', END, values=row)

    def ligaAfisare(self):
        results = connection.cursor()
        results.execute("SELECT * FROM liga_de_fotbal")

        self.recordList.delete(*self.recordList.get_children())
        for row in results:
            self.recordList.insert('', END, values=row)

    def trofeeAfisare(self):
        results = connection.cursor()
        results.execute("SELECT * FROM trofee")

        self.recordList.delete(*self.recordList.get_children())
        for row in results:
            self.recordList.insert('', END, values=row)

    def competitieAfisare(self):
        results = connection.cursor()
        results.execute("SELECT * FROM competitie")

        self.recordList.delete(*self.recordList.get_children())
        for row in results:
            self.recordList.insert('', END, values=row)

    def palmaresAfisare(self):
        results = connection.cursor()
        results.execute("SELECT * FROM Palmares")

        self.recordList.delete(*self.recordList.get_children())
        for row in results:
            self.recordList.insert('', END, values=row)

    def grupeAfisare(self):
        results = connection.cursor()
        results.execute("SELECT * FROM Grupe_nationale")

        self.recordList.delete(*self.recordList.get_children())
        for row in results:
            self.recordList.insert('', END, values=row)

    def optiuneDisplay(self):
        if self.entityTable.get() == ' JUCATOR DE FOTBAL':
            return self.displayJucator()
        elif self.entityTable.get() == ' ECHIPA DE FOTBAL':
            return self.displayClub()
        elif self.entityTable.get() == ' ECHIPA NATIONALA':
            return self.displayNationala()
        elif self.entityTable.get() == ' LIGA DE FOTBAL':
            return self.displayLiga()
        elif self.entityTable.get() == ' TROFEE':
            return self.displayTrofee()
        elif self.entityTable.get() == ' COMPETITII':
            return self.displayCompetitie()
        elif self.entityTable.get() == ' PALMARES':
            return self.displayPalmares()
        elif self.entityTable.get() == ' GRUPE NATIONALE':
            return self.displayGrupe()
        else:
            return

    def optiuneInsert(self):
        Interface.setUpdateorInsert(1)
        if self.entityTable.get() == ' JUCATOR DE FOTBAL':
            w = tk.Toplevel(bg='snow')
            Interface.setUpdateorInsert(1)
            w.title("INSERT JUCATOR")
            w.geometry("500x415+250+250")
            w.resizable(0, 0)
            w.focus_set()
            w.grab_set()
            jucator = Jucator.Jucator(window=w, color='snow', uoi=Interface.getUpdateorInsert())
            return jucator
        elif self.entityTable.get() == ' ECHIPA DE FOTBAL':
            w = tk.Toplevel(bg='snow')
            w.title("INSERT CLUB")
            w.geometry("500x180+250+250")
            w.resizable(0, 0)
            w.focus_set()
            w.grab_set()
            club = Club.Club(window=w, color='snow', uoi=Interface.getUpdateorInsert())
            return club
        elif self.entityTable.get() == ' ECHIPA NATIONALA':
            w = tk.Toplevel(bg='snow')
            Interface.setUpdateorInsert(1)
            w.config(bg='snow')
            w.title("INSERT NATIONALA")
            w.geometry("500x150+250+250")
            w.resizable(0, 0)
            w.focus_set()
            w.grab_set()
            nationala = Nationala.Nationala(window=w, color='snow', uoi=Interface.getUpdateorInsert())
            return nationala
        elif self.entityTable.get() == ' LIGA DE FOTBAL':
            w = tk.Toplevel(bg='snow')
            w.config(bg='snow')
            w.title("INSERT LIGA")
            w.geometry("500x150+250+250")
            w.resizable(0, 0)
            w.focus_set()
            w.grab_set()
            liga = Liga.Liga(window=w, color='snow', uoi=Interface.getUpdateorInsert())
            return liga
        elif self.entityTable.get() == ' TROFEE':
            w = tk.Toplevel(bg='snow')
            w.config(bg='snow')
            w.title("INSERT TROFEE")
            w.geometry("500x150+250+250")
            w.resizable(0, 0)
            w.focus_set()
            w.grab_set()
            trofee = Trofee.Trofee(window=w, color='snow', uoi=Interface.getUpdateorInsert())
            return trofee
        elif self.entityTable.get() == ' COMPETITII':
            w = tk.Toplevel(bg='snow')
            w.config(bg='snow')
            w.title("INSERT COMPETITII")
            w.geometry("500x235+250+250")
            w.resizable(0, 0)
            w.focus_set()
            w.grab_set()
            competitie = Competitie.Competitie(window=w, color='snow', uoi=Interface.getUpdateorInsert())
            return competitie
        elif self.entityTable.get() == ' PALMARES':
            w = tk.Toplevel(bg='snow')
            w.config(bg='snow')
            w.title("INSERT PALMARES")
            w.geometry("500x130+250+250")
            w.resizable(0, 0)
            w.focus_set()
            w.grab_set()
            palmares = Palmares.Palmares(window=w, color='snow', uoi=Interface.getUpdateorInsert())
            return palmares
        elif self.entityTable.get() == ' GRUPE NATIONALE':
            w = tk.Toplevel(bg='snow')
            w.config(bg='snow')
            w.title("INSERT GRUPE NATIONALE")
            w.geometry("500x100+250+250")
            w.resizable(0, 0)
            w.focus_set()
            w.grab_set()
            grupe = Grupe.Grupe(window=w, color='snow', uoi=Interface.getUpdateorInsert())
            return grupe
        else:
            return

    def optiuneUpdate(self):
        Interface.setUpdateorInsert(2)
        if self.entityTable.get() == ' JUCATOR DE FOTBAL':
            w = tk.Toplevel(bg='SlateBlue4')
            Interface.setUpdateorInsert(2)
            w.config(bg='SlateBlue4')
            w.title("UPDATE JUCATOR")
            w.geometry("500x415+250+250")
            w.resizable(0, 0)
            w.focus_set()
            w.grab_set()
            jucator = Jucator.Jucator(window=w, color='SlateBlue4', uoi=Interface.getUpdateorInsert())
            return jucator
        elif self.entityTable.get() == ' ECHIPA DE FOTBAL':
            w = tk.Toplevel(bg='SlateBlue4')
            w.config(bg='SlateBlue4')
            w.title("UPDATE CLUB")
            w.geometry("500x180+250+250")
            w.resizable(0, 0)
            w.focus_set()
            w.grab_set()
            club = Club.Club(window=w, color='SlateBlue4', uoi=Interface.getUpdateorInsert())
            return club
        elif self.entityTable.get() == ' ECHIPA NATIONALA':
            w = tk.Toplevel(bg='SlateBlue4')
            print("Dupa get")
            print(Interface.getUpdateorInsert())
            w.config(bg='SlateBlue4')
            w.title("UPDATE NATIONALA")
            w.geometry("500x150+250+250")
            w.resizable(0, 0)
            w.focus_set()
            w.grab_set()
            nationala = Nationala.Nationala(window=w, color='SlateBlue4', uoi=Interface.getUpdateorInsert())
            return nationala
        elif self.entityTable.get() == ' LIGA DE FOTBAL':
            w = tk.Toplevel(bg='SlateBlue4')
            w.config(bg='SlateBlue4')
            w.title("UPDATE LIGA")
            w.geometry("500x150+250+250")
            w.resizable(0, 0)
            w.focus_set()
            w.grab_set()
            liga = Liga.Liga(window=w, color='SlateBlue4', uoi=Interface.getUpdateorInsert())
            return liga
        elif self.entityTable.get() == ' TROFEE':
            w = tk.Toplevel(bg='SlateBlue4')
            w.config(bg='SlateBlue4')
            w.title("UPDATE TROFEE")
            w.geometry("500x150+250+250")
            w.resizable(0, 0)
            w.focus_set()
            w.grab_set()
            trofee = Trofee.Trofee(window=w, color='SlateBlue4', uoi=Interface.getUpdateorInsert())
            return trofee
        elif self.entityTable.get() == ' COMPETITII':
            w = tk.Toplevel(bg='SlateBlue4')
            w.config(bg='SlateBlue4')
            w.title("UPDATE COMPETITII")
            w.geometry("500x235+250+250")
            w.resizable(0, 0)
            w.focus_set()
            w.grab_set()
            competitie = Competitie.Competitie(window=w, color='SlateBlue4', uoi=Interface.getUpdateorInsert())
            return competitie
        elif self.entityTable.get() == ' PALMARES':
            w = tk.Toplevel(bg='SlateBlue4')
            w.config(bg='SlateBlue4')
            w.title("UPDATE PALMARES")
            w.geometry("500x130+250+250")
            w.resizable(0, 0)
            w.focus_set()
            w.grab_set()
            palmares = Palmares.Palmares(window=w, color='SlateBlue4', uoi=Interface.getUpdateorInsert())
            return palmares
        elif self.entityTable.get() == ' GRUPE NATIONALE':
            w = tk.Toplevel(bg='SlateBlue4')
            w.config(bg='SlateBlue4')
            w.title("UPDATE GRUPE NATIONALE")
            w.geometry("500x100+250+250")
            w.resizable(0, 0)
            w.focus_set()
            w.grab_set()
            grupe = Grupe.Grupe(window=w, color='SlateBlue4', uoi=Interface.getUpdateorInsert())
            return grupe
        else:
            return

    @staticmethod
    def getUpdateorInsert() -> int:
        return Interface.UpdateorInsert

    @staticmethod
    def setUpdateorInsert(newUoI: int):
        Interface.UpdateorInsert = newUoI


if __name__ == '__main__':
    root = tk.Tk()
    application = Interface(root)
    root.mainloop()
