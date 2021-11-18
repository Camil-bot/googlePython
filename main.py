

#Ex1
new_list = [7, 8, 9, 2, 3, 1, 4, 10, 5, 6]

#Ex2
sorted_list = sorted(new_list)
print(sorted_list)

#Ex3
inverted_sorted_list = sorted(new_list)[::-1]
print(inverted_sorted_list)

#Ex4
print(new_list[::2])

#Ex5
print(new_list[1::2])

#Ex6
for number in new_list:
    if number % 3:
        print(number)
