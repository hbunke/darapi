# Test for da|ra API
# hendrik bunke <h.bunke@zbw.eu>, 11.06.2014

import requests


class DaraClient(object):
    """
    doing all the dirty work
    """
    
    def __init__(self, login, password, xml, test=False):
        """
        """
        if test:
            self.URL = 'http://dara-test.gesis.org:8084/dara/study/importXML'
        else:
            self.URL = 'http://www.da-ra.de/dara/study/importXML'
        self.login = login
        self.password = password
        self.xml = xml

        ### for files as files
        files = {'file': open(xml, 'r')}
        req = requests.post(URL, auth=(dara_login, dara_pass), files=files)

        # for files as stream
        #with open(xml, 'r') as stream:
        #    req = requests.post(URL, auth=(dara_login, dara_pass), data=stream)

        # for python string as stream
        #req = requests.post(self.URL, auth=(self.login, self.password), data=xml)

        http_code = req.status_code
        
        print http_code
        
        #import pdb; pdb.set_trace()
        #debug html output
        #of = '/home/bunke/dop.html'
        #of = '/home/bunke/dop_files.html'
        #of = '/home/bunke/dop_stream.html'
        #output = open(of, 'w')
        #text = req.content
        #output.write(text)
        #output.close()
        #print "output written to %s" %of


    
