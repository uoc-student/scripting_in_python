import exam 

def test1():
    print("***************")
    print("testing singleline_diff(line1, line2) -->")
    print(exam.singleline_diff("asdf", "asdf") == -1)
    print(exam.singleline_diff("asdf", "asdg") == 3)
    print(exam.singleline_diff("as", "asdg") == 2)
    print(exam.singleline_diff("asdf", "as") == 2)
    print(exam.singleline_diff("asdf", "poiuuyy") == 0)
    print(exam.singleline_diff("poiuuxy", "poiuuyy") == 5)
    print("***************")

#test1()


def test2():
    print("***************")
    print("testing singleline_diff_format(line1, line2, idx) -->")
    print(exam.singleline_diff_format("line1", "line1", -1))
    print(exam.singleline_diff_format("line1", "line2", 4))
    print(exam.singleline_diff_format("\nabc\n", "\n\n", 0))
    print("***************")

test2()


def test3():
    print("***************")
    print("testing multiline_diff(lines1, lines2) -->")
    print(exam.multiline_diff(["line1\n", "line1\n"], ["line1\n", "line1\n"]) == (exam.IDENTICAL, exam.IDENTICAL))
    print(exam.multiline_diff(["line2\n", "line1\n"], ["line1\n", "line1\n"]) == (0, 4))
    print(exam.multiline_diff(["line2\n", "line1\n"], ["line2\n"]) == (1, 0))
    print(exam.multiline_diff(["line2\n", "li"], ["line2\n", "line1\n"]) == (1, 2))
    print(exam.multiline_diff(["line2\n"], ["line2\n", "line1\n"]) == (1, 0))
    print(exam.multiline_diff(['a'], ['b']) == (0, 0))
    print(exam.multiline_diff([], ['b']) == (0, 0))
    print(exam.multiline_diff(['a'], ['b']) == (0, 0))
    print(exam.multiline_diff([], []) == (-1, -1))
    print(exam.multiline_diff([], []))
    print("***************")

#test3()


def test4():
    print("***************")
    print("testing get_file_lines(filename) -->")
    print(exam.get_file_lines("test.txt"))

#test4()


def test5():
    print("***************")
    print("testing file_diff_format(filename1, filename2) -->")
    print(exam.file_diff_format("file1.txt", "file2.txt"))
    print(exam.file_diff_format("file2.txt", "file2.txt"))

test5()