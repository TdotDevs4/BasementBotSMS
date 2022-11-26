<meta name="viewport" content="width=device-width, initial-scale=1" />

<?php
  require __DIR__ . '/execute_SQL.php';
  echo '<b>Basement Bot SMS ';
  echo nl2br(file_get_contents('version_info.txt'));
  echo '<br>['.date('D M j G:i:s T Y').']</b>';
  echo '<hr style="border-top: 8px solid; border-radius: 5px;"></hr>';
  echo '<form action="index.php">
        <input type="submit" value="Start Over" style="width: 100%; padding: 15px 30px 15px 30px; font-size: 200%; border: 2px solid; border-radius: 10px;">
        </form>';

  
  $strUserType = $_GET["strUserType"];
  $strCommandLvl = $_GET["strCommandLvl"];
  $strCommandHdr = $_GET["strCommandHdr"];
  $UserId = exec('python get_user_id.py '.$strUserType);//TODO
 
  //Populate info that does not need returns from processing.
  if ($strUserType == "1001") {
    $lblUserType = 'ADMIN';
  } else {
    $lblUserType = 'USER';
  }
  
  $ActiveEventCount = isset($_GET["intActiveEvents"])?$_GET["intActiveEvents"]:'';
  $strCommand = isset($_GET["strCommand"])?$_GET["strCommand"]:"commands";

  $lblCommandHdr = "BasementBotSMS";
  if ($strCommandLvl == "c0") {
    $lblCommandLvl = "COMMAND";
  } else {
    $lblCommandLvl = "SUB-COMMAND";
    $lblCommandHdr = $strCommandHdr;
  }
  
  echo '<b>You are now in ['.$lblCommandLvl.'] mode for ['.$lblCommandHdr.']. <br><br>Respond with your next command:<br></b>';
  echo '<hr style="border-top: 2px dashed; border-radius: 2px;"></hr>';
  //Additional info above command processor output
  if ($strCommandHdr == 'event') {
    if ($ActiveEventCount == '') {
      //Get active event info...
    $strSqlType = 'select';
    $strSqlInput = "";
    exec('python3 MYSQL_Functions_EventsNew.py '.$strSqlType.' '.$UserId, $output1);
    foreach ($output1 as $line) {
      $strSqlInput = $strSqlInput.$line;
    }
    $ActiveEventCount = phpExecuteSql($strSqlInput, 0, 'event_count');
    }

    echo 'Active Event Count ['.$ActiveEventCount.']<br><br>';
  }

  //Execute the command processor
  exec('python3 command_processor.py "'.$strUserType.'" '.$UserId.' "'.$strCommandLvl.'" "'.$strCommandHdr.'" "'.$strCommand.'"', $output);
  foreach ($output as $line) {
    echo $line ."<br>";
  }

  //Sub-Command info line
  //echo nl2br(file_get_contents('sub_command_info.txt')).'<br>';

  echo '<hr style="border-top: 2px dashed; border-radius: 2px;"></hr>';
  //Command input field and button
  echo '<form action="command_output.php" method="get">
  <input type="hidden" name="strUserType" value="'.$strUserType.'">
  <input type="hidden" name="intUserId" value="'.$UserId.'">
  <input type="hidden" name="strCommandHdr" value="'.$strCommandHdr.'">
  <input type="hidden" name="strCommandLvl" value="'.$strCommandLvl.'">
  <input type="hidden" name="intActiveEvents" value="'.$ActiveEventCount.'">

  <label style="font-size: 200%"><b>COMMAND:</b><br></label>
    <input type="text" name="strCommand" autocomplete="off" placeholder = "sauce" required maxlength="69" style="width: 100%; padding: 15px 30px 15px 30px; font-size: 200%; border: 2px solid; border-radius: 10px;"><br><br>
    <input type="submit" value="Send Command" style="width: 100%; padding: 15px 30px 15px 30px; font-size: 200%; border: 2px solid; border-radius: 10px;">
  </form>';

  //dev stuff...
  echo '<ul style="list-style-type:square; padding: 10px; margin: 5px;"><li>USER ID : ['.$UserId.']</li><li>USER TYPE : ['.$lblUserType.']</li><li>LAST COMMAND : ['.$strCommand.']</li></ul>';

?>



