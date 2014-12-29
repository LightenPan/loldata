#!/bin/bash

for i in $( seq 0 99)
do
    # $file_index=$((i%10))
    # $file_name=$file_index + ".sql"
    file_name=$((i%10)).sql
    echo "CREATE TABLE if not exist lol.user_match_list_info_$i LIKE lol.user_match_list_info;" >> $file_name
    echo "INSERT INTO lol.user_match_list_info_$i SELECT * FROM lol.user_match_list_info WHERE crc32(user_id_name)%100=$i;" >> $file_name
done
