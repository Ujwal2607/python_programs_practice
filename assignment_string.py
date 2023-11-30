# Assignment

# Find length and index

str_y = "welcome to class"

len_str = len(str_y)
print("The length of string is {}".format(len_str))

# Indexing

stry_zeroth_ind = str_y[0]
print("The zeroth index value of stry is {}".format(stry_zeroth_ind))

stry_fst_ind = str_y[1]
print("The fst index value of stry is {}".format(stry_fst_ind))

stry_snd_ind = str_y[2]
print("The snd index value of stry is {}".format(stry_snd_ind))

stry_trd_ind = str_y[3]
print("The trd index value of stry is {}".format(stry_trd_ind))

stry_fourth_ind = str_y[4]
print("The fourth index value of stry is {}".format(stry_fourth_ind))

stry_fifth_ind = str_y[5]
print("The fifth index value of stry is {}".format(stry_fifth_ind))

stry_sixth_ind = str_y[6]
print("The sixth index value of stry is {}".format(stry_sixth_ind))

stry_svth_ind = str_y[7]
print("The svth index value of stry is {}".format(stry_svth_ind))

stry_eighth_ind = str_y[8]
print("The eighth index value of stry is {}".format(stry_eighth_ind))

stry_ninth_ind = str_y[9]
print("The ninth index value of stry is {}".format(stry_ninth_ind))

stry_tenth_ind = str_y[10]
print("The tenth index value of stry is {}".format(stry_tenth_ind))

stry_eleventh_ind = str_y[11]
print("The eleventh index value of stry is {}".format(stry_eleventh_ind))

stry_twth_ind = str_y[12]
print("The twth index value of stry is {}".format(stry_twth_ind))

stry_thirteenth_ind = str_y[13]
print("The thirteenth index value of stry is {}".format(stry_thirteenth_ind))

stry_fourteenth_ind = str_y[14]
print("The fourteenth index value of stry is {}".format(stry_fourteenth_ind))

stry_fifteenth_ind = str_y[15]
print("The fifteenth index value of stry is {}".format(stry_fifteenth_ind))

#Slicing

str_y = "welcome to class"

ind1_to_ind5 = str_y[1:5]
print("The value of string from first to fifth is {}".format(ind1_to_ind5))

ind0_to_ind9 = str_y[0:9]
print("The value of string from zero to ninth is {}".format(ind0_to_ind9))

ind3_to_ind15 = str_y[3:15]
print("the value of string from third to fifteenth is {}".format(ind3_to_ind15))

#Slicing with step size

str_z = "python practice"

len_str = len(str_z)
print("The length of string z is {}".format(len_str))

slc_with_stp2 = str_z[0:15:2]
print("The value of slicing str z using step size 2 is {}".format(slc_with_stp2))

slc_with_stp2 = str_z[2:15:2]
print("The value of slicing str z using step size 2 is {}".format(slc_with_stp2))

slc_with_stp3 = str_z[0:15:3]
print("The value of slicing str z using step size 3 {}".format(slc_with_stp3))

str_x = "welcome to python"
tit_str = str_x.title()

print("the string is title {}".format(str_x.istitle()))
print("the string is title {}".format(tit_str.istitle()))

str_u = "Hello, welcome to class"
print("the count of l in string is {}".format(str_u.count("l")))

print("index value of w in str u is {}".format(str_u.index("w")))
print("index value of l in str u is {}".format(str_u.index("l")))