<?php header('Access-Control-Allow-Origin: *');
    extract($_GET);
    $image_name = $image_name.".jpg";
    header("Content-Type:image/jpg");
    header("Content-Length:".filesize($image_name));
    //echo $image_name;
    //readfile($image_name);
    $file = fopen($image_name, "r");
    echo fread($file, filesize($image_name));
?>
