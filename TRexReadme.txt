Materials
1. TRex Documentation for documentations:
	https://trex-tgn.cisco.com/trex/doc/

2. Documentation for running it on docker
	https://trex-tgn.cisco.com/trex/doc/trex_vm_manual.html
	Note that the links in the page in 1 do not have https:// as a prefix which will give you connection timed out error. Please add the prefix to avoid seeing the Problem Loading page.
   
3. Guide to download and run TRex from binaries on OS (preferred CentOS)
	https://trex-tgn.cisco.com/trex/doc/trex_manual.html#_obtaining_the_trex_package
    
4. Main Documentation
	https://trex-tgn.cisco.com/trex/doc/trex_book.pdf
	
5. TRex Stateless Documentation
	https://trex-tgn.cisco.com/trex/doc/trex_stateless.html#_getting_started_tutorials
		Use this link as reference for help regarding client side trex and server side trex
		https://groups.google.com/g/trex-tgn/c/jiEhkjYRsHE/m/GdzuQKpSAQAJ
		https://groups.google.com/g/trex-tgn/c/PY6Dca5EisI
		https://groups.google.com/g/trex-tgn/search?q=separate%20machine
		https://groups.google.com/g/trex-tgn/c/-CewQaVF6Cw/m/mfRx-Y8TCgAJ
		https://groups.google.com/g/trex-tgn/c/OT2sbfBSYWs/m/nmQz_Ie_BwAJ
		https://groups.google.com/g/trex-tgn/c/7aYO5rrnx7o
	
	
6. Tutorial is available at
	CISCO LIVE: https://www.ciscolive.com/c/dam/r/ciscolive/us/docs/2017/pdf/DEVNET-2568.pdf   | page 19
  	Random Guy: https://tawmio.com/2019/07/08/trex-ciscos-stateful-stateless-traffic-generator/
	
7. TRex advanced statefull Documentation
	https://trex-tgn.cisco.com/trex/doc/trex_astf.html#_client_server_only_mode
	
8. Comparing TRex Advanced Stateful performance to Linux NGINX
	https://trex-tgn.cisco.com/trex/doc/trex_astf_vs_nginx.html#_setup_trex_vs_trex
	
9. Sample router configuration tutorial is available at
	https://trex-tgn.cisco.com/trex/doc/trex_config_guide.html
	
10. Github repo for GUI
	stateful: 	https://github.com/exalt-tech/trex-stateful-gui/blob/features/bassam/infrastructure/README.md
	stateless: 	https://github.com/cisco-system-traffic-generator/trex-stateless-gui

11. Installation from GitHub:
	https://github.com/cisco-system-traffic-generator/trex-core
	https://github.com/cisco-system-traffic-generator/trex-core/wiki
	
12. Faq:
	https://trex-tgn.cisco.com/trex/doc/trex_faq.html

13. Statless GUI Help				   
	https://learningnetwork.cisco.com/s/question/0D53i00000U2p7sCAB/using-the-trex-stateless-gui-with-the-trex-node-in-cmlp-2

14. Trex Configuration File YAML Help 
	https://trex-tgn.cisco.com/trex/doc/trex_manual.html#trex_config_yaml_config_file
	
15. TRex PCAP captured fixing help
	1. Low RTT due to fast capture can be fixed by increasing the RTT as we want or use centerize the capture point as 
		response time of packet 1 from Server = time average of 2 consequtive sent packages from Client
	2. File size about 1000kb should be trimmed
	https://trex-tgn.cisco.com/trex/doc/trex_appendix_fixing_pcaps.html

16. How to Log in Trex
	help1: https://trex-tgn.cisco.com/trex/doc/trex_rpc_server_spec.html
	help2: https://github.com/cisco-system-traffic-generator/trex-core/issues/306
	
17. Trex API
	Go to 'Python Automation API': https://trex-tgn.cisco.com/trex/doc/
	Tutorial1: https://trex-tgn.cisco.com/trex/doc/trex_control_plane_peek.html
	Tutorial2: https://trex-tgn.cisco.com/trex/doc/trex_control_plane_design_phase1.html
	API Documentation: https://trex-tgn.cisco.com/trex/doc/cp_docs/index.html
	Stateless Python API: https://trex-tgn.cisco.com/trex/doc/cp_stl_docs/index.html
	ASTF Client Module: https://trex-tgn.cisco.com/trex/doc/cp_astf_docs/api/client_code.html
	
	
