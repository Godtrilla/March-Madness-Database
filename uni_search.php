<!--SEARCH DATABASE BY USING UNIVERSITY NAME-->


<html>
<body>
<h2 id="uniSearch">SEARCH FOR YOUR UNIVERSITY</h2>
<p>Enter name of your school</p>
<form action="uni_search.php" method="post">
UNIVERSITY NAME: <input type="text" name="uniName"><br>
<input name="schoolSearch" type="submit" >
</form>
<br><br>



    <a href="http://www.csce.uark.edu/~dtjackso/sport_db/home.html">HOME</a>

</body>
</html>

<?php
// This webpage handles the logic to send UNIVERSITY NAME to 
// the database using POST 
if (isset($_POST['schoolSearch'])) 
{
    // replace ' ' with '\ ' in the strings so they are treated as single command line args
    $uniName = escapeshellarg($_POST[uniName]);



    $command = 'python3 uni_search.py' . ' '.  $uniName;

    // remove dangerous characters from command to protect web server
    $escaped_command = escapeshellcmd($command);
    echo "<p>command: $command <p>"; 
    // run insert_new_item.py
    system($escaped_command);           
}
?>