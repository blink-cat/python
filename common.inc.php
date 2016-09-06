<?php 
require_once('config.php');
require_once("Member.class.php");
require_once("LogEntry.class.php");

function Validatefield($fieldName,$missingField){
	if (in_array($fieldName,$missingField)) {
		echo"class='error'";
	}
}

function setChecked(DataObject $obj,$fieldName,$fieldValue){

 if($obj->getValue($fieldName)==$fieldValue){
 	echo "checked='checked'";
 }
}
 
function setselected(DataObject $obj,$fieldName,$fieldValue){
 	if($obj->getValue($fieldValue)==$fieldValue){
 		echo "selected='selected'";
 	}
 }

function displayPageHeader($pageTitle) {
?>
<!DOCTYPE html PUBLIC "-//W3C//DTD/XHTML 1.0 Strict//EN"
	"http://www.w3c.org/TR/xhtml1/DTD/xhtml-strict.dtd">
<html xmlns="http://ww.w3c.org/1999/xhtml" xml:lang="en" lang="en">
<head>
	<meta charset="UTF-8">
	<title><?php echo $pageTitle; ?></title>
	<style type="text/css">
	th{
		text-align: left;
		background-color: #bbb;
		}
	th,td{padding:0.4em; }
	tr.alt td{background:#ddd;}
	dl {
    margin-bottom:50px;
}
 
dl dt {
    background:#5f9be3;
    color:#fff;
    float:left; 
    font-weight:bold; 
    margin-right:20px; 
    padding:5px;  
    width:100px; 
}
 
dl dd {
    margin:5px 0; 
    padding:5px 0;
}
.error{
	background:#d33;color:white;padding:0.2em;
	}
		</style>

</head>
<body>
	<h1><?php echo $pageTitle ?></h1>
	<?php }
	function displayPageFooter(){ ?>
</body>
</html>
<?php  
} 
?>