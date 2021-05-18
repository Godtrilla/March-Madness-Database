import sys
import traceback
import logging
import marchMadnessDB


mysql_username = 'dtjackso' # turing server username
mysql_password= 'Voozae7e'  # turing server password

try:
    marchMadnessDB.open_database('localhost',mysql_username,mysql_password,mysql_username) # open database
    gameDate = sys.argv[1]
    
    # QUERIES THAT WILL CREATE A VIEW IN ORDER 
    # TO FORM FINAL TABLE THAT'S NEEDED
    v1 = """
        CREATE VIEW v1 
        AS
        SELECT DISTINCT g.gameID, g.home, t.nickname, r.homeScore, g.region, g.date
        FROM Team t, Results r, Game g
        WHERE g.home = t.schoolName AND r.gameID = g.gameID AND g.date = '{0}';
    """

    v2 = """
    CREATE VIEW v2 
    AS
    SELECT DISTINCT g.gameID, g.away, t.nickname, r.awayScore, g.region, g.date
    FROM Team t, Results r, Game g
    WHERE g.away = t.schoolName AND r.gameID = g.gameID AND g.date = '{0}';    
    """

    join = """
    SELECT DISTINCT v1.gameID, v1.home, v1.nickname,
    v1.homeScore, v2.away, v2.nickname, v2.awayScore, v2.region, v2.date
    FROM v1
    INNER JOIN v2 ON v1.gameID = v2.gameID;
    """

    #QUERIES TO DROP VIEWS AFTER DONE FOR EFFICIENCY
    drop1 = """ drop view v1;"""
    drop2 = """ drop view v2;"""

    #EXECUTION OF RESULT OF QUERY AND PRINT TO SCREEN
    marchMadnessDB.executeUpdate(v1.format(gameDate))
    marchMadnessDB.executeUpdate(v2.format(gameDate))
    res = marchMadnessDB.executeSelect(join)
    res=res.split('\n')# split the header and data for printing


    if(len(res) == 2):
        print("NO DATA FOUND")
    else:
        print("<br/>"+ "Table Game before:"+"<br/>" + res[0] + "<br/>"+ res[1] + "<br/>")
        for i in range(len(res)-2):
                print(res[i+2]+"<br/>")
    marchMadnessDB.executeUpdate(drop1)
    marchMadnessDB.executeUpdate(drop2)
    marchMadnessDB.close() # close db    
except Exception as e:
        logging.error(traceback.format_exc())

