import random
import time

num_values = int(input("Enter number of values to generate: "))
start_time = int(input("Enter starting point for start time (in milliseconds): "))
interval = int(input("Enter interval for start time (in milliseconds): "))
jump_frequency = int(input("Enter jump frequency (every X iterations): "))

# generate an initial random value
lane_values = [random.randint(1, 4)]
previous_lane = lane_values[-1]

for i in range(1, num_values):
    if i % jump_frequency == 0:
        # add jump
        jump_lane = random.choice([lane for lane in range(1, 5) if lane != previous_lane])
        lane_values.append(jump_lane)
        print("- StartTime: " + str(start_time) + "\n  Lane: " + str(previous_lane) + "\n  KeySounds: []")
        start_time += interval
        print("- StartTime: " + str(start_time) + "\n  Lane: " + str(jump_lane) + "\n  KeySounds: []")
        previous_lane = jump_lane
    else:
        # generate a random value that is different from the previous value
        available_lanes = [1, 2, 3, 4]
        available_lanes.remove(previous_lane)
        if len(lane_values) > 1 and len(available_lanes) > 1:
            # avoid consecutive repeats by removing the previous value from the available lanes
            available_lanes.remove(lane_values[-2])
        lane_value = random.choice(available_lanes)
        lane_values.append(lane_value)
        print("- StartTime: " + str(start_time) + "\n  Lane: " + str(lane_value) + "\n  KeySounds: []")
        previous_lane = lane_value
        start_time += interval
