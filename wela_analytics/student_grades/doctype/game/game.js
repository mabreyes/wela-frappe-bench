// Copyright (c) 2018, Marc Anthony Reyes and contributors
// For license information, please see license.txt

frappe.ui.form.on('Game', {
	// onload: function (frm) {
	// 	var name_comp = cur.frm
	// },
	refresh: function (frm) {
		var start = new Date(cur_frm.doc.st_dt);
		var end = new Date(cur_frm.doc.en_dt);
		var diff = (end - start);
		var diffHours = Math.floor((diff % 86400000) / 3600000);
		cur_frm.set_value('duration', diffHours);
		refresh_field('duration');
	},
	// after_save: function (frm) {
	// 	console.log('Redirecting to previous form');
	// 	frappe.set_route('Form', 'Competition', '')
	// }
});