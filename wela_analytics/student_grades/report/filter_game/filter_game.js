// Copyright (c) 2016, Marc Anthony Reyes and contributors
// For license information, please see license.txt
/* eslint-disable */

frappe.query_reports["Filter_Game"] = {
	"filters": [
		{
			"fieldname": "athlete",
			"label": __("Athlete Name"),
			"fieldtype": "Link",
			"options": "Athlete",
			"reqd": 0,
			"width": 50,
		},
		{
			"fieldname": "parent",
			"label": __("Competition"),
			"fieldtype": "Link",
			"options": "Competition",
			"reqd": 0,
			"width": 50,
		},
		{
			"fieldname": "game",
			"label": __("Game"),
			"fieldtype": "Link",
			"options": "Game",
			"reqd": 0,
			"width": 50,
		}
	]
}
