# Search DB (created in FireFox SQLite Manager) for chemical names and CAS by IDs 
import csv
import sqlite3
conn = sqlite3.connect('DB_index6.sqlite')

myTerm = input('File term (First part of the file name):\n')

scoreList = [] # create empty list of top scores

# Open File with list of top scores and create a list of top scores
with open (myTerm + '-score.csv') as csvfile:
    myDict = csv.DictReader(csvfile)
    for row in myDict:
        scoreList.append(row['Sample_ID'])
        # print(row['Sample_ID'])

print('Printing scoreList')
print(scoreList)

# Create cusor object
cdb = conn.cursor()

# Creates .csv file with four columns: 'Name', 'Compound_ID', 'Plate_ID','CAS'
with open(myTerm + '-score-id.csv', 'w', newline='') as f:
    spamwriter = csv.writer(f, delimiter=',') #,quotechar='', quoting=csv.QUOTE_MINIMAL)
    spamwriter.writerow(['Name', 'SAMPLE_ID', 'Plate_ID','CAS','ATG_ID'])

# Loops to find DB matches and writes to .csv file created above
for t in scoreList:
    print(t)
    cdb.execute('SELECT * FROM DB_index6 WHERE SAMPLE_ID=?', (t,))  # Coma after "t" is IMPORTANT
    rows = cdb.fetchall()
    print('Database match for ' + str(t) + ':')
    # print(list(rows[0]))
    with open(myTerm + '-score-id.csv', 'a', newline='') as csvfile2:
        score_writer = csv.writer(csvfile2, delimiter=',',quotechar='"', quoting=csv.QUOTE_MINIMAL)
        try:
            score_writer.writerow(list(rows[0]))
        except IndexError:
            score_writer.writerow('null')

conn.close()
