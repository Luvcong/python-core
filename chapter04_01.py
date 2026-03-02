"""
chapter04_01
Python Advanced(3) - Meta Class(1)
Keyword - Class of Class, Type, Meta Class, Custom Meta Class
"""

"""
Meta Class : 클래스를 생성하는 클래스 (class of class)
=> 클래스의 동작과 생석 방식을 정의하는 클래스
=> 일반 객체를 만드는 것이 클래스라면, 메타 클래스는 클래스를 만드는 것

- 기본 메타 클래스 : type
- 클래스 정의 시점에 개입하여 클래스 생성 로직을 제어

주요 목적
- 클래스 구조 검증 (필수 메서드 / 속성 강제)
- 자동 속성 등록 및 메타데이터 수집
- 클래스 생성 규칙 통제 (네이밍, 상속 구조 등)
"""

# ex 1) Type
class SampleA() :   # Class == Object
    pass

obj1 = SampleA()    # 인스턴스화 -> 변수에 할당 및 복사 가능, 새로운 속성 추가 가능 / 함수의 인자로 넘기기 가능

# obj1 -> SampleA instance
# SampleA -> type meta class
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
    print(f'ex 2 : {type(o)}, {type(o) is o.__class__, o.__class__.__class__}') # <class '__main__.SampleB'>, (True, <class 'type'>)

# 여러 자료형의 type 확인
for t in int, float, list, tuple :  
    print('ex2 : ', type(t))    # <class 'type'>

print('ex 2 : ', type(type))    # <class 'type'>