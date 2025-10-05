from datetime import datetime
import os

# Define the filename for the log
log_file = "update_log.txt"

# Get the current time in a readable format
current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S UTC")

# Prepare the content to be written
log_entry = f"File updated at: {current_time}\n"

# Open the file in 'append' mode. If it doesn't exist, it will be created.
try:
    with open(log_file, "a") as f:
        f.write(log_entry)
    print(f"Successfully wrote '{log_entry.strip()}' to {log_file}")

except Exception as e:
    print(f"Error writing to file: {e}")