How To Install and run TRex
1. Download ubuntu20.0 server (without the gui) and install it in your Oracle Virtual Box
2. The screen resolution will be low for the CLI so install virtual box Ubuntu guest utilities by running the below command

sudo apt-get install virtualbox-guest-utils virtualbox-guest-x11 virtualbox-guest-dkms

You will be able to see Display settings when you press right click on the screen to change the screen resolution or you could also go to Oracle Dialogue box and View-> Virtual Screen 1 -> 1024 * 768
3. Remember gnome-terminal won't be available so none of the applications that you can see in the GUI will of any use. So press 

CTL+ALT+F3 

to shift to CLI mode and run

sudo apt install gnome-terminal

4. Press 

CTL+ALT+F2 

to revert back to GUI and press 

CTL+ALT+T 

to start a terminal. 

5. Use the following link to explore TRex

https://trex-tgn.cisco.com/trex/doc/trex_vm_manual.html

6. Go to virtualbox-> settings -> network
change NAT to bridged adapter (I kept Qualcomm)

7. The T-rex gui given in the documentation doesn't work. If we google T-rex gui we will obtain t-rex-stateless-gui which can only work in stateless mode. So run the following command 

sudo docker run --rm -it --privileged --cap-add=ALL -p 4500:4500 -p 4501:4501 -p 4507:4507 trexcisco/trex

within the interactive bash run the stateless version without the  configuration file which ensures t-rex to run stateless

sudo ./t-rex-64 -i 

8. Go to the T-rex-stateless-gui and connect to the ip address of the virtualbox which can be pinged. 
This can be found by 'ifconfig'

-------------------------------------------------
How to Learn Field Engine API

1. https://pypi.org/project/trex-api/
https://trex-tgn.cisco.com/trex/doc/cp_stl_docs/index.html#how-to-install
https://www.digitalocean.com/community/questions/how-to-run-multiple-containers-of-the-same-image-and-expose-different-ports

--------------------------------------------------
How to setup one CentOS server as TRex host and the other CentOS as DUT.

1. In virtualbox go to File -> Host Network Manager -> Create a new "VirtualBox Host Only Ethernet Adapter" with IPv4 Address/Mask at gateway as 192.168.56.1/24 and enable DHCP Server

2. Create 2 host only adapter for the CentOS in virtualbox by selecting Settings->network
Enable 2nd and 3rd Adapter
Attached to: Host-Only Adapter
Name: VirtualBox Host Only Ethernet Adapter (As mentioned in step 1 this will ensure the new adapter be in a separate network)

3. Open the OS and check ifconfig to find 2 new adapters and check their IP addresses and ping to each other to ensure the ARP packet and the MAC address have been discovered as the packet we are going to sent are IP packets with different IP address so it may go out through other adapter (e.g. enp0s3) which will push the packet outside the host-only network. 
If we ping before running TRex or binding the ports then the MAC address will be stored in the "arp -a" and hence the packet wont go out through other gate way but will use 192.168.56.1.

4. Use any of the following method to find out the mac address of the DUT.
	a) ifconfig on each OS find the Host-Only Adapter and see the value with "ether" 
	
	b) go to the installation of trex and run 
	./dpdk_setup_port.py -ifconfig
	which will give you the the ports available and 
==========L2 Configuration: Using MAC Address===================
5. Use ./dpdk_setup_port.py -i to setup the /etc/trex_cfg.yaml file such that the mac address of the DUT is placed as the destination mac address.
Note: We need the mac address of the receiver to finish the configuration. Mac address of the source is autmatically found by the python file

Output of ifconfig in Trex host is 
enp0s8:----
		ether 08:00:27:48:60:1f txqueuelen 1000 (ethernet)
		.
		.
		.
enp0s9:----
		ether 08:00:27:bc:0b:49 txqueuelen 1000 (ethernet)
		
Output of ifconfig in DUT host is
enp0s8:----
		ether 08:00:27:a0:40:5b txqueuelen 1000 (ethernet)
		.
		.
		.
enp0s9:----
		ether 08:00:27:15:82:45 txqueuelen 1000 (ethernet)

The /etc/trex_cfg.yaml output will look like
	port_info:
		-dest_mac: 08:00:27:a0:40:5b
		 src_mac:  08:00:27:48:60:1f
		-dest_mac: 08:00:27:15:82:45
		 src_mac:  08:00:27:bc:0b:49

