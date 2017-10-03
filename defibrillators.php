<?php
// Defibrillators
// https://www.codingame.com/ide/puzzle/defibrillators

fscanf(STDIN, "%s",
    $LON
);
fscanf(STDIN, "%s",
    $LAT
);
fscanf(STDIN, "%d",
    $N
);

$LON = (float)str_replace(',','.',$LON);
$LAT = (float)str_replace(',','.',$LAT);

$items = array();
#echo($LON." | ".$LAT." | ".$N."\n");

$result = null;
$final = null;

$epsilon = 0.00001;

for ($i = 0; $i < $N; $i++)
{
    $DEFIB = stream_get_line(STDIN, 256 + 1, "\n");
    $items = explode(';', $DEFIB);
    $items[4] = (float)str_replace(',','.',array_slice($items, -2)[0]);
    $items[5] = (float)str_replace(',','.',array_slice($items, -1)[0]);
    
    //calculate distance
    $x = ($items[4] - $LON) * cos( ( $LAT + $items[5] ) / 2 );
    $y = ($items[5] - $LAT);
    $d = sqrt( (pow($x,2) + pow($y,2)) * 6371 );
    
    if (abs($result) > abs($d) || $result == null) {
        $result = $d;
        $final = $items;
        
        if ($result == 0) {
            break;
        }
    }
}
// Write an action using echo(). DON'T FORGET THE TRAILING \n
// To debug (equivalent to var_dump): error_log(var_export($var, true));
echo($final[1]);

?>
