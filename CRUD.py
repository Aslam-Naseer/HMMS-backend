
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




