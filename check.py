# -*- coding: utf-8 -*-

# Test for da|ra API
# hendrik bunke <h.bunke@zbw.eu>, 11.06.2014

from darapi import DaraClient
from darapi.tests import XML


def upload():

    dara_login = 'demo'
    dara_pass = 'testdemo'

    dara = DaraClient(dara_login, dara_pass, xml=XML, test=True,
            register=False)

if __name__ == '__main__':
    print "starting upload..."
    upload()

