<?php 
require_once"DataObject.class.php";
require_once"config.php";
class Member extends DataObject{
	public $data=array(
		'id'=>'',
		'username'=>'',
		'password'=>'',
		'firstname'=>'',
		'lastname'=>'',
		'joindate'=>'',
		'gender'=>'',
		'favoriteGenre'=>'',
		'amailAddress'=>'',
		'otherInterests'=>'',
		);
	private $_genres=array(
		"crime"=>"crime",
		"horror"=>"horror",
		"thriller"=>"Thriller",
		"romance"=>"Romance",
		"sciFi"=>"Sci-FI",
		'adventure'=>"Adventure",
		"nonFiction"=>"Non-Fiction"
		);
	public  static function getMembers($startRow,$numRows,$order){
		$conn=(new Member)->connect();
		$sql="SELECT SQL_CALC_FOUND_ROWS * FROM members ORDER BY $order LIMIT :startROW ,:numRows ; ";
		/*使用常量定义的表名查询时候出现语法错误，原因未知。*/
		try{	
			$st=$conn->prepare($sql);
			$st->bindValue(":startROW",$startRow,PDO::PARAM_INT);
			$st->bindValue(":numRows",$numRows,PDO::PARAM_INT);
			$st->execute();	
			//foreach($st->fetchALL() as $row){
			//$members=array( $row );
			//}
			$st1=$conn->query("SELECT found_rows() AS totalRows");
			$row=$st1->fetch();
			parent::disconnect($conn);
			return array($st,$row["totalRows"]);
		}
		catch(PDOException $e){
			parent::disconnect($conn);
			die("query failed:".$e->getMessage());
		}

	}

	public static function getMember($id){
		$conn=(new Member)->connect();
		$sql="SELECT * FROM members WHERE id=:id";
		try{
			$st=$conn->prepare($sql);
			$st->bindValue(":id",$id,PDO::PARAM_INT);
			$st->execute();
			foreach($st->fetchALL() as $S){        //foreach遍历得到的$S必须储存给另一个变量，本身不能返回；
				$S1=$S;		
			return $S1;}

		}catch(PDOException $e){
			parent::disconnect($conn);
			die("query fucking failed:".$e->getMessage());
		}
	}

	public static function getbyusername($username){
		$conn=(new Member)->connect();
		$sql="SELECT * FROM members WHREE username=:username";
		try{
			$st=$conn->preprae();
			$st->bindValue(':username',$username,PDO::PARAM_STR);
			$st->execute();
			$row=$st->fetch();
			if($row){
				return $row;
			}
			(new Member)->disconnect();
		}
		catch(PDOException $e){
			(new Member)->disconnect($conn);
			die('qurey failed'.$e->getMessge);
		}
	}

	public static function gtebyemail($email){
		$conn=(new Member)->connect();
		$sql="SELECT * FROM members WHREE emailaddress=:email";
		try{
			$st=$conn->preprae();
			$st->bindValue(':email',$email,PDO::PARAM_STR);
			$st->execute();
			$row=$st->fetch();
			if($row){
				return $row;
			}
			(new Member)->disconnect();
		}
		catch(PDOException $e){
			(new Member)->disconnect($conn);
			die('qurey failed'.$e->getMessge);
		}

	}

	public function insert(){
		$conn=(new Member)->connect();
		$sql="INSERT INTO members(username,password,firstname,lastname,joindate,gender,favoritegenre,emailaddress,otherInterests) Values(:username,password(:password),:firstname,:lastname,:joindate,:gender,:favoritegenre,:emailaddress,:otherInterests);";
		try{
			$st=$conn-prepare($sql);
			$st->bindValue(':username',$username,PDO::PARAM_STR);
			$st->bindValue(':password',$password,PDO::PARAM_STR);
			$st->bindValue(':firstname',$firstname,PDO::PARAM_STR);
			$st->bindValue(':lastname',$lastname,PDO::PARAM_STR);
			$st->bindValue(':joindate',$joindate,PDO::PARAM_STR);
			$st->bindValue(':gender',$gender,PDO::PARAM_STR);
			$st->bindValue('favoritegenre',$gender,PDO::PARAM_STR);
			$st->bindValue(':emailaddress',$emailaddress,PDO::PARAM_STR);
			$st->bindValue(':otherInterests',$otherInterests,PDO::PARAM_STR);
			$st->execute();
			(new Member)->disconnect();					
		}catch(PDOException $e){
			die('register failed:'.$e->getMessage());
			(new Member)->disconnect();	
		}
	}

	public function getGenres(){
		return $this->_genres;
	}
	public function getGenderString(){
		return($this->data["gender"]=="f")?"Female":"Male";
	}

	public function getFavoriteGenreString(){
		return($this->_genres[$this->data["favoriteGenre"]]);
	}
}

 ?>