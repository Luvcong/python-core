"""
chapter02_04
Python Advanced(1) - Context Manager(1)
Keyword - Contextlib, __enter__, __exit__, exception
"""

"""
Context manager : 원하는 시점에 리소스 할당 및 회수
가장 대표적인 with 구문 이해 필요!
"""

# ex 1)
file = open('./testfile1.txt', 'w')

# 기존 방법
try :
    file.write('context manager test\ncontextlib test1')
finally :
    file.close()

# ex 2)
# with문 사용
with open('./testfile2.txt', 'w') as f :
    f.write('context manager test\ncontextlib test2')
    # with문을 사용하는 경우 close() = 리소스 반환까지 자동으로 수행됨

# ex 3)
# Use Class -> Context Manager with exception handling
class MyFileWriter() :
    def __init__(self, file_name, method) :
        print('MyFileWriter started : __init__')
        self.file_obj = open(file_name, method)

    def __enter__(self) :
        print('MyFileWriter started : __enter__')
        return self.file_obj
    
    def __exit__(self, exc_type, value, trace_back) :
        print('MyFilWriter started : __exit__')
        if exc_type : # 예외 발생한 경우
            print(f'Logging Exception {exc_type, value, trace_back}')
        self.file_obj.close()

with MyFileWriter('./testfile3.txt', 'w') as f :
    f.write('context manager test\ncontextlib test3')

    