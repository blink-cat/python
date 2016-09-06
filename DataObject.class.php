<?php 
 require_once"config.php";
 abstract class DataObject{
 	public $data=array();
 	public function _construct(){
 		foreach($data as $key=>$value){
 			if(array_key_exists($key,$this->data))
 				$this->data[$key]=$value;
 		}
	}
	public function getValue($field){
		if(array_key_exists($field, $this->data)){
			return $this->data[$field];
		}
		else{
			die ('field not found');
		}
	}

	

	protected function connect(){
		try{
			$conn=new PDO(DB_DSN,DB_USERNAME,DB_PASSWORD);
			$conn->setAttribute(PDO::ATTR_PERSISTENT,TRUE);						//keep the connecte;
			$conn->setAttribute(PDO::ATTR_ERRMODE,PDO::ERRMODE_EXCEPTION);
			
		} catch(PDOEXCEPTION $e){
			die("connection failed:".$e->getMessage());
		}
		return $conn;
	}

	protected static function disconnect($conn){
		return $conn="";

	}
 }

 ?>