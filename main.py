from turtle import st
import web_scrapping

def start(value):
    if value == 1:
        name = input('Nom de la crypto : ').lower()
        Dico_Link = {'amp':'amp',
                     'xrp':'xrp',
                     'grt':'the-graph',
                     'xlm':'stellar',
                     'mana':'decentraland',
                     'near':'near-protocol'}
        for name in Dico_Link :
            link = Dico_Link[name]
        print(f"Le cours actuel de {name} est : {web_scrapping.recherche(link)}")





if __name__=='__main__':
    Liste_Actions = ['Tape 1 pour rechercher le cours de la crypto ']
    for i in Liste_Actions:
        print(i)
    val = int(input('Entrez une action '))
    start(val)