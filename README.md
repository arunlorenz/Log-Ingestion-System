
# Project: Enhanced Log Ingestion and Search System

## Description:

This enhanced log ingestion and search system utilizes Elasticsearch for efficient log storage and retrieval, providing a cmd line interface for searching and filtering logs based on various criteria.

## Features:

- **Enhanced Log Ingestion:** Seamlessly ingests logs in JSON format through an HTTP POST request to port 3000.
- **Robust Search Interface:** Provides a search interface for retrieving specific logs based on various fields, including level, message, resourceId, timestamp, traceId, spanId, commit, and metadata.parentResourceId.
- **Refined Filtering:** Enables filtering search results using multiple criteria to narrow down the search scope effectively.
- **Error Handling:** Handles exceptions gracefully during log ingestion and provides informative error messages.
- **Idempotent Ingestion:** Guarantees idempotent ingestion by checking for the existence of the logs index before creating it.
- **Continuous Ingestion:** Continuously listens for incoming log data through HTTP POST requests, ensuring real-time ingestion.
- **Threading:** Optimizes performance by utilizing threading to handle both log ingestion and user interaction concurrently.

## Installation:

### Install the required dependencies:

1. elasticsearch
2. requests

Create an Elasticsearch index named logs with the appropriate mappings for the log data fields.

## Configuration:

Replace the placeholder values in the code with your own credentials:

- In `server.py`, replace the cloud_id, username, and password in the Elasticsearch client setup with your own credentials.
- In `query.py`, update the Elasticsearch hosts, basic_auth, and other relevant configurations with your own credentials.

## Usage:

### Start the log ingestor:

Run the `server.py` script to start the HTTP server that listens on port 3000 and handles incoming log ingestion requests.

### Ingest logs:

Send HTTP POST requests to `http://localhost:3000/ingest` with JSON payloads containing the log data.

### Search logs:

Access the provided search interface and enter a query, such as "level: error" or "message: Failed to connect".
Use the provided filtering options to narrow down the search results based on specific criteria.

### Sample log ingestion using PowerShell

Invoke-RestMethod -Uri http://localhost:3000/ingest -Method POST -Headers @{"Content-Type"="application/json"} -Body '{"level": "info", "message": "Log message", "resourceId": "server-123", "timestamp": "2023-11-19T12:00:00Z", "traceId": "abc123", "spanId": "span456", "commit": "abcdef", "metadata": {"parentResourceId": "parent-server-123"}}'

# Conclusion:

Thank you for exploring this enhanced log ingestion and search system. Feel free to adapt the provided code by replacing placeholder values with your credentials. This project aims to streamline log management, offering a scalable solution. 

Have a good day ^-^
