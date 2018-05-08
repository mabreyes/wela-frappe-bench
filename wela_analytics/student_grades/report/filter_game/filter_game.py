# Copyright (c) 2013, Marc Anthony Reyes and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe


def execute(filters=None):
    columns, data = get_athlete_filter(filters.get('athlete'),
                                       filters.get('parent'),
                                       filters.get('game'))
    return columns, data


def get_athlete_filter(athlete, parent, game):
    # columns = [
    # 	{
    # 		"label": "Athlete Name",
    # 		"width": 300,
    # 		"fieldname": "athlete"
    # 	},
    # 	{
    # 		"label": "Competition",
    # 		"width": 300,
    # 		"fieldname": "competition"
    # 	}
    # ]

    columns = [
        {
            "label": "First Name",
            "width": 150,
            "fieldname": "first_name"
        },
        {
            "label": "Middle Name",
            "width": 150,
            "fieldname": "middle_name"
        },
        {
            "label": "Last Name",
            "width": 150,
            "fieldname": "last_name"
        },
        {
            "label": "Age",
            "width": 100,
            "fieldname": "age"
        },
        {
            "label": "Sport",
            "width": 100,
            "fieldname": "sport"
        },
        {
            "label": "Competition Last Joined",
            "width": 150,
            "fieldname": "parent"
        },
        {
            "label": "Game Last Joined",
            "width": 100,
            "fieldname": "name",
        },
        {
            "label": "Team",
            "width": 100,
            "fieldname": "team"
        },
        {
            "label": "Score",
            "width": 100,
            "fieldname": "score"
        },
        {
            "label": "Duration",
            "width": 100,
            "fieldname": "duration"
        }
    ]

    # data = []

    get_student_sql = """SELECT tabAthlete.first_name, tabAthlete.middle_name, tabAthlete.last_name, tabAthlete.age, tabAthlete.sport, tabParticipants.parent, tabGame.name, tabParticipants.team, tabGame.score, tabGame.duration 
	                    FROM tabAthlete 
						LEFT JOIN tabParticipants 
						ON tabAthlete.first_name = tabParticipants.athlete 
						LEFT JOIN tabGame 
						ON tabParticipants.parent = tabGame.competition
                        """

    if athlete:
        get_student_sql = """SELECT tabAthlete.first_name, tabAthlete.middle_name, tabAthlete.last_name, tabAthlete.age, tabAthlete.sport, tabParticipants.parent, tabGame.name, tabParticipants.team, tabGame.score, tabGame.duration 
	                    FROM tabAthlete 
						LEFT JOIN tabParticipants 
						ON tabAthlete.first_name = tabParticipants.athlete 
						LEFT JOIN tabGame 
						ON tabParticipants.parent = tabGame.competition {where}"""

        get_student_sql = get_student_sql.replace(
            "{where}", "WHERE tabParticipants.athlete='{}'".format(athlete))

    if parent:
        get_student_sql = """SELECT tabAthlete.first_name, tabAthlete.middle_name, tabAthlete.last_name, tabAthlete.age, tabAthlete.sport, tabParticipants.parent, tabGame.name, tabParticipants.team, tabGame.score, tabGame.duration 
	                    FROM tabAthlete 
						LEFT JOIN tabParticipants 
						ON tabAthlete.first_name = tabParticipants.athlete 
						LEFT JOIN tabGame 
						ON tabParticipants.parent = tabGame.competition {where}"""

        get_student_sql = get_student_sql.replace(
            "{where}", "WHERE tabParticipants.parent='{}'".format(parent))

    if game:
        get_student_sql = """SELECT tabAthlete.first_name, tabAthlete.middle_name, tabAthlete.last_name, tabAthlete.age, tabAthlete.sport, tabParticipants.parent, tabGame.name, tabParticipants.team, tabGame.score, tabGame.duration 
	                    FROM tabAthlete 
						LEFT JOIN tabParticipants 
						ON tabAthlete.first_name = tabParticipants.athlete 
						LEFT JOIN tabGame 
						ON tabParticipants.parent = tabGame.competition {where}"""

        get_student_sql = get_student_sql.replace(
            "{where}", "WHERE tabGame.name='{}'".format(game))

    result = frappe.db.sql(get_student_sql, as_dict=True)
    return columns, result
