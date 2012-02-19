#
# Hengjie (c) All rights reserved.
#

import re

copy_pasted_text = """1	Germany	Frankfurt	Frankfurt 2, Germany		s445.pingdom.com	46.165.195.139
2	Czech Republic	Prague	Prague, Czech Republic		s429.pingdom.com	178.255.154.2
3	Switzerland	Zurich	Zurich, Switzerland		s428.pingdom.com	178.255.153.2
4	Italy	Milan	Milan, Italy		s427.pingdom.com	178.255.155.2
5	United States	Newark	Newark, NJ		s426.pingdom.com	64.237.55.3
6	Austria	Vienna	Vienna, Austria		s425.pingdom.com	178.255.152.2
7	Canada	Calgary	Calgary, Canada		s431.pingdom.com	64.141.100.136
8	United Kingdom	Manchester	Manchester, UK		s424.pingdom.com	212.84.74.156
9	United States	San Francisco	San Francisco, CA		s422.pingdom.com	173.204.85.217
10	United States	Charlotte	Charlotte, NC		s430.pingdom.com	69.59.28.19
11	United States	San Jose	San Jose, CA		s432.pingdom.com	50.23.94.74
12	United States	Portland	Portland, OR		s444.pingdom.com	199.87.228.66
13	United States	Philadelphia	Philadelphia, PA		s443.pingdom.com	76.72.167.90
14	United States	St. Louis	St. Louis, MO		s441.pingdom.com	69.64.56.47
15	France	Roubaix	Roubaix, France		s440.pingdom.com	176.31.228.137
16	Canada	Toronto	Toronto, Canada		s439.pingdom.com	184.75.210.186
17	United States	Phoenix	Phoenix, AZ		s435.pingdom.com	108.62.115.226
18	Portugal	Lisbon	Lisbon, Portugal		s434.pingdom.com	94.46.4.1
19	Germany	Dusseldorf	Dusseldorf, Germany		s433.pingdom.com	46.20.45.18
20	United States	Denver	Denver, CO		s421.pingdom.com	173.248.147.18
21	United States	Las Vegas	Las Vegas, NV		s420.pingdom.com	72.46.130.42
22	United Kingdom	London	London, UK		s401.pingdom.com	78.136.27.223
23	United States	Dallas	Dallas 4, TX		s402.pingdom.com	67.192.120.134
24	United States	Herndon	Herndon, VA		s403.pingdom.com	207.97.207.200
25	United States	Houston	Houston 3, TX		s405.pingdom.com	207.218.231.170
26	Netherlands	Amsterdam	Amsterdam 2, Netherlands		s406.pingdom.com	95.211.87.85
27	United Kingdom	London	London 2, UK		s407.pingdom.com	83.170.113.102
28	United States	Dallas	Dallas 5, TX		s408.pingdom.com	74.52.50.50
29	United States	Los Angeles	Los Angeles, CA		s410.pingdom.com	204.152.200.42
30	France	Strasbourg	Strasbourg, France		s411.pingdom.com	85.25.176.167
31	United States	Atlanta	Atlanta, GA		s412.pingdom.com	174.34.162.242
32	Spain	Madrid	Madrid, Spain		s419.pingdom.com	94.46.240.121
33	United States	Washington	Washington, DC		s418.pingdom.com	208.43.68.59
34	United States	Seattle	Seattle, WA		s417.pingdom.com	67.228.213.178
35	United States	Tampa	Tampa, FL		s415.pingdom.com	96.31.66.245
36	Denmark	Copenhagen	Copenhagen, Denmark		s416.pingdom.com	82.103.128.63
37	United States	Chicago	Chicago, IL		s414.pingdom.com	174.34.156.130
38	United States	New York	New York, NY		s413.pingdom.com	70.32.40.2
39	Canada	Montreal	Montreal, Canada		s34.pingdom.com	67.205.112.79
40	Sweden	Falkenberg	Falkenberg, Sweden		s442.pingdom.com	94.247.174.83
41	United States	Dallas	Dallas 6, TX		s409.pingdom.com	74.53.193.66"""

ips = re.findall(r'[0-9]+(?:\.[0-9]+){3}', copy_pasted_text, flags=re.MULTILINE | re.DOTALL)

for ip in ips:
    print "csf -a {0} Pingdom".format(ip)
