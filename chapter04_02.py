"""
chapter04_02
Python Advanced(3) - Meta Class(2)
Keyword - Type(name, base, dct) Dynamic metaclass
"""

"""
Meta Class
1) meta class 동적 생성
2) 동적 생성한 meta class -> 커스텀 생성 가능
3) 의도하는 방향으로 직접 클래스 생성에 관여할 수 있는 장점
"""

# ex 1) Type 동적 클래스 생성

# 정적 형태
# class Sample1() :
#     pass

# Name(이름), Bases(상속), Dct(속성, 메서드)
# 동적 형태
s1 = type('Sample1', (), {})
print('ex 1 : ', s1)
print('ex 1 : ', type(s1))
print('ex 1 : ', s1.__base__)
print('ex 1 : ', s1.__dict__)
print('----------')

# 동적 + 상속
class Parent1 : 
    pass

s2 = type('Sample2', (Parent1,), dict(attr1 = 100, attr2 = 'hi')) # = {'attr1' : 100, 'attr' : 'hi'} 와 동일
print('ex 2 : ', s2)            # <class '__main__.Sample2'>
print('ex 2 : ', type(s2))      # <class 'type'>
print('ex 2 : ', s2.__base__)   # <class '__main__.Parent1'>
print('ex 2 : ', s2.__dict__)   # {'attr1': 100, 'attr2': 'hi', '__module__': '__main__', '__doc__': None}
print('ex 2 : ', s2.attr1, s2.attr2)    # 100 hi
print('----------')

# ex 2)
# type 동적 클래스 생성 + 메서드
class SampleEx() :
    attr1 = 30
    attr2 = 100

    def add(self, m, n) :
        return m + n
    
    def mul(self, m, n) :
        return m * n

ex = SampleEx()
print('ex 2 : ', ex.attr1)
print('ex 2 : ', ex.attr2)
print('ex 2 : ', ex.add(100, 200))
print('ex 2 : ', ex.mul(10, 200))
print('----------')

# s3 = type('Sample3', (), dict({'attr1' : 30, 'attr2' : 100 }))  # 모든 클래스는 object를 상속 -> () 빈 튜플 or (object) 명시적으로 입력 가능
s3 = type('Sample3',
          (object,),
          dict({'attr1' : 30, 'attr2' : 100, 'add' : lambda x, y : x + y, 'mul' : lambda x, y : x * y}))

print('ex 3 : ', s3.attr1)
print('ex 3 : ', s3.attr2)
print('ex 3 : ', s3.add(100, 200))
print('ex 3 : ', s3.mul(10, 200))

