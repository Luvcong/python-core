"""
chapter02_04
Python Advanced(1) - Context Manager(2)
Keyword - Contextlib, __enter__, __exit__, exception
"""

"""
Contextlib = Measure execution(타이머) 제작
"""

# ex 1)
# Use Class
import time

class ExcuteTime() :
    def __init__(self, msg) :
        self._msg = msg
    
    def __enter__(self) :
        self._start = time.monotonic()
        return self._start
    
    def __exit__(self, exc_type, exc_value, exc_traceback) :
        if exc_type :
            print('Logging execption : {}'.format((exc_type, exc_value, exc_traceback)))
        else :
            print(f'{self._msg} : {time.monotonic() - self._start} s')
        return True


with ExcuteTime('Start! job') as v :
    print('Received start monotonic1 : {}'.format(v))
    for i in range(10000000) :
        pass
    raise Exception('Rasie! Exception!')    # 강제로 예외 발생