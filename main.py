import sqlite3
import time
from turtle import st
import update_db
import web_scrapping

def start(value):
    Dico_Link = {'amp':'amp',
                     'xrp':'xrp',
                     'grt':'the-graph',
                     'xlm':'stellar',
                     'mana':'decentraland',
                     'near':'near-protocol',
                     'fantom':'fantom',
                     'cop':'copiosa-coin'}
    if value == 1:
        name = input('Name of crypto searched : ').lower()
        
        for nom in Dico_Link :
            if nom==name:
                link = Dico_Link[nom]
        prix = web_scrapping.recherche(link)
        print(f"{name.upper()} current value is : {prix[1:]} €")    
        valeur= prix[1:]
        valeur = float(valeur)

       
    elif value == 2 :
        update_db.add_invest()

    elif value == 3:
        update_db.update_db_cours()
        print('Database Uploaded !')
        




        



 

  
       



if __name__=='__main__':
    print( '   ___                 _                                                 ')                 
    print( '  / __\ __ _   _ _ __ | |_ ___   /\/\   __ _ _ __   __ _  __ _  ___ _ __ ')  
    print( " / / | '__| | | | '_ \| __/ _ \ /    \ / _` | '_ \ / _` |/ _` |/ _ \ '__|")
    print( '/ /__| |  | |_| | |_) | || (_) / /\/\ \ (_| | | | | (_| | (_| |  __/ |   ') 
    print( '\____/_|   \__, | .__/ \__\___/\/    \/\__,_|_| |_|\__,_|\__, |\___|_| ')
    print( '           |___/|_|                                      |___/    ')
    Liste_Actions = ['-1 search price of crypto in euro','-2 add an investisment in your DataBase','-3 auto-update your DB ']
    for i in Liste_Actions:
        print(i)
    val = int(input('Enter a number : '))
    start(val)