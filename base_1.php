<?php
require_once 'connection.php';
 
$link = mysqli_connect($host, $user, $password, $database) 
    or die ("Ошибка подключения к базе данных" . mysqli_error());

echo "Подключились!<br>";

$sql = "CREATE TABLE doctor (
  doctor_id int(10) NOT NULL,
  doctor_FIO text NOT NULL,
  speciality text NOT NULL,
  sex text NOT NULL,
  birthdate datetime NOT NULL,
  contract_data text NOT NULL, 
  startworkingtime datetime NOT NULL,
  PRIMARY KEY (doctor_id))";
  
if (mysqli_query($link, $sql)) {
  echo "ОК. Принято.";
} else {
  echo "Нужно что-то исправить " . mysqli_error($link);
}

$sql = "INSERT INTO doctor VALUES
  ('1', 'Andreeva A A', 'lor', 'f', '1978-10-30 00:00:00', '7428956242985656', '2001-06-01 00:00:00'),
  ('2', 'Sidorov M M', 'terapevt', 'm', '1977-07-07 00:00:00', '6930265974346', '2006-10-01 00:00:00'),
  ('3', 'Matveev L L', 'terapevt', 'm', '1990-11-13 00:00:00', '5043842645538', '2010-03-31 00:00:00'),
  ('4', 'Sergeeva R R', 'okulist', 'f', '1989-12-04 00:00:00', '7493201235492', '2003-09-01 00:00:00')";
  
if (mysqli_query($link, $sql)) {
  echo "Добавили данные<br>";
} else {
  echo "Не работает <br>" . mysqli_error($link);
}


$sql = "CREATE TABLE client (
  client_id int(10) NOT NULL,
  client_FIO text NOT NULL,
  phonenumber int(10) NOT NULL,
  birthdate text NOT NULL,
  diagnosis text NOT NULL,
  PRIMARY KEY (client_id))";
  
if (mysqli_query($link, $sql)) {
  echo "ОК. Принято.";
} else {
  echo "Нужно что-то исправить" . mysqli_error($link);
}

$sql = "INSERT INTO client VALUES
  ('1', 'Fyodorov K K', '4682829', '1978-11-04', '-'),
  ('2', 'Semyonov W W', '7959245', '1980-03-11', '-'),
  ('3', 'Ivanov I I', '8603582', '1990-08-19', '-')";
  
if (mysqli_query($link, $sql)) {
  echo "Добавили данные<br>";
} else {
  echo "Не работает <br>" . mysqli_error($link);
}


$sql = "CREATE TABLE visit (
  visit_id int(10) NOT NULL,
  client_id int(10) NOT NULL,
  doctor_id int(10) NOT NULL,
  card_id int(10) NOT NULL,
  visit_datetime datetime NOT NULL,
  PRIMARY KEY (visit_id),
  KEY client (client_id),
  KEY doctor (doctor_id),
  CONSTRAINT fk_visitdoc FOREIGN KEY (client_id) REFERENCES client (client_id),
  CONSTRAINT fk_visitcl FOREIGN KEY (doctor_id) REFERENCES doctor (doctor_id))";
  
if (mysqli_query($link, $sql)) {
  echo "ОК. Принято.";
} else {
  echo "Нужно что-то исправить " . mysqli_error($link);
}

$sql = "INSERT INTO visit VALUES
  ('964', '2', '3', '162', '2018-03-02 13:00:00'),
  ('252', '1', '4', '361', '2017-11-11 17:30:00'),
  ('168', '3', '2', '594', '2018-02-17 16:15:00')";
  
if (mysqli_query($link, $sql)) {
  echo "Добавили данные<br>";
} else {
  echo "Не работает <br>" . mysqli_error($link);
}


$sql = "CREATE TABLE medcard (
  client_id int(10) NOT NULL,
  card_id int(10) NOT NULL,
  visit_datetime datetime NOT NULL,
  diagnosis text NOT NULL,
  recommends text NOT NULL,
  PRIMARY KEY (card_id),
  KEY client (client_id),
  CONSTRAINT fk_clientcard FOREIGN KEY (client_id) REFERENCES client (client_id))";
  
if (mysqli_query($link, $sql)) {
  echo "ОК. Принято.";
} else {
  echo "Нужно что-то исправить " . mysqli_error($link);
}

$sql = "INSERT INTO medcard VALUES
  ('2', '162', '2018-03-02 13:00:00', 'orz', '-'),
  ('1', '361', '2017-11-11 17:30:00', '-', '-'),
  ('3', '594', '2018-02-17 16:15:00', 'orz', '-')";
  
