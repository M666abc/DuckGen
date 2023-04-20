import random 
import time

num_values = int(input("Enter number of notes to generate: "))
start_time = int(input("Enter first note position (in milliseconds): "))
interval = int(input("Enter time between notes (in milliseconds): "))
jump_frequency = int(input("Enter jump frequency (every nth note): "))

# generate an initial random value
lane_values = [random.randint(1, 4)]
previous_lanes = lane_values[-4:]

for i in range(1, num_values):
    if i % jump_frequency == 0:
        # add jump
        jump_lane = random.choice([lane for lane in range(1, 5) if lane not in previous_lanes])
        lane_values.append(jump_lane)
        print("- StartTime: " + str(start_time) + "\n  Lane: " + str(previous_lanes[-1]) + "\n  KeySounds: []")
        start_time += interval
        print("- StartTime: " + str(start_time) + "\n  Lane: " + str(jump_lane) + "\n  KeySounds: []")
        previous_lanes.pop(0)
        previous_lanes.append(jump_lane)
    else:
        # generate a random value that is different from the previous value
        available_lanes = [1, 2, 3, 4]
        for lane in previous_lanes:
            if lane in available_lanes:
                available_lanes.remove(lane)
        lane_value = random.choice(available_lanes)
        lane_values.append(lane_value)
        print("- StartTime: " + str(start_time) + "\n  Lane: " + str(lane_value) + "\n  KeySounds: []")
        previous_lanes.pop(0)
        previous_lanes.append(lane_value)
        start_time += interval
