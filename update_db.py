from asyncio import current_task
import csv
from email import header
import re
import sqlite3
import os
from tkinter.messagebox import NO

def update_csv():
    con = sqlite3.connect('Crypto.db')
    cursor = con.cursor()
    cursor.execute("select Invest.Nom_Crypto,Argent_Investit,Nombres_Token,Date,Cours_Euro  from Invest,Cours_Monnaie where Invest.Nom_Crypto=Cours_Monnaie.Nom_Crypto ;")
    with open("Crypto.csv", "w") as csv_file:
      csv_writer = csv.writer(csv_file, delimiter=";")
      csv_writer.writerow([i[0] for i in cursor.description])
      csv_writer.writerows(cursor)

    dirpath = os.getcwd() + "\Crypto.csv"
    print ("Data exported Successfully into {}".format(dirpath))

    con.close()

def update_db_cours(name_crypto,cours_euro):
    con = sqlite3.connect('Crypto.db')
    cur = con.cursor()
    for val in cur.execute('SELECT * From Cours_Monnaie'):
        if val[0]==name_crypto:
            cur.execute(f'UPDATE Cours_Monnaie SET Cours_Euro = {cours_euro} WHERE Nom_Crypto="{name_crypto}"; ')
            con.commit()
            return
    cur.execute(f"INSERT INTO Cours_Monnaie VALUES ('{name_crypto}',{cours_euro});")
    con.commit()
    con.close()

