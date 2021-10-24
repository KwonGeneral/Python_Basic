

# 매개변수로 리스트를 전달했을 때,
# 이 매개변수를 통해 값을 변경했을 시, 원본 리스트의 값이 변하는가?
origin_list = ["1", "2", "3"]


def check_list_memory_address(temp_list):
    temp_list.append("4")
    origin_list.append("5")
    return temp_list


print("\n1-origin_list 메모리 주소 값 : ", id(origin_list))
print(check_list_memory_address(origin_list))
print("2-origin_list 메모리 주소 값 : ", id(origin_list))


# 추가적인 테스트 : Int, String, Dict, Tuple
test_int = 0
test_str = "TEST"
test_dict = {"test": "dict"}
test_tuple = (1, 2, 3)


def check_int_str_dict_tuple_memory_address(temp_int, temp_str, temp_dict, temp_tuple):
    temp_int = 4
    temp_str = "Change"
    temp_dict = {"test": "Change"}
    temp_tuple = (5, 6, 7)
    return temp_int


print("\n\n1-test_int 메모리 주소 값 : ", id(test_int))
print("1-test_str 메모리 주소 값 : ", id(test_str))
print("1-test_dict 메모리 주소 값 : ", id(test_dict))
print("1-test_tuple 메모리 주소 값 : ", id(test_tuple))
print(check_int_str_dict_tuple_memory_address(test_int, test_str, test_dict, test_tuple))
print("2-test_int 메모리 주소 값 : ", id(test_int))
print("2-test_str 메모리 주소 값 : ", id(test_str))
print("2-test_dict 메모리 주소 값 : ", id(test_dict))
print("2-test_tuple 메모리 주소 값 : ", id(test_tuple))
print("\n 'test_int : {}' 'test_str : {}' 'test_dict : {}' 'test_tuple : {}' ".format(test_int, test_str, test_dict, test_tuple))

