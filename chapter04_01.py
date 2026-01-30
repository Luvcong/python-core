"""
chapter04_01
Python Advanced(3) - Meta Class(1)
Keyword - Class of Class, Type, Meta Class, Custom Meta Class
"""

"""
Meta Class
1) 클래스를 만드는 역할 -> 의도하는 방향으로 클래스 커스텀
2) 프레임워크 작성 시 필수
3) 동적 생성(type 함수), 커스텀 생성(type 상속)
4) 커스텀 클래스 -> 검증 클래스 등
5) 엄격한 Class 사용 요구, 메서드 오버라이드 요구
"""

# ex 1) Type
class SampleA() :   # Class == Object
    pass

obj1 = SampleA()    # 인스턴스화 -> 변수에 할당 및 복사 가능, 새로운 속성 추가 가능 / 함수의 인자로 넘기기 가능

# obj1 -> SampleA instance
# SampleA -> type metaclass
# type -> type meta class
print('ex 1 : ', obj1.__class__)    # <class '__main__.SampleA'>
print('ex 1 : ', type(obj1))
print('ex 1 : ', obj1.__class__ is type(obj1))  # True
print('ex 1 : ', obj1.__class__.__class__ is type(obj1).__class__)  # True

print('ex 1 : ', obj1.__class__.__class__)

# ex 2)
# type meta (ex1 증명)

# int, dict
n = 10
d = {'a' : 10, 'b' : 20}
print('----------')

class SampleB() :
    pass

obj2 = SampleB()
for o in (n, d, obj2) :
    print(f'ex 2 : {type(o)}, {type(o) is o.__class__, o.__class__.__class__}')

for t in int, float, list, tuple :
    print('ex2 : ', type(t))

print('ex 2 : ', type(type))