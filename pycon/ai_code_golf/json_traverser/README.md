## JSON Traverser

### Description

Write a Python function that retrieves the value from a nested JSON object given a specific path. The path is a string that specifies the keys and indices to traverse, using dot notation for keys and square brackets `[]` for list indices.

**Path Notation:**

- **Keys**:
  - Accessed using dot notation: `'key1.key2'`.
  - If a key contains dots `.` or brackets `[]`, enclose it in single or double quotes: `'key1."key.with.dots".key2'` or `"key1.'key.with.dots'.key2"`.
  - Backslashes `\` can be used to escape dots and brackets: `'key1.key\.with\.dots.key2'`.

- **Indices**:
  - Accessed using square brackets: `'list_key[0]'`.
  - Indices can be integers or negative integers (for reverse indexing).

- **Combining Keys and Indices**:
  - Any combination is allowed: `'key1.list_key[0].key2'`.

**Requirements:**
- **Error Handling**:
  - If a key or index does not exist, raise a `KeyError`.
  - If an index is out of range, raise an `IndexError`.

### Examples

```python
# Example 1: Simple Nested Keys
json_obj = {"a": {"b": {"c": 42}}}
path = "a.b.c"
output = 42
```

```python
# Example 2: List Indexing
json_obj = {"a": [1, 2, {"b": [3, 4]}]}
path = "a[2].b[1]"
output = 4
```

```python
# Example 3: Keys with Dots and Brackets
json_obj = {"a.b": {"c[d]": 100}}
path = "a\.b.'c[d]'"
output = 100
```
### Start

1. Populate the `traverse_json` function in `main.py`.
2. ```shell
   bash run.sh
   ```
