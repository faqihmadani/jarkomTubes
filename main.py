from mininet.topo import Topo
from mininet.net import Mininet
from mininet.node import Node
from mininet.log import setLogLevel, info
from mininet.cli import CLI
from mininet.link import TCLink
from mininet.node import CPULimitedHost
import time
import os


# CLO 1
class MyTopo (Topo):
	def __init__(self, **opts):
		Topo.__init__(self, **opts)

    		# Membuat objek host
		H1 = self.addHost('H1', ip='10.0.0.1/24')
		H2 = self.addHost('H2', ip='10.0.0.2/24')

    		# Membuat objek router
		R1 = self.addHost('R1')
		R2 = self.addHost('R2')
		R3 = self.addHost('R3')
		R4 = self.addHost('R4')

		# Membuat Link
		self.addLink(R1, R4, bw=1)
		self.addLink(R1, R3, bw=0.5)
		self.addLink(R2, R3, bw=1)
		self.addLink(R2, R4, bw=0.5)
		self.addLink(H1, R1, bw=1)
		self.addLink(H1, R2, bw=1)
		self.addLink(H2, R3, bw=1)
		self.addLink(H2, R4, bw=1)


def runTopo():
	# Memastikan mininet bersih dari cache sebelumnya
	os.system('mn -c')

	# Membangun Topologi
	topo = MyTopo()
	net = Mininet(topo=topo, host=CPULimitedHost, link=TCLink)
	net.start()
