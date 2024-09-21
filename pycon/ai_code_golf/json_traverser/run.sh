#!/bin/bash

# Get the current script directory, ensuring it resolves even if run from another location
PROBLEM_DIR=$(dirname "$(realpath "$0")")
SCRIPT_DIR="$PROBLEM_DIR/../scripts"

CSV_FILE="$(realpath "$SCRIPT_DIR/../../participants.csv")"
KEYSTROKES_FILE="$SCRIPT_DIR/keystrokes.log"
echo $KEYSTROKES_FILE

# Function to update the CSV file based on test results
update_csv() {
  local update_end_time=$1
  local csv_temp_file="${CSV_FILE}.tmp"

  # Check if CSV file exists, if not create it with headers
  if [ ! -f "$CSV_FILE" ]; then
    echo "name,email,phone,question_no,tests_passed,keystrokes,start_time,end_time" > "$CSV_FILE"
  fi

  # Check if keystrokes file exists and read the count
  if [ -f "$KEYSTROKES_FILE" ]; then
    # Read the number of keystrokes from the file
    keystroke_count=$(<"$KEYSTROKES_FILE")
    echo "Keystrokes: $keystroke_count"
  else
    keystroke_count=0
    echo "Keystrokes file not found. Setting keystrokes to 0."
  fi

  # Create or clear the temporary file
  > "$csv_temp_file"

  # Read each row and update the EndTime column if needed
  while IFS=, read -r name email phone question_no tests_passed keystrokes start_time end_time; do
    # Update end time based on the update_end_time flag
    if [ "$update_end_time" = true ] && [ -z "$end_time" ]; then
      end_time="$END_TIME"  # Set end time only if it's not already set
    elif [ "$update_end_time" = false ]; then
      end_time=""  # Clear end time if update_end_time is false
    fi

    # Update the keystrokes column with the value from the keystrokes file
    keystrokes="$keystroke_count"

    # Write the updated row to the temporary file
    echo "$name,$email,$phone,$question_no,$tests_passed,$keystrokes,$start_time,$end_time" >> "$csv_temp_file"
  done < "$CSV_FILE"

  # Replace the original CSV file with the updated one
  mv "$csv_temp_file" "$CSV_FILE"
}

# Full path to main.py and tests.py
TESTS_PATH="$PROBLEM_DIR/tests.py"

# Run pytest and capture output using the correct tests.py path
TEST_OUTPUT=$(pytest "$TESTS_PATH" --tb=short --disable-warnings)

END_TIME=$(date +%s)

PASSED_COUNT=$(echo "$TEST_OUTPUT" | tail -5 | sed -n 's/.* \([0-9]\{1,\}\) \passed.*/\1/p')
FAILED_COUNT=$(echo "$TEST_OUTPUT" | tail -5 | sed -n 's/.* \([0-9]\{1,\}\) \failed.*/\1/p')
PASSED_COUNT=${PASSED_COUNT:-0}
FAILED_COUNT=${FAILED_COUNT:-0}

echo "$TEST_OUTPUT" | sed '/^\s*$/d'

# Check test results and update CSV accordingly
if [ "$FAILED_COUNT" -eq 0 ]; then
  echo "All $PASSED_COUNT tests passed!"
  update_csv true  # Update EndTime if tests passed
else
  echo "$FAILED_COUNT tests failed."
  update_csv false  # Clear EndTime if tests failed
fi

