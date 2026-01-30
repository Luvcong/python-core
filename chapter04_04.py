"""
chapter04_04
Python Advanced(3) - Descriptor(1)
Keyword - descriptor, set, get, del, property
"""

"""
Descriptor
1) 객체에서 서로 다른 객체를 속성 값으로 가지는 것
2) Read, Write, Delete 등을 미리 정의 가능
3) ** data descriptor(set, del), non-data descriptor(get)
4) 읽기 전용 객체 생성 장점 / 클래스를 의도하는 방향으로 생성 가능


메모)
디스크립터 메서드는 python interprter가 자동 호출
  > 호출 규칙이 언어 차원에서 정의되어 시그니처가 고정
"""
# ex 1)
# 기본적인 Descriptor 예제
class DescriptorEx1() :
    def __init__(self, name='Default') :
        self.name = name
    
    def __get__(self, obj, objtype) :   # 파라미터 개수 고정
        return f'Get Method Calld -> self : {self}, obj : {obj}, obj type : {objtype}, name : {self.name}'
    
    def __set__(self, obj, name) :      # 파라미터 개수 고정
        print('Set method called')
        if isinstance(name, str) :
            self.name = name
        else :
            raise TypeError('Name should be string')
    
    def __delete__(self, obj) :         # 파라미터 개수 고정
        print('Delete method called')
        self.name = None

# s = DescriptorEx1()   # 일반 객체 생성 (디스크립터 아님)

# 디스크립터 객체가 클래스 속성으로 정의되어 있어야 함
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


""" 메모)
property 연습 + 데코레이터 활용
"""
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