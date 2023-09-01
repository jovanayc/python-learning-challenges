"""
Jovanay Carter 
Leetcode - Daily Coding Problem
Friday, Sept 1, 2023

Create a class that takes an integer 'n' and outputs an array of the numbers of ccurances of '1'
 in the bit representations of i for numbers 0 through n.
 Example:
    input: n = 5
    output: [0,1,1,2,1]
    explanation:
        # 0 --> 000
        # 1 --> 001
        # 2 --> 010
        # 3 --> 011
        # 4 --> 100
"""

class Solution:
    def countBits (self, n:int) -> list[int]:
        #set variables
        result_list = []
        sum_of_occurances = 0

        for i in range(n+1):
            #get binary
            bin_value = bin(i) #returns string
            print(f"Binary: {bin_value}", type(bin_value))
            #count num occurances
            sum_of_occurances = bin_value.count("1")
            #append result to result_list
            result_list.append(sum_of_occurances)
            print(result_list[i], type(result_list[i]))

        return result_list

solution_instance = Solution()
n = 5
example = solution_instance.countBits(n)
print(example)