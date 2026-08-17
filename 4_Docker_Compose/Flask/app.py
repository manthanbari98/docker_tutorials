from flask import Flask
import pymysql

app = Flask("__name__")


@app.route("/")
def hello():    
    return "Hello, World!"

@app.route("/insert_data")
def insert_data():
    # Connection to the MySQL database
    connection = pymysql.connect(
        host='mysql_container',
        user='root',
        password='demopassword',
        database='demo_db'
        )
    
    # Create a cursor object to interact with the database
    cursor = connection.cursor()

    # SQL query to insert data into the table
    sql_query = "INSERT INTO users (city, temperature) VALUES (%s, %s)"

    data = ("New York", 25.5)  # Example data to insert

    cursor.execute(sql_query, data)

    #commit the changes to the database
    connection.commit()

    # Close the cursor and connection
    cursor.close()

    return "Data inserted successfully!"

if __name__ == "__main__":
    app.run(host="0.0.0.0",port=5000, debug=True)
