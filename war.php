<?php
 // War
 // https://www.codingame.com/ide/puzzle/winamax-battle

 $users = array([],[]);
 $values = array(2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K', 'A');

fscanf(STDIN, "%d",
    $n // the number of cards for player 1
);

for ($i = 0; $i < $n; $i++)
{
    fscanf(STDIN, "%s",
        $cardp1 // the n cards of player 1
    );
    $users[0][] = $cardp1;
}


fscanf(STDIN, "%d",
    $m // the number of cards for player 2
);

for ($i = 0; $i < $m; $i++)
{
    fscanf(STDIN, "%s",
        $cardp2 // the m cards of player 2
    );
    $users[1][] = $cardp2;
}

error_log(var_export($users, true));
$p1Stack = array();
$p2Stack = array();
$i = 0;
$j = 0;

while (true) {
    $p1Stack[] = $users[0][0];
    $p2Stack[] = $users[1][0];
    unset($users[0][0]);
    unset($users[1][0]);
    $users[0] = array_values($users[0]);
    $users[1] = array_values($users[1]);
    
    if (array_search(substr($p1Stack[$i], 0, -1), $values) > array_search(substr($p2Stack[$i], 0, -1), $values)) {
        $users[0] = array_merge($users[0], $p1Stack, $p2Stack);
        $p1Stack = array();
        $p2Stack = array();
        $j++;
        $i = 0;
    } elseif (array_search(substr($p1Stack[$i], 0, -1), $values) < array_search(substr($p2Stack[$i], 0, -1), $values)) {
        $users[1] = array_merge($users[1], $p1Stack, $p2Stack);
        $p1Stack = array();
        $p2Stack = array();
        $j++;
        $i = 0;
    } else {
        if (count($users[1]) < 4 || count($users[0]) < 4) {
            echo("PAT");
            die;
        } else {
            array_push($p1Stack, $users[0][0],$users[0][1],$users[0][2]);
            array_push($p2Stack, $users[1][0],$users[1][1],$users[1][2]);
            unset($users[0][0]);
            unset($users[0][1]);
            unset($users[0][2]);
            unset($users[1][0]);
            unset($users[1][1]);
            unset($users[1][2]);
            $users[0] = array_values($users[0]);
            $users[1] = array_values($users[1]);
            $i = $i + 4;
        }
    }
    
    if (count($users[0]) == 0) {
        echo(2 . " " . ($j) . "\n");
        die;
    } elseif (count($users[1]) == 0) {
        echo(1 . " " . ($j) . "\n");
        die;
    }
}

?>