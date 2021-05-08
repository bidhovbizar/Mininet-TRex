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

To start the experiment just run the following code in sudo or sudo -i
This python script contains the sequence of starting Mininet topology configuring TRex in host1 and connecting TRex to the swtich s1 from root namespace
./runMininet.py

if you dont have permission follow this code
sudo -i
chmod u+x *.py
chmod u+x *.sh
./runMininet.py

The following is the sequence of running files and the sequence to run this is important

./runMininet.py
	starts the mininet with the above topology

./setupH1MininetPart1.sh
	Is called within the runMininet.py using h1.cmd() to setup the links in host 1
Note: The need to split the setup into 2 is the ping h1-> h2 and others fail when the newly created links are not set to up. Hence we run the below file

./setupTrexH1Link.sh
	Is called within the runMininet.py using subprocess.call() to up the links in root namespace

./setupH1MininetPart2.sh
	Is called within the runMininet.py using h1.cmd() to setup the remaining links and connect to the s1 switch using ovs-vsctl 
Note: There is a xterm command inside this but doesn't work for some reason

./setupTrexMininet.sh
	Is called within the runMininet.py using subprocess.call to setup Trex outside the mininet i.e rootnamespace

./cleanup.sh
	Calls cleanupH1Mininet.sh and cleanupTrexMininet.sh

./cleanupH1Mininet.sh
	Removes all the links and connection made to setup the TRex server within h1.

./cleanupTrexMininet.sh
	Removes all the links and connection made to setup the Trex server in rootnamespace

