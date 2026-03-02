"""
chapter02_01
Python Advanced(1) - Python Variable Scope
Keyword - scope, global, nonlocal, locals, globals
"""

"""
전역변수 : 주로 변하지 않는 고정 값에 사용 (지역 내에서 수정되는 것은 권장되지 않음)
    - 생성시점 : 프로그램이 실행되면서 해당 변수 선언문에 도달할 때 생성
    - 소멸 시점 : 프로그램 전체 종료 또는 Python Interpreter가 닫힐때
    - 특징 : 프로그램 어디서든 접근 가능하나 너무 많이 쓰는 경우 관리가 어려워짐

지역변수 : 지역변수는 함수 내에 로직 해결에 국한하여 사용 / 소멸주기 : 함수 실행 해제 시
    - 생성시점 : 함수가 호출되어 실행될 때 메모리에 생성
    - 소멸시점 : 실행한 함수가 종료되는 즉시 메모리에서 삭제
    - 특징 : 함수 외부에서는 접근 불가하며, 함수가 실행될 때마다 새로 만들어지고 사라짐
"""

# ex 1)
a = 10  # Global variable

def foo() :
    # Read global variable
    print('ex 1 : ', a) # 10

foo()

# Read global variable
print('ex 1 : ', a)     # 10

# global variable은 함수 내/외부 모두 접근 가능
print('----------')

# ex 2)
b = 20
def bar() :
    b = 30  # Local variable
    print('ex 2 : ', b) # 30
    
bar()
print('ex 2 : ', b)
# scope 안에 Local variable이 있는 경우 해당 값 먼저 참조
# scope 밖에 Global variable이 있는 경우 해당 값 참조 (없는 변수를 밖에서 참조하는 경우 에러 발생)
print('----------')

# ex 3)
c = 40

def foobar() :
    # c = c + 10
    print('ex 3 : ', c) # UnboundLocalError

foobar()
print('----------')

# ex 4)
d = 50
def barfoo() :
    global d    # global 예약어를 사용하면 전역변수 참조 값 상관없이 값 변경 가능
    d = 60
    d += 100
    print('ex 4 : ', d) # 160

barfoo()

# ex 5) ** 중요
# 지역변수 안에 지역변수의 변수명이 동일한 경우 'nonlocal' 사용
def outer() :
    e = 70
    def inner() :
        nonlocal e
        e += 10
        print('ex 5 : ', e) # UnboundLocalError
    return inner

in_test = outer()   # Closure
in_test()   # 80
in_test()   # 90 
in_test()   # 100 ... 계속 증가

# ex 6)
def func(var) :
    x = 10
    def printer() :
        print('ex 6 : ', 'Printer Func Inner')
    print('Func Inner', locals())   # func() 영역에 있는 객체들을 확인할 수 있음 (지역 전체 출력)

func('Hi')


# ex 7)
print('ex 7 : ', globals()) # 전역에 존재하는 객체 모두 출력 (전역 전체 출력)


# ex 8)
# 지역 -> 전역 변수 생성
for i in range(1, 10) :
    for k in range(1, 10) :
        globals()[f'plus_{i}_{k}'] = i + k

print(globals())

# 변수를 선언하지 않아도 전역에 선언해두었기 때문에 출력 가능
print(plus_5_5) # 10
print(plus_9_2) # 11