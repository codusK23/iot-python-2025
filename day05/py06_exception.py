# 예외 처리
## 오류, Error, 
## 1. Error(문법적 오류) - 코딩하다가 빨간 밑줄생기는 것
##    오류표시가 안나는 코딩을 잘못한 오류 포함(!) 예) mul(7, 6) -> 42예상, 결과 13
## 2. Exception(실행중 발생 예외) - 문법 오류 수정 후 실행하다가 비정상 종료되는 것
## 파이썬은 Error, Exception 구분 없이 Error라고 표현
## 에디터 상에 오류 표시가 나면 Error
## 실행 중에 발생하면 Exception
## try:
##    예외가 발생할 수 있는 로직
## except 예외클래스 as e:
##    예외처리 로직
##    Exception 클래스는 다른 모든 예외 클래스의 조상, Exception만 쓰면 됨
## [finally:] - 옵션
##    예외발생 유무와 상관없이 항상 처리해야 할 로직
## try문을 반복해서 사용하지 말것 - 속도느려짐

# 디버깅 - 천천히 어디에서 예외(오류)가 발생하는지 확인하기 위해 사용
## F9 - 중단점(Break Point) 표시/해제 기능
## F5 - 디버깅 시작, 중단점까지 실행
## F10 - 한줄 실행. 함수가 있어도 함수를 실행하고 넘어감
## F11 - 한줄실행. 함수가 있으면 함수 안으로 진입
## Shift + F5 - 디버깅종료
## 변수 탭 - 현재 변수에 들어있는 값 표시
## 조사식 탭 - 내가 원하는 식을 실행, 결과 표시
numbers = list(range(1, 11))
for i in numbers:
    # print(i)
    pass

def mul(a, b):
    return a * b

def div(a, b):
    return a / b

print("계산 시작")

while True:
    op = input("계산할 연산을 입력(*, /, q) ")
    if op == 'q': # 종료조건
        break

    elif op == '*': # 곱하기
        try:    
            x, y = input('곱할 수 입력 > ').split()
            x = int(x)
            y = int(y)
            print(f'{x} * {y} = {mul(x, y)}')
        except Exception as e:
            # print("입력 실수. 다시 입력해주세요.") # 사용자용 에러메세지
            print(f'입력 실수 {e}')

    elif op == '/': # 나누기
        try:
            x, y = input('나눌 수 입력 > ').split()
            x = int(x)
            y = int(y)
            print(f'{x} / {y} = {div(x, y)}')
        except  ValueError as e:
            # print("입력 실수. 다시 입력해주세요.") # 사용자용 에러메세지
            print(f'입력 실수 {e}')
        except ZeroDivisionError as e:
            print("0으로는 나눌수가 없지 ~~~")
            print(f'{e}')

    else:
        print("정확한 입력 요망")

