from task3 import TestConv

test_list = [(1, 1), (3, 1), (2, 5)]

for i in test_list:
    first = TestConv(i[0], i[1])
    first.test()

first.quit_browser()
