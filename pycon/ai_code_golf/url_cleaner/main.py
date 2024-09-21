
import re
from urllib.parse import urlparse, urlunparse, quote, unquote
def clean_url(url: str) -> str:
    # Step 1: Strip leading/trailing whitespace
    url = url.strip()

    # Step 2: Handle missing scheme (default to http)
    if not re.match(r'^[a-zA-Z]+://', url):
        url = 'http://' + url

    # Step 3: Parse the URL into components
    parsed_url = urlparse(url)

    # Step 4: Normalize the scheme to lowercase
    scheme = parsed_url.scheme.lower()

    # Step 5: Normalize the hostname to lowercase
    netloc = parsed_url.netloc.lower()

    # Handle default ports for HTTP/HTTPS
    if (scheme == 'http' and netloc.endswith(':80')):
        netloc = netloc.rsplit(':', 1)[0]
    elif (scheme == 'https' and netloc.endswith(':443')):
        netloc = netloc.rsplit(':', 1)[0]

    # Normalize domain from variants like "wwww" to "www"
    netloc = re.sub(r'^w{2,}\.', 'www.', netloc)

    # Step 6: Remove multiple slashes in the path, except for "://"
    path = re.sub(r'/+', '/', parsed_url.path)

    # Ensure the root path is "/", not empty (e.g., for "example.com")
    if not path or path == '':
        path = '/'

    # Step 7: Decode percent-encoded characters like %20
    path = unquote(path)

    # Step 8: Normalize the query and fragment (also decode %20 and similar)
    query = unquote(parsed_url.query)
    fragment = unquote(parsed_url.fragment)

    # Step 9: Rebuild the cleaned URL
    cleaned_url = urlunparse((scheme, netloc, path, parsed_url.params, query, fragment))

    return cleaned_url
# def clean_url(url: str) -> str:
#     # Step 1: Strip leading/trailing whitespace
#     url = url.strip()

#     # Step 2: Handle missing scheme (default to http)
#     if not re.match(r'^[a-zA-Z]+://', url):
#         url = 'http://' + url

#     # Step 3: Parse the URL into components
#     parsed_url = urlparse(url)

#     # Step 4: Normalize the scheme to lowercase
#     scheme = parsed_url.scheme.lower()

#     # Step 5: Normalize the hostname to lowercase
#     netloc = parsed_url.netloc.lower()

#     # Handle default ports for HTTP/HTTPS
#     if (scheme == 'http' and netloc.endswith(':80')):
#         netloc = netloc.rsplit(':', 1)[0]
#     elif (scheme == 'https' and netloc.endswith(':443')):
#         netloc = netloc.rsplit(':', 1)[0]

#     # Remove leading "www" variants like "wwww" and normalize it to "www"
#     netloc = re.sub(r'^w{2,}\.', 'www.', netloc)

#     # Step 6: Remove multiple slashes in the path, except for "://"
#     path = re.sub(r'/+', '/', parsed_url.path)

#     # Ensure the root path is "/", not empty (e.g., for "example.com")
#     if not path or path == '':
#         path = '/'

#     # Step 7: Decode percent-encoded characters like %20
#     path = unquote(path)

#     # Step 8: Normalize the query and fragment
#     query = unquote(parsed_url.query)
#     fragment = unquote(parsed_url.fragment)

#     # Step 9: Rebuild the cleaned URL
#     cleaned_url = urlunparse((scheme, netloc, path, parsed_url.params, query, fragment))

#     # Return the cleaned URL
#     return cleaned_url

# # Test cases using pytest
import pytest

