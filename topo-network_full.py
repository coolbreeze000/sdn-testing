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
        h2 = self.addHost('h2')
        h3 = self.addHost('h3')
        h4 = self.addHost('h4')
        h5 = self.addHost('h5')
        h6 = self.addHost('h6')
        h7 = self.addHost('h7')
        h8 = self.addHost('h8')
        h9 = self.addHost('h9')
        h10 = self.addHost('h10')
        h11 = self.addHost('h11')
        h12 = self.addHost('h12')
        h13 = self.addHost('h13')
        h14 = self.addHost('h14')
        h15 = self.addHost('h15')
        h16 = self.addHost('h16')

        # Add switches
        sw1 = self.addSwitch('sw1')
        sw2 = self.addSwitch('sw2')
        sw3 = self.addSwitch('sw3')
        sw4 = self.addSwitch('sw4')
        sw5 = self.addSwitch('sw5')
        sw6 = self.addSwitch('sw6')
        sw7 = self.addSwitch('sw7')
        #sw7 = self.addSwitch('sw8', cls=Lagopus)
        # sw8 is Zodiac FX Physical Switch

        # Add links
        self.addLink(sw1, sw2)
        self.addLink(sw2, sw1)
        self.addLink(sw3, sw1)
        self.addLink(sw3, sw2)
        self.addLink(sw4, sw1)
        self.addLink(sw4, sw2)
        self.addLink(sw5, sw1)
        self.addLink(sw5, sw2)
        self.addLink(sw6, sw1)
        self.addLink(sw6, sw2)
        self.addLink(sw7, sw1)
        self.addLink(sw7, sw2)

        self.addLink(h1, sw1)
        self.addLink(h2, sw2)
        self.addLink(h3, sw3)
        self.addLink(h4, sw3)
        self.addLink(h5, sw3)
        self.addLink(h6, sw3)
        self.addLink(h7, sw3)
        self.addLink(h8, sw4)
        self.addLink(h9, sw4)
        self.addLink(h10, sw5)
        self.addLink(h11, sw5)
        self.addLink(h12, sw6)
        self.addLink(h13, sw6)
        self.addLink(h14, sw6)
        self.addLink(h15, sw7)
        self.addLink(h16, sw7)

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
