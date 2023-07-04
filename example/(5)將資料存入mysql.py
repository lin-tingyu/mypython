import pymysql
from pandas import DataFrame

# DataFrame data
data_0 = ([0.9, -0.2], [0.5, 0.2], [1, 2])
DF_2 = DataFrame(data_0, columns=['A', 'B'], index=['one', 'two', 'three'])

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
    with connection.cursor() as cursor:
        # Create the table if it doesn't exist
        create_table_query = """
        CREATE TABLE IF NOT EXISTS dataframe_data (
            id INT AUTO_INCREMENT PRIMARY KEY,
            A FLOAT,
            B FLOAT
        )
        """
        cursor.execute(create_table_query)
        connection.commit()

        # Iterate over the DataFrame rows and insert data into the table
        for row in DF_2.itertuples():
            insert_query = "INSERT INTO dataframe_data (A, B) VALUES (%s, %s)"
            cursor.execute(insert_query, (row.A, row.B))
            connection.commit()

finally:
    # Close the database connection
    connection.close()

print("DataFrame data saved to MySQL table 'dataframe_data'")



