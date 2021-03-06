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
		self.addLink(r2, r4, cls=TCLink, bw=0.5, **linkopt)
		self.addLink(r2, r3, cls=TCLink, bw=1, **linkopt)
		self.addLink(r1, r4, cls=TCLink, bw=1, **linkopt)
		
class MyTopoBuffer (Topo):
	def __init__(self, queue_size, **opts):
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
		self.addLink(h1, r1, max_queue_size=queue_size, use_htb=True, cls=TCLink, bw=1, **linkopt)
		self.addLink(h1, r2, max_queue_size=queue_size, use_htb=True, cls=TCLink, bw=1, **linkopt)
		self.addLink(h2, r3, max_queue_size=queue_size, use_htb=True, cls=TCLink, bw=1, **linkopt)
		self.addLink(h2, r4, max_queue_size=queue_size, use_htb=True, cls=TCLink, bw=1, **linkopt)
		self.addLink(r1, r3, max_queue_size=queue_size, use_htb=True, cls=TCLink, bw=0.5, **linkopt)
		self.addLink(r2, r4, max_queue_size=queue_size, use_htb=True, cls=TCLink, bw=0.5, **linkopt)
		self.addLink(r2, r3, max_queue_size=queue_size, use_htb=True, cls=TCLink, bw=1, **linkopt)
		self.addLink(r1, r4, max_queue_size=queue_size, use_htb=True, cls=TCLink, bw=1, **linkopt)
		

