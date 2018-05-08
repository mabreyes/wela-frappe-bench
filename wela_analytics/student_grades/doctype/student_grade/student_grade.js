// Copyright (c) 2018, Marc Anthony Reyes and contributors
// For license information, please see license.txt

frappe.ui.form.on('Student Grade', 'refresh', function(frm) {
		var eng_gr = cur_frm.doc.eng_gr;
		var mat_gr = cur_frm.doc.mat_gr;
		var fil_gr = cur_frm.doc.fil_gr;
		var sci_gr = cur_frm.doc.sci_gr;
		var ss_gr = cur_frm.doc.sci_gr;
		var avg_gr = (eng_gr + mat_gr + fil_gr + sci_gr + ss_gr) / 5;
		cur_frm.set_value('avg_gr', avg_gr);
		refresh_field('avg_gr');
});




