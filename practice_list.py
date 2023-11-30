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
print("The zeroth index of lst_y is {}".format(ind0_lsty))

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

# Item reversing in list

str_a = "welcome class"
str_a_lst = str_a.split(" ")
print("The list after splitting is {}".format(str_a_lst))

str_a_lst[0] = str_a_lst[0][::-1]
str_a_lst[1] = str_a_lst[1][::-1]
print(str_a_lst)

# join

str_a_rev = " ".join(str_a_lst)
print("The value after reversing is {}".format(str_a_rev))

lst_x = [1, 2, ["a", "b", "python"], 3, 4]
lst_x[2][2] = lst_x[2][2][::-1]
print(lst_x)

# clear:- it empty the list

lst_a = [1, 2, 3]
lst_a.clear()
print("The value after clearing is {}".format(lst_a))

# pop:- it will only delete last element in the list

lst_b = ["a", "b", "c", "d"]
lst_b.pop()
print("The list after pop is {}".format(lst_b))

lst_b.pop()
print("The list after pop is {}".format(lst_b))

# remove :- it will remove particular element in the list

lst_c = ["john", "bob", "alex", "xyz"]
lst_c.remove("bob")
print("The value after removing is {}".format(lst_c))

lst_c.remove("xyz")
print("The value after removing is {}".format(lst_c))

# reverse

lst_d = [1, 2, 3, 4]
lst_d.reverse()
print("The list after reversing is {}".format(lst_d))

# index and insert

lst_x = ["a", "b", "c", "d", "e"]
ind_val = lst_x.index("b")
print("The index value of b is {}".format(ind_val))

lst_x.insert(1,"x")
print("The list after inserting is {}".format(lst_x))
lst_x.insert(4,"y")
print("The list after inserting y is {}".format(lst_x))

# sort, max, min

lst_z = [3, 2, 6, 1, 5, 4]
lst_z.sort()
print("The list after sorting is {}".format(lst_z))

lst_z = [3, 2, 6, 1, 5, 4]
max_val = lst_z[-1]
print("The value of maximum in lst_z is {}".format(max_val))

min_val = lst_z[0]
print("The value of minimum in lst_z is {}".format(min_val))

# in-built function

lst_z = [3, 2, 6, 1, 5, 4]
lst_z_max = max(lst_z)
print("The value of maximum in lst_z is {}".format(lst_z_max))

sec_max_val = lst_z[-2]
print("The second highest value is {}".format(sec_max_val))

lst_z_min = min(lst_z)
print("The value of minimum in lst_z is {}".format(lst_z_min))

# count

lst_m = ["a", "b", "c", "a", "d"]

cnt_a = lst_m.count("a")
print("The count of a in lstm is {}".format(cnt_a))

cnt_c = lst_m.count("c")
print("the count of c in lstm is {}".format(cnt_c))