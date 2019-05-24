# XXE Lab #

This virtual environment is a simple php web application that contains an example of an XML eXternal Entity vulnerability.

## Setting Up ##

This lab is designed to be used in [vagrant](https://www.vagrantup.com/). To get setup, first you need to clone this repo and then start vagrant.

	$ git clone https://github.com/jbarone/xxelab.git
	$ cd xxelab
	$ vagrant up

## Using ##

Once the site is up and running you simple navigate your browser to [http://192.168.33.10](http://192.168.33.10) and have fun.

## Docker ##

You can now run XXELab in a Docker container. Build the image:

	$ git clone https://github.com/jbarone/xxelab.git
	$ cd xxelab
	$ docker build -t xxelab .

Run:

	$ docker run -it --rm -p 127.0.0.1:5000:80 xxelab

Open [http://localhost:5000](http://localhost:5000) and have fun.

### Notes ###

This lab works best when you make use of a proxy that will allow you to see the requests and responses. There are many you can use, but here are a few recommended ones:

- [Burp Suite](https://portswigger.net/burp/)
- [Zed Attack Proxy (ZAP)](https://www.owasp.org/index.php/OWASP_Zed_Attack_Proxy_Project)
- [Mitm Proxy](https://mitmproxy.org)
