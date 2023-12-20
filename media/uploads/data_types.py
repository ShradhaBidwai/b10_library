import copy

# l1 = [10,20,30,40,50, [60,70]]

# shallow copy -- list alias, cloning, copy
# deepcopy -- 

# l2 = copy.deepcopy(l1)

# l1[5][0] = 600

# print(l1)
# print(l2)

# print(id(l1[5]))
# print(id(l2[5]))




# print(l1)
# l2 = l1  # list aliasing

# l2 = l1[::]  # list cloning

# l2 = l1.copy()  # list cloning

# l2.append(60)

# print(l1, l2)



# print(id(l1))
# print(id(l2))



# DRY -- Do not repeat Yourself --> 


# lst1 = lst[::-1]

# print(lst1)

# lst.sort(reverse=True)  # 
# print(lst)

# lst.reverse()
# print(lst)

# print(lst)

# for i in lst: # 10
    # lst.remove(i)  #

# print(lst)


# del lst[3]

# res = lst.pop(4)

# lst.pop()

# lst.pop()


# lst.pop()





# del lst[25]  # 

# print(lst)

# lst[0] = 100
# print(lst)

# print(dir(lst))  # 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort
# lst.append(70)
# lst.append("abcd")
# lst.append((7,8,9))

# print(lst)
# print(lst.count(90))
# print(lst.index(60, 6, 9))

# lst.insert(2, 100)
# print(lst)



# lst.extend("abcd")
# lst.extend([7,8,9])
# lst.extend({1:10, 2:20,3:30})

# lst.clear()

# print(lst)

# print(dir(tuple))

# print(dir(set)) # 'add', 'clear', 'copy', 'difference', 'difference_update', 'discard', 'intersection', 'intersection_update', 'isdisjoint', 'issubset', 'issuperset', 'pop', 'remove', 'symmetric_difference', 'symmetric_difference_update', 'union', 'update' 
# set
# - does not allow duplicate -- done
# - does not preserve insetion order -- done
# - only allows immutable elements -- done , if mutable element is used, error: unhashable
# - no index based operation - Done
# - no slicing - done
# - homogen + hetro - done
# - mathmatical operations


# s1 = {10, 50, "a", "z", "q", 2, 90,(4,5,6), "o", "a"}

# res = s1.pop()
# print(res)
# print(s1)
# s1.discard((4,5,6))

# s1.remove(5000)
# s1.discard(5000)

# s1.clear()
# print(s1)

# s1.add([44,5,6,6])

# s1.update("jklmno", [1,2,3,4])

# s1.add("f")
# print(s1)


# print(s1[::])


# s1 = {10,20,30,40}
# s2 = {20,30,50,60, (4,5,6)}

# s3 = s1.union(s2)

# s3 = s1 | s2
# print(s3)


# s1 = {10,20,30,40}
# s2 = {20,30,50,60}


# s3 = s1.symmetric_difference(s2)
# print(s3)


# s3 = s2.difference(s1)  # s2 - s1
# print(s3)



# s3 = s1.intersection(s2)
# s3 = s1 & s2

# print(s3)





# comprehension -- 

# l1 = []

# lst = [1,2,3,4,5,6,7,8,9, 10,11,12,13] # 5 sec

# pairs = {(x, y) for x in range(1, 4) for y in range(10, 13)}
# print(pairs)


# dct = {i: i**3 for i in range(65, 91)}
# print(dct)

# dct = {chr(i): chr(i).lower() for i in range(65, 91)}  A - Z
# print(dct)

# d1 = {}  # dict()
# for i in range(1, 11):
#     d1[i] = i ** 2

# print(d1)






# l = []
# for x in range(1, 4):
#     for y in range(10, 13):
#         l.append((x, y))

# print(l)

# l3 = [(i, "even") if i%2 == 0 else (i, "odd") for i in lst]
# print(l3)

# l2 = [chr(i) * 3 for i in range(65, 91)]
# l2 = [(chr(i), chr(i+32)) for i in range(65, 91)]


# for i in range(97, 123):
    # l2.append(chr(i))

# print(l2)

# print(ord("Z"))

# print(chr(85))


# l1 = [i**3 for i in lst]


# l1 = [i for i in lst if i % 2 != 0]
# print(l1)


# l1 = list()  # []
# for i in lst:
#     if i % 2 != 0:
#         l1.append(i)

# print(l1)


# key , value par
# key can not be duplicated
# values -- duplicate
# key -- only immutable elements

# l1 = list()
# for x in range(0, 51):
    # if x % 2 == 0:
        # print(x)


#  'clear', 'copy', 'fromkeys', 'get', 'items', 'keys', 'pop', 'popitem', 'setdefault', 'update', 'values'

# python 3.6 onwards  -- order 
# d1 = {"key1": "value1", "key2": "value2", "key3": "value3", "key4": "value4"}  # key5: None

# res = d1.setdefault("key5", 0)
# print(res)
# print(d1)

# d3 = {}.fromkeys([1,2,3,4], [10,20,30])
# print(d3)



# d1["key5"] = "value5"
# d1["key1"] = "v1"

# print(d1)


# print(d1[0])
# res = d1.pop("key1")
# print(res)
# d1.popitem()
# d1.popitem()

# print(d1)

# all_keys = list(d1.keys())
# print(all_keys)

# all_values = list(d1.values())
# print(all_values)

# res = list(d1.items())  # list of tuples -- 
# print(res)

# for key, value in d1.items():  # [("key1", "value1"), ("key2", "value2"), ("key3", "value3"), ("key4", "value4")]
    # print(key, value)

# print(all_keys, type(all_keys))

# d1.clear()
# d2 = d1.copy()

# print(id(d1), id(d2))

# 3-4 hrs

# print(dir(d1))

# print(d1["key2"])  # KeyError  -- key2 present nasel tar , KeyError yeto

# print(d1.get("key2", 0))  # None, 


# print("completed")

# d1["key1"] = "v1"
# print(d1)

# d2 = {}  # dict()

# d2["a"] = "A"
# d2["b"] = "B"
# d2["a"] = "AA"

# print(d2) # {"a": "AA", "b":"B"}



