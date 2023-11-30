# find the cubes

lst_to_cube = [1, 2, 3, 4, 5, 6, 7, 8, 9]
cube_lst = []
for i in lst_to_cube:
    cube_lst.append(i*i*i)
print("The cube value is {}".format(cube_lst))

# find the sum from range 1, 100

sum_of_items = 0
for i in range(1, 101):
    sum_of_items = sum_of_items+i
print("The sum of range of items from 1 to 100 is {}".format(sum_of_items))

# tpl comprehension

tpl_a = [2, 5, 7, 8]
tpl_b = [7, 8, 9, 2]

summation = [tpl_a[i]+tpl_b[i] for i in range(0, len(tpl_b))]
print("the sum of two lists is {}".format(summation))




