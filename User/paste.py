import sublime, sublime_plugin

import sys

class PasteReplaceCommand(sublime_plugin.TextCommand):
	def replace(self, text):
		vars = [
			('height', 'width'),
			('width', 'height'),
			('top', 'left'),
			('bottom', 'right'),
			('left', 'top'),
			('right', 'bottom'),
			('clientX', 'clientY'),
			('pageX', 'pageY'),
			('.x', '.y'),
			('clientY', 'clientX'),
			('pageY', 'pageX'),
			('.y', '.x'),
			('first-child', 'last-child'),
			('last-child', 'first-child'),
			('latitude', 'longitude'),
			('longitude', 'latitude')
		]

		replace = []

		for s, r in vars:
			replace.append((s, r[0] + '_SMIR_' + r[1:]))

			r = r.capitalize()
			replace.append((s.capitalize(), r[0] + '_SMIR_' + r[1:]))

			r = r.upper()
			replace.append((s.upper(), r[0] + '_SMIR_' + r[1:]))


		for s, r in vars:
			key = r[0] + '_SMIR_' + r[1:]
			replace.append((key, r))

			r = r.capitalize()
			key = r[0] + '_SMIR_' + r[1:]
			replace.append((key, r))

			r = r.upper()
			key = r[0] + '_SMIR_' + r[1:]
			replace.append((key, r))


		for s, r in replace:
			text = text.replace(s, r)

		return text

	def run(self, edit):
		if self.view.settings().get('is_widget'):
			return

		text = self.replace(sublime.get_clipboard())
		if text:
			sublime.set_clipboard(text)
			self.view.run_command("paste")
