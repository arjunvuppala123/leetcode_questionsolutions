class Solution {
    public ListNode mergeTwoLists(ListNode list1, ListNode list2) {
        ListNode head1 = list1;
        ListNode head2 = list2;
        ListNode head = new ListNode(0);
        ListNode temp = head;
        while(head1!=null && head2!=null){
            if(head1.val <= head2.val){
                ListNode node = new ListNode(head1.val);
                temp.next = node;
                temp = temp.next;
                head1 = head1.next;
            }
            else{
                ListNode node = new ListNode(head2.val);
                temp.next = node;
                temp = temp.next;
                head2 = head2.next;
            }
            
        }
        if(head1!=null){
            while(head1!=null){
                ListNode node = new ListNode(head1.val);
                temp.next = node;
                temp = temp.next;
                head1 = head1.next;
            }
        }
        if(head2!=null){
            while(head2!=null){
                ListNode node = new ListNode(head2.val);
                temp.next = node;
                temp = temp.next;
                head2 = head2.next;
            }
        }
        return head.next;
        
    }
}