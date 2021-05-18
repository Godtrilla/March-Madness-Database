<!--SEARCH RESULT BY DATE HOMEPAGE-->
<!--SEARCHES DATABASE BY USING DATE GIVEN BY USER-->

<html>
    <body>
    <h2>DISPLAY RESULTS BY DATE</h2>
    <p>Enter Date of Competition</p>
    <form action="results_by_date.php" method="post">
        DATE: <input type="date" name="gameDate"><br>
    <input name="dateSearch" type="submit">
</form>
<br><br>


<a href="http://www.csce.uark.edu/~dtjackso/sport_db/home.html">HOME</a>

</body>
</html>

<?php

//This webpage handles the logic to send date informaiton 
//To the database using POST 
if (isset($_POST['dateSearch'])) 
{
    // replace ' ' with '\ ' in the strings so they are treated as single command line args
    $gameDate = escapeshellarg($_POST[gameDate]);



    $command = 'python3 results_by_date.py' . ' '.  $gameDate;

    // remove dangerous characters from command to protect web server
    $escaped_command = escapeshellcmd($command);
    echo "<p>command: $command <p>"; 
    // run insert_new_item.py
    system($escaped_command);           
}
?>