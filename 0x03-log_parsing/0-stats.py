#!/usr/bin/python3
"""Log parsing module."""
import sys
import signal

# Initialize global variables
total_size = 0
status_counts = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}
line_count = 0

def print_stats():
    """Function to print the current statistics."""
    global total_size, status_counts
    print(f"File size: {total_size}")
    for code in sorted(status_counts):
        if status_counts[code] > 0:
            print(f"{code}: {status_counts[code]}")

def signal_handler(sig, frame):
    """Handle the interrupt signal (CTRL + C) to print stats."""
    print_stats()
    sys.exit(0)

# Register the signal handler
signal.signal(signal.SIGINT, signal_handler)

# Read stdin line by line
try:
    for line in sys.stdin:
        try:
            parts = line.split()
            if len(parts) < 7:
                continue
            
            ip = parts[0]
            dash = parts[1]
            date = parts[3]
            request = parts[4]
            status_code = parts[-2]
            file_size = parts[-1]

            if request != '"GET' or parts[5] != '/projects/260' or parts[6] != 'HTTP/1.1"':
                continue

            status_code = int(status_code)
            file_size = int(file_size)

            # Update metrics
            total_size += file_size
            if status_code in status_counts:
                status_counts[status_code] += 1

            line_count += 1

            if line_count % 10 == 0:
                print_stats()

        except ValueError:
            # Skip lines with improper formats
            continue

except KeyboardInterrupt:
    print_stats()
    sys.exit(0)
