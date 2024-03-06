class Solution:
    def miceAndCheese(self, reward1: List[int], reward2: List[int], k: int) -> int:
        new_arr=[(reward1[i]-reward2[i],reward1[i] , reward2[i]) for i in range(len(reward2))]
        new_arr.sort(reverse=True)
        res = 0
        for i in range(k):
            res += new_arr[i][1]

        for i in range(k , len(reward1)):
            res += new_arr[i][2]
        return res

        
            