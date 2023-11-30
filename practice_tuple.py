# tuple

tpl_a = ("a", "b", 1, "python")
print("The items of tuple is {}".format(tpl_a))

# Length of tuple
len_tpl_a = len(tpl_a)
print("The length of tuple a is {}".format(len_tpl_a))

# Type of tpl
type_tpl_a = type(tpl_a)
print("The type is {}".format(type_tpl_a))

# indexing

ind0_tpl_a = tpl_a[0]
print("Zeroeth element of tuple a is {}".format(ind0_tpl_a))
ind1_tpl_a = tpl_a[1]
print("First element of tuple a is {}".format(ind1_tpl_a))
ind2_tpl_a = tpl_a[2]
print("Second element of tuple a is {}".format(ind2_tpl_a))
ind3_tpl_a = tpl_a[3]
print("Third element of tuple a is {}".format(ind3_tpl_a))

# index

tpl_b = ("John", "Alex", "Bob", "xyz")
ind_bob = tpl_b.index("Bob")
print("The index value of bob is {}".format(ind_bob))

# count

cnt_john = tpl_b.count("John")
print("The count of John in tuple b is {}".format(cnt_john))
