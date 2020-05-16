import json

# Dictionary holding student_score.json values from collections import default dictionary
SECTION_DATA = {}

# Open student_score.json and pass values and store them in Dictionary
try:
    with open('student_score.json', 'r', encoding='utf-8') as file_data:
        SECTION_DATA = json.load(file_data)
except IOError as e:
    print(e)
    print("IOError: Unable to open student_score.json. Terminating execution.")
    exit(1)


def get_subject_avg(class_name, subject):
    """
    calculating each classrooms average marks, subject vise

    :param class_name: classroom name:string
    :param subject: subject name:string
    :return: subject average of specified classroom:float
    """
    class_count = 0
    full_marks = 0
    for arr in SECTION_DATA:
        if arr['class'] == class_name:
            class_count += 1
            subject_marks = int(arr[subject])
            full_marks += subject_marks
    subject_avg = full_marks/class_count
    return round(subject_avg, 2)


def above_seventy(arr):
    """
    counting marks above 70 from specified subject average mark list

    :param arr: specified subject average mark list:Type list
    :return: above 70 average marks count of specified subject
    """
    above_count = 0
    for marks in arr:
        if marks > 70:
            above_count +=1
    return above_count


def student_avg(class_name):
    """
    calculating average marks of each classroom, student vise

    :param class_name: classroom name:string
    :return: classroom name and average marks of students
    """
    marks_list = []
    class_count = 0
    for arr in SECTION_DATA:
        if arr['class'] == class_name:
            math = int(arr['math'])
            lit = int(arr['literature'])
            sci = int(arr['science'])
            eng = int(arr['english'])
            student_avg_mark = (math + lit + sci + eng)/4
            class_count += 1
            marks_list.append(student_avg_mark)
    class_avg_marks = sum(marks_list) / class_count
    return class_name, round(class_avg_marks, 2)


def max_three(_dict):
    """
    finding the top three maximum values from a dictionary and storing in another dictionary
    :param _dict: sorting dictionary
    :return: top three values of a dictionary stored in another dictionary
    """
    x = 1
    max_dict = {}
    while x <= 3:
        max_class = max(_dict, key=lambda key: _dict[key])
        max_dict[x] = max_class
        _dict.pop(max_class)
        x += 1
    return max_dict


def top_student(class_name):
    """
    finding and returning top student of each class

    :param class_name: classroom name:string
    :return: top student class and student id
    """
    marks_list = {}
    class_count = 0
    for arr in SECTION_DATA:
        if arr['class'] == class_name:
            math = int(arr['math'])
            lit = int(arr['literature'])
            sci = int(arr['science'])
            eng = int(arr['english'])
            stu_id = arr['student_id']
            student_total = (math + lit + sci + eng)
            class_count += 1
            marks_list[stu_id] = student_total
    global mx
    mx = max(marks_list.values())
    global mx_id
    mx_id = [k for k, v in marks_list.items() if v == mx]
    return class_name, mx_id


if __name__ == '__main__':
    _list = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I']  # classroom name list

    # each classrooms, science subject average marks list
    science_avg = list(map(lambda a: get_subject_avg(f"10-{a}", 'science'), _list))

    # each classrooms, literature subject average marks list
    literature_avg = list(map(lambda a: get_subject_avg(f"10-{a}", 'literature'), _list))

    # counting the number of classes which have average marks above 70 for science
    count_1 = above_seventy(science_avg)

    # counting the number of classes which have average marks above 70 for science
    count_2 = above_seventy(literature_avg)

    # storing each classroom average mark in a dictionary
    class_avg = dict(map(lambda a: student_avg(f"10-{a}"), _list))

    # calling max_three() function to find top three classes with average marks
    top_three = max_three(class_avg)

    # calling top_student() function to find top in the class of each classroom
    class_first = dict(map(lambda a: top_student(f"10-{a}"), _list))

    # finding the number of first place students
    len_count = 0
    max_list = {}
    for letter in _list:
        top_student(f'10-{letter}')
        max_list[mx] = mx_id
        y = len(class_first[f'10-{letter}'])
        len_count += y
    max_key = (max(max_list))

    with open("answers.txt", 'w', encoding='utf-8') as ans:
        ans.write("How many classes are there that have an above-average 70 for science?  - ")
        ans.write(f"{count_1}\n\n")
        ans.write("How many classes are there that have an above-average 70 for literature?  - ")
        ans.write(f"{count_2}\n\n")
        ans.write("What are the top 3 classes of grade 10? (based on student score average )? \n")
        ans.write(f"1st place - {top_three[1]}\n2nd place - {top_three[2]}\n3rd place"
                  f" - {top_three[3]}\n\n")
        ans.write("Who scored best in each grade 10 class?\n")
        for letter in _list:
            ans.write(f"10-{letter}: {class_first[f'10-{letter}']}\n")
        ans.write("\nHow many 1st places are there in grade 10   - ")
        ans.write(str(len_count))
        ans.write("\n\nSection 1st student ID   - ")
        ans.write(f"{max_list[max_key]}")
        ans.close()



