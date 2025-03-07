def get_3rd_value(my_list):
    if len(my_list) < 3:
        return None
    else:
        return my_list[2]

def test_get_3rd_value():
    assert get_3rd_value([0, 1, 2]) == 2
    assert get_3rd_value([0, 1]) == None

def get_last_value(my_list):
    item_count = len(my_list) - 1 
    if my_list == []:
        return None
    else:
        return my_list[item_count]

def test_get_last_value():
    assert get_last_value([0, 1, 2]) == 2
    assert get_last_value([0]) == 0
    assert get_last_value([]) == None

def runtime_errors():
    test_get_3rd_value()
    test_get_last_value()

