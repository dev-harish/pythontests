# class A:
#     def whereiam(self):
#         print("I am in A")
#
#
# class B(A):
#     def whereiam(self):
#         pass
#
#
# class C(A):
#     def whereiam(self):
#         pass
#
# class D(B, C):
#     def whereiam(self):
#         pass
#     # def __mro__(self):
#     #     print("dsds")
#
# # print(D.__mro__)

#
# class Animal:
#     def __init__(self, animalName):
#         print(animalName, 'is an animal.');
#
#
# class Mammal(Animal):
#     def __init__(self, mammalName):
#         print(mammalName, 'is a warm-blooded animal.')
#         super().__init__(mammalName)
#
#
# class NonWingedMammal(Mammal):
#     def __init__(self, NonWingedMammalName):
#         print(self)
#         print(NonWingedMammalName, "can't fly.")
#
#         super().__init__(NonWingedMammalName)
#
#
# class NonMarineMammal(Mammal):
#     def __init__(self, NonMarineMammalName):
#         print(NonMarineMammalName, "can't swim.")
#         print(super())
#         super().__init__(NonMarineMammalName)
#         print("dsdd")
#
#
# class Dog(NonMarineMammal, NonWingedMammal):
#     def __init__(self):
#         print('Dog has 4 legs.');
#         print(super())
#         super().__init__('Dog')
#
#
#
# d = Dog()
# print(Dog.mro())
# print(Dog.__mro__)
# print(NonMarineMammal.__mro__)
# print('')
# bat = NonMarineMammal('Bat')



class X:pass
class Y(X): pass
class Z(X):pass
class A(X,Y):pass
class B(Y):pass
class M(B,A,Z):pass

print(M.__mro__)
