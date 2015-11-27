/*
* Find the smallest element in the array
* Move it to the front or behind the smallest element
* Optimizing: Do this but make sure you don't touch the first few element
*/

class PracSelectionSort {

	public static void main(String[] args) { 
		int [] array = {4,1,6,8,10,2,7};
		int[] sortedArray = selectionSort(array);
		
		for (int i=0; i < sortedArray.length; ++i) { 
			System.out.println(sortedArray[i]);
		}
	
	}
	
	public static int[] selectionSort(int[] array) { 
		int smallest = 0;
		int bigIndex = 0;
	
		for (int i=0; i < array.length; ++i) { 
			smallest = array[i];
			bigIndex = i;

			for (int j=i+1; j < array.length; ++j) { // j=i or i+1 
				if (array[j] < smallest) { 
					smallest = array[j];
					bigIndex = j;
				}
			} 
	
			if (array[bigIndex] != array[i]) { 
				array[bigIndex] = array[i];
				array[i] = smallest;
			}
		}
		
		return array;
	
	}
}
