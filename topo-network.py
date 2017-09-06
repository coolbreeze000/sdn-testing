#!/usr/bin/python

from mininet.topo import Topo
from mininet.net import Mininet
from mininet.cli import CLI
from mininet.log import setLogLevel
from mininet.node import Node, RemoteController, OVSSwitch#, Lagopus


class MyTopo(Topo):
    "Simple topology example."

    def __init__(self):
        "Create custom topo."

        # Initialize topology
        Topo.__init__(self)

        # Add hosts
        h1 = self.addHost('h1')
        h3 = self.addHost('h3')
        h4 = self.addHost('h4')

        # Add switches
        sw1 = self.addSwitch('sw1')
        sw3 = self.addSwitch('sw3')

        # Add links
        self.addLink(sw3, sw1)

        self.addLink(h1, sw1)
        self.addLink(h3, sw3)
        self.addLink(h4, sw3)

        # Add NAT
        # nat = self.addNode( 'nat', cls=NAT, ip=natIP, inNamespace=False )
        # self.addLink( nat, sw1 )


def runTopo():
    topo = MyTopo()
    net = Mininet(topo=topo, controller=lambda name: RemoteController(name, ip='127.0.0.1'), switch=OVSSwitch,
                  autoSetMacs=True)
    net.addNAT().configDefault()
    net.start()
    CLI(net)
    net.stop()


if __name__ == '__main__':
    # This runs if this file is executed directly
    setLogLevel('info')
    runTopo()

topos = {'mytopo': (lambda: MyTopo())}
