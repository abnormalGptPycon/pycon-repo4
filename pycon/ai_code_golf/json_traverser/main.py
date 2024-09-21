import re
from typing import Any, Dict

def traverse_json(json_obj: Dict[str, Any], path: str) -> Any:
    pass

if __name__ == "__main__":
    # Test case 1: Simple nested keys
    sample_input = {"a": {"b": {"c": 42}}}
    sample_path = "a.b.c"
    sample_expected_output = 42

    output = traverse_json(sample_input, sample_path)
    assert output == sample_expected_output
    print("Passed sanity check!")

    # Additional test cases to verify correctness
    # Test case 2: List indexing
    json_obj = {"a": [1, 2, {"b": [3, 4]}]}
    path = "a[2].b[1]"
    assert traverse_json(json_obj, path) == 4

    # Test case 3: Keys with dots and brackets
    json_obj = {"a.b": {"c[d]": 100}}
    path = "a\\.b.'c[d]'"
    assert traverse_json(json_obj, path) == 100

    # Test case 4: Complex path with negative index
    json_obj = {"a": {"b.c": {"d[e]": [-10, 30]}}}
    path = "a.'b.c'.'d[e]'[-1]"
    assert traverse_json(json_obj, path) == 30

    # Test case 5: Escaped keys and values
    json_obj = {"a[b]": {"c.d": {"e[f]": {"key": "value"}}}}
    path = "'a[b]'.'c.d'.'e[f]'.key"
    assert traverse_json(json_obj, path) == "value"

    # Test case 6: Complex path with multiple levels of escaping
    json_obj = {
        "level1": {
            "level.2": {
                "level[3]": {
                    "complex.key[4]": {
                        "nested.key[5]": "deep_value"
                    }
                }
            }
        }
    }
    path = "level1.'level\\.2'.'level[3]'.'complex\\.key[4]'.'nested\\.key[5]'"
    assert traverse_json(json_obj, path) == "deep_value"

    print("All tests passed!")

# import re
# from typing import Any, Dict

# def traverse_json(json_obj: Dict[str, Any], path: str) -> Any:
#     # Regex to match both keys and list indices in the path, including quoted keys and escaped characters
#     token_pattern = re.compile(r"""
#         (?:       # Non-capturing group for keys, optionally quoted with single or double quotes
#             '([^']+)'|   # Single quoted key (e.g. 'key.with.dots')
#             "([^"]+)"|   # Double quoted key (e.g. "key.with.dots")
#             ([^.\[\]]+)| # Unquoted key (e.g. key without dots or special chars)
#             (\\.)       # Escaped dot
#         )
#         |
#         (?:       # Non-capturing group for list indices
#             \[(\-?\d+)\]  # Brackets with optional negative integer inside
#         )
#     """, re.VERBOSE)

#     # Find all tokens from the path
#     tokens = token_pattern.findall(path)

#     current = json_obj

#     for single_quote_key, double_quote_key, unquoted_key, escaped_dot, index in tokens:
#         if index:  # Handle list index
#             idx = int(index)
#             if not isinstance(current, list):
#                 raise KeyError(f"Expected a list but found {type(current).__name__}")
#             try:
#                 current = current[idx]
#             except IndexError:
#                 raise IndexError(f"List index {idx} out of range")
#         else:  # Handle dictionary keys
#             if single_quote_key:
#                 key = single_quote_key
#             elif double_quote_key:
#                 key = double_quote_key
#             elif escaped_dot:
#                 key = escaped_dot.strip('\\')
#             else:
#                 key = unquoted_key

#             # Replace escaped characters for unquoted keys
#             if unquoted_key:
#                 key = key.replace('\\.', '.').replace('\\[', '[').replace('\\]', ']')
            
#             if not isinstance(current, dict):
#                 raise KeyError(f"Expected a dictionary but found {type(current).__name__}")
#             try:
#                 current = current[key]
#             except KeyError:
#                 raise KeyError(f"Key '{key}' not found")

#     return current

# if __name__ == "__main__":
#     # Test case 1: Simple nested keys
#     sample_input = {"a": {"b": {"c": 42}}}
#     sample_path = "a.b.c"
#     sample_expected_output = 42

#     output = traverse_json(sample_input, sample_path)
#     assert output == sample_expected_output
#     print("Passed sanity check!")

#     # Additional test cases to verify correctness
#     # Test case 2: List indexing
#     json_obj = {"a": [1, 2, {"b": [3, 4]}]}
#     path = "a[2].b[1]"
#     assert traverse_json(json_obj, path) == 4

#     # Test case 3: Keys with dots and brackets
#     json_obj = {"a.b": {"c[d]": 100}}
#     path = "a\\.b.'c[d]'"
#     assert traverse_json(json_obj, path) == 100

#     # Test case 4: Complex path with negative index
#     json_obj = {"a": {"b.c": {"d[e]": [-10, 30]}}}
#     path = "a.'b.c'.'d[e]'[-1]"
#     assert traverse_json(json_obj, path) == 30

#     # Test case 5: Escaped keys and values
#     json_obj = {"a[b]": {"c.d": {"e[f]": {"key": "value"}}}}
#     path = "'a[b]'.'c.d'.'e[f]'.key"
#     assert traverse_json(json_obj, path) == "value"

#     # Test case 6: Complex path with multiple levels of escaping
#     json_obj = {
#         "level1": {
#             "level.2": {
#                 "level[3]": {
#                     "complex.key[4]": {
#                         "nested.key[5]": "deep_value"
#                     }
#                 }
#             }
#         }
#     }
#     path = "level1.'level\\.2'.'level[3]'.'complex\\.key[4]'.'nested\\.key[5]'"
#     assert traverse_json(json_obj, path) == "deep_value"

#     print("All tests passed!")
