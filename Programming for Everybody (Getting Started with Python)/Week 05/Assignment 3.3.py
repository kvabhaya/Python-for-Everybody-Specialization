# Prompt the user for a score between 0.0 and 1.0
score_str = input("Enter a score between 0.0 and 1.0: ")

# Convert the input string to a float
try:
    score = float(score_str)
except ValueError:
    print("Error: Please enter a valid numeric score.")
    exit()

# Check if the score is out of range
if score < 0.0 or score > 1.0:
    print("Error: Score is out of range.")
    exit()

# Calculate and print the grade
if score >= 0.9:
    print("A")
elif score >= 0.8:
    print("B")
elif score >= 0.7:
    print("C")
elif score >= 0.6:
    print("D")
else:
    print("F")
