<!--ADD RESULT HOMEPAGE-->

<h1>Did you add the Game first?</h1>
<html>
<body>
<h2>ADD GAME RESULT</h2>
<p>Enter Result of Competition</p>
<form action="add_result.php" method="post">
    HOME TEAM: <input type="text" name="homeTeam"><br>
    AWAY TEAM: <input type="text" name="awayTeam"><br>
    HOME SCORE: <input type="number" name="homeScore"><br>
    AWAY SCORE: <input type="number" name="awayScore"><br>
    <input name="addResult" type="submit" >
</form>
<br><br>

<a href="http://www.csce.uark.edu/~dtjackso/sport_db/home.html">HOME</a>

</body>
</html>

<?php

if (isset($_POST['addResult'])) 
{
    // replace ' ' with '\ ' in the strings so they are treated as single command line args
    $homeTeam = escapeshellarg($_POST[homeTeam]);
    $awayTeam = escapeshellarg($_POST[awayTeam]);
    $homeScore = escapeshellarg($_POST[homeScore]);
    $awayScore = escapeshellarg($_POST[awayScore]);


    $command = 'python3 insert_result.py' . ' '.  $homeTeam . ' ' . $awayTeam . ' ' . $homeScore . ' ' . $awayScore;

    // remove dangerous characters from command to protect web server
    $escaped_command = escapeshellcmd($command);
    echo "<p>command: $command <p>"; 
    // run insert_new_item.py
    system($escaped_command);           
}

?>