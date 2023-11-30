empty_string = ""
str_a = "python"
str_n = "10"
str_an = "python4.0"
str_s = " "

# How to find the length of string

len_str = len(str_a)
print("The length of string is {}".format(len_str))

type_str = type(str_an)
print("The type of variable is {}".format(type_str))

# Indexing

str_x = "python"

strx_zeroth_ind = str_x[0]
print("The zeroth index value of strx is {}".format(strx_zeroth_ind))

strx_fst_ind = str_x[1]
print("The fst index value of strx is {}".format(strx_fst_ind))

str_x = " "

strx_zeroth_ind = str_x[0]
print("The zeroth index value of strx is {}".format(strx_zeroth_ind))

# Slicing all from right to laft

str_m = "laptop"

ind1_to_all = str_m[1:]
print("The value of slicing of ind1 to all is {}".format(ind1_to_all))

ind4_to_all = str_m[4:]
print("The value of slicing of ind4 to all is {}".format(ind4_to_all))

till_ind5 = str_m[:5]
print("The value of slicing till ind5 is {}".format(till_ind5))

till_ind3 = str_m[:3]
print("The value of slicing till ind3 is {}".format(till_ind3))

# Reverse indexing

str_p = "computer"

ind1_neg = str_p[-1]
print("The value of negative ind1 is {}".format(ind1_neg))

ind3_neg = str_p[-3]
print("The value of negative ind3 is {}".format(ind3_neg))

ind6_neg = str_p[-6]
print("The value of negative ind6 is {}".format(ind6_neg))

# To reverse whole word

str_c = "strings"
str_p = "computer"

str_rev = str_c[::-1]
print("The value of str c after reversing is {}".format(str_rev))

str_rev = str_p[::-1]
print("The value of str p after reversing is {}".format(str_rev))

# Reverse slicing

str_e = "python"
str_d = "welcome"

str_e_slc = str_e[5:1:-1]
print("The value of slicing from one to five in reverse format is {}".format(str_e_slc))

str_d_slc = str_d[6:1:-1]
print("The value of slicing from one to six in reverse format is {}".format(str_d_slc))

# String concatenation

str1 = "welcome"
str2 = "ujwal"

str_res = str1+" "+str2
print("The value after concatenation is {}".format(str_res))

# Capitalize - it will capitalize first character of string

str_a = "python"
a = str_a.capitalize()
print("The value after capitalize is {}".format(a))

# Upper case - It will change whole characters into uppercase

str_b = "comPuTer"

upp_case = str_b.upper()
print("The value of str_b using uppercase is {}".format(upp_case))

# Lower case - It will change all the characters into lowercase

str_c = "LAPTOP"

low_case = str_c.lower()
print("The value of str_c using lowercase is {}".format(low_case))

str_d = "hello"

res = str_d[0:2]+str_d[2:4].upper()+str_d[-1]
print("The value after capitalizing only 1 is {}".format(res))

# To check whether given string is upper or lower

str_upp = "software"
str_low = "software"
print("The string is upper {}".format(str_upp.isupper()))
print("The string is upper {}".format(str_low.islower()))

# Title - it will convert into title

str_f = "welcome to python class"
tit_str = str_f.title()

print("The value str_f into title is {}".format(tit_str))

# To check whether it is title or not

str_f = "welcome to python class"
tit_str = str_f.title()

print("The string is title {}".format(str_f.istitle()))
print("The string is title {}".format(tit_str.istitle()))

# Count

str_g = "welcome"

print("The count of w in str_g is {}".format(str_g.count("w")))
print("The count of e in str_g is {}".format(str_g.count("e")))

# Index

str_h = "welcome to class"
print("The index value of c in str_g is {}".format(str_g.index("c")))
print("The index value of l in str_g is {}".format(str_g.index("l")))

# Starts with & Ends with

str_i = "Hello everyone"

print("The value is starting with H is {}".format(str_i.startswith("H")))
print("The value is starting with e is {}".format(str_i.startswith("e")))

print("The value is ending with e is {}".format(str_i.endswith("e")))
print("The value is ending with o is {}".format(str_i.endswith("o")))

# split :- splitting the words, it creates a list

str_a = "welcome to class"
str_a_split = str_a.split(" ")
print("The value of str_a after splitting is {}".format(str_a_split))

print("The type after splitting is {}".format(type(str_a_split)))

# Join :- To convert list to sentence or to combine the list

str_b = " ".join(str_a_split)
print("The value after joining is {}".format(str_b))

str_c = "John. Welcome!"
str_c_spl = str_c.split(".")
print("The value after splitting string with . is {}".format(str_c_spl))