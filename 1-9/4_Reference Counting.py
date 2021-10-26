import gc
import sys

# RC(Reference Counting)은 아래와 같이 서로를 참조하는 경우
# Reference Count가 0이 되지 않기 때문에
# 쓰레기(Garbage)가 된다.

origin_list = ["1", "2", "3"]
print(sys.getrefcount(origin_list))
# origin_list의 RC(Reference Count) = 2

origin_list.append("4")
print(sys.getrefcount(origin_list))
# origin_list의 RC(Reference Count) = 2

temp_list = origin_list
print(sys.getrefcount(temp_list))
# temp_list의 RC(Reference Count) = 3

temp2_list = temp_list
print(sys.getrefcount(temp2_list))
# temp2_list의 RC(Reference Count) = 4

temp3_list = temp2_list
print(sys.getrefcount(temp3_list))
# temp3_list의 RC(Reference Count) = 5

temp4_list = origin_list
print(sys.getrefcount(temp4_list))
# temp4_list의 RC(Reference Count) = 6

del temp4_list
del temp3_list
del temp2_list
del temp_list
# temp4_list의 RC(Reference Count) = 1
# temp3_list의 RC(Reference Count) = 1
# temp2_list의 RC(Reference Count) = 1
# temp_list의 RC(Reference Count) = 1

# Reference Count가 1인 경우 메모리를 해제할 수 없다.
# 위와 같은 문제를 참조 주기(Reference Cycle)라고 하며
# RC로 해결할 수 없다.


