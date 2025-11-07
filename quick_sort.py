Print (f"\nOriginal List: {numbers}")

        Results = {}
        sorted_bubble, time_bubble, steps_bubble = bubble_sort(numbers)
        sorted_merge, time_merge, steps_merge = merge_sort(numbers)
        sorted_quick, time_quick, steps_quick = quick_sort(numbers)

        print ("\nSorted Outputs:")
        print(f"Bubble Sort: {sorted_bubble}")
        print(f"Merge Sort:  {sorted_merge}")
        print(f"Quick Sort:  {sorted_quick}")

        results['Bubble Sort'] = {'time': time_bubble, 'steps': steps_bubble}
        results['Merge Sort'] = {'time': time_merge, 'steps': steps_merge}
        results['Quick Sort'] = {'time': time_quick, 'steps': steps_quick

def quick_sort(arr):
    """Perform Quick Sort and measure execution time + steps."""
    steps = 0  # count comparisons and swaps

    def partition(a, low, high):
        nonlocal steps
        pivot = a[high]
        i = low - 1
        for j in range(low, high):
            steps += 1
            if a[j] <= pivot:
                i += 1
                a[i], a[j] = a[j], a[i]
        a[i + 1], a[high] = a[high], a[i + 1]
        return i + 1

    def quick_sort_recursive(a, low, high):
        if low < high:
            pi = partition(a, low, high)
            quick_sort_recursive(a, low, pi - 1)
            quick_sort_recursive(a, pi + 1, high)

