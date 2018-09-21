#Remove Duplicate

def remove_duplicate(duplicate):
    new_list = [] #have to store the new list somewhere
    for i in duplicate:
        if i not in new_list: #if item is not in new list append to new list
            new_list.append(i)
    return(new_list) #return new list


duplicate = [76,98,930,846,84,938,98,76,74,72,849,377,27,74]
print("**************Original List*************")
print(duplicate)
print("**************Duplicates Removed*************")
print(remove_duplicate(duplicate))

#Largest element in array

largest = max(duplicate)
print("*************largest Item*************")
print(largest)

#or

print("*************largest Item*************")
for index in range(0,len(duplicate)):
    max= 0
    for i in duplicate:
        if i > max:
            max=i
print(max)

#Smallest element in array
min_num = min(duplicate)
print("**********SMALLEST NUMBER**************")
print(min_num)
print("**********SMALLEST NUMBER**************")

#or

for i in range(1, len(duplicate)-1):
    min = duplicate[0]
    if duplicate[i] < min:
        min=duplicate[i]

print(min)


#pyramid assignment
rows= int(input("Please enter the number of rows you would like: "))

def pypart(rows):
    # FIRST FOR LOOP BELOW(outer) loop to handle number of rows #range is from 0 to n(number of rows required)
    for i in range(0,rows):
        # SECOND FOR LOOP BELOW is to print empty space
        for j in range(0,rows-i-1): #for 9-0-1 = 8 empty spaces on first row
            print(end=" ")
        #Third for loop is to print "*"
        for j in range(0,i+1): # i = 0 so it will print 0+1=1 star
            print("*",end=" ")
        print()

pypart(rows)
