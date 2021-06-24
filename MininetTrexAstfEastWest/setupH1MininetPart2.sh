#!/bin/sh
#Run the following script to install TRex2 in host1 
#        (Trex1)
#          |
# (h1,Trex2) -- (s1) -- (h2)
#
#			Part 1
#Connect 2 veth pair to switch s1 in mininet
#ip link add veth0 type veth peer name eth0
#ip link add veth1 type veth peer name eth1
#ip link set eth0 netns 1
#ip link set eth1 netns 1
#ovs-vsctl add-port s1 eth0
#ovs-vsctl add-port s1 eth1
#ip address add 10.0.0.10/24 dev veth0
#ip address add 10.0.0.11/24 dev veth1
#ip link set veth0 up
#ip link set veth1 up

#                       End of Part 1 
#eth2 and eth3 are moved to root namespace so run this from there and finish the rest
#ip link set eth0 up
#ip link set eth1 up

#			Part 2
ip address show veth0 | grep inet
ip address show veth1 | grep inet
ping 10.0.0.2 -c 1
ping 10.0.0.3 -c 1
echo ""
ovs-vsctl show
echo ""
cd ./trex1/v2.89/
#Run the Trex Server in on xterm and Trex console/client in another console
xterm -T "h1 Server" -e ./t-rex-64 --cfg /etc/trex_cfg1.yaml -i --astf &
sleep 5 
echo 'Trex1 Server started'
xterm -hold -T "h1 Client/console" -e ./trex-console -f -s 10.0.0.1 -p 4601 &
echo
#echo "The TRex2 will be deleted when Mininet closes"
