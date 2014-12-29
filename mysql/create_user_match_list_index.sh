#!/bin/bash

for i in $( seq 0 99)
do
    echo "CREATE INDEX user_id_name_area_id_name_index on lol.user_match_list_info_$i (user_id_name(15), area_id_name(10));"
    echo "CREATE INDEX user_id_name_index on lol.user_match_list_info_$i (user_id_name(15));"
done
