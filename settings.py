import os
import configparser

class Settings:
    """Settings wrapper"""

    def __init__(self):
        """Constructor"""

        cur_dir = os.path.dirname(os.path.realpath(__file__))
        self.config = configparser.ConfigParser()
        self.config.read(cur_dir + '/settings.ini')

    def getVHosts(self):
        vhosts_dir = str(self.config['nginx']['vhosts'])
        last_char = vhosts_dir[-1]

        return vhosts_dir if last_char == '/' else vhosts_dir + '/'

    def getRootDir(self):
        root_dir = str(self.config['html']['RootDir'])
        last_char = root_dir[-1]

        return root_dir if last_char == '/' else root_dir + '/'

    def getIndex(self):
        return str(self.config['html']['Index'])

    def getCertPath(self):
        return str(self.config['ssl']['Cert'])

    def getCertKey(self):
        return str(self.config['ssl']['CertKey'])

    def getFastCGI(self):
        return str(self.config['php']['FastCgiPass'])
