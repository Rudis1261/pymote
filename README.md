#PyMote Beta V0.1
###Linux Based Remote control (Debian & Fedora)

![Remote](https://raw.github.com/drpain/pymote/master/assets/img/remote.jpg)  ![Hotkeys](https://raw.github.com/drpain/pymote/master/assets/img/hotkeys.jpg) 

The Details
--------- 
 
I originally created this because my stupid remote stopped working with my Ubuntu, but since then I have grown fond of this way of doing things. PyMote consists of a server and a client.

- The **Server** being a simple Python server.
- The **Client** a phone which accesses the server through a browser using a ***WIFI*** connection

Server Installation
--------- 

I am personally running Fedora 18, but theoretically it should work on Ubuntu as it was originally written to work with Ubuntu.

####Installing the server On Ubuntu / Debian based OS's

```terminal
sudo apt-get install python  
sudo apt-get install xdotool  
sudo apt-get install git  
git clone http://github.com/drpain/pymote.git  
cd pymote/  
chmod +x * -R  
./pymote.py  
```

####Installing the server On Fedora  
```terminal  
sudo yum install python  
sudo yum install xdotool  
sudo yum install git  
git clone http://github.com/drpain/pymote.git  
cd pymote/  
firewall-cmd --permanent --zone=home --add-port=8080/tcp
firewall-cmd --permanent --zone=work --add-port=8080/tcp
firewall-cmd --permanent --zone=internal --add-port=8080/tcp
firewall-cmd --permanent --zone=public --add-port=8080/tcp
chmod +x * -R  
./pymote.py  
```  
You may have noted that we need to add firewall rules to open the port. Should you not like port 8080, you can change this to a port of your liking. Have a look as the "Customizing the Server" section.  
Want to know more about the filewall-cmd. ![FirewallD Wiki, check it out](https://fedoraproject.org/wiki/FirewallD)  
  
  
##Customise the server, to suit your needs
![pymote.py](pymote.py) lines 10 through 15
```python
# Variables (Constants)
PORT = 8080
IP = ''
DEFAULT_VIDEO = 'xbmc'
DEFAULT_MUSIC = 'rhythmbox'
APPS = ('totem', 'vlc', 'xbmc', 'rhythmbox')
```
In the pymote.py file you have the ability to define some things to suite your liking.  
   
**PORT = 8080**    

We will attempt to open this port to create the in-directory SimpleHTTPServer. Which will allow us to connecto to the PC from our phone.  

This value can be set to any port of your liking, please note that this port should not conflict with commonly used ports such as 80 if you already have a webserver running on your PC. Or 21 if you have a FTP server. Not sure check this out ![Commonly used Ports](http://en.wikipedia.org/wiki/List_of_TCP_and_UDP_port_numbers)  

**DEFAULT_VIDEO = 'xbmc'** 
 
The default video variable is the application name which will be run if the Video Play icon is clicked. In this case mine is set to xbmc. Ensure that you can launch the application of your choosing from within a terminal and you should have no issues.

**DEFAULT_MUSIC = 'rhythmbox'**   

The default music player can also be set. In this case I am sticking to rhythmbox which does it's job. 

**APPS = ('totem', 'vlc', 'xbmc', 'rhythmbox')**  

This is a ![python tuple](http://www.diveintopython.net/native_data_types/tuples.html) of the applications which should be killed when the following actions are performed:  
- I launch the default video player or default music player
- Click on the Power button in the client side interface

