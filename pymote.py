#!/usr/bin/env python
import SocketServer, SimpleHTTPServer, subprocess, os, commands
from urlparse import urlparse, parse_qsl

# VARS
PORT = 8080
IP = ''


# This function will be used to confirm whether an application is running   
def appRunning(appName):
    getStatus = commands.getoutput('ps -C ' + appName)
    if appName in getStatus:
        return True
    else:
        return False
 
# This will perform the actions   
def commandKeys(pressed):
    
    # To check which applications are running. This will be used for application specific short-cuts.
    # applications = ['xbmc', 'rhythmbox', 'vlc']
    applications = {"vlc"       :   {   'play':['xdotool', 'key', "space"],
                                        'next':['xdotool', 'key', "n"],
                                        'prev':['xdotool', 'key', "b"],
                                        'vol-up':['xdotool', 'key', "ctrl+Up"],
                                        'vol-down':['xdotool', 'key', "ctrl+Down"], 
                                    },
                        
                    "totem"     :   {   'play':['xdotool', 'key', "space"],
                                        'next':['xdotool', 'key', "n"],
                                        'prev':['xdotool', 'key', "b"],
                                        'vol-up':['xdotool', 'key', "XF86AudioRaiseVolume"],
                                        'vol-down':['xdotool', 'key', "XF86AudioLowerVolume"],                                     
                                    },
                    
    }
    
    # The dictionary with the commands and switches to be run
    defaults = {'up':['xdotool', 'key', "Up"],
            'down':['xdotool', 'key', "Down"],
            'left':['xdotool', 'key', "Left"],
            'right':['xdotool', 'key', "Right"],
            'ok':['xdotool', 'key', "KP_Enter"],
            'play':['xdotool', 'key', "XF86AudioPlay"],
            'info':['xdotool', 'key', 'Menu'],
            'back':['xdotool', 'key', "Escape"],
            'next':['xdotool', 'key', "XF86AudioNext"],
            'prev':['xdotool', 'key', "XF86AudioPrev"],
            'xbmc':['xbmc'],
            'stop':['xdotool', 'key', "XF86AudioStop"],
            'music': ['xdotool', 'key', "XF86Go"],
            'vol-up':['xdotool', 'key', "XF86AudioRaiseVolume"],
            'vol-down':['xdotool', 'key', "XF86AudioLowerVolume"],    
            }
    
    # Check if the app is running?
    for app in applications:
        if appRunning(app):
            if pressed in applications[app]:
                xdotool(applications[app][pressed])
    
    # Was the keypress valid? If so, run the relevant command
    if pressed in defaults:        
        xdotool(defaults[pressed])
    else:
        print pressed, "command not found, Eish"
 
# This little baby is what sends the command from the dictionary to the kernel to be processed.
def xdotool(action):
    ps = subprocess.Popen(action);
    print action #Comment this out, if you do not want to see which action was taken. Usefull for debugging
    

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
    print "pressed. Closing server"
    httpd.shutdown()