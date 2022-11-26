<meta name="viewport" content="width=device-width, initial-scale=1" />
<?php
  require __DIR__ . '/execute_SQL.php';
  echo '<a href="https://www.basementbotsms.com/" target="_blank" rel="noopener noreferrer"><b>www.basementbotsms.com</b></a><br>';
  echo '<b>Basement Bot SMS ';
  echo nl2br(file_get_contents('version_info.txt'));
  echo '<br>['.date('D M j G:i:s T Y').']</b>';
  echo '<hr style="border-top: 8px solid; border-radius: 5px;"></hr>';

  $strPhoneNumber = $_GET["strPhoneNumber"];
  $lblPhoneNumber = '('.substr($strPhoneNumber, 0, 3).')-'.substr($strPhoneNumber, 3, 3).'-'.substr($strPhoneNumber, -4);
  $intEventId = $_GET["intEventId"];

  $strSqlType = 'check';
  $strSqlInput1 = '';
  exec('python3 MYSQL_Functions_Users.py '.$strSqlType.' '.$strPhoneNumber, $output1);
  foreach ($output1 as $line1) {
    $strSqlInput1 = $strSqlInput1.$line1;
  }

  //----
  // >1000 == User Exists
  // 0 == User does not exist
  // -1 == User exists more than once, or there is some other issue...
  $UserCheckValue = phpExecuteSql($strSqlInput1, 0, 'sub_output_check');
  //----
  
  if ($UserCheckValue == 0) {
    echo '<h1>SUCCESS: Welcome to Basement Bot SMS!</h1>';
    $strSqlType = 'insert';
    $strSqlInput2 = '';
    exec('python3 MYSQL_Functions_Users.py '.$strSqlType.' '.$strPhoneNumber, $output2);
    foreach ($output2 as $line2) {
      $strSqlInput2 = $strSqlInput2.$line2;
    }
    $UserCheckValue = phpExecuteSql($strSqlInput2, 0, 'sub_output_insert');

  } elseif ($UserCheckValue > 0) {
    echo '<h1>SUCCESS: Welcome back!</h1>';
    $strSqlType = 'active';
    $strSqlInput3 = '';
    exec('python3 MYSQL_Functions_Users.py "'.$strSqlType.'" '.$UserCheckValue.' 1', $output3);
    foreach ($output3 as $line3) {
      $strSqlInput3 = $strSqlInput3.$line3;
    }
    phpExecuteSql($strSqlInput3, 0, 'sub_output_activate');

  } else {
    echo 'Yah...something is wrong...sorry! ERROR:['.$UserCheckValue.']';
    exit;
  }
  
  // insert EventToSub...
  $strSqlType = 'insert';
  $strSqlInputSub = '';
  exec('python3 MYSQL_Functions_eventToSub.py "'.$strSqlType.'" '.$intEventId.' '.$UserCheckValue, $outputSub);
  foreach ($outputSub as $lineSub) {
    $strSqlInputSub = $strSqlInputSub.$lineSub;
  }
  phpExecuteSql($strSqlInputSub, 0, '');
  // end insert...

  // get Event Sub count by User
  $EventSubCount = 1;
  $strSqlType = 'get_subs_by_user';
  $strSqlInputCount = '';
  exec('python3 MYSQL_Functions_eventToSub.py "'.$strSqlType.'" '.$UserCheckValue, $outputCount);
  foreach ($outputCount as $lineCount) {
    $strSqlInputCount = $strSqlInputCount.$lineCount;
  }
  $EventSubCount = phpExecuteSql($strSqlInputCount, 0, 'count');
  echo 'You have subbed to a total of <b>['.$EventSubCount.'] Events</b>!';
  // end get...

  echo '<ul style="list-style-type:square; padding: 15px; margin: 5px;">';
  echo '<li><B>'.$lblPhoneNumber.' is now subscribed to Event #'.$intEventId.'</B></li>';

  $strSqlType = 'get';
  $strSqlInput = '';
  exec('python3 MYSQL_Functions_EventsNew.py '.$strSqlType.' '.$intEventId, $output);
  foreach ($output as $line) {
    $strSqlInput = $strSqlInput.$line;
  }
  echo phpExecuteSql($strSqlInput, 1, 'sub_output');

  echo '</ul>';
 ?>