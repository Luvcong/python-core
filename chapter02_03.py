"""
chapter02_03
Python Advanced(1) - Shallow Copy & Deep Copy
Keyword - shallow & deep cody
"""

"""
객체의 복사 종류 : Copy, Shallow Copy, Deep Copy

Immutable: int, float, tuple, str...
Mutable: dic, list, set...

추가 메모)
- call by value : 값을 복사해서 전달 -> 매개변수 재할당 가능 / 객체 내부 값 변경 시, 호출자 영향 없음 (Python에는 존재하지 않음)
- call by reference : 변수 자체의 참조 값 전달 -> 매개변수 재할당 가능 / 객체 내부 값 변경 시, 호출자 영향 있음 (원본 변경, Python, Java에는 존재하지 않는 방식)

** Python에는 call by value, call by reference 구분이 없음 (call by object reference 모델 사용)
** 객체의 불변성에 따라 재할당 및 객체 변경 여부가 달라짐 (재할당은 항상 호출자에 영향 없음)
- Imutable : 재할당 가능 / 객체 변경 불가
- Mutable  : 재할당 가능 / 객체 변경 가능

- call by object reference (call by value of reference)
  : 객체의 참조 값을 복사해서 전달 -> 매개변수 이름은 새로운 로컬 변수 (객체 자체 변경은 가능) / 변수 재할당은 호출자 영향 없음
  : 객체의 변경 가능 여부는 객체의 불변성에 따라 결정
"""

# ex1) Copy
# mutagble : list, set, dict ...

a_list = [1, 2, 3, [4, 5, 6], [7, 8, 9]] # mutable
b_list = a_list
print((id(a_list), id(b_list)))

# 동일한 주소 값이기 때문에 a_list, b_list 모두 수정됨
b_list[2] = 100
print(a_list)   # [1, 2, 100, [4, 5, 6], [7, 8, 9]]
print(b_list)   # [1, 2, 100, [4, 5, 6], [7, 8, 9]]

b_list[3][2] = 100
print(a_list)
print(b_list)

# immutable : int, str, float, bool, unicode ... 불변형 자료구조


# ex 2) Shallow Copy (얕은복사)
import copy

c_list = [1, 2, 100, [4, 5, 6], [7, 8, 9]]
d_list = copy.copy(c_list)
print('----------')

# id 값 상이
print('ex 2 : ', id(c_list))
print('ex 2 : ', id(d_list))
print('----------')

d_list[1] = 100
print('Ex2 : ', c_list) # [1, 2, 100, [4, 5, 6], [7, 8, 9]]
print('Ex2 : ', d_list) # [1, 100, 100, [4, 5, 6], [7, 8, 9]]
print('----------')

# 얕은 복사의 문제점
d_list[3].append(1000)
d_list[4][1] = 10000
# 가변형 객체 안에 있는 리스트는 복사되지 않아 참조 값이 동일하기 때문에 내부 값을 수정하는 경우 변경된
print('Ex2 : ', c_list) # [1, 2, 100, [4, 5, 6, 1000], [7, 10000, 9]]
print('Ex2 : ', d_list) # [1, 100, 100, [4, 5, 6, 1000], [7, 10000, 9]]
print('----------')


# ex 3) Deep Coly (깊은복사)
e_list = [1, 2, 3, [4, 5, 6], [7, 8, 9]]
f_list = copy.deepcopy(e_list)

# id 값 상이
print('ex 3 : ', id(e_list))
print('ex 3 : ', id(f_list))
print('----------')

f_list[3].append(1000)
f_list[4][1] = 10000
print('ex 3 : ', e_list)
print('ex 3 : ', f_list)