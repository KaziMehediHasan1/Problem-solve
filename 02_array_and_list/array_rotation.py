"""arr = [1,2,3,4,5,6,7]
d = 3
print("After left rotation:", arr[d:] + arr[:d])
"""

# second method
arr = [1, 2, 3, 4, 5, 6, 7]
d = 2
n = len(arr)
# print(n)

temp = arr[:d]    
# print(temp)  
arr[:n-d] = arr[d:]  
# print(arr[:n-d])
arr[n-d:] = temp    

print(arr)