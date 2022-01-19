from asyncio import current_task
import csv
from email import header
from email.utils import localtime
from lib2to3.pgen2 import token
from lib2to3.pgen2.token import tok_name
import re
import sqlite3
import os
from telnetlib import GA
from tkinter.messagebox import NO
import time

import web_scrapping

global Dico_Link
Dico_Link = {'amp':'amp',
                     'xrp':'xrp',
                     'grt':'the-graph',
                     'xlm':'stellar',
                     'mana':'decentraland',
                     'near':'near-protocol',
                     'fantom':'fantom',
                     'cop':'copiosa-coin'}


def update_csv():
    con = sqlite3.connect('Crypto.db')
    cursor = con.cursor()
    cursor.execute("select Invest.Nom_Crypto,Argent_Investit,Nombres_Token,Date,Cours_Euro,Valeur,Gain,Pertes  from Invest,Cours_Monnaie where Invest.Nom_Crypto=Cours_Monnaie.Nom_Crypto ;")
    with open("Crypto.csv", "w") as csv_file:
      csv_writer = csv.writer(csv_file, delimiter=";")
      csv_writer.writerow([i[0] for i in cursor.description])
      csv_writer.writerows(cursor)

    dirpath = os.getcwd() + "\Crypto.csv"
    print ("Data exported Successfully into {}".format(dirpath))

    con.close()

def update_db_cours():
    
    
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


def add_invest():
    con = sqlite3.connect('Crypto.db')
    cur = con.cursor()

    Nom_Crypto = input('Name of crypto : ')
    Amount = float(input('Amount invested in : '))
    Date = input('Enter the date  DD.MM.YYYY (Like that -> 15.03.2022 ) : ')
    Token_Achat = float(input('Amount of tokens bought'))
    for nom in Dico_Link:
            
            if nom==Nom_Crypto.lower():
                link= Dico_Link[nom]
                prix = web_scrapping.recherche(link)
    prix_actuel = float(prix[1:])
            
    ValeurAchat = Amount/Token_Achat
    Gain = ' + 0 %'
    Pertes = ' - 0 % '
    

    cur.execute(f"SELECT * From Invest where Nom_Crypto='{Nom_Crypto.upper()}';")
    if cur.fetchall() == [] : 
        cur.execute(f"Insert into Invest Values ('{Nom_Crypto.upper()}',{Amount},{Token_Achat},{ValeurAchat},'{Date}',{prix_actuel},'{Gain}','{Pertes}');")
        con.commit()
    con.close()


add_invest()
    


