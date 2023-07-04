import pymysql
import pandas as pd

# MySQL connection information
db_settings = {
    "host": "127.0.0.1",
    "port": 3306,
    "user": "root",
    "password": "1234",
    "db": "python_test",
    "charset": "utf8"
}

# Establish a connection to the MySQL database
connection = pymysql.connect(**db_settings)

try:
    # Query to select all rows from the table
    select_query = "SELECT * FROM dataframe_data"

    # Read data from MySQL into a pandas DataFrame
    df = pd.read_sql(select_query, connection)

    # Print the DataFrame
    #print(df)

finally:
    # Close the database connection
    connection.close()
    
    
#print(type(df['A'][0]))
b =df['A'][0]+1
print(b)






