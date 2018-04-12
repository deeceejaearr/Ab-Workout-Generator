#Read in Ab Workouts
#Select 5 random workouts that don't repeat
#Save them
#Add the 5 workouts to a new file
#Save the file


import random


my_list = []

with open('ab_workout_list', 'r') as f:
    my_list = [line.rstrip('\n') for line in f]

    filepath = 'ab_workout_list'
    with open(filepath) as fp:
        line = fp.readline()
        cnt = 1
        while line:
            print("Workout {} {}".format(cnt, line.strip()))
            line = fp.readline()
            cnt += 1

    def compare(a,b):
        for i in range(len(my_list)):
            for j in range(i + 1, len(my_list)):
                compare(my_list[i], my_list[j])

