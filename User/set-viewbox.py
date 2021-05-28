import sublime, sublime_plugin

import sys
import re

class SetViewBoxCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		if self.view.settings().get('is_widget'):
			return
		# <svg xmlns="http://www.w3.org/2000/svg" width="264.8" height="236.6" viewBox="0 0 264.8 236.6">
		for region in self.view.sel():
			if not region.empty():
				s = self.view.substr(region)
				if re.search(r'width="[\d.]+"', s):
					# add viewbox
					s = re.sub(r'width="([\d.]+)"\s*height="([\d.]+)"', r'viewBox="0 0 \1 \2" width="\1" height="\2"', s)
					s = re.sub(r'height="([\d.]+)"\s*width="([\d.]+)"', r'viewBox="0 0 \2 \1" width="\2" height="\1"', s)
				elif re.search(r'viewBox', s):
					# add width and height
					s = re.sub(r"viewBox=\"([\d.-]+) ([\d.-]+) ([\d.]+) ([\d.]+)\"", r'width="\3" height="\4" viewBox="\1 \2 \3 \4"', s)
				self.view.replace(edit, region, s)
