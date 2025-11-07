Save  class bubbleSort        [member 1]

package dataSorter;

import java.util.Scanner;

public class BubbleSort {
public static void bubbleSort(int[] arr) {
int n = arr.length;
int steps = 0;
long startTime = System.nanoTime();

for (int i = 0; i < n - 1; i++) {
for (int j = 0; j < n - i - 1; j++) {
steps++;
if (arr[j] > arr[j + 1]) {
int temp = arr[j];
arr[j] = arr[j + 1];
arr[j + 1] = temp;
steps++;
}
}
}

long endTime = System.nanoTime();
long duration = endTime - startTime;

System.out.println("\nSorted array (Bubble Sort):");
for (int num : arr) {
System.out.print(num + " ");
}
System.out.println("\n");

System.out.println("Bubble Sort Performance:");
System.out.println("Total Steps: " + steps);
System.out.println("Execution Time: " + duration / 1_000_000.0 + " ms");
}

public static void main(String[] args) {
Scanner sc = new Scanner(System.in);
System.out.println("--- Bubble Sort Module (Member 1) ---");
System.out.print("Enter the number of elements: ");
int n = sc.nextInt();

int[] arr = new int[n];
System.out.println("Enter " + n + " numbers:");
for (int i = 0; i < n; i++) {
arr[i] = sc.nextInt();
}

bubbleSort(arr);
sc.close();
}
}


