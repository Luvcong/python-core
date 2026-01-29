"""
chapter02_02
Python Advanced(1) - Lambda, Reduce, Map, Filter Functions
Keyword - lamdba, reducem, map, filter
"""

"""
lambda 장점 : 익명으로 사용, 힙 영역에서 사용 즉시 소멸(메모리 절약 가능), pythinic, 가비지컬렉션(count = 0)
              시퀀스형 전처리에 Reduce, Map, Filter 주로 사용
- 일반 함수 : 재사용성을 위해 메모리 저장이 필요할 떄 사용
"""

# ex 1)
cul = lambda a, b, c : a + b + c
print(cul(1, 2, 3))
print('----------')

# ex 2) map
digits1 = [x * 10 for x in range(1, 11)]
print('ex 1 : ', digits1)

# def ex2_func(x) :
#     return x ** 2

# map(function, interable)
result = list(map(lambda i : i ** 2, digits1))
print('result : ', result)
print('----------')

def also_square(nums) :
    def double(x) :
        return x ** 2
    return map(double, nums)

print('ex 2 : ', list(also_square(digits1)))
print('----------')

# ex 3) filter
digits2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result = list(filter(lambda x : x % 2 == 0, digits2))
print('ex 3 : ', result)    # [2, 4, 6, 8, 10]
print('----------')

# lambda 없이 직접 함수 구현 시
def also_evens(nums) :
    # print('nums : ', nums)    # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    def is_even(x) :
        # print('x : ', x)      # 1 ...
        return x % 2 == 0
    return filter(is_even, nums)

print('also_evens : ', list(also_evens(digits2)))   # [2, 4, 6, 8, 10]
print('----------')

# ex 4) reduce : 누적 연산자
# reduce(function, iterable)
from functools import reduce
digits3 = [x for x in range(1, 101)]
result = reduce(lambda x, y : x + y, digits3)
print('ex 4 : ', result)

def also_add(nums) :
    def add_plus(x, y) :
        return x + y
    return reduce(add_plus, nums)