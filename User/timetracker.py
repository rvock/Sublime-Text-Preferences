import sublime, sublime_plugin

import time

class TimetrackerCommand(sublime_plugin.EventListener):
	def on_post_save(self, view):
		string = open('/Users/rvock/.timetracker', 'r').read()
		saved_file = view.file_name()

		if '4wdmedia/projekte' in saved_file:
			project = saved_file.split('projekte/')[1].split('/')[0]
			output = project + ":" + str(time.time()) + "\n"
			string = string + output;

			f = open('/Users/rvock/.timetracker', 'w')
			f.write(string)
			f.close()

			pass

