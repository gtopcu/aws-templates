
# pip install kafka-python
# 
# Create a topic using Kafka's command-line tools
# kafka-topics.sh --create --topic topic-1 --bootstrap-server localhost:9092 --partitions 1 --replication-factor 1

from kafka import KafkaProducer
import json
import time

def send_message_to_kafka(topic_name="topic-1", bootstrap_servers=['localhost:9092']):
    """
    Send a 'Hello World' message to a specified Kafka topic
    
    Args:
        topic_name (str): Name of the Kafka topic to send message to
        bootstrap_servers (list): List of Kafka broker addresses
    """
    try:
        # Create a Kafka Producer
        producer = KafkaProducer(
            bootstrap_servers=bootstrap_servers,
            # Optional: Serialize messages to JSON
            value_serializer=lambda v: json.dumps(v).encode('utf-8')
        )
        
        # Message to send
        message = {
            'message': 'Hello World',
            'timestamp': time.time()
        }
        
        # Send message to the topic
        future = producer.send(topic_name, message)
        
        # Block until a single message is sent (optional)
        record_metadata = future.get(timeout=10)
        
        # Print successful send details
        print(f"Message sent successfully!")
        print(f"Topic: {record_metadata.topic}")
        print(f"Partition: {record_metadata.partition}")
        print(f"Offset: {record_metadata.offset}")
        
    except Exception as e:
        print(f"Error sending message to Kafka: {e}")
    
    finally:
        # Close the producer
        producer.close()

def main():
    # Kafka configuration (modify as needed)
    KAFKA_BOOTSTRAP_SERVERS = ['localhost:9092']
    KAFKA_TOPIC = 'topic-1'
    
    # Send the message
    send_message_to_kafka(
        topic_name=KAFKA_TOPIC, 
        bootstrap_servers=KAFKA_BOOTSTRAP_SERVERS
    )

if __name__ == "__main__":
    main()