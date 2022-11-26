<meta name="viewport" content="width=device-width, initial-scale=1" />
<?php
  echo '<b><a href="https://www.basementbotsms.com/" target="_blank" rel="noopener noreferrer">www.basementbotsms.com</a> <br>';
  echo 'Basement Bot SMS ';
  echo nl2br(file_get_contents('version_info.txt'));
  echo '<br>['.date('D M j G:i:s T Y').']';
  echo '<hr style="border-top: 8px solid; border-radius: 5px;">';
  echo '</b>';
  
  echo '<form name="cmbUserType" action="command_input.php" method="get">
        <label for="cmbUserType" style="font-size: 150%;"><b>Choose a User Type to begin<br></b></label>

        <select name="strUserType" style="width: 100%; padding: 15px 30px 15px 5px; font-size: 200%; border: 1px solid; border-radius: 0px;">
        <option value="1000" selected hidden>Choose one...</option>
        <option value="1001">Admin</option>
        <option value="1002">Non-Admin</option>
        </select>

        <br><br>

        <input type="hidden" name="strCommandLvl" value="c0">
        <input type="submit" value="Enter Basement Bot SMS" style="width: 100%; font-size: 150%; padding: 15px 30px 15px 30px; border: 2px solid; border-radius: 10px;">
        </form>';
?>
