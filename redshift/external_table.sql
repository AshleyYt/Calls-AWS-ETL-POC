create external schema dwh_external_data_spectrum from data catalog 
database 'aht_external_data' 
iam_role 'xxxxxxx' 
region 'ohio';


create external table dwh_external_data_spectrum.session_data_file(
	session_id varchar(255),
	event_timestamp varchar(150),
	event_type varchar(50),
	employeeid varchar(255),
	call_id varchar(255),
)
row format delimited
fields terminated by ','
stored as textfile 
location 's3://xxxx'
table properties ('skip.header.line.count'='1')
