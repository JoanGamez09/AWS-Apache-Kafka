from kafka import KafkaProducer
from aws_msk_iam_sasl_signer import MSKAuthTokenProvider
import json

# Topic and broker configuration
topicname = 'mytopic'
BROKERS = 'BROKER-ENDPOINT'
region = 'us-east-1'

# Class to obtain the authentication token
class MSKTokenProvider():
    def token(self):
        token, _ = MSKAuthTokenProvider.generate_auth_token(region)
        return token

tp = MSKTokenProvider()

# Kafka producer configuration
producer = KafkaProducer(
    bootstrap_servers=BROKERS,
    # JSON is used to serialize the message
    value_serializer=lambda v: json.dumps(v).encode('utf-8'),
    retry_backoff_ms=500,
    request_timeout_ms=20000,
    security_protocol='SASL_SSL',
    sasl_mechanism='OAUTHBEARER',
    sasl_oauth_token_provider=tp,
)

# Message to be sent
message = "hello world"

# Sending the message
try:
    future = producer.send(topicname, value=message)
    producer.flush()  # Ensures the message is sent immediately
    record_metadata = future.get(timeout=10)
    print("Message sent:", message)
except Exception as e:
    print("Error sending the message:", e)
