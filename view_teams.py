import sys
import traceback
import logging
import marchMadnessDB


mysql_username = 'dtjackso' # turing server username
mysql_password= 'Voozae7e'  # turing server password

try:
    #OPEN DATABASE
    marchMadnessDB.open_database('localhost',mysql_username,mysql_password,mysql_username) # open database
    
    #EXECUTION OF RESULT OF QUERY AND PRINT TO SCREEN
    res =marchMadnessDB.executeSelect('SELECT * FROM Team;')
    res=res.split('\n')# split the header and data for printing
    print("<br/>"+ "Table Team:"+"<br/>" + res[0] + "<br/>"+ res[1] + "<br/>")
    for i in range(len(res)-2):
        print(res[i+2]+"<br/>")

    marchMadnessDB.close() # close db   
except Exception as e:
        logging.error(traceback.format_exc())
