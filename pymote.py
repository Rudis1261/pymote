#!/usr/bin/env python
import SocketServer, SimpleHTTPServer, subprocess, os, commands
from urlparse import urlparse, parse_qsl

# Change the PWD to this location
abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
os.chdir(dname)

# Variables (Constants)
PORT = 8080
IP = ''
DEFAULT_VIDEO = 'xbmc'
DEFAULT_MUSIC = 'rhythmbox'
APPS = ('totem', 'vlc', 'xbmc', 'rhythmbox')

# Kill all running aps
def killApps():

    # Loop through them and kill them as we go along
    for APP in APPS:
        getPid = commands.getoutput("ps -e | grep " + APP + " | awk {'print $1'}")
        #print "ps -e | grep " + APP + " | awk {'print $1'} , PID: " + getPid

        # If there is a PID, then the application is running and we can kill it
        if getPid != '':
            commands.getoutput('kill ' + getPid)
            print 'Killing ' + APP + ", VIA: " + 'kill ' + getPid

# This function will be used to confirm whether an application is running
def appRunning(APP):

    # Get the PID, if it exists then the app is running
    getPid = commands.getoutput("ps -e | grep " + APP + " | awk {'print $1'}")

    # If there is a PID, then the application is indeed running
    if getPid != '':
        return False
    else:
        return True

# This will perform the actions
def commandKeys(pressed):

    # The dictionary with the commands and switches to be run
    defaults = {'up':       ['xdotool', 'key', "Up"],
                'down':     ['xdotool', 'key', "Down"],
                'left':     ['xdotool', 'key', "Left"],
                'right':    ['xdotool', 'key', "Right"],
                'ok':       ['xdotool', 'key', "KP_Enter"],
                'play':     ['xdotool', 'key', "XF86AudioPlay"],
                'info':     ['xdotool', 'key', 'Menu'],
                'back':     ['xdotool', 'key', "Escape"],
                'next':     ['xdotool', 'key', "XF86AudioNext"],
                'prev':     ['xdotool', 'key', "XF86AudioPrev"],
                'video':    [DEFAULT_VIDEO],
                'stop':     ['xdotool', 'key', "XF86AudioStop"],
                'music':    [DEFAULT_MUSIC],
                'vol-up':   ['xdotool', 'key', "XF86AudioRaiseVolume"],
                'vol-down': ['xdotool', 'key', "XF86AudioLowerVolume"]
            }

    # Was the keypress valid? If so, run the relevant command
    if pressed == "power":
        killApps()

    # The media launchers are a bit different, we need to check that the application is not already fired up
    elif pressed == "video" or pressed == "music":

        # Check if it's already running, if not kill all other players listed in apps and open this one
        if appRunning(str(defaults[pressed])) == False:
            #killApps()
            xdotool(defaults[pressed], True)
            print "Launching " + str(defaults[pressed])
        else:
            print str(defaults[pressed]) + " is already running"

    # Othewise lets check the action to be run, based on the key pressed
    elif pressed in defaults:
        xdotool(defaults[pressed])

    # Command not found sadly
    else:
        print pressed, "command not found, Eish"

# This little baby is what sends the command from the dictionary to the kernel to be processed.
def xdotool(action, surpress=False):
    ps = subprocess.Popen(action);
    if surpress == False:
        print action

# Start the SimpleHTTPServer up and look for actions, otherwise server the remote page
class CustomHandler(SimpleHTTPServer.SimpleHTTPRequestHandler):
    def do_GET(self):
        GET = parse_qsl(urlparse(self.path)[4])
        if self.path.find("?") > 0:
            self.send_response(200)
            self.send_header('Content-type','text/html')
            self.end_headers()
            # Is a command provided?
            if GET[0][0] == 'command':
                self.wfile.write('1')
                commandKeys(GET[0][1])

            # Let's do an alive check response as well
            elif GET[0][0] == 'alive':
                self.wfile.write('1');

            # Not, sure give a 0 response
            else:
                self.wfile.write('0')
            return

        # Otherwise render the page as per normal
        else:
            SimpleHTTPServer.SimpleHTTPRequestHandler.do_GET(self) #dir listing

# Launch the server
try:
    httpd = SocketServer.ThreadingTCPServer((IP, PORT),CustomHandler)
    print 'Starting server on PORT:' + str(PORT) + ', use <Ctrl-C> to stop'
    httpd.serve_forever()
except KeyboardInterrupt:
    print " pressed. Closing server"
    httpd.shutdown()
