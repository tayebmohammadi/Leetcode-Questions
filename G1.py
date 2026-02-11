"""
Lunar Rover Route
You are operating a lunar rover on a circular moon track with a given integer circumference. Along this track, there are several gas deposits represented by a 0-indexed array of tuples deposits, where deposits[i] = (position_i, gas_i) indicates that there is gas_i amount of gas at position_i.

The rover has an unlimited gas tank but starts with 0 gas. It can only travel in one direction (forward) around the circular track. Traveling 1 unit of distance consumes 1 unit of gas.

When the rover reaches a gas deposit, it automatically collects all the gas available at that location. However, gas deposits are single-use; once the gas is collected from a deposit, it becomes empty.

Given the deposits array, the track's circumference, and a starting_index indicating the index of the gas deposit where the rover begins its journey, return the maximum total distance the rover can travel before it runs out of gas.

Example 1:

Input: deposits = [(0, 20), (20, 20), (40, 20), (80, 20)], circumference = 100, starting_index = 0
Output: 60
Explanation:

Start at index 0 (position 0), collect 20 gas. Tank = 20.

Drive to index 1 (position 20), distance is 20. Consume 20 gas. Tank = 0. Collect 20 gas. Distance traveled = 20.

Drive to index 2 (position 40), distance is 20. Consume 20 gas. Tank = 0. Collect 20 gas. Distance traveled = 40.

Drive towards index 3 (position 80). The distance is 40, but you only have 20 gas.

You drive 20 units and run out of gas at position 60.

Total distance traveled = 40 + 20 = 60.

Example 2:

Input: deposits = [(0, 20), (20, 20), (40, 20), (80, 20)], circumference = 100, starting_index = 3
Output: 80
Explanation:

Start at index 3 (position 80), collect 20 gas. Tank = 20.

Drive to index 0 (position 0). Since the track is circular, distance is 100 - 80 = 20. Consume 20 gas. Tank = 0. Collect 20 gas. Distance traveled = 20.

Drive to index 1 (position 20), consume 20 gas. Tank = 0. Collect 20 gas. Distance traveled = 40.

Drive to index 2 (position 40), consume 20 gas. Tank = 0. Collect 20 gas. Distance traveled = 60.

Drive towards index 3 (position 80). The distance is 40, but you only have 20 gas.

You drive 20 units and run out of gas at position 60.

Total distance traveled = 60 + 20 = 80.

Constraints:

1 <= deposits.length <= 10^5

0 <= deposits[i][0] < circumference

0 <= deposits[i][1] <= 10^4

The deposits array is sorted in strictly increasing order by position.

0 <= starting_index < deposits.length

1 <= circumference <= 10^9

"""


def gas_station(deposit, circum, start_index):

    current_gas = 0
    current_index = start_index
    distance_travelled = 0
    n = len(deposit)

    while True:
        current_gas += deposit[current_index][1]
        pos = deposit[current_index][0]
        deposit[current_index] = (pos, 0)


        next_index = (current_index + 1) % n
        if next_index > current_index:
            distance_to_next = deposit[next_index][0] - deposit[current_index][0]
        else:
            distance_to_next = circum - deposit[current_index][0] + deposit[next_index][0]
        
        if current_gas >= distance_to_next:
            current_gas -= distance_to_next
            distance_travelled += distance_to_next
            current_index = next_index
        else:
            distance_travelled += current_gas
            return distance_travelled

    return distance_travelled


if __name__ == "__main__":
    deposits = [(0, 20), (20, 20), (40, 20), (80, 20)]
    circumference = 100
    starting_index = 0
    print(f"Starting at index {starting_index}: Max distance = {gas_station(deposits, circumference, starting_index)}")

    starting_index = 3
    print(f"Starting at index {starting_index}: Max distance = {gas_station(deposits, circumference, starting_index)}")
