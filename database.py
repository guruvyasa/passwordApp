import sqlite3
def getConnection():
    return sqlite3.connect("data.db")

def createTables():
    query = '''
        create table if not exists password(id integer primary key,
                              url varchar(100) not null,
                              password varchar(100) not null)
        '''
    conn = getConnection()
    try:
        conn.execute(query)
        conn.commit()
        print("Tables created successfully")
    except Exception as e:
        print(e)
    finally:
        conn.close()

def addPassword(url, password):
    query = '''
        insert into password(url, password) values(?,?)
        '''
    conn = getConnection()
    try:
        conn.execute(query,(url, password))
        conn.commit()
        return "Password added successfully"
    except Exception as e:
        print(e)
        return "Something went wrong!!"
    finally:
        conn.close()
    
def getPasswords():
    query = '''
        select * from password
        '''
    conn = getConnection()
    try:
        return conn.execute(query).fetchall()
    except Exception as e:
        print(e)
        return []
    finally:
        conn.close()
    

if __name__ == "__main__":
    createTables()
    addPassword("github.com","abcd")
    addPassword("gmail.com","1234")
    addPassword("bitbucket","8888")
    addPassword("stackoverflow","999")
    for password in getPasswords():
        print(password)