@pytest.mark.parametrize(
    "url, expected",
    [
        ("example.com:80/path/to/resource", "http://example.com/path/to/resource"),
        ("example.com:443/path/to/resource", "https://example.com/path/to/resource"),
        ("   wwww.example.com:443/path//to//resource?query=1#fragment", "https://www.example.com/path/to/resource?query=1#fragment"),
        ("HTTP://Example.com:80//some//path//to/resource", "http://example.com/some/path/to/resource"),
        ("ww.example.com/%7Euser//profile%20settings", "http://www.example.com/~user/profile settings"),
        ("www.example.com/path/to/resource?query=test#frag", "http://www.example.com/path/to/resource?query=test#frag"),
        ("example.com///path//to/resource?search=%20query%20here", "http://example.com/path/to/resource?search= query here"),
        ("EXAMPLE.COM:80/path?query=TestValue#FragmentValue", "http://example.com/path?query=TestValue#FragmentValue"),
        ("https://www.example.com//path//with%20spaces/", "https://www.example.com/path/with spaces/"),
        ("w.w.w.example.com/path/to///resource?query1=val1&query2=%20val2#frag", "http://www.example.com/path/to/resource?query1=val1&query2= val2#frag"),
        (" wwww.example.com:443/path//to///file", "https://www.example.com/path/to/file"),
        ("HTTP://example.com:80/PaTH?q=abc#Fragment", "http://example.com/PaTH?q=abc#Fragment"),
        ("example.com", "http://example.com/"),
        ("  https://www.Example.com//search?q=foo%20bar&&q2=%2Fbaz%20&frag=abc#top", "https://www.example.com/search?q=foo bar&&q2=/baz &frag=abc#top"),
        ("HTTP://www.EXAMPLE.com:8080/path//to/page", "http://www.example.com:8080/path/to/page"),
        ("https://example.com////some///path//file", "https://example.com/some/path/file"),
        ("example.com:443#section", "https://example.com/#section"),
        ("http://192.168.1.1:80//config?q=1", "http://192.168.1.1/config?q=1"),
        ("https://example.com#section", "https://example.com/#section"),
        (" example.com/search?q=%40user&f=%23top", "http://example.com/search?q=@user&f=#top"),
        (" w.w.w.Example.COM:8080/////path/to////page%20two?Query=Value#Fragment", "http://www.example.com:8080/path/to/page two?Query=Value#Fragment"),
        ("example.com:443/path/to/resource", "https://example.com/path/to/resource"),
        ("   wwww.example.com:443/path//to//resource?query=1#fragment", "https://www.example.com/path/to/resource?query=1#fragment"),
        ("w.w.w.example.com/path/to///resource?query1=val1&query2=%20val2#frag", "http://www.example.com/path/to/resource?query1=val1&query2= val2#frag"),
        (" wwww.example.com:443/path//to///file", "https://www.example.com/path/to/file"),
        ("example.com:443#section", "https://example.com/#section"),
        (" w.w.w.Example.COM:8080/////path/to////page%20two?Query=Value#Fragment", "http://www.example.com:8080/path/to/page two?Query=Value#Fragment")

    ]
)
def test_clean_url(url, expected):
    output = clean_url(url)
    assert output == expected, f"Expected {expected} but got {output}"

# import re
# from urllib.parse import urlparse, urlunparse, quote, unquote

# def clean_url(url: str) -> str:
#     # Step 1: Strip leading/trailing whitespace
#     url = url.strip()
    
#     # Step 2: Handle missing scheme (default to http)
#     if not re.match(r'^[a-zA-Z]+://', url):
#         url = 'http://' + url

#     # Step 3: Parse the URL to normalize different parts
#     parsed_url = urlparse(url)

#     # Step 4: Normalize the scheme to lowercase
#     scheme = parsed_url.scheme.lower()

#     # Step 5: Normalize the hostname to lowercase
#     netloc = parsed_url.netloc.lower()

#     # Handle standard ports for HTTP/HTTPS
#     if (scheme == 'http' and netloc.endswith(':80')) or (scheme == 'https' and netloc.endswith(':443')):
#         netloc = netloc.rsplit(':', 1)[0]

#     # Step 6: Remove multiple slashes in the path, except for "://"
#     path = re.sub(r'/+', '/', parsed_url.path)

#     # Step 7: Decode percent-encoded characters like %20
#     path = unquote(path)

#     # Step 8: Normalize the query and fragment (decode them as well)
#     query = unquote(parsed_url.query)
#     fragment = unquote(parsed_url.fragment)

#     # Step 9: Rebuild the cleaned URL
#     cleaned_url = urlunparse((scheme, netloc, path, parsed_url.params, query, fragment))

#     # Return the cleaned URL
#     return cleaned_url

# # Test cases using pytest, based on your provided data
# import pytest

