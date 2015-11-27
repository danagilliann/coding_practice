/*
* This program deletes duplicates within a linked list
* It uses a hash map (or a buffer)
* O(N) Time
*
* ====================================================
* A note about deleting a node from a linked list:
* ====================================================
* * Given node "n"
* * Find previous node, "prev", and set "prev.next" to "n.next"
*/

void deleteDups(LinkedListNode n) { 
	HashSet<Integer> set = new HashSet<Integer>();
	LinkedListNode previous = null;

	while (n != null) { 
		if (set.contains(n.data)) {
			/*
			* previous.next
			* * Get the current node --> What comes NEXT after the PREVIOUS node?
			* 
			* n.next
			* * Get the next node
			*
			* previous.next = n.next
			* * Set the current node to the next node
			*/
			previous.next = n.next;
		} else { 
			set.add(n.data);
			previous = n;
		}
		n = n.next;
	}
}