if (mysqli_query($link, $sql)) {
  echo "Добавили данные<br>";
} else {
  echo "Не работает <br>" . mysqli_error($link);
}


$sql = "CREATE TABLE room (
  doctor_id int(10) NOT NULL,
  room_number int(10) NOT NULL,
  schedule text NOT NULL,
  responsible text NOT NULL,
  inner_phonenumber int(10) NOT NULL,
  KEY doctor (doctor_id),
  CONSTRAINT fk_roomdoc FOREIGN KEY (doctor_id) REFERENCES doctor (doctor_id))";
  
if (mysqli_query($link, $sql)) {
  echo "ОК. Принято.";
} else {
  echo "Нужно что-то исправить " . mysqli_error($link);
}

$sql = "INSERT INTO room VALUES
  ('1', '21', 'Mon-Fri', 'Andreeva A A', '5833964'),
  ('2', '22', 'Mon-Wed', 'Andreeva A A', '3903596'),
  ('3', '25', 'Tue-Fri', 'Matveev L L', '4833578'),
  ('4', '29', 'Tue-Fri', 'Matveev L L', '5703278')";
  
if (mysqli_query($link, $sql)) {
  echo "Добавили данные<br>";
} else {
  echo "Не работает <br>" . mysqli_error($link);
}


$sql = "CREATE TABLE visit_payment (
  client_id int(10) NOT NULL,
  doctor_id int(10) NOT NULL,
  amount_pay int(10) NOT NULL,
  pay_status tinyint(1) NOT NULL,
  visit_datetime datetime NOT NULL,
  KEY client (client_id),
  KEY doctor (doctor_id),
  CONSTRAINT fk_visitpaycl FOREIGN KEY (client_id) REFERENCES client (client_id),
  CONSTRAINT fk_visitpaydoc FOREIGN KEY (doctor_id) REFERENCES doctor (doctor_id))";
  
if (mysqli_query($link, $sql)) {
  echo "ОК. Принято.";
} else {
  echo "Нужно что-то исправить " . mysqli_error($link);
}

$sql = "INSERT INTO visit_payment VALUES
  ('1', '4', '1500', '1', '2017-11-11 17:30:00'),
  ('2', '3', '1900', '0', '2018-03-02 13:00:00'),
  ('3', '2', '1700', '0', '2018-02-17 16:15:00')";
  
if (mysqli_query($link, $sql)) {
  echo "Добавили данные<br>";
} else {
  echo "Не работает <br>" . mysqli_error($link);
}

$sql = "CREATE TABLE work_schedule (
  doctor_id int(10) NOT NULL,
  workingdays text NOT NULL,
  daysoff text NOT NULL,
  KEY doctor (doctor_id),
  CONSTRAINT fk_scheduledoc FOREIGN KEY (doctor_id) REFERENCES doctor (doctor_id))";
  
if (mysqli_query($link, $sql)) {
  echo "ОК. Принято.";
} else {
  echo "Нужно что-то исправить " . mysqli_error($link);
}

$sql = "INSERT INTO work_schedule VALUES
  ('1', 'Mon, Tue, Fri', 'Wed, Thu, Sat, San'),
  ('2', 'Mon, Tue, Wed, Thu', 'Fri, Sat, San'),
  ('3', 'Tue, Wed, Thu, Fri', 'Mon, Sat, San'),
  ('4', 'Thu, Fri, Sat', 'Mon, Tue, Wed, San')";
  
if (mysqli_query($link, $sql)) {
  echo "Добавили данные<br>";
} else {
  echo "Не работает <br>" . mysqli_error($link);
}



$sql = "CREATE TABLE pricelist (
  doctor_id int(10) NOT NULL,
  price_per_visit int(10) NOT NULL,
  KEY doctor (doctor_id),
  CONSTRAINT fk_pricedoctor FOREIGN KEY (doctor_id) REFERENCES doctor (doctor_id))";
  
if (mysqli_query($link, $sql)) {
  echo "ОК. Принято.";
} else {
  echo "Нужно что-то исправить " . mysqli_error($link);
}

$sql = "INSERT INTO pricelist VALUES
  ('1', '1500'),
  ('2', '1700'),
  ('3', '2000'),
  ('4', '1800')";
  
if (mysqli_query($link, $sql)) {
  echo "Добавили данные<br>";
} else {
  echo "Не работает <br>" . mysqli_error($link);
}

mysqli_close($link);
?>