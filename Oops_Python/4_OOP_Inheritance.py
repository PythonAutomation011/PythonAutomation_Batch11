class A:
    pass
class B:
    pass
class C:
    pass
class X(A,B):
    pass
class Y(B,C):
    pass
class P(X,Y,C):
    pass
# print('A',A.mro())
# print('B',B.mro())
# print('C',C.mro())
# print('X',X.mro())
# print('Y',Y.mro())
# print('P',P.mro())