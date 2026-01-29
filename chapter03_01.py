"""
chapter03_01
Python Advanced(2) - Context Manager Annotation
Keyword - @contextlib.contextmanager, __enter__, __exit__
"""

"""
Contextlib 데코레이터 사용 -> 코드 직관적이고, 예외처리가 용이함
"""

import contextlib
import time

# ex 1)
# Use decorator

@contextlib.contextmanager
def my_file_writer(file_name, method) :
    f = open(file_name, method)
    yield f     # __enter__
    f.close()   # __exit__

with my_file_writer('testfile4.txt', 'w') as f :
    f.write('context manager test4\ncontextlib test4')
print('----------')

# ex 2)
# Use decorator

@contextlib.contextmanager
def ExcuteTimerDc(msg) :
    start = time.monotonic()
    try :   # __enter__
        yield start
    except BaseException as e :
        print(f'Logging Exception : {msg} : {e}')
        raise
    else : # __exit__
        print(f'{msg} : {time.monotonic() - start}')

with ExcuteTimerDc('Start Job!') as v : 
    print(f'Recived start monotonic2 : {v}')
    # Excute job
    for i in range(10000) :
        pass
        # raise ValueError('occurred')
        