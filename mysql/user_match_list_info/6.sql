CREATE TABLE if not exists lol.user_match_list_info_6 LIKE lol.user_match_list_info;
INSERT INTO lol.user_match_list_info_6 SELECT * FROM lol.user_match_list_info WHERE crc32(user_id_name)%100=6;
CREATE TABLE if not exists lol.user_match_list_info_16 LIKE lol.user_match_list_info;
INSERT INTO lol.user_match_list_info_16 SELECT * FROM lol.user_match_list_info WHERE crc32(user_id_name)%100=16;
CREATE TABLE if not exists lol.user_match_list_info_26 LIKE lol.user_match_list_info;
INSERT INTO lol.user_match_list_info_26 SELECT * FROM lol.user_match_list_info WHERE crc32(user_id_name)%100=26;
CREATE TABLE if not exists lol.user_match_list_info_36 LIKE lol.user_match_list_info;
INSERT INTO lol.user_match_list_info_36 SELECT * FROM lol.user_match_list_info WHERE crc32(user_id_name)%100=36;
CREATE TABLE if not exists lol.user_match_list_info_46 LIKE lol.user_match_list_info;
INSERT INTO lol.user_match_list_info_46 SELECT * FROM lol.user_match_list_info WHERE crc32(user_id_name)%100=46;
CREATE TABLE if not exists lol.user_match_list_info_56 LIKE lol.user_match_list_info;
INSERT INTO lol.user_match_list_info_56 SELECT * FROM lol.user_match_list_info WHERE crc32(user_id_name)%100=56;
CREATE TABLE if not exists lol.user_match_list_info_66 LIKE lol.user_match_list_info;
INSERT INTO lol.user_match_list_info_66 SELECT * FROM lol.user_match_list_info WHERE crc32(user_id_name)%100=66;
CREATE TABLE if not exists lol.user_match_list_info_76 LIKE lol.user_match_list_info;
INSERT INTO lol.user_match_list_info_76 SELECT * FROM lol.user_match_list_info WHERE crc32(user_id_name)%100=76;
CREATE TABLE if not exists lol.user_match_list_info_86 LIKE lol.user_match_list_info;
INSERT INTO lol.user_match_list_info_86 SELECT * FROM lol.user_match_list_info WHERE crc32(user_id_name)%100=86;
CREATE TABLE if not exists lol.user_match_list_info_96 LIKE lol.user_match_list_info;
INSERT INTO lol.user_match_list_info_96 SELECT * FROM lol.user_match_list_info WHERE crc32(user_id_name)%100=96;
