#!/bin/bash

for i in $( seq 0 99)
do
    echo "CREATE TABLE lol.match_ex_info_$i LIKE lol.match_ex_info;";
    echo "INSERT INTO lol.match_ex_info_$i SELECT * FROM lol.match_ex_info WHERE match_id%100=$i;";
done
