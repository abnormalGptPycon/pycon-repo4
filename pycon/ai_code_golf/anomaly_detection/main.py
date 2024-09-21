from typing import Dict, Optional

# Refactored detect_security_alert function that stores user events internally
def detect_security_alert(event_stream):
    # Dictionary to keep track of user login events for each user
    user_attempts = {}

    def check_pattern(events):
        # Check if the last 4 events match the pattern: 3 failures followed by 1 success
        if len(events) < 4:
            return False
        # Check for the pattern
        return (events[-4]['status'] == 'failure' and
                events[-3]['status'] == 'failure' and
                events[-2]['status'] == 'failure' and
                events[-1]['status'] == 'success')

    alerts = []
    
    # Process each event in the stream
    for event in event_stream:
        user_id = event['user_id']
        # Parse the timestamp from ISO 8601 format
        timestamp = datetime.fromisoformat(event['timestamp'].replace('Z', '+00:00'))
        status = event['status']

        # Initialize the deque for the user if not present
        if user_id not in user_attempts:
            user_attempts[user_id] = deque()

        # Append the event to the user's deque
        user_attempts[user_id].append({'timestamp': timestamp, 'status': status})

        # Remove events that are older than 10 minutes from the current event
        while (user_attempts[user_id] and 
               (timestamp - user_attempts[user_id][0]['timestamp']) > timedelta(minutes=10)):
            user_attempts[user_id].popleft()

        # Check if we have detected the pattern for this user
        if check_pattern(user_attempts[user_id]):
            # If pattern is detected, append the alert info
            alerts.append({'user_id': user_id, 'timestamp': event['timestamp']})
        else:
            # If no pattern is detected, append None
            alerts.append(None)

    return alerts




if __name__ == "__main__":
    sample_log_stream = [
        {"user_id": "user0", "timestamp": "2023-09-16T12:00:00+00:00", "status": "failure"},
        {"user_id": "user0", "timestamp": "2023-09-16T12:05:00+00:00", "status": "failure"},
        {"user_id": "user0", "timestamp": "2023-09-16T12:07:00+00:00", "status": "failure"},
        {"user_id": "user0", "timestamp": "2023-09-16T12:08:00+00:00", "status": "success"},
    ]
    sample_expected_output = [
        None,
        None,
        None,
        {"user_id": "user0", "timestamp": "2023-09-16T12:08:00+00:00"},
    ]

    for i, ev in enumerate(sample_log_stream):
        alert = detect_security_alert(ev)
        assert (
            alert == sample_expected_output[i]
        ), f"Expected {sample_expected_output[i]}, but got {alert}"

    print("Passed sanity check!")
