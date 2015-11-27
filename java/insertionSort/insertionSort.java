 
public class insertionSort {
 
    public static void main(String a[]){
        int[] arr1 = {10,34,2,56,7,67,88,42};
        int[] arr2 = doInsertionSort(arr1);
        for(int i:arr2){
            System.out.print(i);
						System.out.print(" ");
				}
				System.out.println();
		}
     
    public static int[] doInsertionSort(int[] array){
        for (int i=1; i < array.length; ++i) { // Start at the second element of the list because the first element is considered "sorted" 
					int element = array[i]; // Get the start of the first unsorted element in the list 
					int j; 
					j = i; 
					
					while (j > 0 && array[j-1] > element) { 
					/*
					* Here we are looping through the sorted part of the list
					* Notice that j > 0. This is because the first element of the sorted part of the list is "sorted"
					* Compares the last element in the sorted part of the list, array[j-1]
					* With the first element in the unsorted part of the list, element 
					* If the last element in sorted part is greater than the first element in unsorted,
					* The last element in sorted get "inserted" in unsorted 
					*/
						array[j] = array[j-1];
						j = j-1;
					}
					array[j] = element; // Here we already moved to the end of the sorted part 
				} 
				return array;
    }
}
