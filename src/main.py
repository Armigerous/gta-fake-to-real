import sqlite3
import os

os.chdir(r"C:\Users\tugra\OneDrive\Desktop\fun\gta-fake-to-real\data")
# create database
connection = sqlite3.connect("gta.db")
cursor = connection.cursor()

#the list of gta games
release_list = [
    (1997, "Grand Theft Auto", "state of New Guernsey"),
    (1999, "Grand Theft Auto 2", "Anywhere, USA"),
    (2001, "Grand Theft Auto III", "Liberty City"),
    (2002, "Grand Theft Auto: Vice City", "Vice City"),
    (2004, "Grand Theft Auto: San Andreas", "state of San Andreas"),
    (2008, "Grand Theft Auto IV", "Liberty City"),
    (2013, "Grand Theft Auto V", "Los Santos")
]    

# list of gta cities and their real world equivalent
cities_list = [
    ("state of New Guernsey", "New Jersey"),
    ("Liberty City", "New York City"),
    ("Vice City", "Florida"),
    ("state of San Andreas", "Las Vegas"),
    ("Los Santos", "Los Angeles")
]

# create database table and populate it with release_list
try:
    cursor.execute("CREATE TABLE gta (release_year integer, release_name text, city text)")
    cursor.executemany("INSERT INTO gta VALUES (?,?,?)", release_list)
except:
    print("already exists")
connection.commit()
# print all rows
for row in cursor.execute("SELECT * FROM gta"):
    print(row)

#seperator
print("___________________________________")

#get every entry in the database
cursor.execute("SELECT * FROM gta")
gta_search = cursor.fetchall()
print(gta_search)

#seperator
print("___________________________________")

#make a list of fake and real cities
try:
    cursor.execute("CREATE TABLE cities (gta_city text, real_city text)")
    cursor.executemany("INSERT INTO cities VALUES (?,?)", cities_list)
    cursor.execute("SELECT * FROM cities")
except:
    print("already exists")

connection.commit()
cities_search = cursor.fetchall()
print(cities_search)
#seperator
print("___________________________________")

counter = 0
# replace every gta city with real representations
for i in gta_search:
    adjusted = i
    for j in cities_search:
        if i[2] == j[0]:
            adjusted = (i[0], i[1], j[1])
            cursor.execute("UPDATE gta SET city=? WHERE release_year=?", (j[1], i[0]))
            connection.commit()
            break
    print(adjusted)
    

#ends connection
connection.close()
