<meta name="viewport" content="width=device-width, initial-scale=1" />
<?php
  require __DIR__ . '/execute_SQL.php';
  echo '<b><a href="https://www.basementbotsms.com/" target="_blank" rel="noopener noreferrer">www.basementbotsms.com</a><br>';
  echo 'Basement Bot SMS ';
  echo nl2br(file_get_contents('version_info.txt'));
  echo '<br>['.date('D M j G:i:s T Y').']';
  echo '</b><hr style="border-top: 8px solid; border-radius: 5px;"></hr>';

  echo '<h1>Subscribe to this event to get real-time text notifications!</h1>';
  $intEventId = $_GET["intEventId"];
  $strSqlType = 'get';
  $strSqlInput = '';

  exec('python3 MYSQL_Functions_EventsNew.py '.$strSqlType.' '.$intEventId, $output);
  foreach ($output as $line) {
    $strSqlInput = $strSqlInput.$line;
  }

  echo phpExecuteSql($strSqlInput, 1, 'sub_input');

  echo '<br><br>

  <form action="event_sub_output.php">
    <label for="strPhoneNumber" style="font-size: 200%"><b>Enter a phone number:</b></label><br>

    <select name="strPhoneNumber" style="width: 100%; padding: 15px 30px 15px 5px; font-size: 200%; border: 1px solid; border-radius: 0px;" required>
      <option value="8008675309" selected hidden>Choose one...</option>
      <option value="8008675309">User #1: 8008675309</option>
      <option value="8004080221">User #2: 8004080221</option>
    </select>
    <br><br>

    <input type="submit" value = "Subscribe" style="width: 100%; padding: 15px 30px 15px 30px; font-size: 200%; border: 2px solid; border-radius: 10px;">
    <input type="hidden" name="intEventId" value="'.$intEventId.'">
  </form>';
 ?> 


<!-- 
  
<br><br>
<input type="tel" id="strPhoneNumber" autocomplete="off" style="width: 100%; padding: 15px 30px 15px 30px; font-size: 200%; border: 2px solid; border-radius: 10px;" name="strPhoneNumber" placeholder="8008675309" pattern="[0-9]{3}[0-9]{3}[0-9]{4}" maxlength="10" required><br><br> 
  
-->
