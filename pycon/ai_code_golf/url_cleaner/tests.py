import pytest
from .main import clean_url

# inputs
url1 = "example.com:80/path/to/resource"
url2 = "example.com:443/path/to/resource"
url3 = "   wwww.example.com:443/path//to//resource?query=1#fragment"
url4 = "HTTP://Example.com:80//some//path//to/resource"
url5 = "ww.example.com/%7Euser//profile%20settings"
url6 = "www.example.com/path/to/resource?query=test#frag"
url7 = "example.com///path//to/resource?search=%20query%20here"
url8 = "EXAMPLE.COM:80/path?query=TestValue#FragmentValue"
url9 = "https://www.example.com//path//with%20spaces/"
url10 = "w.w.w.example.com/path/to///resource?query1=val1&query2=%20val2#frag"
url11 = " wwww.example.com:443/path//to///file"
url12 = "HTTP://example.com:80/PaTH?q=abc#Fragment"
url13 = "example.com"
url14 = "  https://www.Example.com//search?q=foo%20bar&&q2=%2Fbaz%20&frag=abc#top"
url15 = "HTTP://www.EXAMPLE.com:8080/path//to/page"
url16 = "https://example.com////some///path//file"
url17 = "example.com:443#section"
url18 = "http://192.168.1.1:80//config?q=1"
url19 = "https://example.com#section"
url20 = " example.com/search?q=%40user&f=%23top"
url21 = " w.w.w.Example.COM:8080/////path/to////page%20two?Query=Value#Fragment"

# Expected outputs
output1 = "http://example.com/path/to/resource"
output2 = "https://example.com/path/to/resource"
output3 = "https://www.example.com/path/to/resource?query=1#fragment"
output4 = "http://example.com/some/path/to/resource"
output5 = "http://www.example.com/~user/profile settings"
output6 = "http://www.example.com/path/to/resource?query=test#frag"
output7 = "http://example.com/path/to/resource?search= query here"
output8 = "http://example.com/path?query=TestValue#FragmentValue"
output9 = "https://www.example.com/path/with spaces/"
output10 = "http://www.example.com/path/to/resource?query1=val1&query2= val2#frag"
output11 = "https://www.example.com/path/to/file"
output12 = "http://example.com/PaTH?q=abc#Fragment"
output13 = "http://example.com/"
output14 = "https://www.example.com/search?q=foo bar&&q2=/baz &frag=abc#top"
output15 = "http://www.example.com:8080/path/to/page"
output16 = "https://example.com/some/path/file"
output17 = "https://example.com/#section"
output18 = "http://192.168.1.1/config?q=1"
output19 = "https://example.com/#section"
output20 = "http://example.com/search?q=@user&f=#top"
output21 = "http://www.example.com:8080/path/to/page two?Query=Value#Fragment"


@pytest.mark.parametrize(
  "url, expected",
  [
    (url1, output1),
    (url2, output2),
    (url3, output3),
    (url4, output4),
    (url5, output5),
    (url6, output6),
    (url7, output7),
    (url8, output8),
    (url9, output9),
    (url10, output10),
    (url11, output11),
    (url12, output12),
    (url13, output13),
    (url14, output14),
    (url15, output15),
    (url16, output16),
    (url17, output17),
    (url18, output18),
    (url19, output19),
    (url20, output20),
    (url21, output21),
  ],
)
def test_clean_url(url, expected):
  output = clean_url(url)
  assert output == expected, f"Expected {expected} but got {output}"
