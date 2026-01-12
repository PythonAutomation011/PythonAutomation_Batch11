'''
        Tuple

        1 immutable in nature ------> but will going on different location

        fixed in nature

        t1=(10,20,30)    ---- 3

        s2 internally supports the array
            index position
            positive  0 to len-1

            negative  -1 to -len

            slice [start:end:step]

        3 tuple is iterable in nature

        4 tuple is collection of homo+hetro

        5 tuple always consider the ordering input --- output

        6 unique and duplicate we can inside the tuple


        How to create the tuple

        t1=10,20,30 or t1=(10,20,30) or t1=tuple([10,20,30])



        how to read
        name of tuple
        t1[index] -----
        slice [start:end:step]


    index(object) -----> index position of object

    count(count) ------> number of occurance of object



fixed in nature----> tuple


day of week 7

month of year 12

data duplicates in future wo data change ho -----> list
data duplicates but in future wo change no-----> tuple



1 write the difference between list and tuple ??
    list                  tuple
    [] or list()          ,, or (,) or tuple()
    mutable                 immutable
    UD                      Doesnt have UD
                            index,count

                            faster than list ???
    list size is always greater than tuple size

    index                   index
    slice                   slice


l1=(10,20,30,40)

want to search 40 inside l1

'''


# l1=[10,20,30,1,s2,3,4,5,(10,20,30)]
# print(l1,len(l1))
# l1.append(100)
# print(l1,len(l1))

t1=(10,20,30,1,2,3,4,5,[10,20,30])
print(t1,len(t1))

t1[-1].clear()
print(t1,len(t1))