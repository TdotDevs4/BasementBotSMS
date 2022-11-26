<?php echo "-- Basement Bot SMS v0.1 --<br>
<br>+ Today's date is [".date('D M j G:i:s T Y'); ?>] +
<br>
<br>

+----------------------------------------------------------------------+
<br>
+ User Type : [<?php echo $_GET["strUserType"]; ?>]
<br>
+ Command : [<?php echo $_GET["strCommand"]; ?>] 
<br>
+----------------------------------------------------------------------+
<br><br?+
+----------------------------------------------------------------------+
<br>
+ Output: <br><br>>><br>
<?php
 $userType = $_GET["strUserType"];
 $command = $_GET["strCommand"];
 echo exec('python command_processor.py ' .$userType .' '. $command);
?>
<br>
>>
<br><br>
+----------------------------------------------------------------------+

<br><br>
<form>
 <input type="button" value="Do it again 'Ma!" onclick="history.back()">
</form>

<br><br>
<form action="index.php">
  <input type="submit" value="Start Over">
</form>