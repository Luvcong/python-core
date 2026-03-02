"""
chapter04_04
Python Advanced(3) - Descriptor(1)
Keyword - descriptor, set, get, del, property
"""

'''
Descriptor : 객체 속성 접근을 가로채는 매커니즘
- 클래스 속성으로 정의된 객체가 __get__, __set__, __delete__ 중 하나 이상을 구현하면 descriptor로 동작
- 속성의 Read, Write, Delete 동작을 제어할 수 있음

- Data Descriptor     : __get__ + (__set 또는 __delete)
- Non-Data Descriptor : __get__만 구현

- descriptor 메서드는 python 인터프리터가 자동 호출
- 호출 시그니처는 언어 차원에서 고정되어 있음 (__get__(self, obj, objtype) 등..)
- 인스턴스 속성 접근 시, 일반 변수처럼 보이지만 내부적으로 메서드가 실행됨

- 읽기 전옹 속성 구현 가능
- 타임 검증 및 값 제어 가능
- 계산 속성 구현 가능
- 클래스 설계를 의도한 방향으로 강제 가능
- property는 대표적인 descriptor 구현체
'''

# ex 1) 기본적인 Descriptor 예제
# Descriptor 구현
class DescriptorEx1() :
    def __init__(self, name='Default') :
        self.name = name
    
    def __get__(self, obj, objtype) :   # 파라미터 개수가 3개로 고정되어 있음
        return f'Get Method Calld -> self : {self}, obj : {obj}, obj type : {objtype}, name : {self.name}'
    
    def __set__(self, obj, name) :      # 파라미터 개수가 3개로 고정되어 있음
        print('Set method called')
        if isinstance(name, str) :
            self.name = name
        else :
            raise TypeError('Name should be string')
    
    def __delete__(self, obj) :         # 파라미터 개수가 2개로 고정되어 있음
        print('Delete method called')
        self.name = None

# Descriptor 활성화 (1) - 불가 : 일반 객체 생성 (해당 코드는 변수에 객체 할당한 것)
s = DescriptorEx1()

# Descriptor 활성화 (2) - 가능 : 디스크립터 객체가 클래스 속성으로 정의되어 있어야 Discriptor 활성화 가능
class Sample1() :
    name = DescriptorEx1()  # 클래스 attribute (name : 클래스 속성 / 값은 DescriptorEx1 인스턴스)

s1 = Sample1()  # name = Default
s1.name = 'Description Test1' # name Discription
# s1.name = 10    # type error

# attr 확인
# __get__호출
print('ex 1 : ', s1.name)   # name : Description Test1

# __delete__ 호출
del s1.name

# 재확인
# __get__호출
print('ex 1 : ', s1.name)   # name : None

print('----------')


# ex 2)
# Property 클래스 사용 Descriptor 직접 구현
# class property(fget=None, fset=None, fdel=None, doc=None)
class DescriptorEx2() :
    def __init__(self, value) :
        self._name = value
    
    def getValue(self) :
        return f'Get method called. self : {self}, name : {self._name}'
    
    def setValue(self, value) :
        print('Set method called')
        if isinstance (value, str) :
            self._name = value
        else :
            raise TypeError('Name Should be string')

    def delValue(self) :
        print('Delete method called')
        self._name = None

    name = property(getValue, setValue, delValue, 'Property Method Example')

    """
    property(getValue, setValue, delValue) -> 아래 코드를 한번에 정의하는 것과 동일
    
    class _PropertyDescriptor:
        def __get__(self, obj, objtype): ...
        def __set__(self, obj, value): ...
        def __delete__(self, obj): ...
    """

# 최초 값 확인
# DescriptorEx2() 객체를 생성하고 s2 변수에 할당했으나 해당 함수 내에 property 객체로 인해 descriptor로 정의됨
s2 = DescriptorEx2('Descriptor Test2')
print('ex 2 : ', s2.name)

# set
s2.name = 'Dscriptor Test2 Modified'
# s2.name = 10    # TypeError

# get
print('ex 2 : ', s2.name)

# delete
del s2.name
print('ex 2 : ', s2.name)   # None

# doc
print('ex 2 : ', DescriptorEx2.name.__doc__)

print('----------')


# property + 데코레이터 활용
class DescriptorEx2() :
    def __init__(self, value='python') :
        self._name = value
    
    @property
    def name(self) :
        print(f'get name : {self._name}')
        return self._name
    
    @name.setter
    def name(self, value) :
        if not isinstance(value, str) :
            raise TypeError('Name musb be string')
        self._name = value
    
    @name.deleter
    def name(self) :
        self._name = None

s2 = DescriptorEx2()
print('s2 : ', s2.name)

s2.name = 'luvcong'
print('s2 : ', s2.name)

del s2.name
print('s2 : ', s2.name)