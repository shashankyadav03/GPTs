<?php
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    $search_term = $_POST['search'];
    $command = "python3 webscrape.py " . escapeshellarg($search_term);
    $output = exec($command);
    echo $output;
}
?>