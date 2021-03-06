from requests.adapters import HTTPAdapter
from requests.packages.urllib3.poolmanager import PoolManager


class SSLAdapter(HTTPAdapter):
    """A HTTPS Transport Adapter that uses an arbitrary SSL version."""
    def __init__(self, ssl_version=None, **kwargs):
        self.ssl_version = ssl_version

        super(SSLAdapter, self).__init__(**kwargs)

    def init_poolmanager(self, connections, maxsize, block):
        self.poolmanager = PoolManager(num_pools=connections,
                                       maxsize=maxsize,
                                       ssl_version=self.ssl_version,
                                       block=block)
