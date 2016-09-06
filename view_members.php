<?php 
 
 require_once("config.php");
 require_once("common.inc.php");
 require_once("Member.class.php");
 $start=isset($_GET["start"])?(int)$_GET["start"]: 0;
 $order=isset($_GET["order"])?preg_replace("/[^a-zA-Z]/", "",$_GET["order"]) : "username";
 list($members,$totalRows)=Member::getMembers($start,PAGE_SIZE,$order);
 displayPageHeader("View book members");
 ?>
 <h2>displaying members <?php echo $start+1?>-<?php echo min($start+PAGE_SIZE,$totalRows)?> of <?php echo $totalRows ?></h2>
 <table cellspacing="0" style="width:30em;border:1px solid #666;">
 	<tr>
	 	<th><?php if($order!="username"){?><a href="view_members.php?order=username"><?php } ?>username<?php if($order!="username"){?></a><?php } ?></th>
	 	<th>
	 		<?php if($order!="firstName"){?><a href="view_members.php?order=firstname"><?php } ?> First Name <?php if($order!="firstName") {?><a/><?php } ?>
	 	</th>

	 	<th>
	 		<?php if($order!="lastName"){?><a href="view_members.php?order=lastname"><?php } ?> last Name <?php if($order!="lastName") {?><a/><?php } ?>
	 	</th>

 	</tr>
 	<?php
 	$rowcount=0;

 	foreach($members->fetchALL() as $member)
 	{	$rowcount++;
 		$st='alt';
 		if($rowcount%2==0)
 		echo'<tr class='.$st.'>';
 		echo '<td><a href=view_member.php?Id='.$member['id'].'>'.$member['username'].'</a></td>';
 		echo '<td>'.$member['firstname'].'</td>';
 		echo '<td>'.$member['lastname'].'</td>';
 		echo '</tr>';
 	};
 	
 	 ?>
	 </table>
	 
	 <div style="width: 30em;margin-top: 20px;text-align: center;">
	 	<?php if($start>0) {?>
	 	<a href="view_members.php?start=<?php echo max($start-PAGE_SIZE,0)?>&amp;order=<?php echo $order; ?>">previous page </a><?php  }?>
	 	&nbsp;
	 	<?php if($start+PAGE_SIZE<$totalRows){?><a href="view_members.php?start=<?php echo min($start+PAGE_SIZE,$totalRows)?>&amp;order=<?php echo $order;?>" >next page</a><?php } ?>
	 </div>
 <?php displayPageFooter() ;?>