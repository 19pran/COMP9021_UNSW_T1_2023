#!/bin/bash

# Loop through each test case in test_cases.txt
while IFS= read -r line; do

  # Check if this is the start of a new test case
  if [[ $line == TEST*BEGIN* ]]; then

    # Parse the test number from the line
    test_num=$(echo "$line" | cut -d' ' -f2)

    # Print the start of the test message
    echo "Running test case $test_num..."

    # Start capturing the output of the command
    output=""

  # Check if this is the end of a test case
  elif [[ $line == TEST*END* ]]; then

    # Compare the captured output to the expected output
    expected_output=$(echo "$line" | sed -E 's/^.*\| (.*)$/\1/')
    if [[ "$output" == "$expected_output" ]]; then
      echo "Test case $test_num passed!"
    else
      echo "Test case $test_num failed:"
      echo "Expected output: $expected_output"
      echo "Actual output: $output"
    fi

  # Otherwise, this is a command to run
  else

    # Run the command and capture the output
    command_output=$(eval "$line" 2>&1)
    output="$output$command_output"

  fi

done < test_cases.txt
