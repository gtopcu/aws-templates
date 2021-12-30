/*---------------------------------------------------------------------------------------
Oracle DB notes - S. Gökhan Topçu
--------------------------------------------------------------------------------------- */

sqlplus / as sysdba

SELECT * FROM $V_SQL

select * from table(dbms_xplan.display)
explain plan for
SELECT IDX, IDENTIFIER, TITLE
FROM INVUSER.INV_IC_GIB_USERLIST_PK
WHERE DENTIFIER = 6430046843
ORDER BY TITLE						
								
--INV_IC_GIB_USERLIST_GB
DROP INDEX INV_IC_GIB_USERLIST_GB_IDX1;

CREATE INDEX INV_IC_GIB_USERLIST_GB_IDX2
ON INV_IC_GIB_USERLIST_GB(CREATION_TIME, APP_TYPE);

CREATE INDEX INV_IC_GIB_USERLIST_GB_IDX3
ON INV_IC_GIB_USERLIST_GB(LOWER("TITLE"));


SELECT * FROM INVUSER.INV_IC_GIB_USERLIST_PK 
WHERE APP_TYPE=0 AND CREATION_TIME >= (SYSDATE-10) AND DELETION_TIME IS NULL;

SELECT * FROM INVUSER.INV_IC_GIB_USERLIST_PK 
WHERE IDENTIFIER='99909701091' AND APP_TYPE= 0 AND DELETION_TIME IS NULL;

SELECT TYPE, COUNT(1) FROM INVUSER.INV_IN_ENV
WHERE INSERT_DATETIME > (SYSDATE-30)
GROUP BY TYPE;

INSERT INTO suppliers
(supplier_id, supplier_name)
VALUES
(5000, 'Apple');

INSERT INTO suppliers
(supplier_id, supplier_name)
SELECT account_no, name
FROM customers
WHERE customer_id > 5000;

FOR i IN 1..v_inv_in_log_process_arr.COUNT LOOP
    INSERT INTO INVUSER.ZARC_INV_IN_LOG_PROCESS VALUES v_inv_in_log_process_arr(i);
    IF mod(i,v_num_del_rows)=0 THEN
      COMMIT;
    END IF;
END LOOP;

-----------------------------------------------------------------------------------------------------------------------------


CREATE TABLESPACE invtblspc DATAFILE 'C:\oracledb\oradata\ORP\invtblspc\INVTBLSPC01.DBF' size 2000M;

CREATE USER INVUSER
IDENTIFIED BY "gt123456"
DEFAULT TABLESPACE INVTBLSPC
TEMPORARY TABLESPACE TEMP
PROFILE DEFAULT
ACCOUNT UNLOCK;

GRANT CONNECT TO INVUSER;
GRANT DBA TO INVUSER;
GRANT RESOURCE TO INVUSER;
GRANT SELECT ANY TABLE TO INVUSER;
GRANT INSERT ANY TABLE TO INVUSER;
GRANT UPDATE ANY TABLE TO INVUSER;
GRANT DELETE ANY TABLE TO INVUSER;
GRANT CREATE ANY TABLE TO INVUSER;
GRANT ALTER ANY TABLE TO INVUSER;
GRANT DROP ANY TABLE TO INVUSER;
GRANT SELECT ANY DICTIONARY TO INVUSER;
GRANT ALTER ANY INDEX TO INVUSER;
GRANT EXECUTE ON DBMS_LOCK TO INVUSER;
ALTER USER INVUSER DEFAULT ROLE ALL;
GRANT sysdba to INVUSER;

ALTER USER INVUSER QUOTA unlimited ON INVTBLSPC;


---------------------------------------------------------------------------------------------------------------------------------------------------------

-----------------------------------------------------------------------------------------
INVUSER.ARCHIVER_REVISED
-----------------------------------------------------------------------------------------

CREATE OR REPLACE PROCEDURE INVUSER.archiver_revised IS
  v_days_to_keep_ws   NUMBER := 3;
  v_days_to_keep_nf   NUMBER := 30;
  v_days_to_keep_batch NUMBER := 30;
  v_days_to_keep_drafts NUMBER := 90;
  v_days_to_keep_log    NUMBER := 30;
  v_num_del_rows PLS_INTEGER := 1000; --How many rows will be deleted at a time
  TYPE v_inv_in_log_process_arr_type IS TABLE OF INVUSER.INV_OUT_LOG_PROCESS%ROWTYPE INDEX BY PLS_INTEGER;
  v_inv_in_log_process_arr   v_inv_in_log_process_arr_type;
  TYPE v_inv_out_log_process_arr_type IS TABLE OF INVUSER.INV_OUT_LOG_PROCESS%ROWTYPE INDEX BY PLS_INTEGER;
  v_inv_out_log_process_arr   v_inv_out_log_process_arr_type;
  TYPE v_inv_ic_log_ws_arr_type IS TABLE OF INVUSER.INV_IC_LOG_WS%ROWTYPE INDEX BY PLS_INTEGER;
  v_inv_ic_log_ws_arr   v_inv_ic_log_ws_arr_type;
  TYPE v_inv_ic_ws_clnt_xs_arr_type IS TABLE OF INVUSER.INV_IC_WS_CLIENT_ACCESS%ROWTYPE INDEX BY PLS_INTEGER;
  v_inv_ic_ws_clnt_xs_arr   v_inv_ic_ws_clnt_xs_arr_type;
  TYPE v_inv_ns_notify_arr_type IS TABLE OF INVUSER.INV_NS_NOTIFY%ROWTYPE INDEX BY PLS_INTEGER;
  v_inv_ns_notify_arr   v_inv_ns_notify_arr_type;
  TYPE v_inv_ns_notify_log_arr_type IS TABLE OF INVUSER.INV_NS_NOTIFY_LOG%ROWTYPE INDEX BY PLS_INTEGER;
  v_inv_ns_notify_log_arr   v_inv_ns_notify_log_arr_type;
 
