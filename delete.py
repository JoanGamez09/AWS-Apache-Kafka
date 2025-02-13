from kafka.admin import KafkaAdminClient
from aws_msk_iam_sasl_signer import MSKAuthTokenProvider

# Region where MSK Serverless is deployed
region = 'us-east-1'

# Class to generate the authentication token using MSKAuthTokenProvider
class MSKTokenProvider():
    def token(self):
        token, _ = MSKAuthTokenProvider.generate_auth_token(region)
        return token

# Instance of the token provider
tp = MSKTokenProvider()

# Configuration of KafkaAdminClient with security parameters
admin_client = KafkaAdminClient(
    bootstrap_servers='BROKER-ENDPOINT',
    client_id='admin_client',
    security_protocol='SASL_SSL',
    sasl_mechanism='OAUTHBEARER',
    sasl_oauth_token_provider=tp,
    # Optional: In some cases, it may be necessary to manually specify the API version.
    # api_version=(2, 8, 1)
)

# Deletion of the topic "mytopic"
admin_client.delete_topics(topics=["mytopic"])
print("Topic deleted")

