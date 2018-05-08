# Copyright (c) 2013, Marc Anthony Reyes and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe


def execute(filters=None):
    columns, data = get_student_list(filters.get('qtr'))
    return columns, data


def get_student_list(qtr):
    columns = [
        {
            "label": "Full Name",
            "width": 300,
            "fieldname": "full_name"
        },
        {
            "label": "Quarter",
            "width": 100,
            "fieldname": "qtr"
        },
        {
            "label": "English Grade",
            "width": 100,
            "fieldname": "eng_gr"
        },
        {
            "label": "Math Grade",
            "width": 100,
            "fieldname": "mat_gr"
        },
        {
            "label": "Filpino Grade",
            "width": 100,
            "fieldname": "fil_gr"
        },
        {
            "label": "Science Grade",
            "width": 100,
            "fieldname": "sci_gr"
        },
        {
            "label": "Social Studies Grade",
            "width": 100,
            "fieldname": "ss_gr"
        },
        {
            "label": "Average Grade",
            "width": 100,
            "fieldname": "avg_gr"
        }
    ]

    get_student_list_sql = """SELECT full_name, qtr, eng_gr, mat_gr, fil_gr, sci_gr, ss_gr, avg_gr
                                FROM `tabStudent Grade`"""

    if qtr:
        get_student_list_sql = """SELECT full_name, qtr, eng_gr, mat_gr, fil_gr, sci_gr, ss_gr, avg_gr
                                FROM `tabStudent Grade` {where}"""

        get_student_list_sql = get_student_list_sql.replace(
            "{where}", "WHERE qtr='{}'".format(qtr))

    result = frappe.db.sql(get_student_list_sql, as_dict=True)
    return columns, result
