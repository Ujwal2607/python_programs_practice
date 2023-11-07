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









# Assignment

lst_n = ["u", "j", "w", 2, 3, "@26"]

print("The value is {}".format(lst_n))

# To find length

len_lst_n = len(lst_n)
print("The length of list n is {}".format(len_lst_n))

# To find type

type_lst_n = type(lst_n)
print("The type of variable is {}".format(type_lst_n))

# Indexing

lst_zeroth_ind = lst_n[0]
print("The zeroth index value of lst n is {}".format(lst_zeroth_ind))

lst_first_ind = lst_n[1]
print("The first index value of lst n is {}".format(lst_first_ind))

lst_second_ind = lst_n[2]
print("The second index value of lst n is {}".format(lst_second_ind))

lst_third_ind = lst_n[3]
print("The third index value of lst n is {}".format(lst_third_ind))

lst_fourth_ind = lst_n[4]
print("The fourth index value of lst n is {}".format(lst_fourth_ind))

lst_fifth_ind = lst_n[5]
print("The fifth index value of lst n is {}".format(lst_fifth_ind))

# changing elements in existing list

lst_n = ["u", "j", "w", 2, 3, "@26"]

lst_n[2] = "ujwal"
print("The value of lst n after changing is {}".format(lst_n))

lst_n[4] = 2000
print("The value of lst n after changing is {}".format(lst_n))

# Append

lst_n = ["u", "j", "w", 2, 3, "@26"]

lst_n.append("python")
print("The value of lst_n after appending is {}".format(lst_n))

lst_n.append(123)
print("The value of lst_n after appending is {}".format(lst_n))

# Extend

lst_n = ["u", "j", "w", 2, 3, "@26"]

lst_n.extend(["a", "b"])
print("The value of lst_n after extending is {}".format(lst_n))

lst_n.extend([456, "@xyz"])
print("The value of lst_n after extending is {}".format(lst_n))

# Slicing

lst_n = ["u", "j", "w", 2, 3, "@26"]

ind0_to_ind4 = lst_n[0:4]
print("The value of element from zeroth to fourth is {}".format(ind0_to_ind4))

ind2_to_ind5 = lst_n[2:5]
print("The value of element from second to fifth is {}".format(ind2_to_ind5))

# Slicing with step size

lst_n = ["u", "j", "w", 2, 3, "@26"]

slc_with_stp2 = lst_n[0:6:2]
print("The value of slicing lst_n using step size 2 is {}".format(slc_with_stp2))

slc_with_stp2 = lst_n[2:6:2]
print("The value of slicing lst_n using step size 2 is {}".format(slc_with_stp2))

slc_with_stp3 = lst_n[0:6:3]
print("The value of slicing lst_n using step size 3 is {}".format(slc_with_stp3))

slc_with_stp3 = lst_n[1:6:3]
print("The value of slicing lst_n using step size 3 is {}".format(slc_with_stp3))
