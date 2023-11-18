from connect import connector


conn,_=connector()

# ///////////////////////////////////////////////////////
# query = """

# CREATE TABLE User_det(
#     inmate_id INT PRIMARY KEY ,
#     password VARCHAR(255) NOT NULL
# );

# """
# update user_det

# query = """
#      ALTER TABLE User_det
    
#     ALTER COLUMN password SET NOT NULL;;
#     """

    # ALTER COLUMN inmate_id TYPE VARCHAR(255) ;


cursor = conn.cursor()
# cursor.execute(query)
# cursor.close()
# conn.commit()
# conn.close()
# ///////////////////////////////////////////////////////

# query = """
#     SELECT table_name
#     FROM information_schema.tables
#     WHERE table_schema = 'public';
#     """
# query = """
#     SELECT *
#     FROM User_det
#     ;
#     """
# id='21mh176'
# query = f"SELECT * FROM inmate where inmate_id = '{id}';"
query = f"SELECT * FROM inmate ;"

# query = """ALTER TABLE Inmate ALTER COLUMN inmate_id TYPE VARCHAR(50);"""

# query = """UPDATE Inmate SET inmate_id = '21mh176' WHERE inmate_id = '1';"""
print(query)
cursor.execute(query)
# column_names = [desc[0] for desc in cursor.description]
# for name in column_names:
#         print(name)
tables = cursor.fetchall()

print (tables)
for table in tables:
        print(table)
cursor.close()
conn.commit()
conn.close()