import os

from settings import Settings
from prompt_vhost import prompt_vhost
from template import Template

import colorama
from termcolor import colored
from pyfiglet import figlet_format

def create_vhost(conf):
    """
    Create a virtual host for nginx and php-fpm
    """

    data = prompt_vhost(conf.getCertPath(), conf.getCertKey(), conf.getRootDir())
    
    http = Template('templates/vhost-http.conf')
    http.addVar('HOST', data['vhost'])
    http.addVar('ROOT_DIR', data['rootDir'])
    http.addVar('INDEX', conf.getIndex())
    http.addVar('FASTCGI_PASS', conf.getFastCGI())

    result = http.build()

    if data['needSSL']:
        ssl = Template('templates/vhost-ssl.conf')
        ssl.addVar('HOST', data['vhost'])
        ssl.addVar('SSL_CERT', data['sslCert'])
        ssl.addVar('SSL_KEY', data['sslKey'])
        ssl.addVar('ROOT_DIR', data['rootDir'])
        ssl.addVar('INDEX', conf.getIndex())
        ssl.addVar('FASTCGI_PASS', conf.getFastCGI())

        result += '\n\n' + ssl.build()

    vhost_file_name = conf.getVHosts() + data['vhost'] + '.conf'
    with open(vhost_file_name, 'w') as f:
        f.write(result)

    print('\n')
    print(colored('✔ SUCCESS: vhost config file created!', 'green'))


def main():
    colorama.init()
    conf = Settings()

    print(colored(figlet_format('mkhost'), 'blue'))

    if not os.access(conf.getVHosts(), os.W_OK):
        print(
            colored('ERROR: Directory of nginx vhosts is not writable (' + 
                conf.getVHosts() + ')', 'red')
        )
        return

    create_vhost(conf)

    print('\n')

if __name__ == "__main__":
    main()