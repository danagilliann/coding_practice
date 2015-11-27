/*
* This program deletes duplicates within a linked list
* Without using a buffer
* It uses a runner instead
* O(1) Space, O(N^2) Time
*
* ====================================================
* A note about deleting a node from a linked list:
* ====================================================
* * Given node "n"
* * Find previous node, "prev", and set "prev.next" to "n.next"
*/

void deleteDups(LinkedListNode head) { 
	LinkedListNode current = head;
	while (current != null) { 
		/* Remove all future nodes that have the same value */
		LinkedListNode runner = current;
		while (runner.next != null) { 
			if (runner.next.data == current.data) { 
				runner.next = runner.next.next; 
				/* runner.next.next  
				* * "Hops" over the next one
				* * Therefore deleting the next one
				*/
			} else { 
				runner = runner.next;
			}
		}
		current = current.next	
	}
}
