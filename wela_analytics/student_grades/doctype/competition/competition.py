# -*- coding: utf-8 -*-
# Copyright (c) 2018, Marc Anthony Reyes and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document

class Competition(Document):
	pass

@frappe.whitelist()
def get_athletes(sport):
    athlete_details = frappe.get_list('Athlete', filters={'sport': sport}, fields=[
                                      'first_name'])

    return athlete_details