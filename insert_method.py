import sys
import traceback
import logging
import marchMadnessDB


mysql_username = 'dtjackso' # turing server username
mysql_password= 'Voozae7e'  # turing server password

try:
    # OPEN DATABSE
    marchMadnessDB.open_database('localhost',mysql_username,mysql_password,mysql_username) # open database
    
    # EXECUTING SELECT TO SHOW TABLE BEFORE ALTERATION
    res =marchMadnessDB.executeSelect('SELECT * FROM Team;')
    res=res.split('\n')# split the header and data for printing
    
    # PRINTING TABLE TO SCREEN 
    print("<br/>"+ "Table TEAM before:"+"<br/>" + res[0] + "<br/>"+ res[1] + "<br/>")
    for i in range(len(res)-2):
        print(res[i+2]+"<br/>")
    
    # FLAG TO KEEP TRACK OF TABLE LENGTH
    flag = len(res)

    # RETRIEVING GAME ID
    q2 = """ 
    SELECT MAX(s.teamID) 
    FROM Team s;
    """
    teamID = marchMadnessDB.read_query(q2)
    temp = int(teamID[0][0])
    teamID = temp + 1
    teamID = str(teamID)

    # insert into item tables by getting the values passed from PHP
    teamName = sys.argv[1]
    nickname = sys.argv[2]
    teamRank = sys.argv[3]

    #EXECUTION OF RESULT OF QUERY AND PRINT TO SCREEN
    val = teamID + ",'" + teamName + "','" + nickname + "','" + teamRank + "'"
    marchMadnessDB.insert("Team",val)
    res = marchMadnessDB.executeSelect('SELECT * FROM Team;')
    if(len(res) == flag):
        print("INSERT FAILED")
    else:
        res=res.split('\n')# split the header and data for printing
        print("<br/>" + "<br/>")
        print("<br/>"+ "Table Team after:"+"<br/>" + res[0]+ "<br/>"+res[1]+ "<br/>")
        for i in range(len(res)-2):
            print(res[i+2]+"<br/>")
    marchMadnessDB.close() # close db    
except Exception as e:
        logging.error(traceback.format_exc())
        print("ADDITION FAILED")
        print(traceback.format_exc())