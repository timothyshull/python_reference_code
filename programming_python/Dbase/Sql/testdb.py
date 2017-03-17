from sqlite3 import connect

conn = connect('dbase1')
curs = conn.cursor()
try:
    curs.execute('DROP TABLE people')
except:
    pass  # did not exist
curs.execute('CREATE TABLE people (name char(30), job char(10), pay INT(4))')

curs.execute('INSERT INTO people VALUES (?, ?, ?)', ('Bob', 'dev', 50000))
curs.execute('INSERT INTO people VALUES (?, ?, ?)', ('Sue', 'dev', 60000))

curs.execute('SELECT * FROM people')
for row in curs.fetchall():
    print(row)

curs.execute('SELECT * FROM people')
colnames = [desc[0] for desc in curs.description]
while True:
    print('-' * 30)
    row = curs.fetchone()
    if not row: break
    for (name, value) in zip(colnames, row):
        print('%s => %s' % (name, value))

conn.commit()  # save inserted records
