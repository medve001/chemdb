# chemdb




#### Examples of Query Sintax (in SQLite Manager for FireFox):
SELECT * FROM DB_index WHERE NAME LIKE '%trazine' OR Sample_ID LIKE 'TX2%'

SELECT * FROM DB_index WHERE Sample_ID='TX001546' OR Sample_ID='TX101546' OR Sample_ID='TX201546'

SELECT * FROM DB_index WHERE Sample_ID IN ('TX001546', 'TX101546', 'TX201546');

SELECT * FROM DB_index WHERE Sample_ID IN ('TX001546', 'TX101546', 'TX201546') OR NAME LIKE '%trazine';

#### Python import csv to sqlite links:
http://stackoverflow.com/questions/31243618/python-import-csv-to-sqlite

http://ask.webatall.com/python/5771_importing-a-csv-file-into-a-sqlite3-database-table-using-python.html

http://hosseinkaz.blogspot.com/2014/11/importing-csv-file-into-sqlite3-python.html

