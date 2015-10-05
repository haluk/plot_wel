#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: hd
# @Date:   2015-10-05 15:41:36
# @Last Modified by:   hd
# @Last Modified time: 2015-10-05 16:29:02
#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: hd
# @Date:   2015-10-05 15:41:36
# @Last Modified by:   hd
# @Last Modified time: 2015-10-05 15:41:36

import logging
import networkx as nx

from sys import argv

FORMAT = '%(asctime)-15s %(message)s'
logging.basicConfig(level = logging.INFO, format = FORMAT)

fh = open(argv[1], 'rb')

G = nx.read_weighted_edgelist(fh, delimiter = " ", nodetype = int)

fh.close()


logging.info("Graph %s is loaded" % (argv[1]))
logging.info("Number of vertices: %d" % (len(G.nodes())))
logging.info("Number of edges: %d" % (len(G.edges())))

# Max degree
node, degree = max(G.degree().iteritems(), key=lambda x:x[1])
logging.info("Maximum degree [Node id: %d, Degree: %d]" % (node, degree))

nx.write_dot(G, argv[2])
