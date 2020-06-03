
n = input("Enter a number, Fibonacci Sequence will be returned up to this number's term     ")
x = 0                                           # Term 0
y = 1                                           # Term 1
z = int                                         # New value
term = 0                                        # For counting iterations
output = [1]                                    # Output in form of list, term 1 provided


while term < int(n) - 1:
    z = x + y                                   # Generate new value from two previous
    output.append(z)                            # Add new value to output list
    term += 1                                   # Increment for counting iterations
    x = y                                       # Re-assign for next iteration
    y = z                                       # Re-assign for next iteration

print(output)