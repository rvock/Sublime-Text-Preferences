import sublime, sublime_plugin

import time

class TimetrackerCommand(sublime_plugin.EventListener):
	def on_post_save(self, view):
		saved_file = view.file_name()

		if '4wdmedia/projekte' in saved_file:
			project = saved_file.split('projekte/')[1].split('/')[0]
			output = project + ":" + str(time.time()) + "\n"

			f = open('/Users/rvock/.timetracker', 'a+')
			f.write(output)
			f.close()

			pass

