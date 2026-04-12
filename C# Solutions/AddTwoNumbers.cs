/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     public int val;
 *     public ListNode next;
 *     public ListNode(int val=0, ListNode next=null) {
 *         this.val = val;
 *         this.next = next;
 *     }
 * }
 */
public class Solution {
    public ListNode AddTwoNumbers(ListNode l1, ListNode l2) {
        ListNode result = new ListNode();
        ListNode dummy = result;
        int carry = 0;

        while (l1 is not null || l2 is not null || carry != 0){
            int val1 = 0;
            if (l1 is not null){
                val1 = l1.val;
                l1 = l1.next;
            }

            int val2 = 0;
            if (l2 is not null){
                val2 = l2.val;
                l2 = l2.next;
            }

            int sum = val1 + val2 + carry;
            carry = sum / 10;
        

            ListNode nextNode = new ListNode(sum%10);
            dummy.next = nextNode;
            dummy = dummy.next;
        }

        return result.next;
    }
}
