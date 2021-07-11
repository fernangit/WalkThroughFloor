<?php
    $text1 = $_POST["filename"];
    $text2 = (int)$_POST["score"];

    if($text1 != "")
    {
        echo("success");
        echo($text1);
        echo($text2);
        $file = fopen($text1, "wb");
        fwrite($file, $text2);
        fclose($file);
    }else
    {
        echo("failed");
    }
?>