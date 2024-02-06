import mysql.connector
mydb=mysql.connector.connect(host='localhost',user='root',password='Linga@12#',database="MediPredict")
mycursor = mydb.cursor()
# mycursor.execute('CREATE DATABASE MediPredict')  #creating Database

# mycursor.execute("SHOW DATABASES")      # showing all databases 
# for x in mycursor:
#     print(x)

# create_table_query = """
# CREATE TABLE BreastCancer(
#     name VARCHAR(255),
#     radius_mean FLOAT,
#     texture_mean FLOAT,
#     perimeter_mean FLOAT,
#     area_mean FLOAT,
#     perimeter_se FLOAT,
#     area_se FLOAT,
#     radius_worst FLOAT,
#     texture_worst FLOAT,
#     perimeter_worst FLOAT,
#     area_worst FLOAT,
#     breast_val INT
# )
# """
# create_table_query = """
# CREATE TABLE counter( 
#     count INT
# )
# """

# mycursor.execute(create_table_query)

# mycursor.execute("SHOW TABLES")
# for x in mycursor:
#     print(x) 

# sql="INSERT INTO counter(count) VALUE (%s) " 
# val=[0]
# mycursor.execute(sql,val) 
# mydb.commit() 

# sql="SELECT * from data"
# mycursor.execute(sql)
# result=mycursor.fetchall()
# for i in result:
#     print(i) 

# sql="SELECT * from DATA WHERE username='Linga Reddy'"
# mycursor.execute(sql)
# result=mycursor.fetchall()
# for i in result:
#     print(i) 

# sql="UPDATE DATA SET username='Linga' WHERE username='Linga Reddy'"
# mycursor.execute(sql)
# mydb.commit() 


sql="SELECT * from counter"
mycursor.execute(sql)
result=mycursor.fetchall()
c=result[0][0]+1

sql=f"UPDATE counter SET count={result[0][0]+1} WHERE count={result[0][0]}"
mycursor.execute(sql)
mydb.commit() 


 







