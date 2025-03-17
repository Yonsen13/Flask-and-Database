import sqlite3

conn = sqlite3.connect("Artistc.db")
cursor = conn.cursor()

#how many artiist in database
cursor.execute('SELECT * FROM artists')
data = cursor.fetchall()
print('Number of artist in Database:',len(data))


cursor.execute('SELECT * FROM artists WHERE gender == "Female" ')
data = cursor.fetchall()
print('Number of Woman:', len(data))


cursor.execute('SELECT name from artists WHERE "Birth Year" < 1900 order by "Birth Year"')
data = cursor.fetchall()
print('The oldest:',data[0][0])