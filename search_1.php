<html>
<body>
	<form action = 'search.php' method = 'get'>
	Значение:
	ФИО врача: <input name = 'doctor' type = 'text' value='<?=@$_GET['doctor']?>'><br/>
	Номер кабинета: <input name = 'room' type = 'text' value='<?=@$_GET['room']?>'><br/>
	<br/>
	<input type = 'submit' name = 'button'>
	</form>
</body>
</html>

<?php
include 'connection.php';
if(isset($_GET['button']))
{
	$doctor = strtr(trim($_GET['doctor']), '*', '%');
	$room = strtr(trim($_GET['room']), '*', '%');

	$query = "SELECT doctor.doctor_FIO, room.room_number
    FROM room 
    INNER JOIN
    doctor ON doctor.doctor_id = room.doctor_id
    WHERE doctor.doctor_FIO LIKE '%$doctor%'";
	
	if (!empty($room)) {
			$query .= " AND room.room_number LIKE '%$room%'";
	}
	
	$result = mysqli_query($link, $query);
	echo "<table border = 1 align=center><tr><td>Имя</td><td>Номер кабинета</td></tr>";
	
	while($row = mysqli_fetch_array($result)) {
			echo "<tr><td>" . $row['doctor_FIO'] . "</td><td>" . $row['room_number'] . "</td></tr>";
	}
	echo "</table>";
	mysqli_close($link);
}