from logging import log
from mininet.topo import Topo
from mininet.net import Mininet
from mininet.node import Node
from mininet.log import setLogLevel, info
from mininet.cli import CLI
from mininet.link import TCLink
from mininet.node import CPULimitedHost
from mininet.node import Host, Node
import time
import os


# CLO 1
class MyTopo (Topo):
	def __init__(self, **opts):
		Topo.__init__(self, **opts)

		linkopt = {'delay' : '0ms', 'loss' : 0}

		# Membuat objek router
		r1 = self.addHost('r1')
		r2 = self.addHost('r2')
		r3 = self.addHost('r3')
		r4 = self.addHost('r4')

    		# Membuat objek host
		h1 = self.addHost('h1', cls=Host)
		h2 = self.addHost('h2', cls=Host)

    		
		# Membuat Link
		self.addLink(h1, r1, cls=TCLink, bw=1, **linkopt)
		self.addLink(h1, r2, cls=TCLink, bw=1, **linkopt)
		self.addLink(h2, r3, cls=TCLink, bw=1, **linkopt)
		self.addLink(h2, r4, cls=TCLink, bw=1, **linkopt)
		self.addLink(r1, r3, cls=TCLink, bw=0.5, **linkopt)
		self.addLink(r1, r4, cls=TCLink, bw=1, **linkopt)
		self.addLink(r2, r3, cls=TCLink, bw=1, **linkopt)
		self.addLink(r2, r4, cls=TCLink, bw=0.5, **linkopt)
		

def runTopo():
	# Memastikan mininet bersih dari cache sebelumnya
	os.system('mn -c')

	# Membangun Topologi
	topo = MyTopo()
	net = Mininet(topo=topo, host=CPULimitedHost, link=TCLink)
	net.start()
	#net.build()
	
	#Memasukkan objek host pada variabel
	h1,h2,r1,r2,r3,r4 = net.get('h1', 'h2', 'r1', 'r2', 'r3', 'r4')
	
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
	h1.cmd("ifconfig h1-eth0 194.169.1.1/30")
	#ke R2
	h1.cmd("ifconfig h1-eth1 194.169.6.1/30")
	
	#H2
	#ke R3
	h2.cmd("ifconfig h2-eth0 194.169.3.1/30")
	#ke R4
	h2.cmd("ifconfig h2-eth1 194.169.4.1/30")
	
	#R1
	#ke H1
	r1.cmd("ifconfig r1-eth0 194.169.1.2/30")
	#ke R3
	r1.cmd("ifconfig r1-eth1 194.169.2.1/30")
	#ke R4
	r1.cmd("ifconfig r1-eth2 194.169.7.1/30")
	
	#R2
	#ke H1
	r2.cmd("ifconfig r2-eth0 194.169.6.2/30")
	#ke R4
	r2.cmd("ifconfig r2-eth1 194.169.5.1/30")
	#ke R3
	r2.cmd("ifconfig r2-eth2 194.169.8.1/30")
	
	#R3
	#ke H2
	r3.cmd("ifconfig r3-eth0 194.169.3.2/30")
	#ke R1	
	r3.cmd("ifconfig r3-eth1 194.169.2.2/30")
	#ke R2
	r3.cmd("ifconfig r3-eth2 194.169.8.2/30")
	
	#R4
	#ke H2
	r4.cmd("ifconfig r4-eth0 194.169.4.2/30")
	#ke R2
	r4.cmd("ifconfig r4-eth1 194.169.5.2/30")
	#ke R1
	r4.cmd("ifconfig r4-eth2 194.169.7.2/30")
	
	
	
	#h1.cmd("ip route add default gw 194.169.1.2 h1-eth0")
	#h1.cmd("ip route add default gw 194.169.6.2 h1-eth1")
	
	#Routing H1
	#h1.cmd("ip rule add from 194.169.1.1 table 1")
	#h1.cmd("ip rule add from 194.169.6.1 table 2")
	#table 1
	#h1.cmd("ip route add 194.169.1.0/30 dev h1-eth0 scope link table 1")
	#h1.cmd("ip route add default via 194.169.1.2 dev h1-eth0 table 1")
	#h1.cmd("ip route add default gw 194.169.1.2 dev h1-eth0")
	#table 2
	#h1.cmd("ip route add 194.169.6.0/30 dev h1-eth1 scope link table 2")
	#h1.cmd("ip route add default via 194.169.6.2 dev h1-eth1 table 2")
	#h1.cmd("ip route add default gw 194.169.6.2 dev h1-eth1")
	
	#Routing H2
	#h2.cmd("ip rule add from 194.169.3.1 table 1")
	#h2.cmd("ip rule add from 194.169.4.1 table 2")
	#table 1
	#h2.cmd("ip route add 194.169.3.0/30 dev h2-eth0 scope link table 1")
	#h2.cmd("ip route add default via 194.169.3.2 dev h2-eth0 table 1")
	#table 2
	#h2.cmd("ip route add 194.169.4.0/30 dev h2-eth1 scope link table 2")
	#h2.cmd("ip route add default via 194.169.4.2 dev h2-eth1 table 2")
	
	
	#Routing R1
	#r1.cmd("route add -net ")
	
	
	#Uji konektivitas
	print("Uji Konektivitas H1-R1")
	h1.cmdPrint('ping -c 3 194.169.1.2')
	
	r1.cmdPrint('ping -c 3 194.169.2.2')
	
	print("Uji Konektivitas H1-R2")
	#h1.cmdPrint('ping -c 3 194.169.1.2')
	
	CLI(net)
	net.stop()
	
if __name__=='__main__':
	setLogLevel('info')
	runTopo()
