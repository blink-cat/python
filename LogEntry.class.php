<?php 
require_once"config.php";
require_once"DataObject.class.php";
class LogEntry extends DataObject{
		public $data=array(
			"memberId"=>"",
			"PageUrl"=>"",
			"numVisits"=>"",
			"lastVisits"=>"",

			);
		public  function getLogEntry($memberId){  //getLogEntry不能设为静态函数，否则无法调用connect(),因为connec是非静态的。
			$conn=parent::connect();
			$sql="SELECT * FROM acceslog WHERE memberId= :memberId ORDER BY lastAccess DESC";
			try{
				$st=$conn->prepare($sql);
				$st->bindValue(":memberId",$memberId,PDO::PARAM_INT);
				$st->execute();
				$logEntries=array();
				foreach($st->fetchALL() as $row){
					$logEntries= array($row);
				}
				parent::disconnect($conn);
				return $logEntries;
			}catch (PDOException $e)
			{
				parent::disconnect($conn);
				die("query failed:".$e->getMessage());
			}
		}
}

?>


