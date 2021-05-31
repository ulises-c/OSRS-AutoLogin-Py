import subprocess
import os
import time

macRuneLite = '/Applications/RuneLite.app'
runeLite = 'RuneLite'

def is_runnning(app):
    count = int(subprocess.check_output(["osascript",
                "-e", "tell application \"System Events\"",
                "-e", "count (every process whose name is \"" + app + "\")",
                "-e", "end tell"]).strip())
    return count > 0

def activate_runelite(rl_status=is_runnning(runeLite)):
    if(not rl_status):
        # Open RuneLite on macOS, if already open it brings the window to the front
        os.system('open ' + macRuneLite)

        # Sleep to let RuneLite load
        time.sleep(20)

    elif(rl_status):
        os.system('open ' + macRuneLite)

        time.sleep(1)

rl_running = is_runnning(runeLite)