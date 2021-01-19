'''
Modify the naive implementation (see below) of a sorting algorithm so that 
the list to be sorted is modified *in place*. (4 Points)

Here is the idea: 

1. Iterate over all indices i = 0, 1, 2, ... of the input list

2. Find the index j of the smallest element in the rest of the list (from i on)

3. Replace the elements at indices i and j

If we want to sort the list [5, 3, 1, 4, 8, 2, 7, 6], for instance, a run of
the algorithm would be:

i=0, j=2, list=[5, 3, 1, 4, 8, 2, 7, 6]
i=1, j=5, list=[1, 3, 5, 4, 8, 2, 7, 6]
i=2, j=5, list=[1, 2, 5, 4, 8, 3, 7, 6]
i=3, j=3, list=[1, 2, 3, 4, 8, 5, 7, 6]
i=4, j=5, list=[1, 2, 3, 4, 8, 5, 7, 6]
i=5, j=7, list=[1, 2, 3, 4, 5, 8, 7, 6]
i=6, j=6, list=[1, 2, 3, 4, 5, 6, 7, 8]

'''


def index_of_smallest_element(some_list):
    '''Returns the index of the smallest element in some_list'''
    for index, val in enumerate(some_list):
        if val == min(some_list):
            break
    return index
        

def naive_sort(some_list):
   sorted_list = []
   while len(some_list) > 0:
            smallest_element = some_list.pop(index_of_smallest_element(some_list))
            sorted_list.append(smallest_element)
   return sorted_list
        
print(naive_sort([-100,2,1,4,5,9,100]))

def naive_sort_inplace(some_list):
    def indexch(some_list, x,y):
        some_list[x],some_list[y] = some_list[y], some_list[x]
    for i in range(0, len(some_list)):
        j = index_of_smallest_element(some_list, i)
        indexch(some_list,i,j)
    return(some_list)

print(naive_sort_inplace([3,2,1,7,87]))
if __name__ == '__main__':
    # test 
    my_list = [5, 3, 1, 4, 8, 2, 7, 6]
    naive_sort_inplace(my_list)
    print('Test: ', my_list == [1, 2, 3, 4, 5, 6, 7, 8])
