# function takes a sorted array and an item. If the item is in the array, the function returns its position (index). 
def binary_search(list, item):
  # low and high keep track of which part of the list you'll search in.
  low = 0
  high = len(list) - 1

  # While you haven't narrowed it down to one element 
  while low <= high:
    # each time check the middle element/ // - floor division will divide the first argument by the second and round the result down to the nearest whole number
    mid = (low + high) // 2 
    guess = list[mid]
    # Found the item.
    if guess == item:
      return mid
    # The guess was too high.
    if guess > item:
      high = mid - 1
    # The guess was too low.
    else:
      low = mid + 1

  # Item doesn't exist
  return None

my_list = [1, 3, 5, 7, 9]
print(binary_search(my_list, 5)) # => 1

# 'None' means nil in Python. We use it to indicate that the item wasn't found.
print(binary_search(my_list, 50)) # => None
