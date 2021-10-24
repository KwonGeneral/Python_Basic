
# Global에 대한 설명.
# global 전역변수 선언은 값을 넣어서 선언할 수 없다.
# 그렇다면 왜 값을 넣어서 선언할 수 없는지 궁금하지 않은가?
# 개인적인 견해이지만, 이는 Global의 쓰임새가 특정 되어 있기 때문이라고 생각한다.

# 직접 써보면서 알아보자.
print("\n === Global Interpreter Lock === \n")
global temp_global
temp_data = 0
temp_global_data = 0


def check_global_data():
    global temp_global
    global temp_global_data
    temp_global = 1
    temp_data = 2
    temp_global_data = 3


try:
    print("1-temp_global : ", temp_global)
except NameError:
    print("1-temp_global : NameError")

print("1-temp_data : ", temp_data)
print("1-temp_global_data : ", temp_global_data)

check_global_data()

print("\n2-temp_global : ", temp_global)
print("2-temp_data : ", temp_data)
print("2-temp_global_data : ", temp_global_data)

"""
1-temp_global : NameError
1-temp_data :  0
1-temp_global_data :  0

2-temp_global :  1
2-temp_data :  0
2-temp_global_data :  3
"""

# 위의 결과로 알 수 있는 것은
# 전역 변수로 선언 하더라도, 함수 내부에서는 값을 수정하더라도 영향이 없다라는 것이다.
# 함수 내부의 temp_data는 전역 변수가 아닌, 지역 변수로 선언 되었음을 의미한다.
# 즉, Global은 함수 내에서 전역 변수에 접근 하고 싶을 때, 사용하는 것이다.

# Global을 활용해, 1번 파일의 List Of Memory Address를 변형해보자.
print("\n\n === List Of Memory Address === \n")
origin_list = ["1", "2", "3"]


def check_list_memory_addresses():
    global origin_list
    origin_list.append("4")
    print("메모리 주소 값 2 : ", id(origin_list))
    return origin_list


print("1-origin_list : ", origin_list)
print("메모리 주소 값 1 : ", id(origin_list))
print("2-origin_list : ", check_list_memory_addresses())