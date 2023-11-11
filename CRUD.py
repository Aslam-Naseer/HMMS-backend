
def insertor(conn,query):


    cursor = conn.cursor()
    cursor.execute(query)
    cursor.close()
    conn.commit()

def fetcher(conn,query):
    cursor = conn.cursor()
    cursor.execute(query)
    datas = cursor.fetchall()
    cursor.close()
    return datas

def user_search (conn,query):  
    cursor = conn.cursor()
    cursor.execute(query)
    data = cursor.fetchone()
    cursor.close()
    return data




