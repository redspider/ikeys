from flask import Flask, render_template, request, make_response
from functools import update_wrapper
from subprocess import Popen, PIPE
app = Flask(__name__)
app.config['DEBUG'] = True

triggers = {
    'bell': """
say "Bing"
    """,
    'expose': """
do shell script "/Applications/Mission\\\\ Control.app/Contents/MacOS/Mission\\\\ Control"
    """,
    'chrome': """
tell application "Chrome" to activate
    """,
    'pycharm': """
tell application "PyCharm" to activate
    """,
    'sparrow': """
tell application "Sparrow" to activate
    """,
    'terminal': """
tell application "iTerm" to activate
    """,
    'textual': """
tell application "Textual" to activate
    """,
    'mute': """
set volumeSettings to get volume settings
if output muted of volumeSettings is false then
    set volume with output muted
else
    set volume without output muted
end if
    """,
    'lock': """
tell application "System Events"
    start current screen saver
end tell
    """
}

def nocache(f):
    def new_func(*args, **kwargs):
        resp = make_response(f(*args, **kwargs))
        resp.cache_control.no_cache = True
        return resp
    return update_wrapper(new_func, f)

@app.route("/")
def index():
    return render_template('panel.jinja2')

@app.route("/trigger", methods=['POST'])
@nocache
def trigger():
    trigger = request.form['trigger']
    if not trigger in triggers:
        return "Unknown trigger"

    p = Popen(['osascript','-'],stdin=PIPE, stdout=PIPE, stderr=PIPE)
    p.communicate(triggers[trigger])
    return "OK"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8181)