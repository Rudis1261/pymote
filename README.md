![Workflow](https://raw.github.com/drpain/pymote/master/assets/img/remote.jpg)  

**The short and the long:**
-----------

######Tested on Fedora 18
######(Requirements)  

Python V2.7 (Normally installed with Linux as standard)
xdotool 

######Installation On Ubuntu / Debian based OS's
```terminal
sudo apt-get install python
sudo apt-get install xdotool
sudo apt-get install git
git clone http://github.com/drpain/pymote.git
cd pymote/
chmod +x * -R
./pymote.py
```

######Installation On Fedora
```terminal
sudo yum install python
sudo yum install xdotool
sudo yum install git
git clone http://github.com/drpain/pymote.git
cd pymote/
chmod +x * -R
./pymote.py
```
You may need to open the port 8080 in your Firewall (Iptables) on Fedora
  
***Once upon a time***  
I wanted a remote for Ubuntu so I created web-the-black-mote which worked, however it required numerous servers and I felt it a tad unnessacary.

I have been reading up and it Python has a load of simple HTTP servers. Neat, hells yeah! So I modified my code and now I am cutting out the need for PHP, Apache and Redis. More of that thank you!

***So what did I need it for?***  
I built a remote for my ***Ubuntu*** since my Compro Remote stopped working.

***How does it work?***  
No 1. Install the Dependencies as indicated in the installation section above.
No 2. If not running you can start the application from withing the pymote directory by running the following command in terminal. 

```terminal
./pymote.py
```
You can expect a result like this if everything is ok:
**Starting server on PORT:8080, use <Ctrl-C> to stop**

You would then access the server "Your computer" with your phone via WIFI on the default port of 8080.
For example my pc's IP Address is 192.168.1.3, so on my phone I go to my browser and I enter 192.168.1.3:8080. You are then presented with the remote which allows you to issue commands to your computer, and in turn the pymote script will dispatch the command via xdotool. Awesome hey?

----------

## The CODE ##
***pymote.py***   
Coming soon
