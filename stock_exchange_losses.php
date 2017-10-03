<?php
// Stock Exchange Losses
// https://www.codingame.com/ide/puzzle/stock-exchange-losses


fscanf(STDIN, "%d",
    $n
);
$inputs = fgets(STDIN);
$inputs = explode(" ",$inputs);

$baseItem = $inputs[0];
$difference = 0;
foreach ($inputs as $input) {
    if ((int)$input > (int)$baseItem) {
        $baseItem = $input;
    } elseif ($input - $baseItem < $difference) {
        $difference = $input - $baseItem;
    }
}

echo($difference);
?>