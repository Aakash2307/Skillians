def Max_of_ones(s):
    original_count = s.count('1')


    gain = []
    for i in s:
        if i == '0':
            gain.append(1)
        else:
            gain.append(-1)
    
    max_count = curr = gain[0]
    for j in gain[1:]:
        curr = max(j, j+curr)
        max_count = max(max_count, curr)


    return max_count + original_count
s = input("Enter the string : ")
print(Max_of_ones(s))