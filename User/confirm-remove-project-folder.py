import sublime
import sublime_plugin


class RemoveFolderConfirmationListener(sublime_plugin.EventListener):
    def on_window_command(self, window, command, args):
        if command == 'remove_folder':
            if not sublime.ok_cancel_dialog('Are you sure you want to remove folder {}?'.format(args['dirs']), 'Yes'):
                return ('noop', args)