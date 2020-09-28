
#!/usr/bin/env python3
import sqlite3
#import os
#connect to database file
dbconnect = sqlite3.connect("part3.db");
#THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
#my_file = os.path.join(THIS_FOLDER, 'part3.db')
#If we want to access columns by name we need to set
#row_factory to sqlite3.Row class
dbconnect.row_factory = sqlite3.Row;
#now we create a cursor to work with db
cursor = dbconnect.cursor();
#execute insert statement
#cursor.execute('''INSERT INTO temps values(date('now'), time('now'), "living room", 21.8);''');
dbconnect.commit();
#execute simple select statement
cursor.execute('SELECT * FROM temps');
#print data
for row in cursor:
    print(row['tdate'],row['ttime'],row['zone'], row['temperature']);
    
#close the connection
dbconnect.close();
