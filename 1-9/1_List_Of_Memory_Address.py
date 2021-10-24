
origin_list = ["1", "2", "3"]


def check_list_memory_address(temp_list):
    temp_list.append("4")
    print("메모리 주소 값 2 : ", id(origin_list))
    return temp_list


print("메모리 주소 값 1 : ", id(origin_list))
print(check_list_memory_address(origin_list))

