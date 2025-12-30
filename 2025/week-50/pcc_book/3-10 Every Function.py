gym_exercises = ['bb chest press', 'overhead shoulder press',
                 'incline db chest press', 'triceps pushdowns', ' lat raises', 'triceps overhead']
print(gym_exercises)

gym_exercises.append('lat raises')
print(gym_exercises)

gym_exercises.pop(-3)
print(gym_exercises)

gym_exercises.insert(-2, 'lat raises')
print(gym_exercises)

gym_exercises.pop()
print(gym_exercises)

gym_exercises.pop()
print(gym_exercises)

gym_exercises.pop()
print(gym_exercises)

gym_exercises.pop()
print(gym_exercises)

gym_exercises.pop()
print(gym_exercises)

del gym_exercises[0]
print(gym_exercises)
del gym_exercises[0]
print(gym_exercises)

gym_exercises.append('squats')
gym_exercises.append('rdls')
gym_exercises.append('leg press')
gym_exercises.append('leg curls')
gym_exercises.append('calfs')
print(gym_exercises)
print(gym_exercises[0].title())
for exercise in gym_exercises:
    print(f"I fuckin' love to do {exercise.title()}.")
gym_exercises.insert(-1, 'hip thrust')
print(gym_exercises)
print(f"When I do leg day I am doing {len(gym_exercises)} exercises.")

print(sorted(gym_exercises))
print(gym_exercises)
print(sorted(gym_exercises, reverse=True))
print(gym_exercises)
gym_exercises.reverse()
print(gym_exercises)
gym_exercises.reverse()
print(gym_exercises)
gym_exercises.sort()
print(gym_exercises)
gym_exercises.sort(reverse=True)
print(gym_exercises)

gym_exercises.append('hack squat')
gym_exercises.append('leg extension')
new_exercise = gym_exercises.pop(-2)
print(f"I like to do {new_exercise.title()}")
bad_exercise = gym_exercises.pop()
print(f"I don't like to do {bad_exercise.upper()}")
favorite_exercise = 'squats'
gym_exercises.remove(favorite_exercise)
print(f"I love to do {favorite_exercise}!!!")

gym_exercises.pop()
gym_exercises.pop()
gym_exercises.pop()
gym_exercises.pop()
print(gym_exercises)
del gym_exercises[0]
print(gym_exercises)
