# Copyright (c) 2013, Marc Anthony Reyes and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
import ast


def execute(filters=None):
    columns, data = show_student_grade_history(
        filters.get('w_student'), filters.get('w_school_year'),
        filters.get('w_subject_short'))

    # print(data_for_chart)
    return columns, data


def remove_brackets(list):
    list = str(list).replace('[', '').replace(']', '')
    list_n = ast.literal_eval('"' + list + '"')
    return list_n


def show_student_grade_history(student, school_year, subject_short):
    columns = [
        {
            "label": "Student Code",
            "width": 100,
            "fieldname": "name"
        },
        {
            "label": "Full Name",
            "width": 300,
            "fieldname": "full_name"
        },
        {
            "label": "School Year",
            "width": 70,
            "fieldname": "school_year"
        },
        {
            "label": "Subject",
            "width": 70,
            "fieldname": "subject_name"
        },
        {
            "label": "First Quarter",
            "width": 70,
            "fieldname": "first_quarter_grade"
        },
        {
            "label": "Second Quarter",
            "width": 70,
            "fieldname": "second_quarter_grade"
        },
        {
            "label": "Third Quarter",
            "width": 70,
            "fieldname": "third_quarter_grade"
        },
        {
            "label": "Fourth Quarter",
            "width": 70,
            "fieldname": "fourth_quarter_grade"
        }
    ]

    student_grade_history_sql = """SELECT tabw_students.name, 
		                        tabw_students.full_name, 
								tabw_student_full.school_year, 
								tabw_student_grade.subject_name, 
								tabw_student_grade.first_quarter_grade, 
								tabw_student_grade.second_quarter_grade, 
								tabw_student_grade.third_quarter_grade, 
								tabw_student_grade.fourth_quarter_grade 
								FROM tabw_students 
								LEFT JOIN tabw_student_full 
								ON tabw_students.name = tabw_student_full.student_name 
								LEFT JOIN tabw_student_grade 
								ON tabw_student_full.name = tabw_student_grade.parent 
								GROUP BY tabw_student_grade.subject_name;
	                            """

    if student:
        student_grade_history_sql = """SELECT tabw_students.name, 
		                            tabw_students.full_name, 
								    tabw_student_full.school_year, 
								    tabw_student_grade.subject_name, 
								    tabw_student_grade.first_quarter_grade, 
								    tabw_student_grade.second_quarter_grade, 
								    tabw_student_grade.third_quarter_grade, 
								    tabw_student_grade.fourth_quarter_grade 
								    FROM tabw_students 
								    LEFT JOIN tabw_student_full 
								    ON tabw_students.name = tabw_student_full.student_name 
								    LEFT JOIN tabw_student_grade 
								    ON tabw_student_full.name = tabw_student_grade.parent {where}
									GROUP BY tabw_student_grade.subject_name;
	                                """
        student_grade_history_sql = student_grade_history_sql.replace("{where}",
                                                                      "WHERE tabw_students.name='{0}'".format(student))

    if school_year:
        student_grade_history_sql = """SELECT tabw_students.name, 
		                            tabw_students.full_name, 
								    tabw_student_full.school_year, 
								    tabw_student_grade.subject_name, 
								    tabw_student_grade.first_quarter_grade, 
								    tabw_student_grade.second_quarter_grade, 
								    tabw_student_grade.third_quarter_grade, 
								    tabw_student_grade.fourth_quarter_grade 
								    FROM tabw_students 
								    LEFT JOIN tabw_student_full 
								    ON tabw_students.name = tabw_student_full.student_name 
								    LEFT JOIN tabw_student_grade 
								    ON tabw_student_full.name = tabw_student_grade.parent {where}
									GROUP BY tabw_student_grade.subject_name;
	                                """
        student_grade_history_sql = student_grade_history_sql.replace("{where}",
                                                                      "WHERE tabw_students.name='{0}' \
																	  AND tabw_student_full.school_year='{1}'".format(student, school_year))

    if subject_short:
        student_grade_history_sql = """SELECT tabw_students.name, 
		                            tabw_students.full_name, 
								    tabw_student_full.school_year, 
								    tabw_student_grade.subject_name, 
								    tabw_student_grade.first_quarter_grade, 
								    tabw_student_grade.second_quarter_grade, 
								    tabw_student_grade.third_quarter_grade, 
								    tabw_student_grade.fourth_quarter_grade 
								    FROM tabw_students 
								    LEFT JOIN tabw_student_full 
								    ON tabw_students.name = tabw_student_full.student_name 
								    LEFT JOIN tabw_student_grade 
								    ON tabw_student_full.name = tabw_student_grade.parent {where}
									GROUP BY tabw_student_grade.subject_name;
	                                """
        student_grade_history_sql = student_grade_history_sql.replace("{where}",
                                                                      "WHERE tabw_students.name='{0}' \
																	  AND tabw_student_grade.subject_name LIKE '{1}%'".format(student, subject_short))

    result = frappe.db.sql(student_grade_history_sql, as_dict=True)

    # c_result = dict(remove_brackets(result[:]))

    # chart = show_data(columns, c_result.get('first_quarter_grade'),
    #                   c_result.get('second_quarter_grade'),
    #                   c_result.get('third_quarter_grade'),
    #                   c_result.get('fourth_quarter_grade'))

    # print(c_result)
    return columns, result


def show_data(columns, first_quarter_grade, second_quarter_grade, third_quarter_grade, fourth_quarter_grade):
    x_intervals = ['x'] + [d.get("label") for d in columns[3:]]
    first_quarter_grade_data, second_quarter_grade_data, third_quarter_grade_data, fourth_quarter_grade_data = [], [], [], []

    for p in columns[3:]:
        if first_quarter_grade:
            first_quarter_grade_data.append(
                first_quarter_grade[0].get(p.get('first_quarter_grade')))
        if second_quarter_grade:
            second_quarter_grade_data.append(
                second_quarter_grade[0].get(p.get('second_quarter_grade')))
        if third_quarter_grade:
            third_quarter_grade_data.append(
                third_quarter_grade[0].get(p.get('third_quarter_grade')))
        if fourth_quarter_grade:
            fourth_quarter_grade_data.append(
                fourth_quarter_grade[0].get(p.get('fourth_quarter_grade')))

    columns = [x_intervals]

    if first_quarter_grade_data:
        columns.append(['First Quarter'] + first_quarter_grade_data)
    if second_quarter_grade_data:
        columns.append(['Second Quarter'] + second_quarter_grade_data)
    if third_quarter_grade_data:
        columns.append(['Third Quarter'] + third_quarter_grade_data)
    if fourth_quarter_grade_data:
        columns.append(['Fourth Quarter'] + fourth_quarter_grade_data)

    chart = {
        "data": {
            'x': 'x',
            'columns': columns
        }
    }

    chart['chart_type'] = "bar"

    return chart
