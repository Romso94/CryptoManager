import csv
from email import header
import sqlite3
import os

def update_csv():
    con = sqlite3.connect('Crypto.db')
    cursor = con.cursor()
    cursor.execute("select * from Invest")
    with open("Crypto.csv", "w") as csv_file:
      csv_writer = csv.writer(csv_file, delimiter=";")
      csv_writer.writerow([i[0] for i in cursor.description])
      csv_writer.writerows(cursor)

    dirpath = os.getcwd() + "\Crypto.csv"
    print ("Data exported Successfully into {}".format(dirpath))

    con.close()

def update_db(name_crypto):
    con = sqlite3.connect('Crypto.db')
    

