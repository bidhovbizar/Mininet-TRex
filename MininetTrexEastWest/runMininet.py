#!/usr/bin/python                                                                            
from mininet.topo import Topo
from mininet.net import Mininet
from mininet.util import dumpNodeConnections
from mininet.log import setLogLevel

from mininet.cli import CLI
import subprocess
import time

def simpleTest():
    "Create and test a simple network"
    net = Mininet()
    c1 = net.addController()
    s1 = net.addSwitch('s1')
    h1 = net.addHost('h1', ip='10.0.0.1')
    net.addLink(h1, s1)
    h2 = net.addHost('h2', ip='10.0.0.2')
    net.addLink(h2, s1)
    h3 = net.addHost('h3', ip='10.0.0.3')
    net.addLink(h3, s1)
    net.start()

    print("Setting up TRex1 on H1")
    h1.cmd("./setupH1MininetPart1.sh")
    print("Setuped Part1: Links and connections")
    subprocess.call("pwd", shell=True)
    subprocess.call("./setupTrexH1Link.sh", shell=True)
    print("\nSetuped Rootnamespace Links to Join to bridge")
    h1.cmd("./setupH1MininetPart2.sh")
    print("Setuped Part2: The server and client is up and running")

    print("Setting up TRex2 on H2")
    h2.cmd("./setupH2MininetPart1.sh")
    print("Setuped Part1: Links and connections")
    subprocess.call("pwd", shell=True)
    subprocess.call("./setupTrexH2Link.sh", shell=True)
    print("\nSetuped Rootnamespace Links to Join to bridge")
    h2.cmd("./setupH2MininetPart2.sh")
    print("Setuped Part2: The server and client is up and running")

    #Setup link and connection for TRex1 in rootnamespace
    #subprocess.call("./setupTrexMininet.sh", shell=True)
    
    #Run the Trex Server in root namespace on xterm and Trex console/client in another console
    #print("\nSetting up Trex1 in rootnamespace")
    #subprocess.call("pwd", shell=True)
    #subprocess.call("cd /opt/trex1/v2.89/;xterm -T 'root namespace server' -e ./t-rex-64 --cfg /etc/trex_cfg1.yaml -i &", shell=True)
    #time.sleep(4)
    #subprocess.call("cd /opt/trex1/v2.89/;xterm -hold -T 'root namespace client/console' -e ./trex-console -f -s localhost -p 4601 &", shell=True)
    #print("\nTrex1 Server started")
    
    #Start the tcpdump for host h1,h2 and h3
    print("\nStarting tcpdump on all the host")
    h1.cmd("xterm -hold -T 'tcpdump h1-eth0' -e tcpdump -nli h1-eth0 &", shell=True)
    h2.cmd("xterm -hold -T 'tcpdump h2-eth0' -e tcpdump -nli h2-eth0 &", shell=True)
    h3.cmd("xterm -hold -T 'tcpdump h3-eth0' -e tcpdump -nli h3-eth0 &", shell=True)
    
    print( "Dumping host connections" )
    dumpNodeConnections(net.hosts)
    print( "Testing network connectivity" )
    net.pingAll()
    
    #h1.cmd('bash ./setupH1Mininet.sh')
    print( "Starting Commandline Interface")
    CLI(net)

    net.stop()

if __name__ == '__main__':
    # Tell mininet to print useful information
    setLogLevel('info')
    simpleTest()
