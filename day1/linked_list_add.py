# https://leetcode.com/problems/add-two-numbers/submissions/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        # go through both lls and create the 2 numbers we have to sum up:
            # we want to create the numbers in reverse

        num_arr1 = []
        num1 = ''
        num_arr2=[]
        num2 = ''
        # keep track of current node        
        cur = l1
        
        # while we're not at the end of the ll, create the number in the order as is for now: will use an array -- easier to reverse
        while cur is not None:
            
            num_arr1 = num_arr1 + [cur.val]
            
            cur = cur.next
            # print(number)
        
        # reverse the order to obtain the number we actually want
        num_arr1.reverse()

        
        # create an actual number -> make a string first then make an int out of it:
        for num in num_arr1:
            num1 += str(num) 
            
        num1 = int(num1)
            
        # print(num1, num_arr1)
        
        # -------------do the same for the other list
        # keep track of current node        
        cur2 = l2
        
        # while we're not at the end of the ll, create the number in the order as is for now
        while cur2 is not None:
            
            num_arr2 = num_arr2 + [cur2.val]
            
            cur2 = cur2.next

        # reverse the order to obtain the number we actually want
        num_arr2.reverse()

        # create an actual number -> make a string first then make int out of it:
        for num in num_arr2:
            num2 += str(num) 
            
        num2 = int(num2)

        # -------------obtain the final sum:
        sum = num1 + num2
        # print(sum)
        
        # make sum a string and then create a new ll giving it values in reverse order
        sum = str(sum)
        
        # make a new ll with the starting node being the last character of sum - remember to keep track of current node
        l3 = ListNode(sum[-1])
        cur = l3
        
        # iterate over sum in reverse (skipping the last number since we already used it) and update each node as we go 
        for i in range(len(sum) -2, -1, -1):
            # print(l3.val)
            cur.next = ListNode(sum[i])
            cur = cur.next
            
        return l3
        
        
              