# @pytest.mark.parametrize(
#     "url, expected",
#     [
#         ("example.com:80/path/to/resource", "http://example.com/path/to/resource"),
#         ("example.com:443/path/to/resource", "https://example.com/path/to/resource"),
#         ("   wwww.example.com:443/path//to//resource?query=1#fragment", "https://www.example.com/path/to/resource?query=1#fragment"),
#         ("HTTP://Example.com:80//some//path//to/resource", "http://example.com/some/path/to/resource"),
#         ("ww.example.com/%7Euser//profile%20settings", "http://www.example.com/~user/profile settings"),
#         ("www.example.com/path/to/resource?query=test#frag", "http://www.example.com/path/to/resource?query=test#frag"),
#         ("example.com///path//to/resource?search=%20query%20here", "http://example.com/path/to/resource?search= query here"),
#         ("EXAMPLE.COM:80/path?query=TestValue#FragmentValue", "http://example.com/path?query=TestValue#FragmentValue"),
#         ("https://www.example.com//path//with%20spaces/", "https://www.example.com/path/with spaces/"),
#         ("w.w.w.example.com/path/to///resource?query1=val1&query2=%20val2#frag", "http://www.example.com/path/to/resource?query1=val1&query2= val2#frag"),
#         (" wwww.example.com:443/path//to///file", "https://www.example.com/path/to/file"),
#         ("HTTP://example.com:80/PaTH?q=abc#Fragment", "http://example.com/PaTH?q=abc#Fragment"),
#         ("example.com", "http://example.com/"),
#         ("  https://www.Example.com//search?q=foo%20bar&&q2=%2Fbaz%20&frag=abc#top", "https://www.example.com/search?q=foo bar&&q2=/baz &frag=abc#top"),
#         ("HTTP://www.EXAMPLE.com:8080/path//to/page", "http://www.example.com:8080/path/to/page"),
#         ("https://example.com////some///path//file", "https://example.com/some/path/file"),
#         ("example.com:443#section", "https://example.com/#section"),
#         ("http://192.168.1.1:80//config?q=1", "http://192.168.1.1/config?q=1"),
#         ("https://example.com#section", "https://example.com/#section"),
#         (" example.com/search?q=%40user&f=%23top", "http://example.com/search?q=@user&f=#top"),
#         (" w.w.w.Example.COM:8080/////path/to////page%20two?Query=Value#Fragment", "http://www.example.com:8080/path/to/page two?Query=Value#Fragment")
#     ]
# )
# def test_clean_url(url, expected):
#     output = clean_url(url)
#     assert output == expected, f"Expected {expected} but got {output}"



# # ############################################################demo#######
# # import re
# # from urllib.parse import urlparse, urlunparse, quote, unquote


# # # def clean_url(raw_url: str):
# # #     pass

# # from urllib.parse import urlparse, urlunparse, quote, unquote

# # def clean_url(url: str) -> str:
# #     # Step 1: Strip leading/trailing whitespace
# #     url = url.strip()
    
# #     # Step 2: Handle missing scheme (default to http)
# #     if not re.match(r'^[a-zA-Z]+://', url):
# #         url = 'http://' + url
    
# #     # Step 3: Parse the URL to normalize different parts
# #     parsed_url = urlparse(url)

# #     # Step 4: Normalize the scheme to lowercase
# #     scheme = parsed_url.scheme.lower()

# #     # Step 5: Normalize the hostname to lowercase
# #     netloc = parsed_url.netloc.lower()

# #     # Step 6: Remove multiple slashes in the path, except for "://"
# #     path = re.sub(r'/+', '/', parsed_url.path)

# #     # Step 7: Decode percent-encoded characters like %20
# #     path = unquote(path)

# #     # Step 8: Normalize the query and fragment (decode them as well)
# #     query = parsed_url.query
# #     fragment = parsed_url.fragment

# #     # Step 9: Rebuild the cleaned URL
# #     cleaned_url = urlunparse((scheme, netloc, path, parsed_url.params, query, fragment))

# #     # Return the cleaned URL
# #     return cleaned_url

# # # Test cases
# # if __name__ == "__main__":
# #     # Test case 1: Missing scheme
# #     url = "example.com/path/to/resource"
# #     output = clean_url(url)
# #     assert output == "http://example.com/path/to/resource", f"Failed: {output}"

# #     # Test case 2: Uppercase scheme and redundant slashes
# #     url = "HTTPS://WWW.EXAMPLE.COM///some//path/?key=value&key2=Value2"
# #     output = clean_url(url)
# #     assert output == "https://www.example.com/some/path/?key=value&key2=Value2", f"Failed: {output}"

# #     # Test case 3: Whitespace, uppercase domain, and spaces
# #     url = " w.w.w.Example.COM:8080/////path/to////page%20two?Query=Value#Fragment "
# #     output = clean_url(url)
# #     assert output == "http://www.example.com:8080/path/to/page two?Query=Value#Fragment", f"Failed: {output}"

# #     # Test case 4: Already clean URL
# #     url = "https://example.com/path"
# #     output = clean_url(url)
# #     assert output == "https://example.com/path", f"Failed: {output}"

# #     # Test case 5: Multiple spaces and no scheme
# #     url = "    WWW.EXAMPLE.COM//test//path  "
# #     output = clean_url(url)
# #     assert output == "http://www.example.com/test/path", f"Failed: {output}"

# #     # Test case 6: Complex URL with query parameters and fragment
# #     url = "HTTP://example.COM/path////to////page?arg1=val1&arg2=val2#Section "
# #     output = clean_url(url)
# #     assert output == "http://example.com/path/to/page?arg1=val1&arg2=val2#Section", f"Failed: {output}"

# #     print("All test cases passed.")


# # if __name__ == "__main__":
# #     # Example sanity check
# #     sample_url = "example.com/path/to/resource"
# #     sample_expected = "http://example.com/path/to/resource"
# #     result = clean_url(sample_url)
# #     assert result == sample_expected, f"Expected {sample_expected} but got {result}"
# #     print("Passed sanity check!")
