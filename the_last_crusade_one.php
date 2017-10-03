<?php
// The Last Crusade - Episode 1
// https://www.codingame.com/ide/puzzle/the-last-crusade-episode-1

$lines = array();


fscanf(STDIN, "%d %d",
    $W, // number of columns.
    $H // number of rows.
);
error_log(var_export("width: ".$W." height: ".$H, true));

for ($i = 0; $i < $H; $i++)
{
    $LINE = stream_get_line(STDIN, 200 + 1, "\n"); // represents a line in the grid and contains W integers. Each integer represents one room of a given type.
    $l = explode(" ", $LINE);
    $lines[] = $l;
    error_log(var_export("line: ".$LINE, true));
}

fscanf(STDIN, "%d",
    $EX // the coordinate along the X axis of the exit (not useful for this first mission, but must be read).
);

// game loop
while (TRUE)
{
    fscanf(STDIN, "%d %d %s",
        $XI,
        $YI,
        $POS
    );
    
    $x = $XI; 
    $y = $YI;

    // Write an action using echo(). DON'T FORGET THE TRAILING \n
    // To debug (equivalent to var_dump): error_log(var_export($var, true));
    error_log(var_export("xi: ".$XI." yi: ".$YI. " pos: ".$POS, true));
    error_log(var_export($lines[$YI][$XI], true));
    // One line containing the X Y coordinates of the room in which you believe Indy will be on the next turn.
    if (($lines[$YI][$XI] == 2 && $POS == "LEFT") || $lines[$YI][$XI] == 11 || ($lines[$YI][$XI] == 6 && $POS == "LEFT") || ($lines[$YI][$XI] == 5 && $POS == "TOP")) {
        $x++;
    } else if ($lines[$YI][$XI] == 10 || ($lines[$YI][$XI] == 2 && $POS == "RIGHT") || ($lines[$YI][$XI] == 4 && $POS == "TOP") || ($lines[$YI][$XI] == 6 && $POS == "RIGHT")) {
        $x--;
    } else if ($lines[$YI][$XI] == 8 || $lines[$YI][$XI] == 1 || $lines[$YI][$XI] == 7 || $lines[$YI][$XI] == 13 || $lines[$YI][$XI] == 3  
    || ($lines[$YI][$XI] == 5 && $POS == "LEFT") || ($lines[$YI][$XI] == 4 && $POS == "RIGHT") || $lines[$YI][$XI] == 9 || $lines[$YI][$XI] == 12) {
        $y++;
    }
    echo($x . " " . $y . "\n");
}
?>