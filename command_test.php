<?php echo "-- Basement Bot SMS v0.1 --<br><br>+ Today's date is ".date('D M j G:i:s T Y'); ?>
<br><br>

Command : [<?php echo $_POST["command"]; ?>]

<br>
<br>

Output (command_processor.py) :<br><br>
<?php
 $command = $_POST["command"];
 $pyout = exec('python command_processor.py ' .$command);
 echo $pyout;
?>

<br><br>
Output (PHP Conditional) :<br><br>
<?php
 $command = $_POST["command"];
 if ($command=="commands" || empty($command) ) {
  echo nl2br(file_get_contents('commands.txt'));
 } else {
 $pyout = exec('python command_processor.py ' .$command);
 echo $pyout;
  }
?>

<br>
<br>
<form>
 <input type="button" value="Do it again 'Ma!" onclick="history.back()">
</form>
