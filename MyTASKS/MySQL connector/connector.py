import mysql.connector

db = mysql.connector.connect(
    host = "localhost",
    user = "root",
    passwd= "qosim",
    database = "giraffe"
)

mycursor = db.cursor()
Q1="SELECT salesman.salesman_id,name,city,ord_date,grade FROM salesman INNER JOIN orders ON salesman.salesman_id = orders.salesman_id"
Q2 = "INSERT INTO orders VALUES(1,5.4,'2022-09-26', 3,5003,300)"
mycursor.execute(Q1)
# db.commit()

for i in mycursor:
    print(i)