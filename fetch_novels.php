<?php
$servername = "localhost";
$username = "yourusername";
$password = "yourpassword";
$dbname = "novels_db";

// Create connection
$conn = new mysqli($servername, $username, $password, $dbname);

// Check connection
if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
}

$sql = "SELECT title, description, cover_image_url FROM novels";
$result = $conn->query($sql);

$novels = array();

if ($result->num_rows > 0) {
    while($row = $result->fetch_assoc()) {
        $novels[] = $row;
    }
}

echo json_encode($novels);

$conn->close();
?>