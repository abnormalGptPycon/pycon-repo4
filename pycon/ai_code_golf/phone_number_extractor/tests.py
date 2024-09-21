import pytest
from .main import extract_international_phone_numbers

# inputs
text1 = "Call us at +1-800-555-1234 ext123 or +44 20.7946 0958#4567."
text2 = "Emergency numbers for block 101: (123)4567890, 1001: +91 98765 43210, 80002: +86 10 6552 9988 ext.12345."
text3 = "Invalid numbers: +0123-456-7890, +44 (0)20-7946-0958 x123456"
text4 = "Reach us at +91-98765-43210. Our backup is +1 (555) 123-4567."
text5 = "Office numbers: +49 30 1234567, 98765, +81 3 1234 5678, ext200."
text6 = "Dial me at +1---800---555----1234!! or reach the office at +44 123-456.7890!!."
text7 = "Call: support@company.com, +39-06-12345678 is Italian. Promo code: 2021SALE123."
text8 = "+00123-456-7890 is wrong, but +61 3 9123 4567 (Australia) is good. +44 (0)20 7946 0958 is tricky!"
text9 = "For inquiries: +55 (11) 91234 5678. Emergencies: +86 21 1234 5678 ext. 1234. Office: +7(495)123-45-67."
text10 = "+0123 123 456 7890, +1 (999) 555-4321, and +91-12345-67890. But this one works: +86 21 9876 5432."
text11 = "Message us at: +44 20 7946 0958, call center: +1-212-555-1234. Fax: +33 1 2345 6789. Email: info@example.com."
text12 = "Partial number: +44 12345, or missing area code: +1 555. Full: +34 91 1234567."

# Expected outputs
expected1 = ["+1-800-555-1234", "+44 20.7946 0958"]
expected2 = ["+91 98765 43210", "+86 10 6552 9988"]
expected3 = []
expected4 = ["+91-98765-43210", "+1 (555) 123-4567"]
expected5 = ["+49 30 1234567", "+81 3 1234 5678"]
expected6 = ["+44 123-456.7890"]
expected7 = ["+39-06-12345678"]
expected8 = ["+61 3 9123 4567"]
expected9 = ["+55 (11) 91234 5678", "+86 21 1234 5678", "+7(495)123-45-67"]
expected10 = ["+1 (999) 555-4321", "+91-12345-67890", "+86 21 9876 5432"]
expected11 = ["+44 20 7946 0958", "+1-212-555-1234", "+33 1 2345 6789"]
expected12 = ["+44 12345", "+34 91 1234567"]


@pytest.mark.parametrize(
  "text, expected",
  [
    (text1, expected1),
    (text2, expected2),
    (text3, expected3),
    (text4, expected4),
    (text5, expected5),
    (text6, expected6),
    (text7, expected7),
    (text8, expected8),
    (text9, expected9),
    (text11, expected11),
    (text12, expected12),
  ],
)
def test_extract_phone_numbers(text, expected):
  output = extract_international_phone_numbers(text)
  assert output == expected, f"Expected {expected}, but got {output}"
