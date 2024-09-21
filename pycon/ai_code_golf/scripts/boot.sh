#!/bin/bash

# ASCII Art Banner
print_banner() {
  echo "    _    _                                      _"
  echo "   / \  | |__  _ __   ___  _ __ _ __ ___   __ _| |"
  echo "  / _ \ | '_ \| '_ \ / _ \| '__| '_ \` _ \ / _\` | |"
  echo " / ___ \| |_) | | | | (_) | |  | | | | | | (_| | |"
  echo "/_/   \_\_.__/|_| |_|\___/|_|  |_| |_| |_|\__,_|_|"
  echo "===================================================="
  echo "             PyCon24 | AI Code Golf                 "
  echo
}

# Function to validate email
validate_email() {
  if [[ "$1" =~ ^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$ ]]; then
    return 0
  else
    return 1
  fi
}

# Function to validate phone number (10 digits)
validate_phone() {
  if [[ "$1" =~ ^[0-9]{10}$ ]]; then
    return 0
  else
    return 1
  fi
}

# Function to prompt user and validate input
prompt_input() {
  local prompt_msg=$1
  local validation_func=$2
  local input_var

  # if validation func is null, return input as is
  if [ -z "$validation_func" ]; then
    read -p "$prompt_msg: " input_var
    echo "$input_var"
    return
  fi

  while true; do
    read -p "$prompt_msg: " input_var
    if $validation_func "$input_var"; then
      echo "$input_var"
      break
    else
      input_var=""
    fi
  done
}

# Print the banner
print_banner

base_dir=/Users/rishitv/Documents/Abnormal/source/projects/pycon

problem_names=("invalid" "anomaly_detection" "json_traverser" "phone_number_extractor" "url_cleaner")

# Function to get problem name from integer input
get_problem_name() {
  local index=$1
  if (( index > 0 && index < ${#problem_names[@]} )); then
    echo "${problem_names[index]}"
  else
    echo ""
  fi
}

# Example usage
#problem_number=$(( (RANDOM % 4) + 1 ))
problem_number=2
problem_name=$(get_problem_name "$problem_number")
csv_file="$base_dir/participants.csv"

# Prompt for user details and validate inputs
echo "Please provide your contact details for the bumper prize."
name=$(prompt_input "Enter your name" "")
email=$(prompt_input "Enter your email" "validate_email")
phone=$(prompt_input "Enter your phone (10 digits)" "validate_phone")

# Confirm valid details and write to CSV
echo "Please confirm your details:"
echo "Name: $name"
echo "Email: $email"
echo "Phone: $phone"
read -p "Are these correct? (y/n): " confirmation

if [[ "$confirmation" != "y" ]]; then
  echo "Details not confirmed. Exiting."
  exit 1
fi

echo "Press enter to begin. Good luck!"
read -r

sudo -v

dirname="$base_dir/ai_code_golf/$problem_name"
zed "$dirname" &

sudo python "$base_dir/ai_code_golf/scripts/counter.py" &
codegolf_pid=$!

nohup bash -c "
    sleep 6
    sudo killall zed
    kill $codegolf_pid
    bash $dirname/run.sh
" &

start_time=$(date +%s)

# Write confirmed details to CSV
if [ ! -f "$csv_file" ]; then
  echo "Name,Email,Phone,QuestionNo,TestsPassed,Keystrokes,StartTime,EndTime" > "$csv_file"
fi
  echo "$name,$email,$phone,$problem_number,,,$start_time," >> "$csv_file"
