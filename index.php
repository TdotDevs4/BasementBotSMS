<a href="https://www.basementbotsms.com/" target="_blank" rel="noopener noreferrer">www.BasementBotSMS.com</a>
<br><br>

<?php echo "-- Basement Bot SMS v0.1 --<br>
<br>+ Today's date is [".date('D M j G:i:s T Y'); ?>] +
<br>
<br>

<html>
<body>

<form name=cmbUserType action="command_input.php" method="get">
  <p>
  <label for="cmbUserType">User Type: </label>
  <select name=strUserType size=1">
    <option value="1000" selected hidden>Choose one...
    <option value="1001">Admin
    <option value="1002">Non-Admin
  </select>
  </p>
<input type="submit" value="Enter Basement Bot SMS">
</form>


</body>
</html>