# Copyright (c) 2013, Marc Anthony Reyes and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe


def execute(filters=None):
    columns, data = show_student_grade_history(
        filters.get('w_student'), filters.get('w_school_year'),
        filters.get('w_subject_short'))
    return columns, data


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

    result = frappe.db.sql(student_grade_history_sql, as_dict=True)

    return columns, result
