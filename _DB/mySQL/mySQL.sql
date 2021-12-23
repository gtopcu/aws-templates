/*---------------------------------------------------------------------------------------
MySQL DB notes - S. Gökhan Topçu
https://www.mysql.com/downloads/
--------------------------------------------------------------------------------------- */

/*-----------------------------------------------------
Parameter Group:
version:8.0.23 / Aurora3.0
Port:3306 
AdminPort:33062
binlog
maxConnections:16000
max_user_connections:4294967295
baseDir:/rdsdbbin/oscar
binlog_format:ROW, STATEMENT, MIXED, OFF
--------------------------------------------------------
CLI
mysql -h<mysqldbaddress> -u$DBUSER -p"$DBPASS" mylab;
show tables;
desc <table_name>;
------------------------------------------------------*/


CREATE DATABASE `myaurorasql` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;
SELECT * FROM sys.sys_config limit 100;

DROP TABLE `myaurorasql`.`myTable`;
CREATE TABLE `myaurorasql`.`myTable` (
  `id` INT NOT NULL,
  `name` VARCHAR(1000) NULL,
  PRIMARY KEY (`id`));

CREATE INDEX `idx_myTable_name` ON `myaurorasql`.`myTable` 
(name) 
COMMENT '' 
ALGORITHM DEFAULT LOCK DEFAULT

SELECT id, name FROM myTable 
WHERE name LIKE '%B'
limit 100;

INSERT INTO `myaurorasql`.`myTable`
(id, name) VALUES (6, 'GB');

INSERT INTO `myaurorasql`.`events`
(event_id, event_date) VALUES (1, now());

/* Procedure */

drop table if exists foo;
create table foo
(
id int unsigned not null auto_increment primary key,
val smallint unsigned not null default 0
)
engine=innodb;

drop procedure if exists load_foo_test_data;

create procedure load_foo_test_data()
begin
declare v_max int unsigned default 1000;
declare v_counter int unsigned default 0;

truncate table foo;
start transaction;
while v_counter < v_max do
  insert into foo (val) values ( floor(0 + (rand() * 65535)) );
  set v_counter=v_counter+1;
end while;
commit;

call load_foo_test_data();
select * from foo order by id;


