#Run the following script to install TRex2 in host1 
#        (Trex1)
#          |
# (h1,Trex2) -- (s1) -- (h2)
#
#			Part 1
#Connect 2 veth pair to switch s1 in mininet
ip link add veth2 type veth peer name eth2
ip link add veth3 type veth peer name eth3
ip link set eth2 netns 1
ip link set eth3 netns 1
ovs-vsctl add-port s1 eth2
ovs-vsctl add-port s1 eth3
ip address add 10.0.0.12/24 dev veth2
ip address add 10.0.0.13/24 dev veth3
ip link set veth2 up
ip link set veth3 up

#			End of Part 1 
#eth2 and eth3 are moved to root namespace so run this from there and finish the rest
#ip link set eth2 up
#ip link set eth3 up

#			Part 2
#ip address show veth2 | grep inet
#ip address show veth3 | grep inet
#ping 10.0.0.10 -c 1
#ping 10.0.0.11 -c 1
#echo ""
#ovs-vsctl show
#echo ""
#cd ./trex2/v2.89/
##Run the Trex Server in on xterm and Trex console/client in another console
#xterm -T "h1 Server" -e ./t-rex-64 --cfg /etc/trex_cfg2.yaml -i &
#sleep 10
##xterm -hold -T "h1 Client/console" -e ./trex-console -f -s 10.0.0.1 -p 4611 
#xterm -hold -T "h1 Client/console" -e ./trex-console -f -p 4611
#echo
#echo "The TRex2 will be deleted when Mininet closes"
