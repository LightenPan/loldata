--  CREATE TABLE lol.match_ex_info_4 LIKE lol.match_ex_info;
INSERT INTO lol.match_ex_info_4 SELECT * FROM lol.match_ex_info WHERE match_id%100=4;
