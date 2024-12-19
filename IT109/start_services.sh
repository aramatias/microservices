#!/bin/bash

# Function to start a service
start_service() {
    echo "Starting $1 Service..."
    python3 $2 &  # Run the service in the background
    if [ $? -eq 0 ]; then  # Check if the last command was successful
        echo "$1 Service started successfully."
    else
        echo "Failed to start $1 Service."
        exit 1
    fi
}

# Start the Order Management Service
start_service "Order Management" "oms/app.py"

# Start the Inventory Management Service
start_service "Inventory Management" "ims/app.py"

# Keep the script running to keep both services active
wait
