def calculate_sum_and_average(input_string):
    total_sum = 0
    count = 0

    for char in input_string:
        if char.isdigit():
            total_sum += int(char)
            count += 1

    if count == 0:
        print("No digits found in the input.")
    else:
        average = total_sum / count
        print(f"Sum of digits: {total_sum}")
        print(f"Average of digits: {average}")

# Test cases
input_str = "abc123def456gh"
calculate_sum_and_average(input_str)

input_str = "7890"
calculate_sum_and_average(input_str)
