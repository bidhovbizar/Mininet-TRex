## Table of Contents
* [General Topology](#general-topology)
* [Pre Requisites](#pre-requisites)
* [Running Trex in Mininet](#running-trex-in-mininet)
* [Explanation](#explanation)

## General Topology
The following the documentation for running 2 TRex and 2 host in the following topology: 
```
 	(h1,Trex1)--(s1)--(h3)
		     |
		     |
		 (h2,Trex2)
```
## Pre requisites
This experiment assumes you have 2 instances of TRex running in 
`$ /opt/trex1/v2.89` 
and 
`$ /opt/trex2/v2.89`. 

This also assumes you have 2 trex configuration file as used to start them using --cfg tag while running TRex server 
`$ /etc/trex_cfg1.yaml` 
and 
`$ /etc/trex_cfg2.yaml`.

If you dont have it, then do the following to copy the files to your /etc/ or use --cfg to redirect to the location of the configuration file.
```
$ cp cfg/trex_cfg1.yaml /etc/
$ cp cfg/trex_cfg2.yaml /etc/
```

Copy the files in astf named my_http_simple.py into trex1 and trex2.
```
cp astf/* /opt/trex1/v2.89/astf/
cp astf/* /opt/trex2/v2.89/astf/
```

To start copy README.md, the bash files (*.sh) and python files (*.py) into /opt/ and run the following:
```
$ sudo -i
$ cd /opt/
$ chmod u+x /opt/*.sh
$ chmod u+x /opt/*.py
```

Output for ls command should be the following after installation of 2 trex instance and extracting all the codes:
```
$ :/opt/# ls
README.md            cleanupH2Mininet.sh  runMininet.py      setupH1MininetPart1.sh  setupH2MininetPart1.sh  setupTrexH1Link.sh
cleanupH1Mininet.sh  cleanup.sh           runTrexMininet.sh  setupH1MininetPart2.sh  setupH2MininetPart2.sh  setupTrexH2Link.sh

```
Install Wireshark and run it in sudo and run `$ sudo wireshark &`. We will monitor interface eth0 which is the peer link of veth0 in H1 to see the communication between H1 and H2.

## Running Trex in Mininet
To start the experiment just run the following code in sudo or sudo -i.
This bash script contains code to start Mininet topology (3 Host, 1 switch), configuring TRex in H1 and H2  and connecting TRex to the swtich s1 from root namespace and finally cleaning up the whole setup.
```
$ ./runTrexMininet.sh
```

If you dont have permission follow this code
```
$ sudo -i
$ cd /opt/
$ chmod u+x *.py
$ chmod u+x *.sh
$ ./runTrexMininet.sh
```

Try to ensure connectivity within the network by `mininet> pingall`. If there is a connectivity issue then just close it and restart again. Usually this works. 

Our code is meant to run Trex1 in H1 as client and Trex2 in H2 as server. Once the setup is ready then go to the trex-console and run the following in the same order. Server should run first only then client should start.
In  trex2-console
```
trex> portattr
```
In trex1-console
```
trex> portattr
```

Now you start the wireshark and observe eth0 port.  
Check whether the address is resolved and you see the mac address. Then you start the server first and then client.
In trex2-console

```
trex> start -f astf/my_http_simple.py
```


In trex1-console
```
trex> start -f astf/my_http_simple.py
```

Now observe wireshark!
Note: Its expected to see so many RST in wireshark.

## Explanation
The following is the sequence of running files and the sequence to run this is important.

`$ ./runTrexMininet.sh`
	This file contains code to start the mininet topology and then cleanup the mininet topology.

`$ ./runMininet.py`
	starts the mininet with the above topology.

Note: The need to split the setup into 2 is the ping h1-> h2 and others fail when the newly created links are not set to up. Hence we run the below file.

`$ ./setupH1MininetPart1.sh`
	Is called within the runMininet.py using h1.cmd() to setup the links in host 1. The code to up the link needs to be run from the rootnamespace so its commented here.

Note: Some of the commands in the file is commented because the same script is converted to python in runMininet.py, if you are adamant about cleaning up just one section. Uncomment and run in H1 in bash.

`$ ./setupTrexH1Link.sh`
	Is called within the runMininet.py using subprocess.call() to up the links in root namespace. This needs to be run before setupH1MininetPart2.sh to ensure connectivity is unhindered.

`$ ./setupH1MininetPart2.sh`
	Is called within the runMininet.py using h1.cmd() to setup the remaining links and connect to the s1 switch using ovs-vsctl.


`$ ./setupH2MininetPart1.sh`
	Is called within the runMininet.py using h2.cmd() to setup the links in host 2. The code to up the link needs to be run from the rootnamespace so its commented here.

Note: Some of the commands in the file is commented because the same script is converted to python in runMininet.py, if you are adamant about cleaning up just one section. Uncomment and run in H2 in bash.

`$ ./setupTrexH2Link.sh`
	Is called within the runMininet.py using subprocess.call() to up the links in root namespace. This needs to be run before setupH2MininetPart2.sh to ensure connectivity is unhindered.

`$ ./setupH2MininetPart2.sh`
	Is called within the runMininet.py using h2.cmd() to setup the remaining links and connect to the s1 switch using ovs-vsctl 

Note: Some of the commands in the file is commented because the same script is converted to python in runMininet.py, if you are adamant about setting up the environment ,then uncomment and run in H2 in bash.


`$ ./cleanup.sh`
	Cleans up the mininet, delete any process using port 6653/tcp and Calls cleanupTrexMininet.sh

`$ ./cleanupH1Mininet.sh`
	Removes all the links and connection made to setup the TRex server within h1. But this isn't called in cleanup as this needs to be run inside mininet to remove connection.

`$ ./cleanupH2Mininet.sh`
	Removes all the links and connection made to setup the TRex server within h1. But this isn't called in cleanup as this needs to be run inside mininet to remove connection.

