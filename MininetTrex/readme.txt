The following the documentation for running 2 TRex and 2 host in the following topology: 
                  (Trex1)
		     |
	             |
 	(h1,Trex2)--(s1)--(h3)
		     |
		     |
		   (h2)
This experiment assumes you have 2 instances of TRex running in 
/opt/trex1/v2.89 
and 
/opt/trex2/v2.289 

This also assumes you have 2 trex configuration file as used to start them using --cfg tag while running TRex server 
/etc/trex_cfg1.yaml 
and 
/etc/trex_cfg2.yaml

if you dont have it then do the following to copy the files to your /etc/ or use --cfg to redirect to the location of the configuration file
cp cfg/trex_cfg1.yaml /etc/
cp cfg/trex_cfg2.yaml /etc/

To start copy all the bash files (*.sh) and python files (*.py) into /opt/ and run the following
sudo -i
cd /opt/
chmod u+x /opt/*.sh
chmod u+x /opt/*.py

Output for ls command should be the following after installation of 2 trex instance and extracting all the codes
:/opt/# ls
cfg   cleanupH1Mininet.sh  cleanup.sh  cleanupTrexMininet.sh  readme.txt  runMininet.py  runTrexMininet.sh  setupH1MininetPart1.sh  setupH1MininetPart2.sh  setupTrexH1Link.sh  setupTrexMininet.sh
trex1 trex2

To start the experiment just run the following code in sudo or sudo -i
This bash script contains the sequence of starting Mininet topology configuring TRex in host1 and connecting TRex to the swtich s1 from root namespace and finally cleaning up the whole setup.
./runTrexMininet.sh

if you dont have permission follow this code
sudo -i
cd /opt/
chmod u+x *.py
chmod u+x *.sh
./runTrexMininet.sh

The following is the sequence of running files and the sequence to run this is important

./runTrexMininet.sh
	This file contains code to start the mininet topology and then cleanup the mininet topology

./runMininet.py
	starts the mininet with the above topology

Note: The need to split the setup into 2 is the ping h1-> h2 and others fail when the newly created links are not set to up. Hence we run the below file

./setupH1MininetPart1.sh
	Is called within the runMininet.py using h1.cmd() to setup the links in host 1. The code to up the link needs to be run from the rootnamespace so its commented here.

Note: Some of the commands in the file is commented because the same script is converted to python in runMininet.py, if you are adamant about cleaning up just one section. Uncomment and run in H1 in bash.

./setupTrexH1Link.sh
	Is called within the runMininet.py using subprocess.call() to up the links in root namespace. This needs to be run before setupH1MininetPart2.sh to ensure connectivity is unhindered.

./setupH1MininetPart2.sh
	Is called within the runMininet.py using h1.cmd() to setup the remaining links and connect to the s1 switch using ovs-vsctl 

Note: Some of the commands in the file is commented because the same script is converted to python in runMininet.py, if you are adamant about setting up the environment ,then uncomment and run in H1 in bash.

./setupTrexMininet.sh
	Is called within the runMininet.py using subprocess.call to setup Trex outside the mininet i.e rootnamespace

./cleanup.sh
	Cleans up the mininet, delete any process using port 6653/tcp and Calls cleanupTrexMininet.sh

./cleanupH1Mininet.sh
	Removes all the links and connection made to setup the TRex server within h1. But this isn't called in cleanup as this needs to be run inside mininet to remove connection.

./cleanupTrexMininet.sh
	Removes all the links and connection made to setup the Trex server in rootnamespace.