BEGIN
--INV_IN_LOG_PROCESS REVISED
   SELECT * BULK COLLECT INTO v_inv_in_log_process_arr  
   FROM INVUSER.inv_in_log_process
   WHERE insert_datetime < (SYSDATE - v_days_to_keep_log);  
   FOR i IN 1..v_inv_in_log_process_arr.COUNT LOOP
      INSERT INTO INVUSER.ZARC_INV_IN_LOG_PROCESS VALUES v_inv_in_log_process_arr(i);
      DELETE FROM INVUSER.inv_in_log_process WHERE idx = v_inv_in_log_process_arr(i).idx;
      IF mod(i,v_num_del_rows)=0 THEN
          COMMIT;
      END IF;
   END LOOP;
   COMMIT;

--INV_OUT_LOG_PROCESS REVISED
   SELECT * BULK COLLECT INTO v_inv_out_log_process_arr  
   FROM INVUSER.inv_out_log_process
   WHERE insert_datetime < (SYSDATE - v_days_to_keep_log);
   FOR i IN 1..v_inv_out_log_process_arr.COUNT LOOP
      INSERT INTO INVUSER.ZARC_INV_OUT_LOG_PROCESS VALUES v_inv_out_log_process_arr(i);
      DELETE FROM INVUSER.inv_out_log_process WHERE idx = v_inv_out_log_process_arr(i).idx;
      IF mod(i,v_num_del_rows)=0 THEN
          COMMIT;
      END IF;
   END LOOP;
   COMMIT;
 
--INV_IC_LOG_WS REVISED
   SELECT * BULK COLLECT INTO v_inv_ic_log_ws_arr  
   FROM INVUSER.inv_ic_log_ws
   WHERE insert_datetime < (SYSDATE - v_days_to_keep_log);
   
   FOR i IN 1..v_inv_ic_log_ws_arr.COUNT LOOP
      INSERT INTO INVUSER.ZARC_INV_IC_LOG_WS VALUES v_inv_ic_log_ws_arr(i);
      DELETE FROM INVUSER.inv_ic_log_ws WHERE idx = v_inv_ic_log_ws_arr(i).idx;
      IF mod(i,v_num_del_rows)=0 THEN
          COMMIT;
      END IF;
   END LOOP;
   COMMIT;


--INV_IC_WS_CLIENT_ACCESS REVISED
   SELECT * BULK COLLECT INTO v_inv_ic_ws_clnt_xs_arr
   FROM INVUSER.INV_IC_WS_CLIENT_ACCESS
   WHERE SYS_LAST_UPDATE < (SYSDATE - v_days_to_keep_ws);
   FOR i IN 1..v_inv_ic_ws_clnt_xs_arr.COUNT LOOP
      DELETE FROM INVUSER.INV_IC_WS_CLIENT_ACCESS WHERE idx = v_inv_ic_ws_clnt_xs_arr(i).idx;
      IF mod(i,v_num_del_rows)=0 THEN
          COMMIT;
      END IF;
   END LOOP;
   COMMIT;

--INV_NS_NOTIFY
   SELECT * BULK COLLECT INTO v_inv_ns_notify_arr
   FROM INVUSER.INV_NS_NOTIFY
   WHERE SYS_LAST_UPDATE < (SYSDATE - v_days_to_keep_nf);
   FOR i IN 1..v_inv_ns_notify_arr.COUNT LOOP
      DELETE FROM INVUSER.INV_NS_NOTIFY WHERE idx = v_inv_ns_notify_arr(i).idx;
      IF mod(i,v_num_del_rows)=0 THEN
          COMMIT;
      END IF;
   END LOOP;
   COMMIT;

  --INV_NS_NOTIFY_LOG
   SELECT * BULK COLLECT INTO v_inv_ns_notify_log_arr  
   FROM INVUSER.INV_NS_NOTIFY_LOG
   WHERE SYS_LAST_UPDATE < (SYSDATE - v_days_to_keep_nf);
   FOR i IN 1..v_inv_ns_notify_log_arr.COUNT LOOP
      DELETE FROM INVUSER.INV_NS_NOTIFY_LOG WHERE idx = v_inv_ns_notify_log_arr(i).idx;
      IF mod(i,v_num_del_rows)=0 THEN
          COMMIT;
      END IF;
   END LOOP;
   COMMIT;

--PT_BATCH
DELETE FROM
INVUSER.INV_PT_BATCH
WHERE
REQUEST_TYPE IN (
                    10,   
                    110,
                    250, 
                    220
                )
AND INSERT_DATETIME < (SYSDATE-v_days_to_keep_batch);
        COMMIT;

--INV_OUT_INV_DRAFT
DELETE FROM INVUSER.INV_OUT_INV_DRAFT
WHERE INSERT_DATE < (SYSDATE - v_days_to_keep_drafts);
    COMMIT;
END;
/


