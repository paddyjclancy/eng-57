# Function to be tested:
def check_if_digit_div_num(digit, num_div):
    return digit % num_div == 0

# Acceptance Criteria:
        # dig 3 div 3       33
        # dig 4 div 3       43
        # dig 5 div 5       55
        # dig 6 div 5       65
        # dig 15 div 3      153
        # dig 15 div 5      155

# Set up

exp_output33 = True
exp_output43 = False
exp_output55 = True
exp_output65 = False
exp_output153 = True
exp_output155 = True

# Explain

print("Testing function: check_if_digit_div_num() \nUsing known examples of digs/divs, expecting 6 x True... ")

# Test

print("Dig = 3, Div = 3 --- ", check_if_digit_div_num(3, 3) == exp_output33)
print("Dig = 4, Div = 3 --- ", check_if_digit_div_num(4, 3) == exp_output43)
print("Dig = 5, Div = 5 --- ", check_if_digit_div_num(5, 5) == exp_output55)
print("Dig = 6, Div = 5 --- ", check_if_digit_div_num(6, 5) == exp_output65)
print("Dig = 15, Div = 3 --- ", check_if_digit_div_num(15, 3) == exp_output153)
print("Dig = 15, Div = 5 --- ", check_if_digit_div_num(15, 5) == exp_output155)
