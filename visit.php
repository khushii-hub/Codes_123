<?php

session_start();

if (isset($_SESSION['visit_count'])) {
    $_SESSION['visit_count']++;
} else {
    $_SESSION['visit_count'] = 1;
}

$visitCount = $_SESSION['visit_count'];

echo "You have visited this page $visitCount times.";

?>