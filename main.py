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
		H1 = self.addHost('H1')
		H2 = self.addHost('H2')

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
	#net.start()
	net.build()
	
	#Memasukkan objek host pada variabel
	h1,h2,r1,r2,r3,r4 = net.get('H1', 'H2', 'R1', 'R2', 'R3', 'R4')
	
	#Setting H1
	h1.cmd("ifconfig h1-eth0 0")
	h1.cmd("ifconfig h1-eth1 0")
	
	#Setting H2
	h1.cmd("ifconfig h2-eth0 0")
	h1.cmd("ifconfig h2-eth1 0")
	
	#Setting R1
	r1.cmd("ifconfig r1-eth0 0")
	r1.cmd("ifconfig r1-eth1 0")
	r1.cmd("ifconfig r1-eth2 0")
	
	#Setting R2
	r2.cmd("ifconfig r2-eth0 0")
	r2.cmd("ifconfig r2-eth1 0")
	r2.cmd("ifconfig r2-eth2 0")
	
	#Setting R3
	r3.cmd("ifconfig r3-eth0 0")
	r3.cmd("ifconfig r3-eth1 0")
	r3.cmd("ifconfig r3-eth2 0")
	
	#Setting R4
	r4.cmd("ifconfig r4-eth0 0")
	r4.cmd("ifconfig r4-eth1 0")
	r4.cmd("ifconfig r4-eth2 0")
	
	#H1
	#ke R1
	h1.cmd("ifconfig h1-eth0 194.169.20.1/30")
	#ke R2
	h1.cmd("ifconfig h1-eth1 194.169.40.17/30")
	
	#R1
	#ke H1
	r1.cmd("ifconfig r1-eth0 194.169.20.2/30")
	#ke R3
	r1.cmd("ifconfig r1-eth1 194.169.20.5/30")
	#ke R4
	r1.cmd("ifconfig r1-eth2 194.169.20.29/30")
	
	#R2
	#ke H1
	r2.cmd("ifconfig r2-eth0 194.169.40.18/30")
	#ke R3
	r2.cmd("ifconfig r2-eth1 194.169.20.13/30")
	#ke R4
	r2.cmd("ifconfig r2-eth2 194.169.20.10/30")
	
	#R3
	#ke H2
	r3.cmd("ifconfig r3-eth0 194.169.20.21/30")
	#ke R1	
	r3.cmd("ifconfig r3-eth1 194.169.20.6/30")
	#ke R2
	r3.cmd("ifconfig r3-eth2 194.169.20.14/30")
	
	#R4
	#ke H2
	r4.cmd("ifconfig r4-eth0 194.169.40.25/30")
	#ke R1
	r4.cmd("ifconfig r4-eth1 194.169.20.30/30")
	#ke R2
	r4.cmd("ifconfig r4-eth2 194.169.20.9/30")
	
	#H2
	#ke R3
	h2.cmd("ifconfig h2-eth0 194.169.20.22/30")
	#ke R4
	h2.cmd("ifconfig h2-eth1 194.169.40.26/30")
	
	
	#Routing H1
	h1.cmd("ip rule add from 194.169.20.1 table 1")
	h1.cmd("ip rule add from 194.169.40.17 table 2")
	#table 1
	h1.cmd("ip route add 194.169.20.0/30 dev h1-eth0 scope link table 1")
	h1.cmd("ip route add default via 194.169.20.2 dev h1-eth0 table 1")
	#table 2
	h1.cmd("ip route add 194.169.40.16/30 dev h1-eth1 scope link table 2")
	h1.cmd("ip route add default via 194.169.40.18 dev h1-eth1 table 2")
	
	#Routing H2
	h2.cmd("ip rule add from 194.169.20.22 table 1")
	h2.cmd("ip rule add from 194.169.40.26 table 2")
	#table 1
	h2.cmd("ip route add 194.169.20.20/30 dev h2-eth0 scope link table 1")
	h2.cmd("ip route add default via 194.169.20.21 dev h2-eth0 table 1")
	#table 2
	h2.cmd("ip route add 194.169.40.24/30 dev h2-eth1 scope link table 2")
	h2.cmd("ip route add default via 194.169.40.25 dev h2-eth1 table 2")
	
	
	#Routing R1
	r1.cmd("route add -net ")
	
	
	
	
if __name__=='__main__':
	setLogLevel('info')
	runTopo()
