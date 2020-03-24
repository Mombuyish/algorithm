<?php

function twoSum($nums, $target) 
{
    $hash = [];

    foreach($nums as $k => $v) { //O(n)
        $result = $target - $v;

        if(isset($hash[$result])) { //
            return [$hash[$result], $k];
        }

        $hash[$v] = $k;
    }

    return $hash;
}

print_r(twoSum([2, 7, 11, 15], 9)); // [0, 1]