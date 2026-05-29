### sqllite 
* based on c library  
* import sqlite3 
* >>  after this make connections  
* con = sqlite3.connect("file name.extention)  
___ return connection object<br>
* commit is done by connection 
* cur = con.cursor()  
__connectiob object direct talk to database  in form of queries  
* cur.execute("sql queries") ##   
* value comes in the form of tuples ('hello',)