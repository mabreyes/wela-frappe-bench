// Copyright (c) 2018, Marc Anthony Reyes and contributors
// For license information, please see license.txt

frappe.ui.form.on('Honor Students', 'gr_qtr', function (frm) {
	frappe.call({
		'method': 'student_grades.doctype.honor_students.honor_students.get_honor_students',
		'args': {
			'qtr': cur_frm.gr_qtr,
		},
		'callback': function (res) {
			console.log(res)
		}
	})
});
