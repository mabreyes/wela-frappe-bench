// Copyright (c) 2018, Marc Anthony Reyes and contributors
// For license information, please see license.txt

frappe.ui.form.on('Competition', 'get_athlete', function (frm) {
	frappe.call({
		method: 'wela_analytics.student_grades.doctype.competition.competition.get_athletes',
		args: {
			'sport': cur_frm.doc.sport,
		},
		'callback': function (r) {
			console.log(r);
			for (var n = 0; n < r.message.length; n++) {
				frappe.model.add_child(cur_frm.doc, 'Competition', 'participants');
				$.each(frm.doc.participants || [], function (i, v) {
					frappe.model.set_value(v.doctype, v.name, 'athlete', r.message[n].first_name);
					frappe.model.set_value(v.doctype, v.name, 'team', 'Team A');
				});
			}
			frm.refresh_field('participants');
		}
	})
});

frappe.ui.form.on('Competition', 'make_game', function (frm) {
	frappe.route_options = { 'name': cur_frm.doc.name };
	frappe.set_route('Form', 'Game', 'New Form');
});
