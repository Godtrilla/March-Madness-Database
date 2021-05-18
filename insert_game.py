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
    res =marchMadnessDB.executeSelect('SELECT * FROM Game;')
    res=res.split('\n')# split the header and data for printing
    
    # PRINTING TABLE TO SCREEN 
    print("<br/>"+ "Table Game before:"+"<br/>" + res[0] + "<br/>"+ res[1] + "<br/>")
    for i in range(len(res)-2):
        print(res[i+2]+"<br/>")
    
    # FLAG TO KEEP TRACK OF TABLE LENGTH
    flag = len(res)

    # RETRIEVING GAME ID
    q3 = """ 
    SELECT r.gameID
    FROM Result r
    WHERE '{0}' LIKE r.homeTeam AND '{1}' LIKE r.awayTeam;
    """
    #RETRIEVING ARGUMENTS FROM USER
    home = sys.argv[1]
    away = sys.argv[2]
    city = sys.argv[3]
    date = sys.argv[4]

    # SETTING ID, IF RECORD HAS RELATION TO RESULT
    # GAME.ID = RESULT.ID IF NOT, ID IS SET AUTOMATICALLY
    teamID = marchMadnessDB.read_query(q3.format(home,away))
    if(teamID == []):
            q2 = """ 
            SELECT MAX(g.gameID) 
            FROM Game g;
            """
            teamID = marchMadnessDB.read_query(q2)
            temp = int(teamID[0][0])
            teamID = temp + 1
            teamID = str(teamID)
            print(teamID)

    else:
        temp = int(teamID[0][0])
        teamID = temp
        teamID = str(teamID)

    #EXECUTION OF RESULT OF QUERY AND PRINT TO SCREEN
    val = teamID + ",'" + home + "','" + away + "','" + city + "','" + date + "'"
    marchMadnessDB.insert("Game",val)
    res = marchMadnessDB.executeSelect('SELECT * FROM Game;')
    if(len(res) == flag):
        print("INSERT FAILED")
    else:
        res=res.split('\n')# split the header and data for printing
        print("<br/>" + "<br/>")
        print("<br/>"+ "Table Game after:"+"<br/>" + res[0]+ "<br/>"+res[1]+ "<br/>")
        for i in range(len(res)-2):
            print(res[i+2]+"<br/>")
    marchMadnessDB.close() # close db    
except Exception as e:
        logging.error(traceback.format_exc())


