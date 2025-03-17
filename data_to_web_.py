#your code is here
from flask import Flask, url_for, redirect
import sqlite3

def index():
    conn = sqlite3.connect("Artistc.db")
    cursor = conn.cursor()
    cursor.execute('SELECT name FROM artists WHERE "Birth Year"  = (?)', [year])
    data = cursor.fetchall()

    if len (data) == 0 :
        return 'There is no data in the database about artists born in '+ str(year)+'year'

    elif len(data)== 1:
        return 'In' + str(year)+ 'year was born (born)'+ data[0][0]

    else:
        result = '<h3>List of artists born in '+ str(year)+ 'year</h3><ol>'
        for person in data:
            result += '<li>' + person [0] + '</li>'
        result += '</ol>'
    return result 

year = int(input("Enter the artist's year of birth:"))
app = Flask(__name__)
app.add_url_rule('/', 'index', index)

if __name__ == "__main__":
    app.run()

