"""
chapter03_03
Python Advanced(2) - Property(2) : Method Overrding
Keyword - Overriding, OOP, 다형성
"""

"""
메서드 오버라이딩 효과
1) 서브클래스(자식)에서 슈퍼(부모)클래스를 호출 후 사용
2) 메서드 재정의 후 사용 가능
3) 부모 클래스의 메서드를 추상화 후 사용 가능 (구조적 접근)
4) 확장 가능, 다형성 (다양한 방식으로 동작)
5) 가독성 증가, 오류 가능성 감소, 메서드명 절약, 유지보수성 증가 등
"""

# ex 1)
# 기본 Overriding 예제
class parentEx1() :
    def __init__(self) :
        self.value = 5
    
    def get_value(self) :
        return self.value
    
class ChildEx1(parentEx1) :
    pass

c1 = ChildEx1()
p1 = parentEx1()

# 부모클래스 메서드 호출
print('ex 1 : ', c1.get_value())

# 자식클래스 모든 속성 출력
print('ex 1 : ', dir(c1))   # get_value 확인 가능

# 부모 / 자식 모든 속성 출력
print('ex 1 parentEx1 : ', dir(parentEx1))
print('ex 1 ChildEx1  : ', dir(ChildEx1))
print('----------')

print('ex 1 parentEx1 : ', parentEx1.__dict__)
print('ex 1 ChildEx1  : ', ChildEx1.__dict__)
print('----------')


# ex 2)
# 기본 Overrding 메서드 재정의
class ParentEx2() :
    def __init__(self):
        self.value = 5

    def get_value(self):
        return self.value

class ChildEx2(ParentEx2) :
    def get_value(self) :
        return self.value * 10

c2 = ChildEx2()
print('ex 2 : ', c2.get_value())    # 50
print('ex 2 : ', ParentEx2().get_value())   # 5
print('----------')


# ex 3)
# Overrding 다형성 예제

import datetime
class Logger() :
    def log(self, msg) :
        print(msg)

class TimestampLogger(Logger) :
    def log(self, msg) :
        message = "{ts} {msg}".format(ts=datetime.datetime.now(), msg=msg)
        super(TimestampLogger, self).log(message)   # super().log(message) 와 동일

class DateLogger(Logger) :
    def log(self, msg) :
        message = "{ts} {msg}".format(ts=datetime.datetime.now().strftime('%Y-%m-%d'), msg=msg)
        super(DateLogger, self).log(message)   # super().log(message) 와 동일

l = Logger()
t = TimestampLogger()
d = DateLogger()

print('Ex3 : ', l.log(' Called logger.'))   # None (부모에서 print가 실행되기 때문에 부모 클래스에서 Called logger 메시지가 출력됨)
print('Ex3 : ', t.log(' Called timestamp logger.'))
print('Ex3 : ', d.log(' Called date logger.'))