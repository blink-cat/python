<?php 
require_once('common.inc.php');
require_once('config.php');
require_once('Member.class.php');
require_once('LogEntry.class.php');
$ID=$_GET["Id"];
$Id=isset($ID)?(int)$ID:0;
if(!$member=(new Member)->getMember($ID)){
	displayPageHeader('error');
	echo 'member not found';
	displayPageFooter();
	exit;
}
$logentries=(new LogEntry)->getLogEntry($ID);

displayPageHeader('view member'.$Id);
$memberdetail=(new Member)->getMember($ID);

?>
<dl style="width:30em;">
 <dt>Username</dt>
 <dd><?php echo $memberdetail['username'];?></dd>
 <dt>firstname</dt>
 <dd><?php  echo $memberdetail['firstname'];?></dd>
 <dt>lastname</dt>
 <dd><?php  echo $memberdetail['lastname'];?></dd>	
 <dt>joindate</dt>
 <dd><?php  echo $memberdetail['joindate'];?></dd>
 <dt>Gender</dt>
 <dd><?php  echo $memberdetail['gender'];?></dd>
</dl>
<h2>Access log</h2>
<table>
<tr>
<th>Web page</th>
<th>Number of visits</th>
<th>Last visits</th>
</tr>
<?php
	foreach($logentries as $detail){
echo'<br></br>';
echo "<td>".$detail['PageUrl'].'</td>';
echo "<td>".$detail['numVisits'].'</td>';
echo "<td>".$detail['lastAccess'].'</td>';
}
?>
</table>
<div><a href=view_members.php >back</a></div>
<?php
displayPageFooter();
?>
 