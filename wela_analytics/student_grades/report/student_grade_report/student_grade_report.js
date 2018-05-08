// Copyright (c) 2016, Marc Anthony Reyes and contributors
// For license information, please see license.txt
/* eslint-disable */

/*frappe.query_reports["Student_Grade_Report"] = {
	"filters": [
		{
			"fieldname": "full_name",
			"label": __("Full Name"),
			"fieldtype": "Data",
			"reqd": 0,
		},
		{
			"fieldname": "eng_gr",
			"label": __("English"),
			"fieldtype": "Int",
			"reqd": 0,
		},
		{
			"fieldname": "mat_gr",
			"label": __("Math"),
			"fieldtype": "Int",
			"reqd": 0,
		},
		{
			"fieldname": "fil_gr",
			"label": __("Filipino"),
			"fieldtype": "Int",
			"reqd": 0,
		},
		{
			"fieldname": "sci_gr",
			"label": __("Science"),
			"fieldtype": "Int",
			"reqd": 0,
		},
		{
			"fieldname": "ss_gr",
			"label": __("Social Studies"),
			"fieldtype": "Int",
			"reqd": 0,
		},
		{
			"fieldname": "avg_gr",
			"label": __("Average"),
			"fieldtype": "Int",
			"reqd": 0,
		}
	]
}
*/

frappe.query_reports["Student_Grade_Report"] = {
	"filters": [
		{
			"fieldname": "qtr",
			"label": __("Quarter"),
			"fieldtype": "Link",
			"options": "Grade Quarter",
			"reqd": 0,
			"width": 20,
		}
	]
}
