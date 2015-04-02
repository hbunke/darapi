# -*- coding: utf-8 -*-
# hendrik bunke <h.bunke@zbw.eu>, 11.06.2014

import requests


#TODO:
#    -   Error handling
#    -   DOI check (does not work with dara test instance)
#    -  needs additional method to return http codes (or at least success
#       message)

class DaraClient(object):
    """
    class for talking with da|ra API. Submits XML via POST, dara returns HTTP
    Status Codes and --if you are lucky-- a more or less helpful message. See
    da|ra API reference: 
    http://www.da-ra.de/fileadmin/media/da-ra.de/PDFs/dara_API_reference_v1.pdf

    :param login: the username for the account at da|ra
    :param password: password for the account at da|ra
    :param xml: the XML string to post to da|ra, *without* the <?xml ... ?>
                instruction. XML must validate against the dara XSD-Schema
    :param test: if True connects to dara production server, otherwise it uses
                the test-server (default: False)
    :param register: register a DOI. Note that the test server cannot register
                    DOI. If you try it will return an additional message
                    (default: False)

    dara response http codes:
    
        201 Created operation successful, returned if a new dataset created
    
        200 OK operation successful, returned if an existing dataset updated
    

        400 Bad Request - request body must be valid xml
    
        401 Unauthorized - no or wrong login
    
        500 Internal Server Error - server internal error, try later and if
        problem persists please contact da|ra

    500 usually means that there's an error in your request.
    
    Error 500 unfortunately also returns a huge chunk of html output. However,
    it can be used for debugging. See commented code at bottom for saving
    output

    """
    
    
    def __init__(self, login, password, xml, test=False, 
            register=False):
        """
        """
        if test:
            self.URL = 'http://dara-test.gesis.org:8084/dara/study/importXML'
        else:
            self.URL = 'http://www.da-ra.de/dara/study/importXML'
        
        self.login = login
        self.password = password
        self.doi = register

        #socket does not take unicode, so we need to encode our unicode object
        #see http://stackoverflow.com/questions/9752521/sending-utf-8-with-sockets
        #XXX do we always get unicode object??? 
        self.xml = xml.encode('utf-8')
        
                
    def call(self):
        
        # we could also simply give 'true' or 'false' as parameter (as dara
        #expects), but that's confusing
        params = {}
        if self.doi:
            params = {'registration': 'true'}
        
        headers = {'content-type': 'application/xml;charset=UTF-8'}
        
        req = requests.post(self.URL, auth=(self.login, self.password),
                headers=headers, data=self.xml, params=params)

        return req.status_code



       #XXX debug html output
       #of = '/home/bunke/dop.html'
       ##of = '/home/bunke/dop_files.html'
       ##of = '/home/bunke/dop_stream.html'
       #output = open(of, 'w')
       #output.write(body)
       #output.close()
       #print "output written to %s" %of

    
