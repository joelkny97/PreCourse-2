# Time Complexity : O(log n)
# Space Complexity : O(1)

# Python code to implement iterative Binary  
# Search. 
  
# It returns location of x in given array arr  
# if present, else returns -1 
def binarySearch(arr, l, r, x): 
  
  #write your code here
  
  # if right index is less than left index, return -1 as element not found
  if r < l:
      return -1
    
  # find middle index 
  mid = l + (r - l) // 2
  
  if arr[mid] == x:
      return mid
  elif arr[mid] > x:
      # search in left half
      return binarySearch(arr, l, mid-1, x)
  elif arr[mid] < x:
      # search in right half
      return binarySearch(arr, mid+1, r, x)
  else:
    return -1
  
    
  
# Test array 
arr = [ 2, 3, 4, 10, 40 ] 
x = 10
  
# Function call 
result = binarySearch(arr, 0, len(arr)-1, x) 
  
if result != -1: 
    print(f"Element is present at index {result}") 
else: 
    print("Element is not present in array")
