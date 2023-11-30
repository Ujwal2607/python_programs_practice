# Assignment

tpl_x = ("u", "j", "@2607", 0, 7)
print("The items is {}".format(tpl_x))

# length of the tuple

len_tpl_x = len(tpl_x)
print("The length of tuple x is {}".format(len_tpl_x))

# type of tuple

type_tpl_X = type(tpl_x)
print("The type is {}".format(type_tpl_X))

# indexing

tpl_zeroth_ind = tpl_x[0]
print("The zeroth index value of tpl x is {}".format(tpl_zeroth_ind))

tpl_first_ind = tpl_x[1]
print("The first index value of tpl x is {}".format(tpl_first_ind))

tpl_second_ind = tpl_x[2]
print("The second index value of tpl x is {}".format(tpl_second_ind))

tpl_third_ind = tpl_x[3]
print("The third index value of tpl x is {}".format(tpl_third_ind))

tpl_fourth_ind = tpl_x[4]
print("The fourth index value of tpl x is {}".format(tpl_fourth_ind))

# slicing

ind0_to_ind3 = tpl_x[0:3]
print("The value of tuple from zeroth to third is {}".format(ind0_to_ind3))

ind2_to_ind5 = tpl_x[2:5]
print("The value of tuple from first to fifth is {}".format(ind2_to_ind5))

# slicing with step size

slc_with_stp2 = tpl_x[0:5:2]
print("The value of slicing of tpl x with step size 2 is {}".format(slc_with_stp2))

slc_with_stp3 = tpl_x[0:5:3]
print("The value of slicing of tpl x with step size 3 is {}".format(slc_with_stp3))