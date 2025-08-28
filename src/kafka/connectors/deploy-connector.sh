#!/bin/bash

# --- Script to register connectors in Kafka Connect from JSON files ---

# Kafka Connect API endpoint
CONNECT_URL="http://localhost:8083/connectors"

# File names for the connector configurations
SOURCE_CONNECTOR_FILE="sources/debezium-source.json"
SINK_CONNECTOR_FILE="sinks/postgres-sink.json"

# --- Create connectors by posting the JSON files ---
echo "--- DEBUG: Printing content of $SOURCE_CONNECTOR_FILE before sending ---"
cat "$SOURCE_CONNECTOR_FILE"
echo "--- END DEBUG ---"
echo "⚙️  Creating Debezium Source connector from $SOURCE_CONNECTOR_FILE..."
curl -i -X POST -H "Content-Type:application/json" --data "@$SOURCE_CONNECTOR_FILE" $CONNECT_URL

# Newline for better readability
echo -e "\n"

echo "⚙️  Creating JDBC Sink connector from $SINK_CONNECTOR_FILE..."
curl -i -X POST -H "Content-Type:application/json" --data "@$SINK_CONNECTOR_FILE" $CONNECT_URL

echo -e "\n\n✅ Script finished. Check the command output for confirmation (look for 'HTTP/1.1 201 Created')."