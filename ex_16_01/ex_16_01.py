import sqlite3

conn = sqlite3.connect('count1.sqlite')
cur = conn.cursor()
#execute() just excute one sql command!!!
cur.execute('DROP TABLE IF EXISTS Counts')
cur.execute('CREATE TABLE Counts(org TEXT, count INTEGER)')

fname = input('Enter file name: ')
if (len(fname) < 1): fname = 'mbox-short.txt'
fh = open(fname)
for line in fh:
    if not line.startswith('From: '): continue
    pieces = line.split('@')
#print(pieces[1])
    org = pieces[1]
    #prevent sql injection!!, second one is tuple
    cur.execute('SELECT count FROM Counts WHERE org = ? ', (org,))
    # grab the first one to row
    row = cur.fetchone()
    if row is None:
        cur.execute('INSERT INTO Counts(org, count)VALUES (?, 1)', (org,))
    else:
        cur.execute('UPDATE Counts SET count = count + 1 WHERE org = ?', (org,))
    #write data to disk
conn.commit()
sqlstr = 'SELECT org, count FROM Counts ORDER BY count DESC LIMIT 10'

for row in cur.execute(sqlstr):
    print(str(row[0]), row[1])
cur.close()
