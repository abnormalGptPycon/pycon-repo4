## International Phone Number Extraction

### Description

Write a Python function that extracts all valid international phone numbers from a given text. A valid phone number must meet the following criteria:

- **Country Code**:
  - Starts with an optional `'+'` sign.
  - Followed by 1 to 3 digits (cannot start with zero).

- **Area Code**:
  - Optional and can be enclosed in parentheses `()`.
  - If present, consists of 1 to 5 digits (cannot start with zero).

- **Subscriber Number**:
  - Consists of 4 to 10 digits.
  - May be separated by spaces, dashes `'-'`, dots `'.'`, or no separator.
  - Multiple separators can be mixed.

- **Separators**:
  - The different parts may be separated by spaces, dashes `'-'`, dots `'.'`, or no separator.

**Constraints:**

- The total length of the digits (excluding country code) should be between 7 and 15 digits.
- Ignore invalid numbers where any part (country code, area code, subscriber number) starts with zero.
- The function should return a list of extracted phone numbers in the order they appear in the text.

### Examples

```python
# 1
text = "Call us at +1-800-555-1234 ext123 or +44 20.7946 0958#4567."
output = ['+1-800-555-1234', '+44 20.7946 0958']
```

```python
# 2
text = "Emergency numbers for block 101: (123)4567890, 1001: +91 98765 43210, 80002: +86 10 6552 9988 ext.12345."
output = ['+91 98765 43210', '+86 10 6552 9988']
```

```python
# 3
text = "Invalid numbers: +0123-456-7890, +44 (0)20-7946-0958 x123456"
output = []
```

### Start

1. Populate the `extract_international_phone_numbers` function in `main.py`.
2. ```shell
   bash run.sh
   ```
   