6. run tcpdump -i enp0s8 on one terminal
	run tcpdump -i enp0s9 on another terminal assuming enp0s8 and enp0s9 are the 2 newly created ports on DUT OS for receiveing the packets from the TRex server

==========L3 Configuration: Using IP Address===================
7. Similarly to setup /etc/trex_cfg.yaml file to sent packets using IP address use the following template
Assuming TRex Host and DUT Host have IP addresses as 
TRex Host 
enp0s8: 192.168.56.6
enp0s9: 192.168.56.7

DUT Host
enp0s8: 192.168.56.3
enp0s9: 192.168.56.5

port_info:
	-ip: 192.168.56.6
	 default_gw: 192.168.56.3
	-ip: 192.168.56.7
	 default_gw: 192.168.56.5

Return to step 6 to see the packets
						Method I
8. Use the following command to run the TRex with a specified packet profile

sudo ./t-rex-64 -f cap2/dns.yaml -d 10

This will use template in dns.yaml file to run the TRex server for 10 seconds

Look at the tcpdump screens at step 6. to see output 
						
						METHOD II (Ref: https://www.ciscolive.com/c/dam/r/ciscolive/us/docs/2017/pdf/DEVNET-2568.pdf)
8. Launch TRex Server 
sudo ./t-rex-64 -i 

Switch to second terminal and launch TRex console
sudo trex-console

Use the following commands to see the src and dst IP and mac ID (This way we know whether TRex is configured in L2(mac) or L3(IP) mode)
trex> portattr


To change the sender address or move from L2 to L3
	a. Enter service mode
		trex> service
	b. Configure port 0 and 1 with source address 192.168.56.6 and 56.7(doesnt matter 1.1.1.1 would work) and destination address 192.168.56.3 and 192.168.56.5
	
	trex(service)> l3 -p 0 --src 192.168.56.6 --dst 192.168.56.3
	trex(service)> l3 -p 1 --src 192.168.56.7 --dst 192.168.56.5
	
	c. Sent arp to check connectivity and response.
	
	trex(service)> arp
	
	d. service --off
	
	e. start -f cap2/dns.yaml 
		Do this for mimicing tcp communication i.e. server client communication. Packets will be sent in the following template
		16.0.0.1 -> 48.0.0.1
		48.0.0.1 -> 16.0.0.1
		
					OR
	   start -f stl/udp_1pkt.py
		Do this for mimicing UDP communication. Packets will be sent in the following template
		16.0.0.1 -> 48.0.0.1
		16.0.0.1 -> 48.0.0.1
		
8. We need to figure out how to do TCP communication using TRex as all the rest is UDP communication. The server and host is set. 

-------------------------------------------------------------------------
==========L2/L3 Configuration: Network Namespace with veth pair on Single Machine ===================
1. Create a network namespace (netns) called DUT
2. Create 2 veth pair named veth0-d<-->eth0-d and veth1-d<-->eth1-d. Shift eth0-d and eth1-d to netns DUT named
3. Do the basic chore of adding IP address UP the links and lo.
3. Run TRex in root namespace with interfaces as [veth0-d, veth1-d] in /etc/trex_cfg.yaml with mac address of the device in netns DUT as destination and source as mac address of interface veth0-d and veth1-d.
4. Run tcpdump in DUT on eth0-d and eth1-d
5. Run portattr in trex console and see the arp resolution. 

NB: arp resolution had some trouble. L3 configuration didn't resolve properly.
	Check the following
	1. ip route	
	See that device connected to port 0 is the device at the route in root network namespace and DUT netns
	2. /etc/trex_cfg.yaml is not set in low_footprint mode
	3. TRex is in promiscous mode
	4. There is a dpdk driver problem that creates arp issue. Need more investigation
	
6. If the resolution doesn't give you the mac address of the DUT then manually enter the values assuming port 0 has arp missing
	service 
	l2 -p 0 --dst aa:bb:cc:dd:ee
	service --off
7. To run stateless UDP packets 
	start -f stl/udp_1pkt.py -d 5
	
	NB: stateful tcp packets like cap2/dns.yaml wont work while running /t-rex-64 -i 
		Run TRex separately in non interactive mode sudo ./t-rex-64 -f cap2/dns.yaml -d 5