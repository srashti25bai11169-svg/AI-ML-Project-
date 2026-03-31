# STUDY TIME SUGGESTION AI

def suggest_study_time(free_hours, difficulty, days_left):
    study_time = 0

    # Base on difficulty
    if difficulty == "easy":
        study_time += 1
    elif difficulty == "medium":
        study_time += 2
    elif difficulty == "hard":
        study_time += 3

    # Based on days left
    if days_left <= 3:
        study_time += 2
    elif days_left <= 7:
        study_time += 1

    # Adjust based on free time
    if free_hours < study_time:
        study_time = free_hours  # can't exceed free time

    return study_time


# User input
print("---- Study Time Suggestion AI ----")

free_hours = int(input("Enter your free hours per day: "))
difficulty = input("Enter subject difficulty (easy/medium/hard): ").lower()
days_left = int(input("Enter days left for exam: "))

# Get suggestion
result = suggest_study_time(free_hours, difficulty, days_left)

print("\n📚 Recommended study time:", result, "hours/day")

# Extra tip
if result >= 4:
    print("🔥 Tip: Take short breaks to avoid burnout!")
else:
    print("👍 Tip: Stay consistent and revise daily!")
