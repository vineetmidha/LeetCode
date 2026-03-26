'''
Problem-74

Search in Sorted_2D_Matrix

https://leetcode.com/problems/search-a-2d-matrix/description/

Efficiency: m x log(n)

'''

def b_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return True
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return False

def searchMatrix(matrix, target):
    total_rows = len(matrix)

    # Corner Cases
  
    # 1. if target < first element
    if target < matrix[0][0]: return False
    
    # 2. if target > last element
    last_idx = len(matrix[total_rows-1])-1
    if target > matrix[total_rows-1][last_idx]: return False

    # Main loop
  
    cur_row = 0
    while cur_row < total_rows:
        # get last index of current row
        last_idx = len(matrix[cur_row])-1

        # if target is on boundary of current row        
        if target==matrix[cur_row][0] or target==matrix[cur_row][last_idx]:
            return True
        
        # if target lies in the current row
        if target > matrix[cur_row][last_idx] and target < matrix[cur_row][last_idx]:
            return b_search(matrix[cur_row], target)

        # go to next row
        cur_row += 1
        
    return False
    
matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
target = int(input())

print(searchMatrix(matrix, target))
