# Linear search is the simplest way to look for an item in a list (or any collection):

# Start at the beginning of the list.

# Check each item one by one.

# If you find what you’re looking for → return it (or its index).

# If you reach the end without finding it → the item is not there.


          
print(list(enumerate(['a', 'b', 'c', 'd', 'e', 'f'], start=1)))

                #print index and elements in the list

fruits = [ 'apple', 'banana', 'mango', 'orange', 'strawberry']

for  iterable, index in enumerate(fruits):
    print(iterable, index)                                                                                                                                                                                                                                                                                   
#find element in arr

def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return  1 
    return -1

    
print(linear_search([10,20,30, 40,50, 60 ], 50 ))                                                                                        
    


#max even number


arr = [2, 5, 2, 9, 2, 5]


def largest_even(arr):
    max_even = None
    for num in arr:
        if num % 2 == 0:
            if max_even is None or num > max_even:
                max_even = num
    return max_even

print(largest_even([5, 12, 7, 8, 3, 10]))  


#count occurances

# arr = [1, 3, 5, 3, 7, 3, 3]
# target = 3

def count(arr, target):
    count = 0
    for i in arr:
        if i == target:
            count += 1 
    return count
    
print(count(arr=[1, 3, 5, 3, 7, 3, 3], target=3))
        
    
#return index of the string if substring found , if not found, return -1


def find_index(arr, substring):
    for i, word in enumerate(arr):
        if substring in word:
            return i
    return -1
    
print(find_index(['Java', 'Python', 'bootstrap'], "Py"))


#  Check Existence (Boolean)

def check_existance(arr, check):
    if check in arr:
        return True
    return False

# var = check_existance(["java" ,'python', 'react', "HTML"], "HTML")
print(check_existance(["java" ,'python', 'react', "HTML"], "HTML"))
# print(var)


# Find First Element index Greater than K

def find_greater(arr, k):
    greater_value = 0
    for integer, i in enumerate(arr):
        if  i > k:
            greater_value = integer
            return greater_value
    return -1

print(find_greater([1,2,5,20,25,35], 20))



#  Search for Even Number

def search_even(arr):
    for i in arr:
        if i %2 == 0:
            return i 
    return -1

print(search_even([1,5,7,25,60,13,22,12,6,8]))
print(search_even([1,3,5,7,9,11,13,25,35,41,77]))#testing for all odd numbers


#  Sum of Elements Greater than Target

def sum_of_elements(arr, target):
    greater_element = 0
    for i in arr:
        if i > target:
            greater_element = greater_element + i 
            
    return greater_element
print(sum_of_elements([2,3,4,10,15,1,8,3], 4))


# Search for Lowercase Word

def search_lower(words):
    for word in words:
        if word == word.lower():
            return word
    return -1 

print(search_lower(['Hello', "World", "python", "HTML"]))
print(search_lower(['Hello', "World", "PYTHON", "HTML"])) #testing for Upper



# Find All Indices of a Target


def find_indices(arr, target):
    index_list= []
    for index, value in enumerate(arr):
        if value == target:
            index_list.append(index)
    return index_list

print(find_indices([7, 10, 4, 7, 15, 6, 4, 7, 3, 7], 7))