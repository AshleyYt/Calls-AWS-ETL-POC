SELECT *
FROM all_historical
WHERE schemaname = 'call_center_dw' 
    

SELECT "column", type, distkey, sortkey
FROM 	all_historical
WHERE schemaname = 'call_center_dw 
AND tablename = 'calls'


ALTER TABLE call_center_dw.calls_length 
ALTER COMPOUND SORTKEY(AHT,Weekday,call_id)


