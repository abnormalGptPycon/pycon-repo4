import pytest
from .main import detect_security_alert


error_cls_map = {
  "KeyError": KeyError,
  "IndexError": IndexError,
}

# Inputs
stream2 = [
  {"user_id": "user2", "timestamp": "2023-09-16T12:00:00+00:00", "status": "failure"},
  {"user_id": "user2", "timestamp": "2023-09-16T12:11:00+00:00", "status": "failure"},
  {"user_id": "user2", "timestamp": "2023-09-16T12:21:00+00:00", "status": "failure"},
  {"user_id": "user2", "timestamp": "2023-09-16T12:22:00+00:00", "status": "success"},
  {"user_id": "user2", "timestamp": "2023-09-16T12:22:00+00:00", "status": "failure"},
  {"user_id": "user2", "timestamp": "2023-09-16T12:23:00+00:00", "status": "failure"},
  {"user_id": "user2", "timestamp": "2023-09-16T12:24:00+00:00", "status": "failure"},
  {"user_id": "user2", "timestamp": "2023-09-16T12:26:00+00:00", "status": "success"},
  {"user_id": "user2", "timestamp": "2023-09-16T12:26:00+00:00", "status": "success"},
]

stream7 = [
  {"user_id": "user9", "timestamp": "2023-09-16T17:00:00+00:00", "status": "success"},
  {"user_id": "user9", "timestamp": "2023-09-16T17:01:00+00:00", "status": "success"},
  {"user_id": "user9", "timestamp": "2023-09-16T17:05:00+00:00", "status": "success"},
  {"user_id": "user9", "timestamp": "2023-09-16T17:07:00+00:00", "status": "success"},
]

stream5 = [
  {"user_id": "user6", "timestamp": "2023-09-16T15:09:00+00:00", "status": "success"},
  {"user_id": "user6", "timestamp": "2023-09-16T15:00:00+00:00", "status": "failure"},
  {"user_id": "user6", "timestamp": "2023-09-16T15:05:00+00:00", "status": "failure"},
  {"user_id": "user7", "timestamp": "2023-09-16T15:11:00+00:00", "status": "success"},
  {"user_id": "user7", "timestamp": "2023-09-16T15:10:00+00:00", "status": "failure"},
  {"user_id": "user7", "timestamp": "2023-09-16T15:09:00+00:00", "status": "failure"},
  {"user_id": "user7", "timestamp": "2023-09-16T15:09:00+00:00", "status": "failure"},
  {"user_id": "user6", "timestamp": "2023-09-16T15:07:00+00:00", "status": "failure"},
]


stream8 = [
  {"user_id": "user10", "timestamp": "2023-09-16T18:00:00+00:00", "status": "failure"},
  {"user_id": "user10", "timestamp": "2023-09-16T18:05:00+00:00", "status": "failure"},
  {"user_id": "user10", "timestamp": "2023-09-16T18:11:00+00:00", "status": "failure"},
  {"user_id": "user10", "timestamp": "2023-09-16T18:12:00+00:00", "status": "success"},
  {"user_id": "user10", "timestamp": "2023-09-16T18:09:00+00:00", "status": "failure"},
]

stream4 = [
  {"user_id": "user4", "timestamp": "2023-09-16T14:00:00+00:00", "status": "failure"},
  {"user_id": "user5", "timestamp": "2023-09-16T14:01:00+00:00", "status": "failure"},
  {"user_id": "user4", "timestamp": "2023-09-16T14:05:00+00:00", "status": "failure"},
  {"user_id": "user5", "timestamp": "2023-09-16T14:06:00+00:00", "status": "failure"},
  {"user_id": "user4", "timestamp": "2023-09-16T14:07:00+00:00", "status": "failure"},
  {"user_id": "user5", "timestamp": "2023-09-16T14:09:00+00:00", "status": "failure"},
  {"user_id": "user4", "timestamp": "2023-09-16T14:08:00+00:00", "status": "success"},
  {"user_id": "user5", "timestamp": "2023-09-16T14:10:00+00:00", "status": "success"},
  {"user_id": "user5", "timestamp": "2023-09-16T14:11:00+00:00", "status": "success"},
]

# Expected outputs
output1 = [None, None, None, {"user_id": "user1", "timestamp": "2023-09-16T12:08:00+00:00"}]
output2 = [
  None,
  None,
  None,
  None,
  None,
  None,
  None,
  {"user_id": "user2", "timestamp": "2023-09-16T12:26:00+00:00"},
  None,
]
output3 = [None, None, None, {"user_id": "user3", "timestamp": "2023-09-16T13:10:00+00:00"}]
output4 = [
  None,
  None,
  None,
  None,
  None,
  None,
  {"user_id": "user4", "timestamp": "2023-09-16T14:08:00+00:00"},
  {"user_id": "user5", "timestamp": "2023-09-16T14:10:00+00:00"},
  None,
]
output5 = [
  None,
  None,
  None,
  None,
  None,
  None,
  {"user_id": "user7", "timestamp": "2023-09-16T15:11:00+00:00"},
  {"user_id": "user6", "timestamp": "2023-09-16T15:09:00+00:00"},
]
output6 = [None, None, None, None, {"user_id": "user8", "timestamp": "2023-09-16T16:08:00+00:00"}]
output7 = [None, None, None, None]
output8 = [None, None, None, None, {"user_id": "user10", "timestamp": "2023-09-16T18:12:00+00:00"}]


def equate(alert1, alert2):
  if not (alert1 and alert2):
    if alert1 or alert2:
      return False
    return True
  return alert1.get("user_id") == alert2.get("user_id") and alert1.get("timestamp") == alert2.get(
    "timestamp"
  )


@pytest.mark.parametrize(
  "stream, expected",
  [
    (stream2, output2),
    (stream4, output4),
    (stream5, output5),
    (stream7, output7),
    (stream8, output8),
  ],
)
def test_extract_phone_numbers(stream, expected):
  for i, ev in enumerate(stream):
    alert = detect_security_alert(ev)
    assert alert == expected[i], f"Expected {expected[i]}, but got {alert}"
