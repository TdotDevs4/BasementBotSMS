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

 //TESTING CONFIG SPOT
 $CommandInputFile = '/command_input';
 //$CommandInputFile = '/test_command_input';

 //Remove any special characters, numbers and spaces
 $UserType = $_GET["strUserType"];
 $UserId = $_GET["intUserId"];
 $CommandHdr = $_GET["strCommandHdr"];
 $strCommand = $_GET["strCommand"];

 //Remove spaces from the command, unless it is an input command that is not [rcommand_add_1*]
 if (strpos($CommandHdr, '*') > -1 && $CommandHdr !== 'rcommand_add_1*') {
  $PyCleanCommand = exec('python3 clean_command_capture.py "'.$strCommand.'"');
 } else {
  $PyCleanCommand = exec('python3 clean_command.py "'.$strCommand.'"');
 }
 
 //Sub-Command logic...go back to input with new level and header...
 //Get command level
 $PyCommandLvl = exec('python3 sub_command_check.py "'.$CommandHdr.'" '.$UserType.' "'.$PyCleanCommand.'"');

 if (isset($_GET["intActiveEvents"])) {
  $ActiveEventCount = $_GET["intActiveEvents"];
  if ($ActiveEventCount > 0 && $CommandHdr == 'event' && $PyCleanCommand == 'create') {
    $PyCommandLvl = 'c0';

  } elseif ($ActiveEventCount == 0 && $CommandHdr == 'event' &&  $PyCleanCommand == 'info') {
    $PyCommandLvl = 'c0';
  }
 }

 if ($PyCommandLvl == "c1")
 {
  $UpdatedCommandHdr = $PyCleanCommand;
  $CommandInputURL = $CommandInputFile.".php?strUserType=".$UserType."&intUserId=".$UserId."&strCommandHdr=".$UpdatedCommandHdr."&strCommandLvl=".$PyCommandLvl."&strCommand=".$PyCleanCommand;
  if ($UpdatedCommandHdr == "event") {
    // //Get active event info...
    // $strSqlType = 'select';
    // $strSqlInput = "";
    // exec('python3 MYSQL_Functions_EventsNew.py '.$strSqlType.' '.$UserId, $output);
    // foreach ($output as $line) {
    //   $strSqlInput = $strSqlInput.$line;
    // }
    // $ActiveEventCount = phpExecuteSql($strSqlInput, 1, 'event_count');
    // if ($ActiveEventCount == '') {$ActiveEventCount = 0;}
    $CommandInputURL = $CommandInputURL.'&intActiveEvents='.$ActiveEventCount;
  }
  header("Location: $CommandInputURL");
  exit;
 }
 elseif ($PyCommandLvl == "c2")
 {
  $UpdatedCommandHdr = $CommandHdr.'_'.$PyCleanCommand.'_1*';
  $CommandInputURL = $CommandInputFile.".php?strUserType=".$UserType."&intUserId=".$UserId."&strCommandHdr=".$UpdatedCommandHdr."&strCommandLvl=".$PyCommandLvl."&strCommand=".$PyCleanCommand;
  header("Location: $CommandInputURL");
  exit;
 }
 elseif ($PyCommandLvl == "c3")
 {
  $IndexOfStar = strpos($CommandHdr, '*');
  $LengthOfHdr = strlen($CommandHdr);
  $C3InputNum = substr($CommandHdr, $IndexOfStar-1,1) +1;

  if (($IndexOfStar) == $LengthOfHdr-1) {
    $PreviousInput = '*_';
  } else {
    $PreviousInput = substr($CommandHdr, $IndexOfStar, $LengthOfHdr-$IndexOfStar).'_';
  }

  $UpdatedCommandHdr = substr($CommandHdr, 0, $IndexOfStar-1).$C3InputNum.$PreviousInput.$PyCleanCommand;
  
  $CommandInputURL = $CommandInputFile.".php?strUserType=".$UserType."&intUserId=".$UserId."&strCommandHdr=".$UpdatedCommandHdr."&strCommandLvl=".$PyCommandLvl."&strCommand=".$PyCleanCommand;
  header("Location: $CommandInputURL");
  exit;
  //}
 }

 echo '<h2>OUTPUT</h2>';
 echo '<hr style="border-top: 2px dashed; border-radius: 2px;"></hr>';

 /////////////PHP SQL STUFF START/////////////////
 $strLastCommandLvl = $_GET['strCommandLvl'];

 //We petered out and now are at c0 output after going through a c1+ command sequence
 if ($PyCommandLvl == 'c0' and ($strLastCommandLvl != $PyCommandLvl)) {
  //if ($CommandHdr)

  //hard config for c1 sequences...
  if ($strLastCommandLvl == "c1")
  {
    if ($CommandHdr == "rcommand" && $PyCleanCommand == "requests") {

      $strSqlType = 'select';
    
      $strSqlInput = "";
      exec('python3 MYSQL_Functions_commandRequestLog.py '.$strSqlType.' '.$UserId, $output);
      foreach ($output as $line) {
        $strSqlInput = $strSqlInput.$line;
      }

      echo phpExecuteSql($strSqlInput, 1, $CommandHdr.'_'.$PyCleanCommand);
    } elseif ($CommandHdr == "event" && $PyCleanCommand == "info") {

      $strSqlType = 'select';
    
      $strSqlInput = "";
      exec('python3 MYSQL_Functions_EventsNew.py '.$strSqlType.' '.$UserId, $output);
      foreach ($output as $line) {
        $strSqlInput = $strSqlInput.$line;
      }
      echo phpExecuteSql($strSqlInput, 1, $CommandHdr.'_'.$PyCleanCommand);

    }
 }

  //hard config for c2 sequences...
  elseif ($strLastCommandLvl == "c2") {

    if ($CommandHdr == 'event_cancel_1*') {
        if ($PyCleanCommand == 'yeet') {
          $strSqlType = 'cancel';
          $strSqlInput = "";
          exec('python3 MYSQL_Functions_EventsNew.py "'.$strSqlType.'" '.$UserId, $select_output);

          foreach ($select_output as $line) {
           $strSqlInput = $strSqlInput3.$line;
          }
          //Execute update to event
          phpExecuteSQL($strSqlInput, 0, 'event_info');

          } else {

          //go back to event c1...
          $CommandInputURL = $CommandInputFile.".php?strUserType=".$UserType."&intUserId=".$UserId."&strCommandHdr=event&strCommandLvl=c1&strCommand=event";
          header("Location: $CommandInputURL");
          exit;
        }
    }
  }

// hard config for c3 sequences...
 elseif ($strLastCommandLvl == "c3")
 {
  $Header = substr($CommandHdr, 0, strpos($CommandHdr, '*'));
  if ($Header == 'rcommand_add_2') {
    $strSqlType = 'insert';
    $strCommandRequest = substr($CommandHdr, strpos($CommandHdr, '*')+2);//add 2 to move past the *_
    $strDescription = '"'.$PyCleanCommand.'"';
    
    $strSqlInput = "";
    exec('python3 MYSQL_Functions_commandRequestLog.py '.$strSqlType.' '.$UserId.' '.$strCommandRequest.' '.$strDescription.' ', $insert_output);
    
    foreach ($insert_output as $line) {
      $strSqlInput = $strSqlInput.$line;
    }

    phpExecuteSql($strSqlInput, 0, '');
  } elseif ($Header == 'event_create_4') {

    if ($PyCleanCommand == 'yeet') {
      $strSqlType = 'insert';

      $IndexOfStar = strpos($CommandHdr, '*');
      $LengthOfHdr = strlen($CommandHdr);
      $InputsHdr = substr($CommandHdr, $IndexOfStar+2, $LengthOfHdr-$IndexOfStar);
      $arrInputs = explode('_', $InputsHdr);

      $strEventTitle = $arrInputs[0];
      $strEventLocation = $arrInputs[1];
      $strEventDateAndTime = $arrInputs[2];

      $strSqlInput = "";
      exec('python3 MYSQL_Functions_EventsNew.py "'.$strSqlType.'" '.$UserId.' "'.$strEventTitle.'" "'.$strEventLocation.'" "'.$strEventDateAndTime.'"', $insert_output);
      
      foreach ($insert_output as $line) {
        $strSqlInput = $strSqlInput.$line;
      }
      //insert new event
      $NewEventId = phpExecuteSql($strSqlInput, 0, 'event_create');
      
      //insert sublink
      if ($NewEventId > 0) {
        $strSqlType = 'sublink';
        $strSqlInput2 = "";
        exec('python3 MYSQL_Functions_EventsNew.py "'.$strSqlType.'" '.$NewEventId, $insert_output2);
        foreach ($insert_output2 as $line2) {
          $strSqlInput2 = $strSqlInput2.$line2;
        }
        phpExecuteSQL($strSqlInput2, 0, 'sublink');
      } else {
        //try to get active event id for user
        $strSqlType = 'select';
        $strSqlInputEvent = "";
        exec('python3 MYSQL_Functions_EventsNew.py "'.$strSqlType.'" '.$UserId, $insert_outputEvent);
        foreach ($insert_outputEvent as $lineEvent) {
          $strSqlInputEvent = $strSqlInputEvent.$lineEvent;
        }
        $NewEventId = phpExecuteSQL($strSqlInputEvent, 0, 'active_event_id');
        echo "NEW EVENT ID:".$NewEventId;
      }

      $strSqlType = 'get';
      $strSqlInput3 = "";
      exec('python3 MYSQL_Functions_EventsNew.py "'.$strSqlType.'" '.$NewEventId, $select_output);

      foreach ($select_output as $line3) {
        $strSqlInput3 = $strSqlInput3.$line3;
      }
 
      //get and print event info
      phpExecuteSQL($strSqlInput3, 1, 'event_info');

    } else {
      //they did not yeet, go back to start of event_create
      $CommandInputURL = $CommandInputFile.".php?strUserType=".$UserType."&intUserId=".$UserId."&strCommandHdr=event_create_1*&strCommandLvl=c2&strCommand=create";
      header("Location: $CommandInputURL");
      exit;
    }
    
  }
 }
}
///////////PHP SQL STUFF END/////////////////

 exec('python3 command_processor.py '.$UserType.' '.$UserId.' '.$PyCommandLvl.' "'.$CommandHdr.'" "'.$PyCleanCommand.'"', $command_output);
 foreach ($command_output as $line) {
  echo $line ."<br>";
 }
 echo '<hr style="border-top: 2px dashed; border-radius: 2px;"></hr>';
 if (strpos($CommandHdr, '*') == FALSE){
  
  echo '<br><input type="button" value="Do it again \'Ma!" onclick="history.back()"
        style="width: 100%; padding: 15px 30px 15px 30px; font-size: 200%; border: 2px solid; border-radius: 10px;">';
 }

 //dev stuff
 
 echo '<ul style="list-style-type:square; padding: 10px; margin: 5px;"><li>USER ID : ['.$UserId.']</li><li>USER TYPE : ['.$UserType.']</li><li>LAST COMMAND : ['.$PyCleanCommand.']</li></ul>';

 //testing stuff if all goes wrong...again...
 //echo '[HARDCODED TEST VALUE]<br>'.$PyCommandLvl;
 //echo exec('python test.py', $output);
?>