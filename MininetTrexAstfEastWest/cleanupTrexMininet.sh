#!/bin/bash
#Run the following script to have a functioning mininet linear topology with TRex installed in one host and connected to the switch
#        (Trex)
#          |
# (h1) -- (s1) -- (h2)
#
#Connect 2 veth pair to switch s1 in mininet
echo "cleaning connection in rootnamespace"
ip link delete veth0 
ip link delete veth1
ovs-vsctl del-port s1 eth0
ovs-vsctl del-port s1 eth1
ip link
echo ""
ovs-vsctl show
echo "Cleanup successfull"
echo ""
