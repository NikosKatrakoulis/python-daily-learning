gym_exercises = ['bb chest press', 'db seated overhead shoulder press', 'db incline chest press',
                 'triceps pushdowns', 'lat raises', 'triceps overhead pushup', 'lat raises', 'abs', 'cardio']
print("The first three exercises of the program/list are:")
for exercise in gym_exercises[:2]:
    print(exercise.title())

print("\nThree exercises from the middle of the program/list are:")
for exercise in gym_exercises[2:6]:
    print(exercise.title())

print("\nThe last three exercises of the program/list are:")
for exercise in gym_exercises[-3:]:
    print(exercise.title())

print("\nThese are the exercises I'm doing when I do push in the gym.")
