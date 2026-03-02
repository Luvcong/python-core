"""
chapter03_02
Python Advanced(2) - Property(1) : Underscore
Keyword - access modifier(접근지정자), underscore
"""

"""
다양한 언더스코어 활용
파이썬 접근지정자 설명
"""

# ex 1)
# Use underscore
# 인터프리터, 값 무시, 네이밍(국재화, 자릿수 등)... 등

# Unpacking
x, _, y = [1, 2, 3]
print(x, y) # 1 3

# a, i, b = (1, 2, 3, 4, 5)
# print(a, b, i)  # ValueError

# Packing
a, *i, b = (1, 2, 3, 4, 5)
print(a, b, i)  # 1 5 [2, 3, 4]
print('ex 1 : ', x, y, a, b)

# for문에서의 underscore 사용 (1)
for _ in range(19) :    # unpaking 값을 사용하는게 아니라 반복만 수행할 경우에도 사용 가능
    pass

# for문에서의 underscore 사용 (2)
# enumerate() : 반복 가능한 객체에 인덱스를 붙임
for _, val in enumerate(range(10)) :  # [(0,0), (1,1), (2,2), ..., (9,9)]
    pass
print('----------')

# ex 2)
# 접근지정자
# python에는 Java 등과 달리 강제 접근 제한 문법이 없음 => 대신 '관례 + 네이밍 규칙'으로 제어

# name   : public
# _name  : protected
# __name : private

# 타 클래스(클래스 변수, 인스턴스 변수 값 쓰기 장려 안함) ->  Nameing Mnagling
# 타 클래스 __ 접근하지 않는 것이 원칙

# No user Property
class SampleA :
    def __init__(self) :
        self.x = 0   # 어디서든 접근 가능 (제약 없음)
        self.__y = 0 # 내부적으로 Name Mangling 발생 (private처럼 보이도록 python이 자동으로 이름을 변경 : _SampleA__y)
        self._z = 0  # 실제로는 접근 가능하나 외부에서 접근하지 않는 것이 좋다는 의미로 사용

a = SampleA()
a.x = 1

print(f'ex 2 : {a.x}')
# print(f'ex 2 : {a.__y}')  # AttributeError
print(f'ex 2 : {a._z}')
print('----------')

print(dir(a))   # _SampleA__y / _z / x ...

a._SampleA__y = 2
print(f'{a._SampleA__y}')   # 2 (0 -> 2로 변경되어 출력 : 값 변경에 강제성은 없음)
print('----------')

# ex 3)
# method 활용 (Getter, Setter)
# 외부에서는 변수처럼 보이고, 내부에서는 메서드로 제어됨
class SampleB :
    def __init__(self) :
        self.x = 0
        self.__y = 0    # __SampleB__y

    def get_y(self) :
        return self.__y
    
    def set_y(self, value) :
        self.__y = value

b = SampleB()
b.x = 1
print(b.get_y())    # 0

b.set_y(5)
print(b.get_y())    # 5