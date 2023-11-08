# to find length of list

lst_x =["a", "b", "c", 1, 2]

len_lstx = len(lst_x)
print("The length of list x is {}".format(len_lstx))

# to find type
print("The of the variable is {}".format(type(lst_x)))

lst_y = ["1", "2", "python", 123, "@abc"]

len_lsty = len(lst_y)
print("The length of list is {}".format(len_lsty))

# Indexing of lst_y

ind0_lsty = lst_y[0]
print("The zeroeth index of lst_y is {}".format(ind0_lsty))

ind1_lsty = lst_y[1]
print("The first index of lst_y is {}".format(ind1_lsty))

ind2_lsty = lst_y[2]
print("The second index of lst_y is {}".format(ind2_lsty))

ind3_lsty = lst_y[3]
print("the third index of lst_y is {}".format(ind3_lsty))

ind4_lsty = lst_y[4]
print("The fourth index of lst_y is {}".format(ind4_lsty))

# To print h from python which is an item of lst_y

lst_y = ["1", "2", "python", 123, "@abc"]

lst_python = lst_y[2]
print("the value is {}".format(lst_python))

lsty_h = lst_python[3]
print("The value is {}".format(lsty_h))

lst_y_h = lst_y[2][3]
print("Another way of indexing {}".format(lst_y_h))

lst_y[3] = 456
print("The lst_y after changing the value is {}".format(lst_y))

# Append

lst_y.append(123)
print("the value of lst_y after appending is {}".format(lst_y))

# Extend

lst_y.extend(["a", "b"])
print("The lst_y after extending is {}".format(lst_y))

lst_y.extend(["3", "4"])
print("the value of lst_y after extending list is {}".format(lst_y))

