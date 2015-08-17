import sublime
import sublime_plugin
import subprocess
import re

class CommandOnSave(sublime_plugin.EventListener):
    def on_post_save(self, view):

        settings = sublime.load_settings('CommandOnSave.sublime-settings').get('commands')
        filepath = view.file_name()
        file = re.search('[^\/]*$').group(0)
        
        if not settings == None:
            for path in settings.keys():
                commands = settings.get(path)
                if filepath.startswith(path) and len(commands) > 0:
                    print("Command on Save:")
                    for command in commands:
                        p = subprocess.Popen([command, file], shell=True, stdout=subprocess.PIPE)
                        out, err = p.communicate()
                        print (out.decode('utf-8'))