/* Status 
----------------------------------------------------------------------------------------------------

GLOBAL STATUS:
Aborted_clients................................................... 0
Aborted_connects.................................................. 2
Acl_cache_items_count............................................. 1
AuroraDb_commits.................................................. 0
AuroraDb_commit_latency........................................... 0
AuroraDb_ddl_stmt_duration........................................ 124465807
AuroraDb_select_stmt_duration..................................... 5998932
AuroraDb_insert_stmt_duration..................................... 0
AuroraDb_update_stmt_duration..................................... 0
AuroraDb_delete_stmt_duration..................................... 0
Aurora_binlog_io_cache_allocated.................................. 0
Aurora_binlog_io_cache_read_requests.............................. 0
Aurora_binlog_io_cache_reads...................................... 0
Aurora_external_connection_count.................................. 4
Aurora_fast_insert_cache_hits..................................... 0
Aurora_fast_insert_cache_misses................................... 0
Aurora_fwd_replica_dml_stmt_count................................. 0
Aurora_fwd_replica_dml_stmt_duration.............................. 0
Aurora_fwd_replica_errors_rpc_timeout............................. 0.000000
Aurora_fwd_replica_errors_session_limit........................... 0
Aurora_fwd_replica_errors_session_terminated...................... 0
Aurora_fwd_replica_open_sessions.................................. 0
Aurora_fwd_replica_read_wait_count................................ 0
Aurora_fwd_replica_read_wait_duration............................. 0
Aurora_fwd_replica_select_stmt_count.............................. 0
Aurora_fwd_replica_select_stmt_duration........................... 0
Aurora_lockmgr_memory_used........................................ 0
Aurora_ml_actual_request_cnt...................................... 0
Aurora_ml_actual_response_cnt..................................... 0
Aurora_ml_cache_hit_cnt........................................... 0
Aurora_ml_logical_request_cnt..................................... 0
Aurora_ml_logical_response_cnt.................................... 0
Aurora_ml_retry_request_cnt....................................... 0
Aurora_ml_single_request_cnt...................................... 0
Aurora_pq_request_attempted....................................... 0
Aurora_pq_request_attempted_grouping_aggr......................... 0
Aurora_pq_request_attempted_partition_table....................... 0
Aurora_pq_request_by_force_config................................. 0
Aurora_pq_request_by_global_config................................ 0
Aurora_pq_request_by_hint......................................... 0
Aurora_pq_request_by_session_config............................... 0
Aurora_pq_request_executed........................................ 0
Aurora_pq_request_executed_grouping_aggr.......................... 0
Aurora_pq_request_executed_partition_table........................ 0
Aurora_pq_request_failed.......................................... 0
Aurora_pq_request_failed_grouping_aggr............................ 0
Aurora_pq_request_failed_partition_table.......................... 0
Aurora_pq_request_in_instance_type_r_12xlarge..................... 0
Aurora_pq_request_in_instance_type_r_16xlarge..................... 0
Aurora_pq_request_in_instance_type_r_24xlarge..................... 0
Aurora_pq_request_in_instance_type_r_2xlarge...................... 0
Aurora_pq_request_in_instance_type_r_4xlarge...................... 0
Aurora_pq_request_in_instance_type_r_8xlarge...................... 0
Aurora_pq_request_in_instance_type_r_large........................ 0
Aurora_pq_request_in_instance_type_r_xlarge....................... 0
Aurora_pq_request_in_instance_type_unsupported.................... 0
Aurora_pq_request_in_progress..................................... 0
Aurora_pq_request_in_reader_instance.............................. 0
Aurora_pq_request_in_writer_instance.............................. 0
Aurora_pq_request_not_chosen...................................... 0
Aurora_pq_request_not_chosen_below_min_rows....................... 0
Aurora_pq_request_not_chosen_column_bit........................... 0
Aurora_pq_request_not_chosen_column_geometry...................... 0
Aurora_pq_request_not_chosen_column_lob........................... 0
Aurora_pq_request_not_chosen_column_virtual....................... 0
Aurora_pq_request_not_chosen_custom_charset....................... 0
Aurora_pq_request_not_chosen_few_pages_outside_buffer_pool........ 0
Aurora_pq_request_not_chosen_full_text_index...................... 0
Aurora_pq_request_not_chosen_grouping_aggr........................ 0
Aurora_pq_request_not_chosen_grouping_aggr_aggr_type.............. 0
Aurora_pq_request_not_chosen_grouping_aggr_config................. 0
Aurora_pq_request_not_chosen_grouping_aggr_distinct_aggr_uniq..... 0
Aurora_pq_request_not_chosen_grouping_aggr_expression............. 0
Aurora_pq_request_not_chosen_grouping_aggr_filter................. 0
Aurora_pq_request_not_chosen_grouping_aggr_large_aggr_result...... 0
Aurora_pq_request_not_chosen_grouping_aggr_large_groups........... 0
Aurora_pq_request_not_chosen_grouping_aggr_many_grouping_cols..... 0
Aurora_pq_request_not_chosen_grouping_aggr_unique_key............. 0
Aurora_pq_request_not_chosen_high_buffer_pool_pct................. 0
Aurora_pq_request_not_chosen_index_hint........................... 0
Aurora_pq_request_not_chosen_innodb_table_format.................. 0
Aurora_pq_request_not_chosen_instant_ddl.......................... 0
Aurora_pq_request_not_chosen_long_trx............................. 0
Aurora_pq_request_not_chosen_no_where_clause...................... 0
Aurora_pq_request_not_chosen_range_scan........................... 0
Aurora_pq_request_not_chosen_row_length_too_long.................. 0
Aurora_pq_request_not_chosen_small_table.......................... 0
Aurora_pq_request_not_chosen_temporary_table...................... 0
Aurora_pq_request_not_chosen_tx_isolation......................... 0
Aurora_pq_request_not_chosen_unsupported_access................... 0
Aurora_pq_request_not_chosen_update_delete_stmts.................. 0
Aurora_pq_request_throttled....................................... 0
Aurora_pq_request_with_bloom_filter............................... 0
Aurora_pq_request_with_lob........................................ 0
Aurora_pq_stmt_attempted.......................................... 0
Aurora_pq_stmt_attempted_hash_join................................ 0
Aurora_repl_bytes_received........................................ 83760222
Aurora_replica_disconnect_duration_in_sec......................... 0
Aurora_reserved_mem_exceeded_incidents............................ 0
Aurora_thread_pool_thread_count................................... 4
Binlog_cache_disk_use............................................. 0
Binlog_cache_use.................................................. 0
Binlog_stmt_cache_disk_use........................................ 0
Binlog_stmt_cache_use............................................. 0
Bytes_received.................................................... 1147775
Bytes_sent........................................................ 5550656
Caching_sha2_password_rsa_public_key.............................. -----BEGIN PUBLIC KEY-----
MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEArshWO9DsVb3x3zE2wL9U
kosy0Cg4I3oMBAhTyQpKZ8yijHKPbmmx1z7wE+gcI7lnwhkhzNdsC/P+ed0Ive/+
zxnhT53w234yimAekYct9aaKzf0niPVzc6pM8SkYKU2AjA5HZVPkqI22Yqsjn8FC
tyODbdSuRUqkNdaFothoASgqwo+7UtAFRk9WYKcS87DP9g6IX56Jd6hfDP8WJXOP
gQCTmaqex4rwJJk3Lb4yVI+u/hx7eObGFcClNY1jZXWmQ1ej11xSs6SYkr+eJWAJ
v1eKMoIT7pnTgOy/sWzXcQlDhX+h2ZUsTHMevQBgA00doEN76uoyIlxPzJ75R+2g
UwIDAQAB
-----END PUBLIC KEY-----

Com_admin_commands................................................ 56
Com_assign_to_keycache............................................ 0
Com_alter_db...................................................... 0
Com_alter_event................................................... 0
Com_alter_function................................................ 0
Com_alter_instance................................................ 0
Com_alter_procedure............................................... 0
Com_alter_resource_group.......................................... 0
Com_alter_server.................................................. 0
Com_alter_table................................................... 0
Com_alter_tablespace.............................................. 0
Com_alter_user.................................................... 0
Com_alter_user_default_role....................................... 0
Com_analyze....................................................... 0
Com_begin......................................................... 0
Com_binlog........................................................ 0
Com_call_procedure................................................ 0
Com_change_db..................................................... 3
Com_change_master................................................. 0
Com_change_repl_filter............................................ 0
Com_change_replication_source..................................... 0
Com_check......................................................... 0
Com_checksum...................................................... 0
Com_clone......................................................... 0
Com_commit........................................................ 0
Com_create_db..................................................... 1
Com_create_event.................................................. 0
Com_create_function............................................... 0
Com_create_index.................................................. 0
Com_create_procedure.............................................. 0
Com_create_role................................................... 0
Com_create_server................................................. 0
Com_create_table.................................................. 35
Com_create_resource_group......................................... 0
Com_create_trigger................................................ 0
Com_create_udf.................................................... 0
Com_create_user................................................... 0
Com_create_view................................................... 0
Com_create_spatial_reference_system............................... 0
Com_dealloc_sql................................................... 0
Com_delete........................................................ 0
Com_delete_multi.................................................. 0
Com_do............................................................ 0
Com_drop_db....................................................... 0
Com_drop_event.................................................... 0
Com_drop_function................................................. 0
Com_drop_index.................................................... 0
Com_drop_procedure................................................ 0
Com_drop_resource_group........................................... 0
Com_drop_role..................................................... 0
Com_drop_server................................................... 0
Com_drop_spatial_reference_system................................. 0
Com_drop_table.................................................... 0
Com_drop_trigger.................................................. 0
Com_drop_user..................................................... 0
Com_drop_view..................................................... 0
Com_empty_query................................................... 0
Com_execute_sql................................................... 0
Com_explain_other................................................. 0
Com_flush......................................................... 37
Com_get_diagnostics............................................... 0
Com_grant......................................................... 0
Com_grant_roles................................................... 0
Com_ha_close...................................................... 0
Com_ha_open....................................................... 0
Com_ha_read....................................................... 0
Com_help.......................................................... 0
Com_import........................................................ 0
Com_insert........................................................ 0
Com_insert_select................................................. 0
Com_install_component............................................. 0
Com_install_plugin................................................ 0
Com_kill.......................................................... 0
Com_load.......................................................... 0
Com_lock_instance................................................. 0
Com_lock_tables................................................... 0
Com_optimize...................................................... 0
Com_preload_keys.................................................. 0
Com_prepare_sql................................................... 0
Com_purge......................................................... 0
Com_purge_before_date............................................. 0
Com_release_savepoint............................................. 0
Com_rename_table.................................................. 0
Com_rename_user................................................... 0
Com_repair........................................................ 0
Com_replace....................................................... 0
Com_replace_select................................................ 0
Com_reset......................................................... 0
Com_resignal...................................................... 0
Com_restart....................................................... 0
Com_revoke........................................................ 0
Com_revoke_all.................................................... 0
Com_revoke_roles.................................................. 0
Com_rollback...................................................... 0
Com_rollback_to_savepoint......................................... 0
Com_savepoint..................................................... 0
Com_select........................................................ 7424
Com_set_option.................................................... 6270
Com_set_password.................................................. 0
Com_set_resource_group............................................ 0
Com_set_role...................................................... 0
Com_signal........................................................ 0
Com_show_binlog_events............................................ 0
Com_show_binlogs.................................................. 0
Com_show_charsets................................................. 5
Com_show_collations............................................... 1
Com_show_create_db................................................ 2
Com_show_create_event............................................. 0
Com_show_create_func.............................................. 1
Com_show_create_proc.............................................. 0
Com_show_create_table............................................. 1
Com_show_create_trigger........................................... 0
Com_show_databases................................................ 4
Com_show_engine_logs.............................................. 0
Com_show_engine_mutex............................................. 0
Com_show_engine_status............................................ 0
Com_show_events................................................... 1
Com_show_errors................................................... 0
Com_show_fields................................................... 107
Com_show_function_code............................................ 0
Com_show_function_status.......................................... 3
Com_show_grants................................................... 0
Com_show_keys..................................................... 4
Com_show_master_status............................................ 0
Com_show_open_tables.............................................. 0
Com_show_plugins.................................................. 1
Com_show_privileges............................................... 0
Com_show_procedure_code........................................... 0
Com_show_procedure_status......................................... 3
Com_show_processlist.............................................. 2
Com_show_profile.................................................. 0
Com_show_profiles................................................. 0
Com_show_relaylog_events.......................................... 0
Com_show_replicas................................................. 0
Com_show_slave_hosts.............................................. 0
Com_show_replica_status........................................... 1
Com_show_slave_status............................................. 1
Com_show_status................................................... 246
Com_show_storage_engines.......................................... 1
Com_show_table_status............................................. 2
Com_show_tables................................................... 7
Com_show_triggers................................................. 2
Com_show_variables................................................ 29
Com_show_warnings................................................. 24
Com_show_create_user.............................................. 0
Com_shutdown...................................................... 0
Com_replica_start................................................. 0
Com_slave_start................................................... 0
Com_replica_stop.................................................. 0
Com_slave_stop.................................................... 0
Com_group_replication_start....................................... 0
Com_group_replication_stop........................................ 0
Com_stmt_execute.................................................. 0
Com_stmt_close.................................................... 0
Com_stmt_fetch.................................................... 0
Com_stmt_prepare.................................................. 0
Com_stmt_reset.................................................... 0
Com_stmt_send_long_data........................................... 0
Com_truncate...................................................... 0
Com_uninstall_component........................................... 0
Com_uninstall_plugin.............................................. 0
Com_unlock_instance............................................... 0
Com_unlock_tables................................................. 0
Com_update........................................................ 0
Com_update_multi.................................................. 0
Com_xa_commit..................................................... 0
Com_xa_end........................................................ 0
Com_xa_prepare.................................................... 0
Com_xa_recover.................................................... 0
Com_xa_rollback................................................... 0
Com_xa_start...................................................... 0
Com_awslambda..................................................... 0
Com_alter_system.................................................. 0
Com_unit_test..................................................... 0
Com_show_volume_status............................................ 0
Com_stmt_reprepare................................................ 0
Connection_errors_accept.......................................... 0
Connection_errors_internal........................................ 0
Connection_errors_max_connections................................. 0
Connection_errors_peer_address.................................... 0
Connection_errors_select.......................................... 0
Connection_errors_tcpwrap......................................... 0
Connections....................................................... 36
Created_tmp_disk_tables........................................... 0
Created_tmp_files................................................. 0
Created_tmp_tables................................................ 3840
Current_tls_ca.................................................... /rdsdbdata/rds-metadata/ca-cert.pem
Current_tls_capath................................................ 
Current_tls_cert.................................................. /rdsdbdata/rds-metadata/server-cert.pem
Current_tls_cipher................................................ AES256-SHA:AES128-SHA:DES-CBC3-SHA:ADH-DES-CBC3-SHA:EDH-RSA-DES-CBC3-SHA:EDH-DSS-DES-CBC3-SHA:ADH-AES256-SHA:DHE-RSA-AES256-SHA:DHE-DSS-AES256-SHA:ADH-AES128-SHA:DHE-RSA-AES128-SHA:DHE-DSS-AES128-SHA:HIGH
Current_tls_ciphersuites.......................................... 
Current_tls_crl................................................... 
Current_tls_crlpath............................................... 
Current_tls_key................................................... /rdsdbdata/rds-metadata/server-key.pem
Current_tls_version............................................... TLSv1,TLSv1.1,TLSv1.2
Delayed_errors.................................................... 0
Delayed_insert_threads............................................ 0
Delayed_writes.................................................... 0
Error_log_buffered_bytes.......................................... 5968
Error_log_buffered_events......................................... 44
Error_log_expired_events.......................................... 0
Error_log_latest_write............................................ 1639834339078386
Flush_commands.................................................... 3
Handler_commit.................................................... 3170
Handler_delete.................................................... 0
Handler_discover.................................................. 0
Handler_external_lock............................................. 16357
Handler_mrr_init.................................................. 0
Handler_prepare................................................... 0
Handler_read_first................................................ 2658
Handler_read_key.................................................. 12770
Handler_read_last................................................. 0
Handler_read_next................................................. 9011
Handler_read_prev................................................. 0
Handler_read_rnd.................................................. 1085
Handler_read_rnd_next............................................. 309001
Handler_rollback.................................................. 0
Handler_savepoint................................................. 0
Handler_savepoint_rollback........................................ 0
Handler_update.................................................... 0
Handler_write..................................................... 123830
Innodb_buffer_pool_dump_status.................................... 
Innodb_buffer_pool_load_status.................................... 
Innodb_buffer_pool_resize_status.................................. 
Innodb_buffer_pool_pages_data..................................... 335
Innodb_buffer_pool_bytes_data..................................... 5488640
Innodb_buffer_pool_pages_dirty.................................... 0
Innodb_buffer_pool_bytes_dirty.................................... 0
Innodb_buffer_pool_pages_flushed.................................. 0
Innodb_buffer_pool_pages_free..................................... 96217
Innodb_buffer_pool_pages_misc..................................... 18446744073709551576
Innodb_buffer_pool_pages_total.................................... 96512
Innodb_buffer_pool_read_ahead_rnd................................. 0
Innodb_buffer_pool_read_ahead..................................... 0
Innodb_buffer_pool_read_ahead_evicted............................. 0
Innodb_logical_read_ahead_page_count.............................. 0
Innodb_aurora_average_batched_read_request_size................... 0
Innodb_aurora_batched_read_requests............................... 0
Innodb_aurora_shm_batched_read_requests........................... 0
Innodb_aurora_shm_read_requests................................... 335
Innodb_buffer_pool_read_requests.................................. 92813
Innodb_buffer_pool_reads.......................................... 335
Innodb_buffer_pool_wait_free...................................... 0
Innodb_buffer_pool_write_requests................................. 0
Innodb_data_fsyncs................................................ 0
Innodb_data_pending_fsyncs........................................ 0
Innodb_data_pending_reads......................................... 0
Innodb_data_pending_writes........................................ 0
Innodb_data_read.................................................. 5488640
Innodb_data_reads................................................. 0
Innodb_data_writes................................................ 0
Innodb_data_written............................................... 0
Innodb_dblwr_pages_written........................................ 0
Innodb_dblwr_writes............................................... 0
Innodb_log_waits.................................................. 0
Innodb_log_write_requests......................................... 0
Innodb_log_writes................................................. 0
Innodb_os_log_fsyncs.............................................. 0
Innodb_os_log_pending_fsyncs...................................... 0
Innodb_os_log_pending_writes...................................... 0
Innodb_os_log_written............................................. 0
Innodb_page_size.................................................. 16384
Innodb_pages_created.............................................. 0
Innodb_pages_read................................................. 335
Innodb_pages_written.............................................. 0
Innodb_redo_log_enabled........................................... ON
Innodb_row_lock_current_waits..................................... 0
Innodb_row_lock_time.............................................. 0
Innodb_row_lock_time_avg.......................................... 0
Innodb_row_lock_time_max.......................................... 0
Innodb_row_lock_waits............................................. 0
Innodb_rows_deleted............................................... 0
Innodb_rows_inserted.............................................. 0
Innodb_rows_read.................................................. 12
Innodb_rows_updated............................................... 0
Innodb_system_rows_deleted........................................ 0
Innodb_system_rows_inserted....................................... 0
Innodb_system_rows_read........................................... 14039
Innodb_system_rows_updated........................................ 0
Innodb_sampled_pages_read......................................... 0
Innodb_sampled_pages_skipped...................................... 0
Innodb_num_open_files............................................. 14
Innodb_truncated_status_writes.................................... 0
Innodb_undo_tablespaces_total..................................... 2
Innodb_undo_tablespaces_implicit.................................. 2
Innodb_undo_tablespaces_explicit.................................. 0
Innodb_undo_tablespaces_active.................................... 0
Key_blocks_not_flushed............................................ 0
Key_blocks_unused................................................. 13396
Key_blocks_used................................................... 0
Key_read_requests................................................. 0
Key_reads......................................................... 0
Key_write_requests................................................ 0
Key_writes........................................................ 0
Locked_connects................................................... 0
Max_execution_time_exceeded....................................... 0
Max_execution_time_set............................................ 0
Max_execution_time_set_failed..................................... 0
Max_used_connections.............................................. 8
Max_used_connections_time......................................... 2021-12-18 13:43:53
Not_flushed_delayed_rows.......................................... 0
Ongoing_anonymous_transaction_count............................... 0
Open_files........................................................ 1
Open_streams...................................................... 0
Open_table_definitions............................................ 71
Open_tables....................................................... 136
Opened_files...................................................... 1
Opened_table_definitions.......................................... 129
Opened_tables..................................................... 182
Performance_schema_accounts_lost.................................. 0
Performance_schema_cond_classes_lost.............................. 0
Performance_schema_cond_instances_lost............................ 0
Performance_schema_digest_lost.................................... 0
Performance_schema_file_classes_lost.............................. 0
Performance_schema_file_handles_lost.............................. 0
Performance_schema_file_instances_lost............................ 0
Performance_schema_hosts_lost..................................... 0
Performance_schema_index_stat_lost................................ 0
Performance_schema_locker_lost.................................... 0
Performance_schema_memory_classes_lost............................ 0
Performance_schema_metadata_lock_lost............................. 0
Performance_schema_mutex_classes_lost............................. 0
Performance_schema_mutex_instances_lost........................... 0
Performance_schema_nested_statement_lost.......................... 0
Performance_schema_prepared_statements_lost....................... 0
Performance_schema_program_lost................................... 0
Performance_schema_rwlock_classes_lost............................ 0
Performance_schema_rwlock_instances_lost.......................... 0
Performance_schema_session_connect_attrs_longest_seen............. 0
Performance_schema_session_connect_attrs_lost..................... 0
Performance_schema_socket_classes_lost............................ 0
Performance_schema_socket_instances_lost.......................... 0
Performance_schema_stage_classes_lost............................. 0
Performance_schema_statement_classes_lost......................... 0
Performance_schema_table_handles_lost............................. 0
Performance_schema_table_instances_lost........................... 0
Performance_schema_table_lock_stat_lost........................... 0
Performance_schema_thread_classes_lost............................ 0
Performance_schema_thread_instances_lost.......................... 0
Performance_schema_users_lost..................................... 0
Prepared_stmt_count............................................... 0
Queries........................................................... 14272
Questions......................................................... 14215
Replica_open_temp_tables.......................................... 0
Rsa_public_key.................................................... -----BEGIN PUBLIC KEY-----
MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEArshWO9DsVb3x3zE2wL9U
kosy0Cg4I3oMBAhTyQpKZ8yijHKPbmmx1z7wE+gcI7lnwhkhzNdsC/P+ed0Ive/+
zxnhT53w234yimAekYct9aaKzf0niPVzc6pM8SkYKU2AjA5HZVPkqI22Yqsjn8FC
tyODbdSuRUqkNdaFothoASgqwo+7UtAFRk9WYKcS87DP9g6IX56Jd6hfDP8WJXOP
gQCTmaqex4rwJJk3Lb4yVI+u/hx7eObGFcClNY1jZXWmQ1ej11xSs6SYkr+eJWAJ
v1eKMoIT7pnTgOy/sWzXcQlDhX+h2ZUsTHMevQBgA00doEN76uoyIlxPzJ75R+2g
UwIDAQAB
-----END PUBLIC KEY-----

Secondary_engine_execution_count.................................. 0
Select_full_join.................................................. 168
Select_full_range_join............................................ 0
Select_range...................................................... 237
Select_range_check................................................ 0
Select_scan....................................................... 6466
Slave_open_temp_tables............................................ 0
Slow_launch_threads............................................... 0
Slow_queries...................................................... 0
Sort_merge_passes................................................. 0
Sort_range........................................................ 0
Sort_rows......................................................... 1585
Sort_scan......................................................... 135
Ssl_accept_renegotiates........................................... 0
Ssl_accepts....................................................... 5
Ssl_callback_cache_hits........................................... 0
Ssl_cipher........................................................ ECDHE-RSA-AES128-GCM-SHA256
Ssl_cipher_list................................................... AES256-SHA:AES128-SHA:DHE-RSA-AES256-SHA:DHE-DSS-AES256-SHA:DHE-RSA-AES128-SHA:DHE-DSS-AES128-SHA:ECDHE-RSA-AES256-GCM-SHA384:ECDHE-ECDSA-AES256-GCM-SHA384:ECDHE-RSA-AES256-SHA384:ECDHE-ECDSA-AES256-SHA384:ECDHE-RSA-AES256-SHA:ECDHE-ECDSA-AES256-SHA:DH-DSS-AES256-GCM-SHA384:DHE-DSS-AES256-GCM-SHA384:DH-RSA-AES256-GCM-SHA384:DHE-RSA-AES256-GCM-SHA384:DHE-RSA-AES256-SHA256:DHE-DSS-AES256-SHA256:DH-RSA-AES256-SHA256:DH-DSS-AES256-SHA256:DH-RSA-AES256-SHA:DH-DSS-AES256-SHA:DHE-RSA-CAMELLIA256-SHA:DHE-DSS-CAMELLIA256-SHA:DH-RSA-CAMELLIA256-SHA:DH-DSS-CAMELLIA256-SHA:ECDH-RSA-AES256-GCM-SHA384:ECDH-ECDSA-AES256-GCM-SHA384:ECDH-RSA-AES256-SHA384:ECDH-ECDSA-AES256-SHA384:ECDH-RSA-AES256-SHA:ECDH-ECDSA-AES256-SHA:AES256-GCM-SHA384:AES256-SHA256:CAMELLIA256-SHA:ECDHE-RSA-AES128-GCM-SHA256:ECDHE-ECDSA-AES128-GCM-SHA256:ECDHE-RSA-AES128-SHA256:ECDHE-ECDSA-AES128-SHA256:ECDHE-RSA-AES128-SHA:ECDHE-ECDSA-AES128-SHA:DH-DSS-AES128-GCM-SHA256:DHE-DSS-AES128-GCM-SHA256:DH-RSA-AES128-GCM-SHA256:DHE-RSA-AES128-GCM-SHA256:DHE-RSA
Ssl_client_connects............................................... 0
Ssl_connect_renegotiates.......................................... 0
Ssl_ctx_verify_depth.............................................. 18446744073709551615
Ssl_ctx_verify_mode............................................... 5
Ssl_default_timeout............................................... 7200
Ssl_finished_accepts.............................................. 5
Ssl_finished_connects............................................. 0
Ssl_server_not_after.............................................. Aug 22 17:08:50 2024 GMT
Ssl_server_not_before............................................. Dec 18 12:28:13 2021 GMT
Ssl_session_cache_hits............................................ 0
Ssl_session_cache_misses.......................................... 5
Ssl_session_cache_mode............................................ SERVER
Ssl_session_cache_overflows....................................... 0
Ssl_session_cache_size............................................ 128
Ssl_session_cache_timeouts........................................ 0
Ssl_sessions_reused............................................... 0
Ssl_used_session_cache_entries.................................... 0
Ssl_verify_depth.................................................. 18446744073709551615
Ssl_verify_mode................................................... 5
Ssl_version....................................................... TLSv1.2
Table_locks_immediate............................................. 537
Table_locks_waited................................................ 0
Table_open_cache_hits............................................. 7998
Table_open_cache_misses........................................... 182
Table_open_cache_overflows........................................ 0
Tc_log_max_pages_used............................................. 0
Tc_log_page_size.................................................. 0
Tc_log_page_waits................................................. 0
Threads_cached.................................................... 0
Threads_connected................................................. 8
Threads_created................................................... 6
Threads_running................................................... 1
Uptime............................................................ 4759
Uptime_since_flush_status......................................... 4759
aurora_tuple_storage_mode......................................... DISABLED
server_audit_active............................................... OFF
server_audit_last_error........................................... 
server_audit_writes_failed........................................ 0
server_aurora_das_messages_missed................................. 0
server_aurora_das_messages_queued................................. 0
server_aurora_das_num_fatal_errors................................ 0
server_aurora_das_running......................................... OFF

GLOBAL VARIABLES:
activate_all_roles_on_login....................................... OFF
admin_address..................................................... 
admin_port........................................................ 33062
admin_ssl_ca...................................................... 
admin_ssl_capath.................................................. 
admin_ssl_cert.................................................... 
admin_ssl_cipher.................................................. 
admin_ssl_crl..................................................... 
admin_ssl_crlpath................................................. 
admin_ssl_key..................................................... 
admin_tls_ciphersuites............................................ 
admin_tls_version................................................. TLSv1,TLSv1.1,TLSv1.2
aurora_backtrace_dedupe_string_filename........................... backtrace_dedupe_strings.txt
aurora_binlog_reserved_event_bytes................................ 1024
aurora_das_persistence_threads.................................... 0
aurora_disable_lambda_natives..................................... OFF
aurora_enable_emergency_volume_growth............................. OFF
aurora_enable_repl_bin_log_filtering.............................. ON
aurora_enable_staggered_replica_restart........................... OFF
aurora_full_double_precision_in_json.............................. OFF
aurora_fwd_master_idle_timeout.................................... 60
aurora_fwd_master_max_connections_pct............................. 10
aurora_fwd_writer_idle_timeout.................................... 60
aurora_fwd_writer_max_connections_pct............................. 10
aurora_ignore_default_storage_engine_errors....................... OFF
aurora_load_from_s3_role.......................................... 
aurora_max_connections_limit...................................... 16000
aurora_oom_response............................................... 
aurora_parallel_query............................................. OFF
aurora_performance_schema_sql_info_max_size....................... 1024
aurora_pq_force................................................... OFF
aurora_read_replica_read_committed................................ OFF
aurora_replica_read_consistency................................... 
aurora_s3_chunk_size.............................................. 10485760
aurora_s3_upload_file_size_threshold.............................. 6442450944
aurora_s3_upload_iocache_chunk_size............................... 0
aurora_s3_upload_stream_chunk_size................................ 10485760
aurora_select_into_s3_encryption_default.......................... OFF
aurora_select_into_s3_role........................................ 
aurora_server_id.................................................. database-1-instance-1-eu-west-1b
aurora_use_key_prefetch........................................... ON
aurora_version.................................................... 3.01.0
auto_generate_certs............................................... ON
auto_increment_increment.......................................... 1
auto_increment_offset............................................. 1
autocommit........................................................ ON
automatic_sp_privileges........................................... ON
avoid_temporal_upgrade............................................ OFF
aws_default_comprehend_role....................................... 
aws_default_lambda_role........................................... 
aws_default_s3_role............................................... 
aws_default_sagemaker_role........................................ 
awsauthenticationplugin_max_backoff_delay......................... 2000
awsauthenticationplugin_max_retry_count........................... 3
awsauthenticationplugin_retry_delay............................... 250
back_log.......................................................... 90
basedir........................................................... /rdsdbbin/oscar-8.0.mysql_aurora.3.01.0.0.9430.0/
big_tables........................................................ OFF
bind_address...................................................... *
binlog_cache_size................................................. 32768
binlog_checksum................................................... CRC32
binlog_direct_non_transactional_updates........................... OFF
binlog_encryption................................................. OFF
binlog_error_action............................................... ABORT_SERVER
binlog_expire_logs_seconds........................................ 0
binlog_format..................................................... ROW
binlog_group_commit_sync_delay.................................... 0
binlog_group_commit_sync_no_delay_count........................... 0
binlog_gtid_simple_recovery....................................... ON
binlog_max_flush_queue_time....................................... 0
binlog_order_commits.............................................. ON
binlog_rotate_encryption_master_key_at_startup.................... OFF
binlog_row_event_max_size......................................... 8192
binlog_row_image.................................................. FULL
binlog_row_metadata............................................... MINIMAL
binlog_row_value_options.......................................... 
binlog_rows_query_log_events...................................... OFF
binlog_stmt_cache_size............................................ 32768
binlog_transaction_compression.................................... OFF
binlog_transaction_compression_level_zstd......................... 3
binlog_transaction_dependency_history_size........................ 25000
binlog_transaction_dependency_tracking............................ COMMIT_ORDER
block_encryption_mode............................................. aes-128-ecb
bulk_insert_buffer_size........................................... 8388608
caching_sha2_password_auto_generate_rsa_keys...................... ON
caching_sha2_password_private_key_path............................ private_key.pem
caching_sha2_password_public_key_path............................. public_key.pem
character_set_client.............................................. utf8mb4
character_set_connection.......................................... utf8mb4
character_set_database............................................ utf8mb4
character_set_filesystem.......................................... binary
character_set_results............................................. utf8mb4
character_set_server.............................................. utf8mb4
character_set_system.............................................. utf8
character_sets_dir................................................ /rdsdbbin/oscar-8.0.mysql_aurora.3.01.0.0.9430.0/share/charsets/
check_proxy_users................................................. OFF
collation_connection.............................................. utf8mb4_0900_ai_ci
collation_database................................................ utf8mb4_0900_ai_ci
collation_server.................................................. utf8mb4_0900_ai_ci
completion_type................................................... NO_CHAIN
concurrent_insert................................................. AUTO
connect_timeout................................................... 10
core_file......................................................... ON
create_admin_listener_thread...................................... OFF
cte_max_recursion_depth........................................... 1000
datadir........................................................... /rdsdbdata/db/
default_authentication_plugin..................................... mysql_native_password
default_collation_for_utf8mb4..................................... utf8mb4_0900_ai_ci
default_password_lifetime......................................... 0
default_storage_engine............................................ InnoDB
default_tmp_storage_engine........................................ MyISAM
default_week_format............................................... 0
delay_key_write................................................... ON
delayed_insert_limit.............................................. 100
delayed_insert_timeout............................................ 300
delayed_queue_size................................................ 1000
disabled_storage_engines.......................................... 
disconnect_on_expired_password.................................... ON
div_precision_increment........................................... 4
end_markers_in_json............................................... OFF
enforce_gtid_consistency.......................................... OFF
eq_range_index_dive_limit......................................... 200
event_scheduler................................................... DISABLED
expire_logs_days.................................................. 0
explicit_defaults_for_timestamp................................... ON
external_log_file................................................. /tmp/mysql-external.log
flush............................................................. OFF
flush_time........................................................ 0
foreign_key_checks................................................ ON
ft_boolean_syntax................................................. + -><()~*:""&|
ft_max_word_len................................................... 84
ft_min_word_len................................................... 4
ft_query_expansion_limit.......................................... 20
ft_stopword_file.................................................. (built-in)
general_log....................................................... OFF
general_log_file.................................................. /rdsdbdata/log/general/mysql-general.log
generated_random_password_length.................................. 20
group_concat_max_len.............................................. 1024
group_replication_consistency..................................... EVENTUAL
gtid_executed..................................................... 
gtid_executed_compression_period.................................. 0
gtid_mode......................................................... OFF_PERMISSIVE
gtid_owned........................................................ 
gtid_purged....................................................... 
have_compress..................................................... YES
have_dynamic_loading.............................................. YES
have_geometry..................................................... YES
have_openssl...................................................... YES
have_profiling.................................................... YES
have_query_cache.................................................. NO
have_rtree_keys................................................... YES
have_ssl.......................................................... YES
have_statement_timeout............................................ YES
have_symlink...................................................... DISABLED
histogram_generation_max_mem_size................................. 20000000
host_cache_size................................................... 218
hostname.......................................................... ip-172-20-2-107
information_schema_stats_expiry................................... 86400
init_connect...................................................... 
init_file......................................................... 
init_replica...................................................... 
init_slave........................................................ 
innodb_adaptive_flushing.......................................... ON
innodb_adaptive_flushing_lwm...................................... 10
innodb_adaptive_hash_index........................................ OFF
innodb_adaptive_hash_index_parts.................................. 8
innodb_adaptive_max_sleep_delay................................... 150000
innodb_api_bk_commit_interval..................................... 5
innodb_api_disable_rowlock........................................ OFF
innodb_api_enable_binlog.......................................... OFF
innodb_api_enable_mdl............................................. OFF
innodb_api_trx_level.............................................. 0
innodb_aurora_enable_auto_akp..................................... OFF
innodb_autoextend_increment....................................... 64
innodb_autoinc_lock_mode.......................................... 2
innodb_buffer_pool_chunk_size..................................... 790626304
innodb_buffer_pool_dump_at_shutdown............................... OFF
innodb_buffer_pool_dump_now....................................... OFF
innodb_buffer_pool_dump_pct....................................... 25
innodb_buffer_pool_filename....................................... ib_buffer_pool
innodb_buffer_pool_in_core_file................................... ON
innodb_buffer_pool_instances...................................... 2
innodb_buffer_pool_load_abort..................................... OFF
innodb_buffer_pool_load_at_startup................................ OFF
innodb_buffer_pool_load_now....................................... OFF
innodb_buffer_pool_size........................................... 1581252608
innodb_change_buffer_max_size..................................... 25
innodb_change_buffering........................................... none
innodb_checksum_algorithm......................................... none
innodb_cleanup_temp_tablespaces_in_background..................... ON
innodb_cmp_per_index_enabled...................................... OFF
innodb_commit_concurrency......................................... 0
innodb_compression_failure_threshold_pct.......................... 5
innodb_compression_level.......................................... 6
innodb_compression_pad_pct_max.................................... 50
innodb_concurrency_tickets........................................ 5000
innodb_data_file_path............................................. ibdata1:12M:autoextend
innodb_data_home_dir.............................................. 
innodb_deadlock_detect............................................ ON
innodb_dedicated_server........................................... OFF
innodb_default_row_format......................................... dynamic
innodb_directories................................................ 
innodb_disable_shm_reads.......................................... OFF
innodb_disable_sort_file_cache.................................... OFF
innodb_doublewrite................................................ OFF
innodb_doublewrite_batch_size..................................... 0
innodb_doublewrite_dir............................................ 
innodb_doublewrite_files.......................................... 0
innodb_doublewrite_pages.......................................... 0
innodb_extend_and_initialize...................................... OFF
innodb_fast_shutdown.............................................. 1
innodb_file_per_table............................................. ON
innodb_fill_factor................................................ 100
innodb_flush_log_at_timeout....................................... 1
innodb_flush_log_at_trx_commit.................................... 1
innodb_flush_method............................................... O_DIRECT
innodb_flush_neighbors............................................ 0
innodb_flush_sync................................................. ON
innodb_flushing_avg_loops......................................... 30
innodb_force_load_corrupted....................................... OFF
innodb_force_recovery............................................. 0
innodb_fsync_threshold............................................ 0
innodb_ft_aux_table............................................... 
innodb_ft_cache_size.............................................. 8000000
innodb_ft_enable_diag_print....................................... OFF
innodb_ft_enable_stopword......................................... ON
innodb_ft_max_token_size.......................................... 84
innodb_ft_min_token_size.......................................... 3
innodb_ft_num_word_optimize....................................... 2000
innodb_ft_result_cache_limit...................................... 2000000000
innodb_ft_server_stopword_table................................... 
innodb_ft_sort_pll_degree......................................... 2
innodb_ft_total_cache_size........................................ 640000000
innodb_ft_user_stopword_table..................................... 
innodb_idle_flush_pct............................................. 100
innodb_io_capacity................................................ 200
innodb_io_capacity_max............................................ 2000
innodb_lock_wait_timeout.......................................... 50
innodb_log_buffer_size............................................ 16777216
innodb_log_checksums.............................................. ON
innodb_log_compressed_pages....................................... ON
innodb_log_file_size.............................................. 50331648
innodb_log_files_in_group......................................... 2
innodb_log_group_home_dir......................................... ./
innodb_log_spin_cpu_abs_lwm....................................... 80
innodb_log_spin_cpu_pct_hwm....................................... 50
innodb_log_wait_for_flush_spin_hwm................................ 400
innodb_log_write_ahead_size....................................... 8192
innodb_log_writer_threads......................................... ON
innodb_lru_scan_depth............................................. 1024
innodb_max_dirty_pages_pct........................................ 90.000000
innodb_max_dirty_pages_pct_lwm.................................... 10.000000
innodb_max_purge_lag.............................................. 0
innodb_max_purge_lag_delay........................................ 0
innodb_max_undo_log_size.......................................... 1073741824
innodb_monitor_disable............................................ 
innodb_monitor_enable............................................. 
innodb_monitor_reset.............................................. 
innodb_monitor_reset_all.......................................... 
innodb_old_blocks_pct............................................. 37
innodb_old_blocks_time............................................ 1000
innodb_online_alter_log_max_size.................................. 134217728
innodb_open_files................................................. 1788
innodb_optimize_fulltext_only..................................... OFF
innodb_page_cleaners.............................................. 2
innodb_page_size.................................................. 16384
innodb_parallel_read_threads...................................... 4
innodb_print_all_deadlocks........................................ OFF
innodb_print_ddl_logs............................................. OFF
innodb_purge_batch_size........................................... 600
innodb_purge_rseg_truncate_frequency.............................. 128
innodb_purge_threads.............................................. 1
innodb_random_read_ahead.......................................... OFF
innodb_read_ahead_threshold....................................... 56
innodb_read_io_threads............................................ 1
innodb_read_only.................................................. ON
innodb_redo_log_archive_dirs...................................... 
innodb_redo_log_encrypt........................................... OFF
innodb_replication_delay.......................................... 0
innodb_rollback_on_timeout........................................ OFF
innodb_rollback_segments.......................................... 128
innodb_shared_buffer_pool_uses_huge_pages......................... ON
innodb_sort_buffer_size........................................... 1048576
innodb_spin_wait_delay............................................ 6
innodb_spin_wait_pause_multiplier................................. 50
innodb_stats_auto_recalc.......................................... ON
innodb_stats_include_delete_marked................................ OFF
innodb_stats_method............................................... nulls_equal
innodb_stats_on_metadata.......................................... OFF
innodb_stats_persistent........................................... ON
innodb_stats_persistent_sample_pages.............................. 20
innodb_stats_transient_sample_pages............................... 8
innodb_status_output.............................................. OFF
innodb_status_output_locks........................................ OFF
innodb_strict_mode................................................ ON
innodb_sync_array_size............................................ 1
innodb_sync_spin_loops............................................ 30
innodb_table_locks................................................ ON
innodb_temp_data_file_path........................................ ibtmp1:12M:autoextend
innodb_temp_tablespaces_dir....................................... ./
innodb_thread_concurrency......................................... 0
innodb_thread_sleep_delay......................................... 10000
innodb_tmpdir..................................................... 
innodb_undo_directory............................................. ./
innodb_undo_log_encrypt........................................... OFF
innodb_undo_log_truncate.......................................... OFF
innodb_undo_tablespaces........................................... 2
innodb_use_native_aio............................................. OFF
innodb_validate_tablespace_paths.................................. OFF
innodb_version.................................................... 8.0.23
innodb_write_io_threads........................................... 4
interactive_timeout............................................... 28800
internal_tmp_mem_storage_engine................................... TempTable
join_buffer_size.................................................. 262144
keep_files_on_create.............................................. OFF
key_buffer_size................................................... 16777216
key_cache_age_threshold........................................... 300
key_cache_block_size.............................................. 1024
key_cache_division_limit.......................................... 100
keyring_operations................................................ ON
large_files_support............................................... ON
large_page_size................................................... 0
large_pages....................................................... OFF
lc_messages....................................................... en_US
lc_messages_dir................................................... /rdsdbbin/oscar-8.0.mysql_aurora.3.01.0.0.9430.0/share/
lc_time_names..................................................... en_US
license........................................................... GPL
local_infile...................................................... ON
lock_wait_timeout................................................. 31536000
locked_in_memory.................................................. OFF
log_bin........................................................... OFF
log_bin_basename.................................................. 
log_bin_index..................................................... 
log_bin_trust_function_creators................................... OFF
log_bin_use_v1_row_events......................................... OFF
log_error......................................................... /rdsdbdata/log/error/mysql-error.log
log_error_services................................................ log_filter_internal; log_sink_internal
log_error_suppression_list........................................ 
log_error_verbosity............................................... 3
log_output........................................................ FILE
log_queries_not_using_indexes..................................... OFF
log_raw........................................................... OFF
log_replica_updates............................................... OFF
log_slave_updates................................................. OFF
log_slow_admin_statements......................................... OFF
log_slow_extra.................................................... OFF
log_slow_replica_statements....................................... OFF
log_slow_slave_statements......................................... OFF
log_statements_unsafe_for_binlog.................................. ON
log_throttle_queries_not_using_indexes............................ 0
log_timestamps.................................................... UTC
long_query_time................................................... 10.000000
low_priority_updates.............................................. OFF
lower_case_file_system............................................ OFF
lower_case_table_names............................................ 0
mandatory_roles................................................... 
master_info_repository............................................ TABLE
master_verify_checksum............................................ OFF
max_allowed_packet................................................ 67108864
max_binlog_cache_size............................................. 18446744073709547520
max_binlog_size................................................... 134217728
max_binlog_stmt_cache_size........................................ 18446744073709547520
max_connect_errors................................................ 100
max_connections................................................... 90
max_delayed_threads............................................... 20
max_digest_length................................................. 1024
max_error_count................................................... 1024
max_execution_time................................................ 0
max_heap_table_size............................................... 16777216
max_insert_delayed_threads........................................ 20
max_join_size..................................................... 18446744073709551615
max_length_for_sort_data.......................................... 4096
max_points_in_geometry............................................ 65536
max_prepared_stmt_count........................................... 16382
max_relay_log_size................................................ 0
max_seeks_for_key................................................. 18446744073709551615
max_sort_length................................................... 1024
max_sp_recursion_depth............................................ 0
max_user_connections.............................................. 0
max_write_lock_count.............................................. 18446744073709551615
min_examined_row_limit............................................ 0
myisam_data_pointer_size.......................................... 6
myisam_max_sort_file_size......................................... 9223372036853727232
myisam_mmap_size.................................................. 18446744073709551615
myisam_recover_options............................................ OFF
myisam_repair_threads............................................. 1
myisam_sort_buffer_size........................................... 8388608
myisam_stats_method............................................... nulls_unequal
myisam_use_mmap................................................... OFF
mysql_native_password_proxy_users................................. OFF
net_buffer_length................................................. 16384
net_read_timeout.................................................. 30
net_retry_count................................................... 10
net_write_timeout................................................. 60
new............................................................... OFF
ngram_token_size.................................................. 2
offline_mode...................................................... OFF
old............................................................... OFF
old_alter_table................................................... OFF
open_files_limit.................................................. 65535
optimizer_prune_level............................................. 1
optimizer_search_depth............................................ 62
optimizer_switch.................................................. index_merge=on,index_merge_union=on,index_merge_sort_union=on,index_merge_intersection=on,engine_condition_pushdown=on,index_condition_pushdown=on,mrr=on,mrr_cost_based=on,block_nested_loop=on,batched_key_access=off,materialization=on,semijoin=on,loosescan=on,firstmatch=on,duplicateweedout=on,subquery_materialization_cost_based=on,use_index_extensions=on,condition_fanout_filter=on,derived_merge=on,use_invisible_indexes=off,skip_scan=on,hash_join=on,subquery_to_derived=off,prefer_ordering_index=on,hypergraph_optimizer=off,derived_condition_pushdown=on
optimizer_trace................................................... enabled=off,one_line=off
optimizer_trace_features.......................................... greedy_search=on,range_optimizer=on,dynamic_range=on,repeated_subselect=on
optimizer_trace_limit............................................. 1
optimizer_trace_max_mem_size...................................... 1048576
optimizer_trace_offset............................................ -1
parser_max_mem_size............................................... 18446744073709551615
partial_revokes................................................... OFF
password_history.................................................. 0
password_require_current.......................................... OFF
password_reuse_interval........................................... 0
performance_schema................................................ OFF
performance_schema__auto__........................................ OFF
performance_schema_accounts_size.................................. 0
performance_schema_digests_size................................... 0
performance_schema_error_size..................................... 4880
performance_schema_events_stages_history_long_size................ 0
performance_schema_events_stages_history_size..................... 0
performance_schema_events_statements_history_long_size............ 0
performance_schema_events_statements_history_size................. 0
performance_schema_events_transactions_history_long_size.......... 0
performance_schema_events_transactions_history_size............... 0
performance_schema_events_waits_history_long_size................. 0
performance_schema_events_waits_history_size...................... 0
performance_schema_hosts_size..................................... 0
performance_schema_max_cond_classes............................... 0
performance_schema_max_cond_instances............................. 0
performance_schema_max_digest_length.............................. 0
performance_schema_max_digest_sample_age.......................... 60
performance_schema_max_file_classes............................... 0
performance_schema_max_file_handles............................... 0
performance_schema_max_file_instances............................. 0
performance_schema_max_index_stat................................. 0
performance_schema_max_memory_classes............................. 0
performance_schema_max_metadata_locks............................. 0
performance_schema_max_mutex_classes.............................. 0
performance_schema_max_mutex_instances............................ 0
performance_schema_max_prepared_statements_instances.............. 0
performance_schema_max_program_instances.......................... 0
performance_schema_max_rwlock_classes............................. 0
performance_schema_max_rwlock_instances........................... 0
performance_schema_max_socket_classes............................. 0
performance_schema_max_socket_instances........................... 0
performance_schema_max_sql_text_length............................ 0
performance_schema_max_stage_classes.............................. 0
performance_schema_max_statement_classes.......................... 0
performance_schema_max_statement_stack............................ 0
performance_schema_max_table_handles.............................. 0
performance_schema_max_table_instances............................ 0
performance_schema_max_table_lock_stat............................ 0
performance_schema_max_thread_classes............................. 0
performance_schema_max_thread_instances........................... 0
performance_schema_session_connect_attrs_size..................... 0
performance_schema_setup_actors_size.............................. 0
performance_schema_setup_objects_size............................. 0
performance_schema_show_processlist............................... OFF
performance_schema_users_size..................................... 0
persist_only_admin_x509_subject................................... 
persisted_globals_load............................................ ON
pid_file.......................................................... /rdsdbdata/log/mysql-3306.pid
plugin_dir........................................................ /rdsdbbin/oscar-8.0.mysql_aurora.3.01.0.0.9430.0/lib/plugin/
port.............................................................. 3306
preload_buffer_size............................................... 32768
print_identified_with_as_hex...................................... OFF
profiling......................................................... OFF
profiling_history_size............................................ 15
protocol_compression_algorithms................................... zlib,zstd,uncompressed
protocol_version.................................................. 10
query_alloc_block_size............................................ 8192
query_prealloc_size............................................... 8192
range_alloc_block_size............................................ 4096
range_optimizer_max_mem_size...................................... 8388608
rbr_exec_mode..................................................... STRICT
read_buffer_size.................................................. 262144
read_only......................................................... OFF
read_rnd_buffer_size.............................................. 524288
regexp_stack_limit................................................ 8000000
regexp_time_limit................................................. 32
relay_log......................................................... /rdsdbdata/log/relaylog/relaylog
relay_log_basename................................................ /rdsdbdata/log/relaylog/relaylog
relay_log_index................................................... /rdsdbdata/log/relaylog/relaylog.index
relay_log_info_file............................................... relay-log.info
relay_log_info_repository......................................... TABLE
relay_log_purge................................................... ON
relay_log_recovery................................................ OFF
relay_log_space_limit............................................. 1000000000
replica_allow_batching............................................ OFF
replica_checkpoint_group.......................................... 512
replica_checkpoint_period......................................... 300
replica_compressed_protocol....................................... OFF
replica_exec_mode................................................. STRICT
replica_load_tmpdir............................................... /rdsdbdata/tmp/
replica_max_allowed_packet........................................ 1073741824
replica_net_timeout............................................... 60
replica_parallel_type............................................. DATABASE
replica_parallel_workers.......................................... 0
replica_pending_jobs_size_max..................................... 134217728
replica_preserve_commit_order..................................... OFF
replica_skip_errors............................................... OFF
replica_sql_verify_checksum....................................... ON
replica_transaction_retries....................................... 10
replica_type_conversions.......................................... 
replication_optimize_for_static_plugin_config..................... OFF
replication_sender_observe_commit_only............................ OFF
report_host....................................................... 
report_password................................................... 
report_port....................................................... 3306
report_user....................................................... 
require_secure_transport.......................................... OFF
rpl_read_size..................................................... 5242880
rpl_stop_replica_timeout.......................................... 31536000
rpl_stop_slave_timeout............................................ 31536000
schema_definition_cache........................................... 256
secondary_engine_cost_threshold................................... 100000.000000
secure_file_priv.................................................. /secure_file_priv_dir/
select_into_buffer_size........................................... 131072
select_into_disk_sync............................................. OFF
select_into_disk_sync_delay....................................... 0
server_audit_cw_upload............................................ OFF
server_audit_events............................................... 
server_audit_excl_users........................................... 
server_audit_incl_users........................................... 
server_audit_logging.............................................. OFF
server_audit_mode................................................. 0
server_audit_query_log_limit...................................... 65536
server_id......................................................... 0
server_id_bits.................................................... 32
server_uuid....................................................... 49fe17b6-426c-3adb-9aa6-e21ae9f35082
session_track_gtids............................................... OFF
session_track_schema.............................................. ON
session_track_state_change........................................ OFF
session_track_system_variables.................................... time_zone,autocommit,character_set_client,character_set_results,character_set_connection
session_track_transaction_info.................................... OFF
sha256_password_auto_generate_rsa_keys............................ ON
sha256_password_private_key_path.................................. private_key.pem
sha256_password_proxy_users....................................... OFF
sha256_password_public_key_path................................... public_key.pem
show_create_table_verbosity....................................... OFF
show_old_temporals................................................ OFF
skip_external_locking............................................. ON
skip_name_resolve................................................. ON
skip_networking................................................... OFF
skip_show_database................................................ OFF
slave_allow_batching.............................................. OFF
slave_checkpoint_group............................................ 512
slave_checkpoint_period........................................... 300
slave_compressed_protocol......................................... OFF
slave_exec_mode................................................... STRICT
slave_load_tmpdir................................................. /rdsdbdata/tmp/
slave_max_allowed_packet.......................................... 1073741824
slave_net_timeout................................................. 60
slave_parallel_type............................................... DATABASE
slave_parallel_workers............................................ 0
slave_pending_jobs_size_max....................................... 134217728
slave_preserve_commit_order....................................... OFF
slave_rows_search_algorithms...................................... INDEX_SCAN,HASH_SCAN
slave_skip_errors................................................. OFF
slave_sql_verify_checksum......................................... ON
slave_transaction_retries......................................... 10
slave_type_conversions............................................ 
slow_launch_time.................................................. 2
slow_query_log.................................................... OFF
slow_query_log_file............................................... /rdsdbdata/log/slowquery/mysql-slowquery.log
socket............................................................ /tmp/mysql.sock
sort_buffer_size.................................................. 262144
source_verify_checksum............................................ OFF
sql_auto_is_null.................................................. OFF
sql_big_selects................................................... ON
sql_buffer_result................................................. OFF
sql_log_off....................................................... OFF
sql_mode.......................................................... 
sql_notes......................................................... ON
sql_quote_show_create............................................. ON
sql_replica_skip_counter.......................................... 0
sql_require_primary_key........................................... OFF
sql_safe_updates.................................................. OFF
sql_select_limit.................................................. 18446744073709551615
sql_slave_skip_counter............................................ 0
sql_warnings...................................................... OFF
ssl_ca............................................................ /rdsdbdata/rds-metadata/ca-cert.pem
ssl_capath........................................................ 
ssl_cert.......................................................... /rdsdbdata/rds-metadata/server-cert.pem
ssl_cipher........................................................ AES256-SHA:AES128-SHA:DES-CBC3-SHA:ADH-DES-CBC3-SHA:EDH-RSA-DES-CBC3-SHA:EDH-DSS-DES-CBC3-SHA:ADH-AES256-SHA:DHE-RSA-AES256-SHA:DHE-DSS-AES256-SHA:ADH-AES128-SHA:DHE-RSA-AES128-SHA:DHE-DSS-AES128-SHA:HIGH
ssl_crl........................................................... 
ssl_crlpath....................................................... 
ssl_fips_mode..................................................... OFF
ssl_key........................................................... /rdsdbdata/rds-metadata/server-key.pem
stored_program_cache.............................................. 256
stored_program_definition_cache................................... 256
super_read_only................................................... OFF
sync_binlog....................................................... 1
sync_master_info.................................................. 10000
sync_relay_log.................................................... 10000
sync_relay_log_info............................................... 10000
sync_source_info.................................................. 10000
system_time_zone.................................................. UTC
table_definition_cache............................................ 5366
table_encryption_privilege_check.................................. OFF
table_open_cache.................................................. 1788
table_open_cache_instances........................................ 4
tablespace_definition_cache....................................... 256
temptable_max_mmap................................................ 1073741824
temptable_max_ram................................................. 1073741824
temptable_use_mmap................................................ ON
thread_cache_size................................................. 2
thread_handling................................................... thread-pools
thread_stack...................................................... 262144
time_zone......................................................... SYSTEM
tls_ciphersuites.................................................. 
tls_version....................................................... TLSv1,TLSv1.1,TLSv1.2
tmp_table_size.................................................... 16777216
tmpdir............................................................ /rdsdbdata/tmp/
transaction_alloc_block_size...................................... 8192
transaction_isolation............................................. REPEATABLE-READ
transaction_prealloc_size......................................... 4096
transaction_read_only............................................. OFF
transaction_write_set_extraction.................................. XXHASH64
unique_checks..................................................... ON
updatable_views_with_limit........................................ YES
user_disable_external_log......................................... OFF
version........................................................... 8.0.23
version_comment................................................... Source distribution
version_compile_machine........................................... x86_64
version_compile_os................................................ Linux
version_compile_zlib.............................................. 1.2.11
wait_timeout...................................................... 28800
windowing_use_high_precision...................................... ON

*/
