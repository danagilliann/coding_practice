class PracMergeSort { 
	int[] tempArray;
	int[] array;

	public static void main(String[] args) { 
		array = {10,1,5,7,2,8,3,4};
		tempArray = new int[array.length];
		
		int firstIndex = array[0];
		int endIndex = array.length-1;
	
		splitArray(firstIndex, endIndex);
	}

	public static void splitArray(int firstIndex, int endIndex) { 
		if (firstIndex < endIndex) { 
			int midpointIndex = (array.length-1)/2;	
			int firstIndex = array[0];

			splitArray(firstIndex, midpointIndex-1);
			splitArray(midpointIndex, array.length-1);
			mergeParts(firstIndex, endIndex);	
		} 
	}

	public static void mergeParts(int firstIndex, int endIndex) { 
		int temp = 0;

		for (int i=firstIndex; i <= endIndex; ++i) { 
			tempArray[i] = array[i];	
		}	
		
		if (tempArray[firstIndex] > tempArray[endIndex]) { 
			temp = array[firstIndex];
			array[firstIndex] = array[endIndex];
			array[endIndex] = temp;
		}
	}

}
