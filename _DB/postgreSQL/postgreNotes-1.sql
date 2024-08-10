

docker run --name local-db --env-file ./.env -dp 5432:5432 postgres:latest

https://docs.rapidapp.io/blog/streaming-postgresql-changes-to-kafka-with-debezium
docker run --rm --name debezium \
  -e BOOTSTRAP_SERVERS=<bootstrap_servers> \
  -e GROUP_ID=1 \
  -e CONFIG_STORAGE_TOPIC=connect_configs \
  -e OFFSET_STORAGE_TOPIC=connect_offsets \
  -e STATUS_STORAGE_TOPIC=connect_statuses \
  -e ENABLE_DEBEZIUM_SCRIPTING='true' \
  -e CONNECT_SASL_MECHANISM=SCRAM-SHA-256 \
  -e CONNECT_SECURITY_PROTOCOL=SASL_SSL \
  -e CONNECT_SASL_JAAS_CONFIG='org.apache.kafka.common.security.scram.ScramLoginModule required username="<username>" password="<password>";' \
 -p 8083:8083 debezium/connect:2.7