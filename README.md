# AWS-Apache-Kafka

## Overview
This project sets up a Kafka-based messaging system using AWS MSK Serverless. It includes a producer, a consumer, and administrative scripts for managing Kafka topics. Authentication is handled using IAM-based SASL/OAUTHBEARER authentication.

## Prerequisites
Before running the scripts, ensure you have the following:
- **Python 3.11** installed
- **pip** package manager
- **AWS CLI** configured with appropriate permissions
- **Kafka Python Library** (`kafka-python`)
- **AWS MSK IAM SASL Signer** (`aws-msk-iam-sasl-signer`)
- A deployed **AWS MSK Serverless Cluster**

### Install Required Dependencies
Run the following command to install required dependencies:
```sh
pip install kafka-python aws-msk-iam-sasl-signer
```

## Project Structure
- **`holamundo.py`** - Kafka producer script that sends messages.
- **`consumer.py`** - Kafka consumer script that reads messages.
- **`topic.py`** - Script to create a Kafka topic.
- **`delete.py`** - Script to delete a Kafka topic.

## Steps to Execute

### Step 1: Set Up Kafka Topic
Run the topic creation script to ensure the topic exists before producing messages:
```sh
python topic.py
```

### Step 2: Start the Consumer
The consumer listens for messages on the specified topic:
```sh
python consumer.py
```

### Step 3: Send Messages Using the Producer
Run the producer to send messages:
```sh
python holamundo.py
```

## Expected Outputs
- **Producer (`holamundo.py`)**:
  ```
  Message sent: hello world
  ```
- **Consumer (`consumer.py`)**:
  ```
  Consumer started. Waiting for messages...
  Message received:
    Topic: mytopic
    Partition: 0
    Offset: 3
    Value: hello world
  ```
- **Topic Creation (`topic.py`)**:
  ```
  Topic has been created
  ```


## Notes
- Ensure your `BROKER-ENDPOINT` is correctly set in each script.
- The authentication method uses AWS IAM-based SASL/OAUTHBEARER.

This project provides a simple and secure way to interact with AWS MSK Serverless using Kafka Python clients.

