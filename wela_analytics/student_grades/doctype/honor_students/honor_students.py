# -*- coding: utf-8 -*-
# Copyright (c) 2018, Marc Anthony Reyes and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document


class HonorStudents(Document):
    pass


def get_honor_students(qtr):
    s_avg_gr = frappe.get_list('Student Grade',
                               filters={},
                               fields=['avg_gr'])

    if (s_avg_gr <= 92):
        honor_student_list = frappe.get_list('Student Grade',
                                             filters={'qtr': qtr,
                                                      'avg_gr': s_avg_gr},
                                             fields=[
                                                 'full_name',
                                                 'qtr',
                                                 'avg_gr'
                                             ])
    else:
        honor_student_list = frappe.get_list('Student Grade',
                                             filters={},
                                             fields=[])
    return honor_student_list
