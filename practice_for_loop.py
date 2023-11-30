str_a = "hello"
for i in str_a:
    print(i)

# 1st iteration i = "h"     ------->>>> print(i)-------->>>> "h"
# 2nd iteration i = "e"     ------->>>> print(i)-------->>>> "e"
# 3rd iteration i = "l"     ------->>>> print(i)-------->>>> "l"
# 4th iteration i = "l"     ------->>>> print(i)-------->>>> "l"
# 5th iteration i = "o"     ------->>>> print(i)-------->>>> "o"

lst_a = ["a", "b", "c", "d"]
for i in lst_a:
    print(i)

# 1st iteration i = "a"   ---->>>print(i)----->>>> "a"
# 2nd iteration i = "b"   ---->>>print(i)----->>>> "b"
# 3rd iteration i = "c"   ---->>>print(i)----->>>> "c"
# 4th iteration i = "d"   ---->>>print(i)----->>>> "d"

tpl_a = ("e", "f", "g")
for i in tpl_a:
    print(i)

str_x = "xyz"
str_y = "abc"
for i in str_x:
    print(i)
for i in str_y:
    print(i)

str_x = "xyz"
str_y = "abc"
for i in str_x:
    for j in str_y:
        print(i, j)

# 1st iteration of str_x----->>> i = "x"
# 1st iteration of stry --->>>j = "a"---->>>("x", "a")
# 2nd iteration of str_y -->>>j = "b"---->>>("x", "b")
# 3rd iteration of str_y--->>>j = "c"---->>>("x", "c")

# 2nd iteration of str_x----->>>>>>i = "y"
# 1st iteration of str_y -----> j = "a"-->>("y", "a")
# 2nd iteration of str_y -----> j = "b"-->>("y", "b")
# 3rd iteration of str_y -----> j = "c" -->>("y", "c")

# 3rd iteration of str_x  ---->>>>i = "z"
# 1st iteration of str_y ---->>> j = "a" ---> ("z", "a")
# 2nd iteration of str_y ----->>> j = "b"---> ("z", "b")
# 3rd iteration of str_y --->>>>> j = "c" ---> ("z", "c")

str_a = "John is clever"
res = []
split_stra = str_a.split(" ")
for i in split_stra:
    res.append(i[::-1])
rev_str = " ".join(res)
print("the rev string is {}".format(rev_str))

# List comprehension

str_a = "John is clever"
res_lst = [i[::-1] for i in str_a.split(" ")]
print(res_lst)
reversed_str = " ".join(res_lst)
print("the rev string is {}".format(rev_str))

# squares of elements in list

lst_to_sqr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
sqr_lst = []
for i in lst_to_sqr:
    sqr_lst.append(i*i)
print("The square value is {}".format(sqr_lst))

# squares with list comprehension

lst_to_sqr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
squared_lst = [i**2 for i in lst_to_sqr]
print("The squared value of list items is {}".format(sqr_lst))

# using range function
# for i in range(0, 5):
# print(i)

# for i in range(1, 10):
#     print(i)
#
# for i in range(1, 10, 2):   # with step size 2
#     print(i)

# square the numbers from 1 to 9

lst_sqr = [i**2 for i in range(1, 10)]
print("The square value from range 1 to 10 is {}".format(lst_sqr))
# or
print([i**2 for i in range(1, 10)])

# sum from 1 to 10

lst_to_sum = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
summation = 0       # 0 is called as initialization
for i in lst_to_sum:
    summation = summation+i
print("The sum of all items in list is {}".format(summation))

# using range function

sum_of_items = 0
for i in range(1, 11):
    sum_of_items = sum_of_items+i
print("The sum of range of items from 1 to 11 is {}".format(sum_of_items))

# indexing

str_x = "Python"
len_str_x = len(str_x)
for i in range(0, len_str_x):
    print("The value of {} index is {}".format(i, str_x[i]))    # {} is 0 index, 1 index, 2 index....

# summation of both list in one list

lst_x = [1, 2, 3, 4]
lst_y = [5, 6, 7, 8]
len_lst_x = len(lst_x)
sum_lst_x_y = []
for i in range(0, len_lst_x):
    summation = lst_x[i] + lst_y[i]
    sum_lst_x_y.append(summation)                           # append is not used for tuple, it is immutable
print("the sum of two lists are {}".format(sum_lst_x_y))

"""
len_lst_x = 4   
1st iteration i = 0-->summation=lst_x[0]+lst_y[0]=1+5=6--->>sum_lst_x_y=[6]
2nd iteration i = 1-->summation=lst_x[1]+lst_y[1]=2+6=8--->>sum_lst_x_y=[6,8]
3rd iteration i = 2-->summation=lst_x[2]+lst_y[2]=3+7=10--->>sum_lst_x_y=[6,8,10]
4th iteration i = 3-->summation=lst_x[3]+lst_y[3]=4+8=12--->>sum_lst_x_y=[6,8,10,12]
"""

# Another method to add to lists in one list

# list comprehension

lst_x = [1, 2, 3, 4]
lst_y = [5, 6, 7, 8]
summation = [lst_x[i]+lst_y[i] for i in range(0, len(lst_y))]
print("the sum of two lists is {}".format(summation))

# count of characters

str_y = "Alex is in class"
for i in str_y:
    cnt = str_y.count(i)
    print("The character {} occurred {} time".format(i, cnt))

# reverse string without string

str_y = "hello"
rev_str = " "
for i in str_y:
    rev_str = i + rev_str
    print("the value after reversing string is {}".format(rev_str))

"""
1st iteration i = "h" ---->rev_str="h"+""="h"
2nd iteration i = "e" ---->rev_str="e"+"h"="eh"
3rd iteration i = "l" ---->rev_str="l"+"eh"="leh"
4th iteration i = "l" ---->rev_str="l"+"leh"="lleh"
5th iteration i = "o" ---->rev_str="o"+"lleh"="olleh"
"""




