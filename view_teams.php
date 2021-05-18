<!--HOMEPAGE TO PRINT ALL TEAM INFO TO SCREEN-->


<html>
    <body>
    <h2>VIEW ALL TEAMS</h2>
<p>Display all team information</p>
<form action="view_teams.php" method="post">
    <input 
        name="viewTeams" 
        type="submit" 
        value="VIEW TEAM DATA">
</form>
<br><br>

<a href="http://www.csce.uark.edu/~dtjackso/sport_db/home.html">HOME</a>


</body>
</html>

<?php
//This webpage handles the logic to TEAM informaiton 
//To the database using POST 
if (isset($_POST['viewTeams'])) 
{
    // replace ' ' with '\ ' in the strings so they are treated as single command line args

    $command = 'python3 view_teams.py';

    // remove dangerous characters from command to protect web server
    $escaped_command = escapeshellcmd($command);
    echo "<p>command: $command <p>"; 
    // run insert_new_item.py
    system($escaped_command);           
}
?>