import sublime
import sublime_plugin
import webbrowser

class GitlinkCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        path = self.view.file_name()
        (row, col) = self.view.rowcol(self.view.sel()[0].begin())
        url = localPathToUrl(path, str(1+row))
        if url == "":
            print "File is not managed by git.musta.ch"
            pass
        else:
            webbrowser.open_new(url)

def localPathToUrl(path, row):
    repoPaths = path.split("/repos/", 1)
    if len(repoPaths) == 1:
        return ""
    repoPath = repoPaths[1]
    segs = repoPath.split("/", 1)
    branch = "production" if segs[0].lower() == "chef" else "master"
    return "https://git.musta.ch/airbnb/" + segs[0] + "/blob/" + branch + "/" + segs[1] + "#L" + row
