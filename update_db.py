from asyncio import current_task
import csv
from email import header
from email.utils import localtime
import re
import sqlite3
import os
from tkinter.messagebox import NO
import time

import web_scrapping

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

def update_db_cours():
    Dico_Link = {'amp':'amp',
                     'xrp':'xrp',
                     'grt':'the-graph',
                     'xlm':'stellar',
                     'mana':'decentraland',
                     'near':'near-protocol'}
    
    con = sqlite3.connect('Crypto.db')
    cur = con.cursor()
    Liste_Info = []
    
    for row in cur.execute('SELECT * from Cours_Monnaie;'):
        Liste_info = []
        
        for nom in Dico_Link:
            
            if nom==row[0].lower():
                link= Dico_Link[nom]
                prix = web_scrapping.recherche(link)
                prix = float(prix[1:])
                Liste_info.append(row[0])
                Liste_info.append(prix)
        Liste_Info.append(Liste_info)
    
    for element in Liste_Info:
        temps = time.asctime(time.localtime())
        cur.execute(f'UPDATE Cours_Monnaie SET Cours_Euro = {element[1]}, Date = "{temps}" WHERE Nom_Crypto="{element[0]}"; ')
        con.commit()    
   
    con.close()



update_db_cours()