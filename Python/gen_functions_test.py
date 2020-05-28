from gen_functions_def import return_formatted_name

# This file tests the above imported function
# Set up:

input = " paTRicK    "
expected_output = "Patrick"

# Explain
print("Testing function: return_formatted_name() with input = ' paTRicK    ' --> 'Patrick...")

# Actual test: returns either True or False
print(return_formatted_name(input) == expected_output)

