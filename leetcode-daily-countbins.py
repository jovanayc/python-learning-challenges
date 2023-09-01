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
n = 17
example = solution_instance.countBits(n)
print(example)