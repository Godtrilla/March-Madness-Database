import mysql.connector
from tabulate import tabulate

def open_database (hostname,user_name,mysql_pw,database_name):
      global conn
      conn= mysql.connector.connect(host= hostname, 
      user= user_name,  
      password= mysql_pw, 
      database= database_name 
    ) 
      global cursor
      cursor = conn.cursor() 

def read_query(query):
    result = None
    cursor.execute(query)
    result = cursor.fetchall()
    return result

def printFormat(result):
    header=[]
    for cd in cursor.description:# get headers
        header.append(cd[0])
    print('')
    print('Query Result:')
    print('')
    return(tabulate(result, headers=header))# print results in table format

# select and display query
def executeSelect (query):
    cursor.execute(query)
    res = printFormat(cursor.fetchall())
    return res

def  insert(table,values):
     query ="INSERT into " + table + " values (" + values + ")" +';'
     cursor.execute(query)
     conn.commit()


def executeUpdate(query): # use this function for delete and update
    cursor.execute(query)
    conn.commit()


def close_db ():  # use this function to close db
    cursor.close()
    conn.close()


