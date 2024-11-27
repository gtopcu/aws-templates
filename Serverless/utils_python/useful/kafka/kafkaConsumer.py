# pip install kafka-python
# 
# Create a topic using Kafka's command-line tools
# kafka-topics.sh --create --topic topic-1 --bootstrap-server localhost:9092 --partitions 1 --replication-factor 1
# 
# Press Ctrl+C to stop consuming

from kafka import KafkaConsumer
import json
import sys

# Fix for ModuleNotFoundError: No module named 'kafka.vendor.six.moves' on Python 3.12
# https://stackoverflow.com/questions/77287622/modulenotfounderror-no-module-named-kafka-vendor-six-moves-in-dockerized-djan
# import six
# import sys
# if sys.version_info >= (3, 12, 0):
#     sys.modules['kafka.vendor.six.moves'] = six.moves

def consume_messages_from_kafka(
    topic_name='topic-1', 
    bootstrap_servers=['localhost:9092'],
    consumer_group_id='hello-world-group'
):
    """
    Consume messages from a specified Kafka topic
    
    Args:
        topic_name (str): Name of the Kafka topic to consume from
        bootstrap_servers (list): List of Kafka broker addresses
        consumer_group_id (str): Consumer group identifier
    """
    try:
        # Create a Kafka Consumer
        consumer = KafkaConsumer(
            topic_name,
            bootstrap_servers=bootstrap_servers,
            group_id=consumer_group_id,
            # Auto-commit offsets
            enable_auto_commit=True,
            # Deserialize messages from JSON
            value_deserializer=lambda x: json.loads(x.decode('utf-8')),
            # Start reading from the earliest available message
            auto_offset_reset='earliest'
        )
        
        print(f"Consuming messages from topic: {topic_name}")
        print("Press Ctrl+C to stop consuming...")
        
        # Continuously consume messages
        for message in consumer:
            try:
                # Print message details
                print("\n--- New Message Received ---")
                print(f"Topic: {message.topic}")
                print(f"Partition: {message.partition}")
                print(f"Offset: {message.offset}")
                print(f"Key: {message.key}")
                
                # Parse and print message value
                value = message.value
                print("Message Content:")
                for key, val in value.items():
                    print(f"  {key}: {val}")
                
            except Exception as msg_error:
                print(f"Error processing message: {msg_error}")
    
    except Exception as e:
        print(f"Error setting up Kafka consumer: {e}")
    
    except KeyboardInterrupt:
        print("\nConsumer stopped by user.")
        sys.exit(0)

def main():
    # Kafka configuration (modify as needed)
    KAFKA_BOOTSTRAP_SERVERS = ['localhost:9092']
    KAFKA_TOPIC = 'topic-1'
    CONSUMER_GROUP_ID = 'hello-world-group'
    
    # Start consuming messages
    consume_messages_from_kafka(
        topic_name=KAFKA_TOPIC,
        bootstrap_servers=KAFKA_BOOTSTRAP_SERVERS,
        consumer_group_id=CONSUMER_GROUP_ID
    )

if __name__ == "__main__":
    main()