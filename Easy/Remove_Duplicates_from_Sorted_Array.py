num = [1, 3, 2, 5, 6, 5]

def remove(num):
    i = 0
    while i < len(num):
        k = i + 1
        while k < len(num):
            if num[i] == num[k]:
                num.pop(k)  # Remove the duplicate at index k
            else:
                k += 1  # Only move k forward if no duplicate was removed
        i += 1  # Move i forward after checking all elements with index i

    print(num)

remove(num)
