import project as pr


def print_table(table):
    for row in table:
        print(row)


def test1():
    test1_table = pr.read_csv_fieldnames("table1.csv", ',', None)
    print("table1.csv --> ", test1_table)
    test2_table = pr.read_csv_fieldnames("table2.csv", ',', '"')
    print("table2.csv --> ", test2_table)
    print("Equal tables? -> ", test1_table == test2_table)
    test3_table = pr.read_csv_fieldnames("table3.csv", ',', '\'')
    print("table3.csv --> ", test3_table)
    print("Equal tables? -> ", test1_table == test3_table)
    test1_table = pr.read_csv_fieldnames("table4.csv", ',', '"')
    print("table4.csv --> ", test1_table)

#test1()


def test2():
    test1_list = pr.read_csv_as_list_dict("table1.csv", ',', None)
    print("table1.csv --> ", test1_list)
    test2_list = pr.read_csv_as_list_dict("table2.csv", ',', '"')
    print("table2.csv --> ", test2_list)
    print("Equal lists? --> ", test1_list == test2_list)
    test3_list = pr.read_csv_as_list_dict("table3.csv", ',', '\'')
    print("table3.csv --> ", test3_list)
    print("Equal lists? --> ", test1_list == test3_list)

#test2()

keyfields = pr.read_csv_fieldnames("table1.csv", ',', None)

def test3():
    nested_dict1 = pr.read_csv_as_nested_dict('table1.csv', 'Field1', ',', '"')
    print(nested_dict1)

test3()

test1_list = pr.read_csv_as_list_dict("table1.csv", ',', None)

def test4():
    test1_write = pr.write_csv_from_list_dict("table1_copy.csv", test1_list, keyfields, ',', None)

#test4()