def runTopo():
	# Memastikan mininet bersih dari cache sebelumnya
	os.system('mn -c')

	# CLO 1 Membangun Topologi
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
	#h1.cmd("ip route add default gw 194.169.1.2 h1-eth0")
	#ke R2
	h1.cmd("ifconfig h1-eth1 194.169.6.1/30")
	#h1.cmd("ip route add default gw 194.169.6.2 h1-eth1")
	
	#H2
	#ke R3
	h2.cmd("ifconfig h2-eth0 194.169.3.1/30")
	#h2.cmd("ip route add default gw 194.169.3.2 h2-eth0")
	#ke R4
	h2.cmd("ifconfig h2-eth1 194.169.4.1/30")
	#h2.cmd("ip route add default gw 194.169.4.2 h2-eth1")
	
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
	
	#Uji konektivitas
	'''
	print("\nUji Konektivitas R1-R3")
	r1.cmdPrint('ping -c 5 194.169.2.2')
	print("\n Uji Konektivitas R1-R4")
	r1.cmdPrint('ping -c 5 194.169.7.2')
	
	print("\nUji Konektivitas R2-R3")
	r2.cmdPrint('ping -c 5 194.169.8.2')
	print("\nUji Konektivitas R2-R4")
	r2.cmdPrint('ping -c 5 194.169.5.2')
	
	print("\nUji Konektivitas H1-R1")
	h1.cmdPrint('ping -c 5 194.169.1.2')
	print("\nUji Konektivitas H1-R2")
	h1.cmdPrint('ping -c 5 194.169.6.2')
	
	print("\nUji Konektivitas H2-R3")
	h2.cmdPrint('ping -c 5 194.169.3.2')
	print("\nUji Konektivitas H2-R4")
	h2.cmdPrint('ping -c 5 194.169.4.2')
	'''
	
	#CLO 2 Routing
	
	#Routing H1
	h1.cmd("ip rule add from 194.169.1.1 table 1")
	h1.cmd("ip rule add from 194.169.6.1 table 2")
	#table 1
	h1.cmd("ip route add 194.169.1.0/30 dev h1-eth0 scope link table 1")
	h1.cmd("ip route add default via 194.169.1.2 dev h1-eth0 table 1")
	h1.cmd("ip route add default gw 194.169.1.2 dev h1-eth0")
	h1.cmd("ip route add default scope global nexthop via 194.169.1.2 dev h1-eth0")
	#table 2
	h1.cmd("ip route add 194.169.6.0/30 dev h1-eth1 scope link table 2")
	h1.cmd("ip route add default via 194.169.6.2 dev h1-eth1 table 2")
	h1.cmd("ip route add default gw 194.169.6.2 dev h1-eth1")
	h1.cmd("ip route add default scope global nexthop via 194.169.6.2 dev h1-eth1")
	
	#Routing H2
	h2.cmd("ip rule add from 194.169.3.1 table 1")
	h2.cmd("ip rule add from 194.169.4.1 table 2")
	#table 1
	h2.cmd("ip route add 194.169.3.0/30 dev h2-eth0 scope link table 1")
	h2.cmd("ip route add default via 194.169.3.2 dev h2-eth0 table 1")
	h2.cmd("ip route add default gw 194.169.3.2 dev h2-eth0")
	h2.cmd("ip route add default scope global nexthop via 194.169.3.2 dev h2-eth0")
	#table 2
	h2.cmd("ip route add 194.169.4.0/30 dev h2-eth1 scope link table 2")
	h2.cmd("ip route add default via 194.169.4.2 dev h2-eth1 table 2")
	h2.cmd("ip route add default gw 194.169.4.2 dev h2-eth1")
	h2.cmd("ip route add default scope global nexthop via 194.169.4.2 dev h2-eth1")
	
	
	#Routing R1
	r1.cmd("sysctl net.ipv4.ip_forward=1")
	r1.cmd("route add -net 194.169.3.0/30 gw 194.169.2.2")
	r1.cmd("route add -net 194.169.4.0/30 gw 194.169.7.2")
	r1.cmd("route add -net 194.169.6.0/30 gw 194.169.7.2")
	r1.cmd("route add -net 194.169.8.0/30 gw 194.169.2.2")
	r1.cmd("route add -net 194.169.5.0/30 gw 194.169.7.2")
	
	#Routing R2
	r2.cmd("sysctl net.ipv4.ip_forward=1")
	r2.cmd("route add -net 194.169.1.0/30 gw 194.169.8.2")
	r2.cmd("route add -net 194.169.3.0/30 gw 194.169.8.2")
	r2.cmd("route add -net 194.169.4.0/30 gw 194.169.5.2")
	r2.cmd("route add -net 194.169.7.0/30 gw 194.169.5.2")
	r2.cmd("route add -net 194.169.2.0/30 gw 194.169.8.2")
	
	#Routing R3
	r3.cmd("sysctl net.ipv4.ip_forward=1")
	r3.cmd("route add -net 194.169.1.0/30 gw 194.169.2.1")
	r3.cmd("route add -net 194.169.6.0/30 gw 194.169.8.1")
	r3.cmd("route add -net 194.169.4.0/30 gw 194.169.8.1")
	r3.cmd("route add -net 194.169.7.0/30 gw 194.169.2.1")
	r3.cmd("route add -net 194.169.5.0/30 gw 194.169.8.1")
	
	#Routing R4
	r4.cmd("sysctl net.ipv4.ip_forward=1")
	r4.cmd("route add -net 194.169.1.0/30 gw 194.169.7.1")
	r4.cmd("route add -net 194.169.6.0/30 gw 194.169.5.1")
	r4.cmd("route add -net 194.169.3.0/30 gw 194.169.7.1")
	r4.cmd("route add -net 194.169.8.0/30 gw 194.169.5.1")
	r4.cmd("route add -net 194.169.2.0/30 gw 194.169.7.1")
	
	print("\nRouting telah selesai\n")

	#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
	'''
	#CLO 3 TCP
	#setting h2 sebagai server
	h2.cmd("iperf -s &")
	
	#tcpdump
	h2.cmd("tcpdump -c 15 -w result.pcap tcp& -i h2-eth0 ")
	time.sleep(2)
	
	#h1 client
	h1.cmd("iperf -t 5 -c 194.169.3.1 &")
	time.sleep(5)
	h1.cmdPrint("tcpdump -r result.pcap")
	
	print("Proses tcpdump telah selesai")
	'''
	
	CLI(net)
	net.stop()
	
