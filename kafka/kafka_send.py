from kazoo.client import KazooClient
from samsa.cluster import Cluster

zookeeper = KazooClient(hosts='20.26.19.36:10080')
zookeeper.start()
cluster = Cluster(zookeeper)
topic = cluster.topics['mk_simple_1']
topic.publish('topic=mk_simple_0&message=13454008077|13454008078|3|2015-02-26 11:36:32|2015-02-26 11:57:39|12|f1|1426810802530&key=17')
zookeeper.close()