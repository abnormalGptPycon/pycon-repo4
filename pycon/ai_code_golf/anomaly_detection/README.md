## Event Pattern Detection in Log Streams

### Description

Write a Python function that processes a stream of login events to detect a specific security-critical pattern:

- **Pattern to Detect:** For any user, detect when there are **three consecutive failed login attempts** followed by a **successful login**, all occurring within a **rolling 10-minute window**.

- **Input Structure:**
  - Each event is a dictionary with the following keys:
    - `'user_id'`: Unique identifier for the user (string).
    - `'timestamp'`: ISO 8601 formatted string with timezone information (e.g., `'2023-10-14T10:00:00Z'`).
    - `'status'`: Either `'success'` or `'failure'`.

Optionally return a message dict, if a given event triggers the pattern, with these keys:
  - `'user_id'`: The affected user's ID.
  - `'timestamp'`: The timestamp of the anomaly (the successful login event that triggered the pattern).

### Examples

```python
# Example 1
log_stream = [
    {'user_id': 'user1', 'timestamp': '2023-09-16T12:07:00+00:00', 'status': 'failure'},
    {'user_id': 'user1', 'timestamp': '2023-09-16T12:08:00+00:00', 'status': 'success'},
    {'user_id': 'user1', 'timestamp': '2023-09-16T12:05:00+00:00', 'status': 'failure'},
    {'user_id': 'user1', 'timestamp': '2023-09-16T12:00:00+00:00', 'status': 'failure'}
]

## output
"""
  None
  None
  None
  {'user_id': 'user1', 'timestamp': '2023-09-16T12:08:00+00:00'}
"""
```

```python
# Example 2
log_stream = [
    {'user_id': 'user4', 'timestamp': '2023-09-16T14:00:00+00:00', 'status': 'failure'},
    {'user_id': 'user5', 'timestamp': '2023-09-16T14:01:00+00:00', 'status': 'failure'},
    {'user_id': 'user4', 'timestamp': '2023-09-16T14:05:00+00:00', 'status': 'failure'},
    {'user_id': 'user5', 'timestamp': '2023-09-16T14:06:00+00:00', 'status': 'failure'},
    {'user_id': 'user4', 'timestamp': '2023-09-16T14:07:00+00:00', 'status': 'failure'},
    {'user_id': 'user5', 'timestamp': '2023-09-16T14:09:00+00:00', 'status': 'failure'},
    {'user_id': 'user4', 'timestamp': '2023-09-16T14:08:00+00:00', 'status': 'success'},
    {'user_id': 'user5', 'timestamp': '2023-09-16T14:10:00+00:00', 'status': 'success'},
    {'user_id': 'user5', 'timestamp': '2023-09-16T14:11:00+00:00', 'status': 'success'},
]

## output
"""
  None
  None
  None
  None
  None
  None
  {'user_id': 'user4', 'timestamp': '2023-09-16T14:08:00+00:00'}
  {'user_id': 'user5', 'timestamp': '2023-09-16T14:10:00+00:00'}
  None
"""
```


### Start

1. Populate the `detect_security_alert` function in `main.py`.
2. ```shell
   bash run.sh
   ```
