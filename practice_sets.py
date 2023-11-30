"""
What is sets?
Set is mutable, but items inside set is unchangeable, it is unordered, unindexed collection of item.
Set is enclosed b/w {}. Set doesn't allow duplicates.
Note: internally items of set is mapped to hash key
"""

empty_set = set()
print("The value of set is {}".format(empty_set))

"""

Difference b/w lists and sets
Lists:-
*List is ordered collections
*List can have duplicates
*Existing items of list can be changed
*List is slow compared to set.(If we fetch an item from list it iterates through all the index)

Sets:-
*Sets are unordered collections
*Sets doesn't have duplicates
*Existing items of sets can't be changed
*Set is faster compared to list (Internally Set is mapped to hash key)

"""

set_a = {"a", 1, "b", 2}

# add - we can add single item to set

set_a.add("c")
print("The value after adding c is {}".format(set_a))

# update - we can add multiple items to set

set_a.update((3,4))
print("The value after updating is {}".format(set_a))

# remove - it removes element from the set.
#           it throws an error if the element is not present in the set

set_a.remove("c")
print("The value after removing is {}".format(set_a))

# discard - it removes the specified item from the set
#           it returns none if element is not present

set_a.discard("b")
print("The value after discarding is {}".format(set_a))

set_a = set_a.discard("c")
print("The value after discarding is {}".format(set_a))

# pop - it will delete some random item in set

set_b = {"a", "b", "c", 1, 2}

set_b.pop()
print("The value of set a after popping is {}".format(set_b))

# clear - it will delete all the elements in the set

set_b.clear()
print("THe value after clearing is {}".format(set_b))

# union of set

set_x = {1, 2, 3}
set_y = {4, 5}

union_set = set_x.union(set_y)
print("The value of union of sets is {}".format(union_set))

# intersection of sets - both sets having same element

set_x = {1, 2, 3}
set_y = {3, 4, 5}

intersection_set = set_x.intersection(set_y)
print("The value of intersection of sets is {}".format(intersection_set))

set_z = {1, 2, 3, 4, 5}

set_c = frozenset(set_z)
print("The value after freezing is {}".format(set_c))

# removing duplicates in list

lst_a = {1, 2, 3, 2, 5, 1}
lst_b = list(set(lst_a))
print("The value after removing is {}".format(lst_b))
