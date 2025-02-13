from kafka import KafkaConsumer
import json
from aws_msk_iam_sasl_signer import MSKAuthTokenProvider

# Topic, brokers, and region configuration
topicname = 'mytopic'
BROKERS = 'BROKER-ENDPOINT'
region = 'us-east-1'

# Definition of the class that generates the authentication token, same as in the producer
class MSKTokenProvider():
    def token(self):
        token, _ = MSKAuthTokenProvider.generate_auth_token(region)
        return token

tp = MSKTokenProvider()

# Consumer configuration
consumer = KafkaConsumer(
    topicname,
    bootstrap_servers=BROKERS,
    auto_offset_reset='earliest',            # Read from the beginning if no offset is committed
    enable_auto_commit=True,                 # Automatically commits offsets
    group_id='my_consumer_group',            # Defines a group ID (modify as needed)
    value_deserializer=lambda m: json.loads(m.decode('utf-8')),  # Deserialize message from JSON to dict
    security_protocol='SASL_SSL',
    sasl_mechanism='OAUTHBEARER',
    sasl_oauth_token_provider=tp,
)

print("Consumer started. Waiting for messages...")

# Infinite loop to read and process messages
try:
    for message in consumer:
        # Each 'message' is an object containing metadata (topic, partition, offset, key, value, etc.)
        print("Message received:")
        print("  Topic:     ", message.topic)
        print("  Partition: ", message.partition)
        print("  Offset:    ", message.offset)
        print("  Value:     ", message.value)
except KeyboardInterrupt:
    print("Consumer interrupted by user.")
finally:
    consumer.close()
