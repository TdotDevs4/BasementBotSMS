<?php echo "-- Basement Bot SMS v0.1 --<br>
<br>+ Today's date is [".date('D M j G:i:s T Y'); ?>] +
<br>
<br>

<?php
$strUserType = $_GET["strUserType"];
if ($strUserType == "1001") {
  echo nl2br(file_get_contents('admin_commands.txt'));
} else {
  echo nl2br(file_get_contents('user_commands.txt'));
}
?>

<br><br><br>
+----------------------------------------------<br>
+ User Type : 
[<?php
$strUserType = $_GET["strUserType"];
if ($strUserType == "1001") {
  echo 'Admin';
} else {
  echo 'Non-Admin';
  if ($strUserType == "1000") { echo '...or don\'t, have not figured out how to prevent that yet.';}
}
?>]

<br>
+ User ID : 
[<?php
$strUserType = $_GET["strUserType"];
if ($strUserType == "1001") {
  echo '1001';
} else {
  echo '1002';
}
?>]

<br>
<form action="command_output.php" method="get">
  Command : 
 <input type="hidden" name="strUserType"  value=<?php echo $_GET["strUserType"]; ?> >
 <input type="text" name="strCommand" required><br>
 <input type="submit">
</form>
<br>
<br>