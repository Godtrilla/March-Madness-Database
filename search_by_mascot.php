<html>
<!--SEARCH DATABASE BY MASCOT HOMEPAGE-->
<!--SEARCHES DATBASE BY USING MASCOT KEYWORKD GIVEN BY USER-->



<body>
<h2 id="uniSearch">SEARCH BY MASCOT</h2>
<p>Enter name of your school mascot</p>
<form action="search_by_mascot.php" method="post">
MASCOT NAME: <input type="text" name="mascot"><br>
<input name="mascotSearch" type="submit" >
</form>
<br><br>



    <a href="http://www.csce.uark.edu/~dtjackso/sport_db/home.html">HOME</a>

</body>
</html>

<?php
//This webpage handles the logic to mascot informaiton 
//To the database using POST 
if (isset($_POST['mascotSearch'])) 
{
    // replace ' ' with '\ ' in the strings so they are treated as single command line args
    $mascot = escapeshellarg($_POST[mascot]);



    $command = 'python3 search_by_mascot.py' . ' '.  $mascot;

    // remove dangerous characters from command to protect web server
    $escaped_command = escapeshellcmd($command);
    echo "<p>command: $command <p>"; 
    // run insert_new_item.py
    system($escaped_command);           
}
?>