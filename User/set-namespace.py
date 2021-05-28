import sublime, sublime_plugin

import sys
import re
import os

class SetNamespaceCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		if self.view.settings().get('is_widget'):
			return

		namespace = os.path.dirname(self.view.file_name())

		extensionName = re.sub(r'.*(?:typo3conf/ext|packages)/([^/]*)/.*', r'\1', namespace)
		if extensionName:
			extensionName = extensionName.title().replace('_', '') + '\\'

		# strip everything before Classes or src
		namespace = re.sub(r'.*(Classes|src)/', r'', namespace)

		# Change / to \
		namespace = re.sub(r'/', r'\\', namespace)

		namespace = 'namespace Vierwd\\' + extensionName + namespace + ';'


		for region in self.view.sel():
			s = self.view.substr(region)
			self.view.replace(edit, region, namespace)

	def is_enabled(self):
		return len(self.view.file_name()) > 0