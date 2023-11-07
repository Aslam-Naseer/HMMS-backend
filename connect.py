import psycopg2

DATABASE_URL = 'postgres://anant:WoyrN8EmXl850EZ3PMX9JCJeLy14Mhij@dpg-cl4fbviuuipc73a7mk7g-a.oregon-postgres.render.com/hmms'
def connector():

    try:
        
        conn = psycopg2.connect(DATABASE_URL)

        return conn,"Successfully connected"

    except (Exception, psycopg2.Error) as error:
        print("Error fetching tables:", error)
        return None,"Connection failed"
