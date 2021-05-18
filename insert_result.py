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
    res =marchMadnessDB.executeSelect('SELECT * FROM Results;')
    res=res.split('\n')# split the header and data for printing
    
    # PRINTING TABLE TO SCREEN 
    print("<br/>"+ "Table Results before:"+"<br/>" + res[0] + "<br/>"+ res[1] + "<br/>")
    for i in range(len(res)-2):
        print(res[i+2]+"<br/>")
    flag = len(res)

    # RETRIEVING GAME ID
    q3 = """ 
    SELECT g.gameID
    FROM Game g
    WHERE '{0}' = g.home AND '{1}' = g.away;
    """

    homeTeam = sys.argv[1]
    awayTeam = sys.argv[2]
    homeScore = sys.argv[3]
    awayScore = sys.argv[4]

    # homeTeam = 'Creighton'
    # awayTeam = 'Ohio'
    # homeScore = '72'
    # awayScore = '58'

    # SETTING ID, IF RECORD HAS RELATION TO RESULT
    # GAME.ID = RESULT.ID IF NOT, ID IS SET AUTOMATICALLY
    teamID = marchMadnessDB.read_query(q3.format(homeTeam,awayTeam))
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
    # val = homeTeam + "','" + awayTeam + "','" + homeScore + "','" + awayScore + "'"
    val = teamID + ",'" + homeTeam + "','" + awayTeam + "','" + homeScore + "','" + awayScore + "'"
    marchMadnessDB.insert("Results",val)
    res = marchMadnessDB.executeSelect('SELECT * FROM Results;')
    res=res.split('\n')# split the header and data for printing
    if(len(res) == flag):
        print("INSERT FAILED")
    else:
        print("<br/>" + "<br/>")
        print("<br/>"+ "Table Results after:"+"<br/>" + res[0]+ "<br/>"+res[1]+ "<br/>")
        for i in range(len(res)-2):
            print(res[i+2]+"<br/>")
    marchMadnessDB.close() # close db 
except Exception as e:
        logging.error(traceback.format_exc())
        print(traceback.format_exc())

