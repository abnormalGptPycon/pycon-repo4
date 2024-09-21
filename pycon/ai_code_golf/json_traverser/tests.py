import pytest
from .main import traverse_json

error_cls_map = {
  "KeyError": KeyError,
  "IndexError": IndexError,
}

# Inputs
input2 = {"a": [1, 2, {"b": [3, 4]}]}
path2 = "a[2].b[1]"

input9 = {
  "x": [{"y0": [{"z": 1}, {"z": 2}, {"z": [100, 200]}]}, {"y1": [{"z": [300, 400]}, {"z": 500}]}]
}
path9 = "x[1].y1[0].z[-1]"

input5 = {"a": {"b.c": {"d[e]": [10, 20, 30]}}}
path5 = "a.'b.c'.'d[e]'[-1]"

input10 = {"a[b]": {"c.d": {"e[f]": {"key": "value"}}}}
path10 = "'a[b]'.'c.d'.'e[f]'.key"

input3 = {"a.b": {"c[d]": 100}}
path3 = "a\\.b.'c[d]'"

input11 = {"level1": {"level.2": {"level[3]": {"complex.key[4]": {"nested.key[5]": "deep_value"}}}}}
path11 = "level1.'level\\.2'.'level[3]'.'complex\\.key[4]'.'nested\\.key[5]'"

# Expected outputs
output1 = 42
output2 = 4
output3 = 100
output4 = 30
output5 = 30
output6 = KeyError
output7 = IndexError
output8 = 99
output9 = 400
output10 = "value"
output11 = "deep_value"
output12 = IndexError


@pytest.mark.parametrize(
  "json_obj, path, expected",
  [
    (input2, path2, output2),
    (input3, path3, output3),
    (input5, path5, output5),
    (input9, path9, output9),
    (input10, path10, output10),
    (input11, path11, output11),
  ],
)
def test_json_traversal(json_obj, path, expected):
  try:
    output = traverse_json(json_obj, path)
  except (KeyError, IndexError) as e:
    output = e.__class__
  assert output == expected, f"Expected {expected}, but got {output}"


