first_num = int(input("Number:\n")) # 12

def check_grade(first_num, check=False):
    if first_num < 10 and check:
        return
    if first_num > 33:#false
        result = "pass"
    else: 
        result = "fail"
    print(result)

check_grade(first_num)

second_num = int(input("Number:\n"))
check_grade(second_num, True)

# if num_1 is greater than 10 check if number is pass or fail
