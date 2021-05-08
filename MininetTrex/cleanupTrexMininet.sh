#!/bin/bash
#Run the following script to have a functioning mininet linear topology with TRex installed in one host and connected to the switch
#        (Trex)
#          |
# (h1) -- (s1) -- (h2)
#

# Create a mininet topology with 2 host
#fuser -k 6653/tcp
#sudo mn -c
#sudo mn 

#Connect 2 veth pair to switch s1 in mininet
ip link delete veth0 
ip link delete veth1
ovs-vsctl del-port s1 eth0
ovs-vsctl del-port s1 eth1
ip link
echo ""
ovs-vsctl show
echo "Cleanup successfull"
