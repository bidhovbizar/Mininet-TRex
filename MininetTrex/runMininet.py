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

    h1.cmd("./setupH1MininetPart1.sh")
    print("Setuped Part1")
    subprocess.call("pwd")
    subprocess.call("./setupTrexH1Link.sh")
    print("Setuped Rootnamespace Links")
    h1.cmd("./setupH1MinientPart2.sh")
    print("Setuped Part2")

    #Install TRex2 in host1
    h1.cmd("cd /opt/trex2/v2.89/;xterm -T 'h1 Server' -e ./t-rex-64 --cfg /etc/trex_cfg2.yaml -i &")
    time.sleep(2)
    print("Server started")
    h1.cmd("cd /opt/trex2/v2.89/;xterm -hold -T 'h1 Client/console' -e ./trex-console -f -s 10.0.0.1 -p 4611 &")
  
    #Install TRex1 in rootnamespace
#    subprocess.call("cd /opt/;./setupTrexMininet.sh")

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
