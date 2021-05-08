#Run the following script to have a functioning mininet linear topology with TRex installed in one host and connected to the switch
#              (Trex1)
#                |
# (h1,Trex2) -- (s1) -- (h3)
#                |
#                |
#              (h2)


#Connect 2 veth pair to switch s1 in mininet
ip link add veth0 type veth peer name eth0
ip link add veth1 type veth peer name eth1
ovs-vsctl add-port s1 eth0
ovs-vsctl add-port s1 eth1
ip address add 10.0.0.10/24 dev veth0
ip address add 10.0.0.11/24 dev veth1
ip link set veth0 up
ip link set veth1 up
ip link set eth0 up
ip link set eth1 up
ip address show veth0 | grep inet
ip address show veth1 | grep inet
#ping 10.0.0.10 -c 1
#ping 10.0.0.11 -c 1
echo ""
ovs-vsctl show
echo ""
cd ./trex1/v2.89/
#Run the Trex Server in on xterm and Trex console/client in another console
xterm -e ./t-rex-64 --cfg /etc/trex_cfg1.yaml -i &
sleep 2
xterm -hold -e ./trex-console -f -s localhost -p 4601 

#echo
#echo "Deleting TRex1 Setup"
#bash ../../cleanupTrexMininet.sh
