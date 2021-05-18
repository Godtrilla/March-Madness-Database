<!--ADD TEAM HOMEPAGE-->

<html>
<body>
<h2>ADD TEAM</h2>
<form action="add_team.php" method="post" id="addTeam">
    University Name: <input type="text" name="teamName"><br>
    Team Name: <input type="text" name="nickname"><br>
    Team National Rank: <input type="number" name="teamRank"><br>
    <input name="submit" type="submit" >
</form>
<br><br>

<a href="http://www.csce.uark.edu/~dtjackso/sport_db/home.html">HOME</a>

</body>
</html>

<?php 
if (isset($_POST['submit'])) 
{
    // replace ' ' with '\ ' in the strings so they are treated as single command line args
    $teamName = escapeshellarg($_POST[teamName]);
    $nickname = escapeshellarg($_POST[nickname]);
    $teamRank = escapeshellarg($_POST[teamRank]);

    $command = 'python3 insert_method.py' . ' '.  $teamName . ' ' . $nickname . ' ' . $teamRank;

    // remove dangerous characters from command to protect web server
    $escaped_command = escapeshellcmd($command);
    echo "<p>command: $command <p>"; 
    // run insert_new_item.py
    system($escaped_command);           
}

?>

