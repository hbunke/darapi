# Test for da|ra API
# hendrik bunke <h.bunke@zbw.eu>, 11.06.2014

#import poster
#import urllib2
#import requests
import darapi.client

def upload():

    dara_login = 'demo'
    dara_pass = 'testdemo'
    xml = '/home/bunke/dev/darapi/darapi/clean.xml'

    dara = darapi.client.DaraClient(dara_login, dara_pass, test=True, xml=xml,
            registration=True)

    

if __name__ == '__main__':
    print "starting upload..."
    r = upload()
    print r


