<!--ADD GAME HOMEPAGE-->


<html>
<body>
<h2>ADD GAME</h2>
<p>Enter Competition Information</p>
<form action="add_game.php" method="post">
    HOME TEAM NAME: <input type="text" name="home"><br>
    AWAY TEAM NAME: <input type="text" name="away"><br>
    LOCATION OF COMPETITION: <input type="text" name="city"><br>
    DATE OF COMPETITION: <input type="date" name="date"><br>
    <input name="addGame" type="submit" >
</form>
<br><br>

<a href="http://www.csce.uark.edu/~dtjackso/sport_db/home.html">HOME</a>

</body>
</html>

<?php
//This webpage handles the logic to game informaiton 
//To the database using POST 

if (isset($_POST['addGame'])) 
{
    // replace ' ' with '\ ' in the strings so they are treated as single command line args
    $home = escapeshellarg($_POST[home]);
    $away = escapeshellarg($_POST[away]);
    $city = escapeshellarg($_POST[city]);
    $date = escapeshellarg($_POST[date]);


    $command = 'python3 insert_game.py' . ' '.  $home . ' ' . $away . ' ' . $city . ' ' . $date;

    // remove dangerous characters from command to protect web server
    $escaped_command = escapeshellcmd($command);
    echo "<p>command: $command <p>"; 
    // run insert_new_item.py
    system($escaped_command);           
}

?>