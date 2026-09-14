scores = [72, 45, 90, 61, 38]

pass_count = 0
fail_count = 0
total = 0

for score in scores:
    total = total + score
    
    if score >= 80:
        grade = "A"
    elif score >= 70:
        grade = "B"
    elif score >= 50:
        grade = "C"
    else:
        grade = "F"
    
    print(f"{score}: {grade}")

    if score >= 50:
        pass_count = pass_count + 1
    else:
        fail_count = fail_count + 1

average = total / len(scores)
print(f"Passed: {pass_count}")
print(f"Failed: {fail_count}")
print(f"Average: {round(average, 1)}")
