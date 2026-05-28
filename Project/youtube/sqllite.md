### sqllite 
* based on c library  
* import sqlite3  
* con = sqlite3.connect("file name.extention)  
___ return connection object  <br>
* cur = con.cursor()  
__connectiob object direct talk to database  in form of queries  
* cur.execute("sql queries") ##   
* value comes in the form of tuples ('hello',)