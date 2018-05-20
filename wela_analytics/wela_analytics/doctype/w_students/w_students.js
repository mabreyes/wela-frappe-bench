// Copyright (c) 2018, Marc Anthony Reyes and contributors
// For license information, please see license.txt

frappe.ui.form.on('w_students', 'refresh', function (frm) {
	var f_name = cur_frm.doc.first_name;
	var m_name = cur_frm.doc.middle_name;
	var l_name = cur_frm.doc.last_name;
	var fl_name = f_name + ' ' + m_name + ' ' + l_name;
	cur_frm.set_value('full_name', fl_name);
	refresh_field('full_name');
	console.log(fl_name);
});
