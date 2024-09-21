## Malformed URL Cleanup

### Description

Write a Python function that cleans a potentially malformed URL.

Return the cleaned URL as a string.

### Examples

```python
# Example 1
url = "example.com/path/to/resource"
output = "http://example.com/path/to/resource"
```
  
```python
# Example 2
url = "HTTPS://WWW.EXAMPLE.COM///some//path/?key=value&key2=Value2"
output = "https://www.example.com/some/path/?key=value&key2=Value2"
```

```python
# Example 3
url = " w.w.w.Example.COM:8080/////path/to////page%20two?Query=Value#Fragment "
output = "http://www.example.com:8080/path/to/page two?Query=Value#Fragment"
```

### Start

1. Populate the `clean_url` function in `main.py`.
2. ```shell
   bash run.sh
   ```
