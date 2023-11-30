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

# Assignment reverse

lst_z = ["a", "b", ["john", "class", "alex"], 4, 5, 7]   # (output:- ["a", "b", ["john", "ssalc", "alex"], 4, 5, 7] )
lst_z[2][1] = lst_z[2][1][::-1]
print(lst_z)