import re
from typing import List

def extract_international_phone_numbers(text: str) -> List[str]:
  numbers = []
  phone_pattern = r"\+?\d{1,4}[-.\s]?\(?\d{1,4}?\)?[-.\s]?\d{1,4}[-.\s]?\d{1,9}"
  phone_numbers = re.findall(phone_pattern, text)
  cleaned_numbers = [re.sub(r"[-.\s]", "", number) for number in phone_numbers]

# Print the cleaned phone numbers
  valid_numbers = []
  for number in phone_numbers:
      # Clean up the number by removing non-digit characters
      cleaned_number = re.sub(r"[-.\s()]", "", number)
      
      # Check if the number has 7 to 15 digits and doesn't start with zero in any part
      if 7 <= len(cleaned_number) <= 15 and not re.search(r"\b0", cleaned_number):
          valid_numbers.append(cleaned_number)
    
  return valid_numbers




def extract_phone_numbers(text):
    phone_pattern = r"\+?\d{1,4}[-.\s]?\(?\d{1,4}?\)?[-.\s]?\d{1,4}[-.\s]?\d{1,9}"
    # Find all potential phone numbers in the text
    phone_numbers = re.findall(phone_pattern, text)

    # Return the valid phone numbers (ignoring any part after 'ext' or '#')
    return phone_numbers

if __name__ == "__main__":
  sample_input = "Call us at +1-800-555-1234 ext123 or +44 20.7946 0958#4567."
  sample_extracted = ["+1-800-555-1234", "+44 20.7946 0958"]

  sample_output = extract_international_phone_numbers(sample_input)
  assert sample_output == sample_extracted, f"Expected {sample_extracted}, but got {sample_output}"
  print("Passed sanity check!")
