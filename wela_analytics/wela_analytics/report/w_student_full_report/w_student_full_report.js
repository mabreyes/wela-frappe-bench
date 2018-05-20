// Copyright (c) 2016, Marc Anthony Reyes and contributors
// For license information, please see license.txt
/* eslint-disable */

frappe.query_reports["w_student_full_report"] = {
	"filters": [
		{
			"fieldname": "w_student",
			"label": __("Student Code"),
			"fieldtype": "Link",
			"options": "w_students",
			"reqd": 1,
			"width": 20,
			"default": "w_student_004"
		},
		{
			"fieldname": "w_school_year",
			"label": __("School Year"),
			"fieldtype": "Link",
			"options": "w_school_year",
			"reqd": 0,
			"width": 20,
		},
		{
			"fieldname": "w_subject_short",
			"label": __("Subject"),
			"fieldtype": "Link",
			"options": "w_subject_short",
			"reqd": 0,
			"width": 20,
		},
	]
}
