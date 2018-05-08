# -*- coding: utf-8 -*-
# Copyright (c) 2018, Marc Anthony Reyes and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document


class StudentGrade(Document):
    pass


def get_avg_gr():
    students_info = frappe.get_list('Student Grade',
                                    filters={},
                                    fields=['avg_qtr'])
    return students_info
