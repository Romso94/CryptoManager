import sqlite3
import time
from turtle import st
from update_db import  update_csv, update_db_cours
import web_scrapping

def start(value):
    Dico_Link = {'amp':'amp',
                     'xrp':'xrp',
                     'grt':'the-graph',
                     'xlm':'stellar',
                     'mana':'decentraland',
                     'near':'near-protocol'}
    if value == 1:
        name = input('Name of crypto searched : ').lower()
        
        for nom in Dico_Link :
            if nom==name:
                link = Dico_Link[nom]
        prix = web_scrapping.recherche(link)
        print(f"{name.upper()} value is currently : {prix[1:]} €")    
        valeur= prix[1:]
        valeur = float(valeur)

       
    elif value == 2 :
        pass

    elif value == 3:
        update_db_cours()
        




        





if __name__=='__main__':
    print( '_________                        __       ____   ____      .__')                 
    print( '\_   ___ \_______ ___.__._______/  |_  ___\   \ /   /____  |  |  __ __   ____')  
    print( '/    \  \/\_  __ <   |  |\____ \   __\/  _ \   Y   /\__  \ |  | |  |  \_/ __ \ ')
    print( '\     \____|  | \/\___  ||  |_> >  | (  <_> )     /  / __ \|  |_|  |  /\  ___/') 
    print( ' \______  /|__|   / ____||   __/|__|  \____/ \___/  (____  /____/____/  \___  >')
    print( '        \/        \/     |__|                            \/                 \/ ')
    Liste_Actions = ['-1 looking for price of crypto in euro','-2 add an investisment in your DataBase','-3 update your DB']
    for i in Liste_Actions:
        print(i)
    val = int(input('Enter a number : '))
    start(val)