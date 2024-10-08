#bubble sort a sorting algorithm
# time complexity O(n^2) space complexity O(1)
def bubble_sort(elements):
    size = len(elements)
    print(size)
    for i in range(0,size-1):
        swapped = False
        for j in range(0,size-1-i):
            if elements[j] > elements[j+1]:
                tmp = elements[j]
                elements[j] = elements[j+1]
                elements[j+1] = tmp
                swapped = True
        if not swapped:
            break
            
            
            
if __name__ == "__main__":
    array = [5,9,2,1,67,34,88,34]
    abc_list = ['b', 'a', 'c', 'd' ,'f', 'e', 'g', 'h', 'i']
    print(array)
    bs = bubble_sort(array)
    bubble_sort(abc_list)
    print(abc_list)
    print(array)
    print(bs)
    #print(len(array))
    #a = list(range(0,len(array)))
    #print(f"{a}")
    
    
    #for i in range(0,8):
    #    print(array[i])