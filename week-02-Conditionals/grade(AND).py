# This program takes a score as input and outputs the corresponding letter grade based on standard grading scales using if, elif, and else statements.
score = int(input("Score: "))

# Compare the score and print the corresponding letter grade using if, elif, and else statements also the AND operator to check the range of the score
#if score >= 90 and score <= 100:
 #   print("Grade: A")
#elif score >= 80 and score < 90:
 #   print("Grade: B")
#elif score >= 70 and score < 80:
 #   print("Grade: C")
#elif score >= 60 and score < 70:
 #   print("Grade: D")
#else:
 #   print("Grade: F")

# The same logic can be implemented using chained comparisons to make the code more concise and readable. The following code uses chained comparisons to check the range of the score and print the corresponding letter grade.
if 90 <= score <= 100:
    print("Grade: A")   
elif 80 <= score < 90:
    print("Grade: B")
elif 70 <= score < 80:
    print("Grade: C")
elif 60 <= score < 70:
    print("Grade: D")
else:
    print("Grade: F")

# The same logic can be implemented using only if, elif, and else statements without the AND operator or chained comparisons. The following code uses only if, elif, and else statements to check the range of the score and print the corresponding letter grade.
#if score >=90:
 #   print("Grade: A")
#elif score >= 80:
 #   print("Grade: B")
#elif score >= 70:
 #   print("Grade: C")
#elif score >= 60:
 #   print("Grade: D")
#else:
 #   print("Grade: F")

 