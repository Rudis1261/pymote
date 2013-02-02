#PyMote Beta V0.1
###Linux Based Remote control (Debian & Fedora)

![Remote](https://raw.github.com/drpain/pymote/master/assets/img/remote.jpg)  ![Hotkeys](https://raw.github.com/drpain/pymote/master/assets/img/hotkeys.jpg) 

The Details
--------- 
 
I originally created this because my stupid remote stopped working with my Ubuntu, but since then I have grown fond of this way of doing things. PyMote consists of a server and a client.

- The **Server** being a simple Python server.
- The **Client** a phone which accesses the server through a browser using a ***WIFI*** connection

Installation
--------- 

I am personally running Fedora 18, but theoretically it should work on Ubuntu as it was originally written to work with Ubuntu.

####Installation On Ubuntu / Debian based OS's

```terminal
sudo apt-get install python  
sudo apt-get install xdotool  
sudo apt-get install git  
git clone http://github.com/drpain/pymote.git  
cd pymote/  
chmod +x * -R  
./pymote.py  
```

####Installation On Fedora
```terminal
sudo yum install python  
sudo yum install xdotool  
sudo yum install git  
git clone http://github.com/drpain/pymote.git  
cd pymote/  
chmod +x * -R  
./pymote.py  
```

**On Fedora, You will need to open a "Persistent" port in your firewall for port 8080 otherwise you will not be able to open the server on your phone!!**

![code](https://raw.github.com/drpain/pymote/master/pymote.py)
