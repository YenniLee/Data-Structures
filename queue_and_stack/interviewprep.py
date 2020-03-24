# Add up and print the sum of the all of the minimum elements of each inner array:
# [[8, 4], [90, -1, 3], [9, 62], [-7, -1, -56, -6], [201], [76, 18]]
# You may use whatever programming language you'd like.
# Verbalize your thought process as much as possible before writing any code. Run through the UPER problem solving framework while going through your thought process.

arr_list = [[8,4], [90, -1, 3], [9, 62], [-7, -1, -56, -6], [201], [76, 18]]
def sum_mins( arr_list ):
    total = 0
    for sub in arr_list:
        sorted_arr = sorted(sub)
        total += sorted_arr[0]
    return total
            


print(sum_mins(arr_list))