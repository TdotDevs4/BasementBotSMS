<?php echo "-- Basement Bot SMS v0.1 --<br><br>+ Today's date is ".date('D M j G:i:s T Y'); ?> +
<br>
<br>

<?php
$strUserType = $_POST["strUserType"];
$_GET['newUserType'] = $strUserType;

if ($strUserType == "1") {
  echo nl2br(file_get_contents('admin_commands.txt'));
} else {
  echo nl2br(file_get_contents('user_commands.txt'));
}
?>

<br><br>
<br>

<form action="command_output.php" method="get">
  Command (UserType=[<?php echo $_POST["strUserType"]; ?>]): 

 <input type="text" name="strCommand"><br>
 <input type="submit">
</form>
<br>
<br>