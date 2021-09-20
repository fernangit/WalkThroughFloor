<?php
    $text1 = $_POST["filename"];
    $text2 = (int)$_POST["score"];
    $text3 = (int)$_POST["comment"];
    $option = (int)$_POST["option"];

    if($text1 != "")
    {
        echo("success");
        echo($text1);
        echo($text2);
        $file = fopen($text1, option);
        fwrite($file, $text2, $text3);
        fclose($file);
    }else
    {
        echo("failed");
    }
?>