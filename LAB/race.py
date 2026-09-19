# Get the finishing times of all runners
def get_times():
    times = []

    # Ask how many runners will be entered
    n = int(input("Enter number of runners: "))

    # Ask for each runner's finishing time
    for i in range(n):
        time = float(input(f"Enter finishing time of runner {i + 1}: "))
        times.append(time)

    return times


# Sort the finishing times using Bubble Sort
def bubble_sort(times):
    n = len(times)

    # Repeat the sorting process
    for i in range(n):

        # Compare adjacent values
        for j in range(0, n - i - 1):

            # If the first time is slower, swap the values
            if times[j] > times[j + 1]:
                times[j], times[j + 1] = times[j + 1], times[j]

    return times


# Display the runners from fastest to slowest
def display_ranking(times):
    print("\nRace Ranking:")

    # Display each finishing time with its rank
    for i in range(len(times)):
        print(f"{i + 1}. {times[i]} seconds")


# Main program
times = get_times()
times = bubble_sort(times)
display_ranking(times)