def runTopoBuffer():
	print("\nUji Buffer pada Topologi\n")
	ukuran_buffer = int(input("Masukkan ukuran buffer "))

	# Memastikan mininet bersih dari cache sebelumnya
	os.system('mn -c')

	# CLO 1 Membangun Topologi
	topo = MyTopoBuffer(ukuran_buffer)
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
	#h1.cmd("ip route add default gw 194.169.1.2 h1-eth0")
	#ke R2
	h1.cmd("ifconfig h1-eth1 194.169.6.1/30")
	#h1.cmd("ip route add default gw 194.169.6.2 h1-eth1")
	
	#H2
	#ke R3
	h2.cmd("ifconfig h2-eth0 194.169.3.1/30")
	#h2.cmd("ip route add default gw 194.169.3.2 h2-eth0")
	#ke R4
	h2.cmd("ifconfig h2-eth1 194.169.4.1/30")
	#h2.cmd("ip route add default gw 194.169.4.2 h2-eth1")
	
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
	
	#CLO 2 Routing
	
	#Routing H1
	h1.cmd("ip rule add from 194.169.1.1 table 1")
	h1.cmd("ip rule add from 194.169.6.1 table 2")
	#table 1
	h1.cmd("ip route add 194.169.1.0/30 dev h1-eth0 scope link table 1")
	h1.cmd("ip route add default via 194.169.1.2 dev h1-eth0 table 1")
	h1.cmd("ip route add default gw 194.169.1.2 dev h1-eth0")
	h1.cmd("ip route add default scope global nexthop via 194.169.1.2 dev h1-eth0")
	#table 2
	h1.cmd("ip route add 194.169.6.0/30 dev h1-eth1 scope link table 2")
	h1.cmd("ip route add default via 194.169.6.2 dev h1-eth1 table 2")
	h1.cmd("ip route add default gw 194.169.6.2 dev h1-eth1")
	h1.cmd("ip route add default scope global nexthop via 194.169.6.2 dev h1-eth1")
	
	#Routing H2
	h2.cmd("ip rule add from 194.169.3.1 table 1")
	h2.cmd("ip rule add from 194.169.4.1 table 2")
	#table 1
	h2.cmd("ip route add 194.169.3.0/30 dev h2-eth0 scope link table 1")
	h2.cmd("ip route add default via 194.169.3.2 dev h2-eth0 table 1")
	h2.cmd("ip route add default gw 194.169.3.2 dev h2-eth0")
	h2.cmd("ip route add default scope global nexthop via 194.169.3.2 dev h2-eth0")
	#table 2
	h2.cmd("ip route add 194.169.4.0/30 dev h2-eth1 scope link table 2")
	h2.cmd("ip route add default via 194.169.4.2 dev h2-eth1 table 2")
	h2.cmd("ip route add default gw 194.169.4.2 dev h2-eth1")
	h2.cmd("ip route add default scope global nexthop via 194.169.4.2 dev h2-eth1")
	
	
	#Routing R1
	r1.cmd("sysctl net.ipv4.ip_forward=1")
	r1.cmd("route add -net 194.169.3.0/30 gw 194.169.2.2")
	r1.cmd("route add -net 194.169.4.0/30 gw 194.169.7.2")
	r1.cmd("route add -net 194.169.6.0/30 gw 194.169.7.2")
	r1.cmd("route add -net 194.169.8.0/30 gw 194.169.2.2")
	r1.cmd("route add -net 194.169.5.0/30 gw 194.169.7.2")
	
	#Routing R2
	r2.cmd("sysctl net.ipv4.ip_forward=1")
	r2.cmd("route add -net 194.169.1.0/30 gw 194.169.8.2")
	r2.cmd("route add -net 194.169.3.0/30 gw 194.169.8.2")
	r2.cmd("route add -net 194.169.4.0/30 gw 194.169.5.2")
	r2.cmd("route add -net 194.169.7.0/30 gw 194.169.5.2")
	r2.cmd("route add -net 194.169.2.0/30 gw 194.169.8.2")
	
	#Routing R3
	r3.cmd("sysctl net.ipv4.ip_forward=1")
	r3.cmd("route add -net 194.169.1.0/30 gw 194.169.2.1")
	r3.cmd("route add -net 194.169.6.0/30 gw 194.169.8.1")
	r3.cmd("route add -net 194.169.4.0/30 gw 194.169.8.1")
	r3.cmd("route add -net 194.169.7.0/30 gw 194.169.2.1")
	r3.cmd("route add -net 194.169.5.0/30 gw 194.169.8.1")
	
	#Routing R4
	r4.cmd("sysctl net.ipv4.ip_forward=1")
	r4.cmd("route add -net 194.169.1.0/30 gw 194.169.7.1")
	r4.cmd("route add -net 194.169.6.0/30 gw 194.169.5.1")
	r4.cmd("route add -net 194.169.3.0/30 gw 194.169.7.1")
	r4.cmd("route add -net 194.169.8.0/30 gw 194.169.5.1")
	r4.cmd("route add -net 194.169.2.0/30 gw 194.169.7.1")
	
	print("\nRouting telah selesai\n")
	
	#setting traffic dengan iperf
	h2.cmd("iperf -s &")
	h1.cmd("iperf -t 40 -B 194.169.1.1 -c 194.169.3.1 &")
	h1.cmd("iperf -t 40 -B 194.169.6.1 -c 194.169.3.1 &")
	
	CLI(net)
	net.stop()
	
if __name__=='__main__':
	setLogLevel('info')
	runTopo()
	test_buffer = 'y'
	while test_buffer == 'y':
		runTopoBuffer()
		test_buffer = input("Test buffer kembali? y/n   ")
