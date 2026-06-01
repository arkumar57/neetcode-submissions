class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        mylist = [];
        left = 0;

        right = len(numbers) - 1;

        while(left < right):

            if(numbers[left] + numbers[right] == target):

                mylist.append(left + 1);
                mylist.append(right + 1);

                return mylist;
            
            if(numbers[left] + numbers[right] > target):
                right = right -1;
            else:
                left += 1;

        
        return mylist;
        

        