def example_xml():
    """
    for testing just import this string
    """
    
    xml = u'<?xml version="1.0" encoding="UTF-8"?>\n<resource>\n  <resourceType>2</resourceType>\n  <resourceIdentifier>\n    <identifier>110665</identifier>\n    <currentVersion>1.0</currentVersion>\n  </resourceIdentifier>\n  <titles>\n    <title>\n      <language>de</language>\n      <titleName>Real household net disposable income 2012/1</titleName>\n    </title>\n    <title>\n      <language>en</language>\n      <titleName>Real household net disposable income 2012/1</titleName>\n    </title>\n  </titles>\n  <creators>\n    <creator>\n      <institution>\n        <institutionName>\n          <language>de</language>\n          <name>OECD Publishing</name>\n        </institutionName>\n      </institution>\n    </creator>\n    <creator>\n      <institution>\n        <institutionName>\n          <language>en</language>\n          <name>OECD Publishing</name>\n        </institutionName>\n      </institution>\n    </creator>\n  </creators>\n  <dataURLs>\n    <dataURL>http://dx.doi.org/10.1787/hsinc-table-2012-1-en</dataURL>\n  </dataURLs>\n  <publicationDate>\n    <date>2012-01-24</date>\n  </publicationDate>\n  <availability>\n    <availabilityControlled>1</availabilityControlled>\n    <availabilityFree>\n      <language>en</language>\n      <availabilityText>Available. Excel 2007 - Internal HTML - PDF</availabilityText>\n    </availabilityFree>\n    <availabilityFree>\n      <language>de</language>\n      <availabilityText>Verfuegbar. Excel 2007 - Internal HTML - PDF</availabilityText>\n    </availabilityFree>\n  </availability>\n  <resourceLanguage>eng</resourceLanguage>\n  <alternativeIDs>\n    <alternativeID>\n      <identifier>doi:10.1787/hsinc-table-2012-1-en</identifier>\n      <type>DOI</type>\n    </alternativeID>\n  </alternativeIDs>\n  <classifications>\n    <classification>\n      <classificationExternal>\n        <language>en</language>\n        <schema>OECD</schema>\n        <terms>\n          <term>Economics;</term>\n        </terms>\n      </classificationExternal>\n    </classification>\n    <classification>\n      <classificationExternal>\n        <language>de</language>\n        <schema>OECD</schema>\n        <terms>\n          <term>Oekonomie</term>\n        </terms>\n      </classificationExternal>\n    </classification>\n  </classifications>\n  <geographicCoverages>\n    <geographicCoverage>\n      <language>en</language>\n      <geographicCoverageControlled>AU</geographicCoverageControlled>\n    </geographicCoverage>\n    <geographicCoverage>\n      <language>en</language>\n      <geographicCoverageControlled>AT</geographicCoverageControlled>\n    </geographicCoverage>\n    <geographicCoverage>\n      <language>en</language>\n      <geographicCoverageControlled>BE</geographicCoverageControlled>\n    </geographicCoverage>\n    <geographicCoverage>\n      <language>en</language>\n      <geographicCoverageControlled>CA</geographicCoverageControlled>\n    </geographicCoverage>\n    <geographicCoverage>\n      <language>en</language>\n      <geographicCoverageControlled>CL</geographicCoverageControlled>\n    </geographicCoverage>\n    <geographicCoverage>\n      <language>en</language>\n      <geographicCoverageControlled>CZ</geographicCoverageControlled>\n    </geographicCoverage>\n    <geographicCoverage>\n      <language>en</language>\n      <geographicCoverageControlled>DK</geographicCoverageControlled>\n    </geographicCoverage>\n    <geographicCoverage>\n      <language>en</language>\n      <geographicCoverageControlled>EE</geographicCoverageControlled>\n    </geographicCoverage>\n    <geographicCoverage>\n      <language>en</language>\n      <geographicCoverageControlled>FI</geographicCoverageControlled>\n    </geographicCoverage>\n    <geographicCoverage>\n      <language>en</language>\n      <geographicCoverageControlled>FR</geographicCoverageControlled>\n    </geographicCoverage>\n    <geographicCoverage>\n      <language>en</language>\n      <geographicCoverageControlled>GE</geographicCoverageControlled>\n    </geographicCoverage>\n    <geographicCoverage>\n      <language>en</language>\n      <geographicCoverageControlled>GR</geographicCoverageControlled>\n    </geographicCoverage>\n    <geographicCoverage>\n      <language>en</language>\n      <geographicCoverageControlled>HU</geographicCoverageControlled>\n    </geographicCoverage>\n    <geographicCoverage>\n      <language>en</language>\n      <geographicCoverageControlled>IS</geographicCoverageControlled>\n    </geographicCoverage>\n    <geographicCoverage>\n      <language>en</language>\n      <geographicCoverageControlled>IE</geographicCoverageControlled>\n    </geographicCoverage>\n    <geographicCoverage>\n      <language>en</language>\n      <geographicCoverageControlled>IL</geographicCoverageControlled>\n    </geographicCoverage>\n    <geographicCoverage>\n      <language>en</language>\n      <geographicCoverageControlled>IT</geographicCoverageControlled>\n    </geographicCoverage>\n    <geographicCoverage>\n      <language>en</language>\n      <geographicCoverageControlled>JP</geographicCoverageControlled>\n    </geographicCoverage>\n    <geographicCoverage>\n      <language>en</language>\n      <geographicCoverageControlled>KR</geographicCoverageControlled>\n    </geographicCoverage>\n    <geographicCoverage>\n      <language>en</language>\n      <geographicCoverageControlled>LU</geographicCoverageControlled>\n    </geographicCoverage>\n    <geographicCoverage>\n      <language>en</language>\n      <geographicCoverageControlled>MX</geographicCoverageControlled>\n    </geographicCoverage>\n    <geographicCoverage>\n      <language>en</language>\n      <geographicCoverageControlled>NL</geographicCoverageControlled>\n    </geographicCoverage>\n    <geographicCoverage>\n      <language>en</language>\n      <geographicCoverageControlled>NZ</geographicCoverageControlled>\n    </geographicCoverage>\n    <geographicCoverage>\n      <language>en</language>\n      <geographicCoverageControlled>NO</geographicCoverageControlled>\n    </geographicCoverage>\n    <geographicCoverage>\n      <language>en</language>\n      <geographicCoverageControlled>PL</geographicCoverageControlled>\n    </geographicCoverage>\n    <geographicCoverage>\n      <language>en</language>\n      <geographicCoverageControlled>PT</geographicCoverageControlled>\n    </geographicCoverage>\n    <geographicCoverage>\n      <language>en</language>\n      <geographicCoverageControlled>SK</geographicCoverageControlled>\n    </geographicCoverage>\n    <geographicCoverage>\n      <language>en</language>\n      <geographicCoverageControlled>SI</geographicCoverageControlled>\n    </geographicCoverage>\n    <geographicCoverage>\n      <language>en</language>\n      <geographicCoverageControlled>ES</geographicCoverageControlled>\n    </geographicCoverage>\n    <geographicCoverage>\n      <language>en</language>\n      <geographicCoverageControlled>SE</geographicCoverageControlled>\n    </geographicCoverage>\n    <geographicCoverage>\n      <language>de</language>\n      <geographicCoverageControlled>DE</geographicCoverageControlled>\n      <freetext>berlin</freetext>\n      <geoLocationPoint>52.000000 69.000000</geoLocationPoint>\n    </geographicCoverage>\n  </geographicCoverages>\n  <temporalCoverages>\n    <temporalCoverage>\n      <language>en</language>\n      <temporalCoverageFormal>\n        <startDate>\n          <year>2012</year>\n        </startDate>\n      </temporalCoverageFormal>\n    </temporalCoverage>\n    <temporalCoverage>\n      <language>de</language>\n      <temporalCoverageFormal>\n        <startDate>\n          <year>2012</year>\n        </startDate>\n      </temporalCoverageFormal>\n    </temporalCoverage>\n  </temporalCoverages>\n  <relations>\n    <relation>\n      <identifier>10.1787/hsinc-table-2012-1-fr</identifier>\n      <identifierType>DOI</identifierType>\n      <relationType>17</relationType>\n    </relation>\n  </relations>\n</resource>\n'
    
    return xml
        




