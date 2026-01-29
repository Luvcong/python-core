"""
chapter03_03
Python Advanced(2) - Property(2) : Method Overloading
Keyword - overloading, oop, multiple dispatch
"""

"""
메서드 오버로딩 효과
1) 동일 메서드 재정의
2 ) 네이밍으로 기능 예측
3) 코드 절약 및 가독성 향상
4) 메서드 파라미터 기반 호출 방식
"""

# ex 1)
# 동일 이름 메서드 사용
# 동적 타입 검사 -> 런타임 시 실행되고, 타입 에러가 실행 시에 발견 (타입 에러가 실행 시 발생)

class SampleA() :
    def add(self, x, y) :
        return x + y
    
    def add(self, x, y, z) : 
        return x + y + z
    
    # 참고 - packing으로도 사용 가능
    # def add(self, *args) :
        # return sum(args)

a = SampleA()
# print('ex 1 : ', a.add(2, 3))   # TypeError

# 모든 속성 개체 확인
print('ex 1 : ', dir(a))
print('----------')

# ex 2)
# 동일 이름 메서드 사용
# 자료형에 따른 분기 처리
class SampleB() :
    def add(self, datatype, *args) :
        if datatype == 'int' :
            return sum(args)
        
        if datatype == 'str' :
            return ''.join([x for x in args])
        
b = SampleB()
print('ex 2 : ', b.add('int', 5, 6))
print('ex 2 : ', b.add('str', 'Hi', ' ', 'Python'))
print('----------')

# ex 3)
# multipledispatch
# 함수명이 중요한 것이 아니라 파라미터의 자료형이 중요
from multipledispatch import dispatch

class SampleC() :
    @dispatch(int, int)
    def product(x, y) :
        return x * y
    
    @dispatch(int, int, int)
    def product(x, y, z) :
        return x * y * z
    
    @dispatch(float, float, float)
    def product(x, y, z) :
        return x * y * z
    
c = SampleC()
print('ex 3 : ', c.product(5, 6))
print('ex 3 : ', c.product(5, 6, 7))
print('ex 3 : ', c.product(2.5, 6.0, 3.5))