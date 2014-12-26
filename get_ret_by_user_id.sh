#!/bin/bash

set -x

match_id_list=`cat user_match_list.csv | awk -F, '{print $8}' | sort | uniq | xargs`

for match_id in $match_id_list
do
	# echo match_id
	python match-info.py --area_id_name=电信一 --user_id_name=LightenPan --match_id=$match_id
done

