import random

def generate_notes(num_values, jump_frequency):
    # generate the first ran val
    lane_values = [[random.randint(1, 4)]]
    previous_lanes = lane_values[-1]
    for i in range(1, num_values):
        if i % jump_frequency == 0:
            # add jump
            jump_lane = random.choice([lane for lane in range(1, 5) if lane not in previous_lanes])
            previous_lanes.append(jump_lane)
            jump_lane2 = random.choice([lane for lane in range(1, 5) if lane not in previous_lanes])
            lane_values.append([jump_lane, jump_lane2])
            previous_lanes = [jump_lane, jump_lane2]
        else:
            available_lanes = [1, 2, 3, 4]
            for lane in previous_lanes:
                available_lanes.remove(lane)
            lane_value = random.choice(available_lanes)
            lane_values.append([lane_value])
            previous_lanes = [lane_value]
    return lane_values

def generate_output(lane_values, start_time, interval, stop_time=None):
    output = ""
    current_time = start_time
    for i in range(len(lane_values)):
        if stop_time is not None and current_time >= stop_time:
            break
        for lane in lane_values[i]:
            output += f"- StartTime: {current_time}\n  Lane: {lane}\n  KeySounds: []\n"
        current_time += interval
    return output

def main():
    num_values = int(input("Enter number of notes to generate (put in a random number if you have a StopTime): "))
    start_time = int(input("Enter first note position (in milliseconds): "))
    interval = int(input("Enter time between notes (in milliseconds): "))
    jump_frequency = int(input("Enter jump frequency (every nth note): "))
    stop_time = int(input("Enter stop time (in milliseconds): "))

    lane_values = generate_notes(num_values, jump_frequency)
    output = generate_output(lane_values, start_time, interval, stop_time)
    print(output)

if __name__ == "__main__":
    main()
