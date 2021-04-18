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

5. Tutorial is available at
	CISCO LIVE: https://www.ciscolive.com/c/dam/r/ciscolive/us/docs/2017/pdf/DEVNET-2568.pdf
	Random Guy: https://tawmio.com/2019/07/08/trex-ciscos-stateful-stateless-traffic-generator/
	
6. Sample router configuration tutorial is available at
	https://trex-tgn.cisco.com/trex/doc/trex_config_guide.html
	
7. Github repo for GUI
	stateful: 	https://github.com/exalt-tech/trex-stateful-gui/blob/features/bassam/infrastructure/README.md
	stateless: 	https://github.com/cisco-system-traffic-generator/trex-stateless-gui

8. Installation from GitHub:
	https://github.com/cisco-system-traffic-generator/trex-core
	https://github.com/cisco-system-traffic-generator/trex-core/wiki
	
9. Faq:
	https://trex-tgn.cisco.com/trex/doc/trex_faq.html
	
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

8. Use the following command to run the TRex with a specified packet profile

sudo ./t-rex-64 -f cap2/dns.yaml -d 10

This will use template in dns.yaml file to run the TRex server for 10 seconds

Look at the tcpdump screens at step 6. to see output 

8. We need to figure out how to do TCP communication using TRex as all the rest is UDP communication. The server and host is set. 