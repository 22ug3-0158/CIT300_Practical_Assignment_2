import random
import time





def bubble_sort(arr):
    n = len(arr)
    data = arr.copy()
    start_time = time.time()
    for i in range(n):
        for j in range(0, n - i - 1):
            if data[j] > data[j + 1]:
                data[j], data[j + 1] = data[j + 1], data[j]
    end_time = time.time()
    return data, end_time - start_time


def merge_sort(arr):
    start_time = time.time()

    def merge(left, right):
        result = []
        i = j = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1
        result.extend(left[i:])
        result.extend(right[j:])
        return result

    def _merge_sort(data):
        if len(data) <= 1:
            return data
        mid = len(data) // 2
        left = _merge_sort(data[:mid])
        right = _merge_sort(data[mid:])
        return merge(left, right)

    sorted_arr = _merge_sort(arr)
    end_time = time.time()
    return sorted_arr, end_time - start_time


def quick_sort(arr):
    start_time = time.time()

    def _quick_sort(data):
        if len(data) <= 1:
            return data
        pivot = data[len(data) // 2]
        left = [x for x in data if x < pivot]
        middle = [x for x in data if x == pivot]
        right = [x for x in data if x > pivot]
        return _quick_sort(left) + middle + _quick_sort(right)

    sorted_arr = _quick_sort(arr)
    end_time = time.time()
    return sorted_arr, end_time - start_time





def generate_random_numbers(n=10, lower=1, upper=100):
    return [random.randint(lower, upper) for _ in range(n)]


def compare_algorithms(arr):
    print("\n--- Algorithm Performance Comparison ---")
    results = {}

    _, t_bubble = bubble_sort(arr)
    results['Bubble Sort'] = t_bubble

    _, t_merge = merge_sort(arr)
    results['Merge Sort'] = t_merge

    _, t_quick = quick_sort(arr)
    results['Quick Sort'] = t_quick

    print(f"{'Algorithm':<15}{'Time (seconds)':>20}")
    print("-" * 35)
    for algo, time_taken in results.items():
        print(f"{algo:<15}{time_taken:>20.6f}")

    print("-----------------------------------\n")






def main():
    data = []

    while True:
        print("\n--- Data Sorter: Sorting Algorithm Comparison Tool ---")
        print("1. Enter numbers manually")
        print("2. Generate random numbers")
        print("3. Perform Bubble Sort")
        print("4. Perform Merge Sort")
        print("5. Perform Quick Sort")
        print("6. Compare all algorithms (show performance table)")
        print("7. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            data = list(map(int, input("Enter numbers separated by spaces: ").split()))
            print("Data set updated:", data)

        elif choice == '2':
            n = int(input("How many numbers to generate? "))
            data = generate_random_numbers(n)
            print("Generated data:", data)

        elif choice == '3':
            if not data:
                print("No data available. Please enter or generate numbers first.")
            else:
                sorted_data, time_taken = bubble_sort(data)
                print("Bubble Sorted Data:", sorted_data)
                print(f"Time taken: {time_taken:.6f} seconds")

        elif choice == '4':
            if not data:
                print("No data available. Please enter or generate numbers first.")
            else:
                sorted_data, time_taken = merge_sort(data)
                print("Merge Sorted Data:", sorted_data)
                print(f"Time taken: {time_taken:.6f} seconds")

        elif choice == '5':
            if not data:
                print("No data available. Please enter or generate numbers first.")
            else:
                sorted_data, time_taken = quick_sort(data)
                print("Quick Sorted Data:", sorted_data)
                print(f"Time taken: {time_taken:.6f} seconds")

        elif choice == '6':
            if not data:
                print("No data available. Please enter or generate numbers first.")
            else:
                compare_algorithms(data)

        elif choice == '7':
            print("Exiting program. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
