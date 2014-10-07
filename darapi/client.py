# -*- coding: utf-8 -*-
# Test for da|ra API
# hendrik bunke <h.bunke@zbw.eu>, 11.06.2014

import requests
import pprint

###works!

class DaraClient(object):
    """
    doing all the dirty work
    """
    
    def __init__(self, login, password, test=False, xml=None):
        """
        """
        
        #if test:
        #    self.URL = 'http://dara-test.gesis.org:8084/dara/study/importXML'
        #else:
        #    self.URL = 'http://www.da-ra.de/dara/study/importXML'
        self.URL = 'http://dara-test.gesis.org:8084/dara/study/importXML'
        
        self.login = login
        self.password = password
        #self.xml = xml
        self.xml = example_xml()
        
        ### for files as files
        #self.files = {'file': open(self.xml, 'r')}
        #self.files = {'file': (self.xml)}
        
        #import pdb; pdb.set_trace()

        req = self.__request()

        http_code = req[0]
        body = req[1]

        print http_code
        #pp = pprint.PrettyPrinter(indent=4)
        #pp.pprint(body)
        

        #debug html output
       #of = '/home/bunke/dop.html'
       ##of = '/home/bunke/dop_files.html'
       ##of = '/home/bunke/dop_stream.html'
       #output = open(of, 'w')
       #output.write(body)
       #output.close()
       #print "output written to %s" %of


    def __request(self):
        """
        calling dara API with request
        """
        headers = {'content-type': 'application/xml;charset=UTF-8'}
        req = requests.post(self.URL, auth=(self.login, self.password),
                headers=headers, data=self.xml)

        response_code = req.status_code
        response_content = req.content
        import pdb; pdb.set_trace()
        
        return (response_code, response_content)


    
def example_xml():
    """
    for testing just import this string. NOTE that dara does not like the
    <?xml processing instruction, so avoid it here 
    """
    xml = """
    <resource>
  <resourceType>2</resourceType>
  <resourceIdentifier>
    <identifier>110665</identifier>
    <currentVersion>1.0</currentVersion>
  </resourceIdentifier>
  <titles>
    <title>
      <language>de</language>
      <titleName>Real household net disposable income 2012/1</titleName>
    </title>
    <title>
      <language>en</language>
      <titleName>Real household net disposable income 2012/1</titleName>
    </title>
  </titles>
  <creators>
    <creator>
      <institution>
        <institutionName>
          <language>de</language>
          <name>OECD Publishing</name>
        </institutionName>
      </institution>
    </creator>
    <creator>
      <institution>
        <institutionName>
          <language>en</language>
          <name>OECD Publishing</name>
        </institutionName>
      </institution>
    </creator>
  </creators>
  <dataURLs>
    <dataURL>http://dx.doi.org/10.1787/hsinc-table-2012-1-en</dataURL>
  </dataURLs>
  <publicationDate>
    <date>2012-01-24</date>
  </publicationDate>
  <availability>
    <availabilityControlled>1</availabilityControlled>
    <availabilityFree>
      <language>en</language>
      <availabilityText>Available. Excel 2007 - Internal HTML - PDF</availabilityText>
    </availabilityFree>
    <availabilityFree>
      <language>de</language>
      <availabilityText>Verfügbar. Excel 2007 - Internal HTML - PDF</availabilityText>
    </availabilityFree>
  </availability>
  <resourceLanguage>eng</resourceLanguage>
  <alternativeIDs>
    <alternativeID>
      <identifier>doi:10.1787/hsinc-table-2012-1-en</identifier>
      <type>DOI</type>
    </alternativeID>
  </alternativeIDs>
  <classifications>
    <classification>
      <classificationExternal>
        <language>en</language>
        <schema>OECD</schema>
        <terms>
          <term>Economics;</term>
        </terms>
      </classificationExternal>
    </classification>
    <classification>
      <classificationExternal>
        <language>de</language>
        <schema>OECD</schema>
        <terms>
          <term>Ökonomie</term>
        </terms>
      </classificationExternal>
    </classification>
  </classifications>
  <geographicCoverages>
    <geographicCoverage>
      <language>en</language>
      <geographicCoverageControlled>AU</geographicCoverageControlled>
    </geographicCoverage>
    <geographicCoverage>
      <language>en</language>
      <geographicCoverageControlled>AT</geographicCoverageControlled>
    </geographicCoverage>
    <geographicCoverage>
      <language>en</language>
      <geographicCoverageControlled>BE</geographicCoverageControlled>
    </geographicCoverage>
    <geographicCoverage>
      <language>en</language>
      <geographicCoverageControlled>CA</geographicCoverageControlled>
    </geographicCoverage>
    <geographicCoverage>
      <language>en</language>
      <geographicCoverageControlled>CL</geographicCoverageControlled>
    </geographicCoverage>
    <geographicCoverage>
      <language>en</language>
      <geographicCoverageControlled>CZ</geographicCoverageControlled>
    </geographicCoverage>
    <geographicCoverage>
      <language>en</language>
      <geographicCoverageControlled>DK</geographicCoverageControlled>
    </geographicCoverage>
    <geographicCoverage>
      <language>en</language>
      <geographicCoverageControlled>EE</geographicCoverageControlled>
    </geographicCoverage>
    <geographicCoverage>
      <language>en</language>
      <geographicCoverageControlled>FI</geographicCoverageControlled>
    </geographicCoverage>
    <geographicCoverage>
      <language>en</language>
      <geographicCoverageControlled>FR</geographicCoverageControlled>
    </geographicCoverage>
    <geographicCoverage>
      <language>en</language>
      <geographicCoverageControlled>GE</geographicCoverageControlled>
    </geographicCoverage>
    <geographicCoverage>
      <language>en</language>
      <geographicCoverageControlled>GR</geographicCoverageControlled>
    </geographicCoverage>
    <geographicCoverage>
      <language>en</language>
      <geographicCoverageControlled>HU</geographicCoverageControlled>
    </geographicCoverage>
    <geographicCoverage>
      <language>en</language>
      <geographicCoverageControlled>IS</geographicCoverageControlled>
    </geographicCoverage>
    <geographicCoverage>
      <language>en</language>
      <geographicCoverageControlled>IE</geographicCoverageControlled>
    </geographicCoverage>
    <geographicCoverage>
      <language>en</language>
      <geographicCoverageControlled>IL</geographicCoverageControlled>
    </geographicCoverage>
    <geographicCoverage>
      <language>en</language>
      <geographicCoverageControlled>IT</geographicCoverageControlled>
    </geographicCoverage>
    <geographicCoverage>
      <language>en</language>
      <geographicCoverageControlled>JP</geographicCoverageControlled>
    </geographicCoverage>
    <geographicCoverage>
      <language>en</language>
      <geographicCoverageControlled>KR</geographicCoverageControlled>
    </geographicCoverage>
    <geographicCoverage>
      <language>en</language>
      <geographicCoverageControlled>LU</geographicCoverageControlled>
    </geographicCoverage>
    <geographicCoverage>
      <language>en</language>
      <geographicCoverageControlled>MX</geographicCoverageControlled>
    </geographicCoverage>
    <geographicCoverage>
      <language>en</language>
      <geographicCoverageControlled>NL</geographicCoverageControlled>
    </geographicCoverage>
    <geographicCoverage>
      <language>en</language>
      <geographicCoverageControlled>NZ</geographicCoverageControlled>
    </geographicCoverage>
    <geographicCoverage>
      <language>en</language>
      <geographicCoverageControlled>NO</geographicCoverageControlled>
    </geographicCoverage>
    <geographicCoverage>
      <language>en</language>
      <geographicCoverageControlled>PL</geographicCoverageControlled>
    </geographicCoverage>
    <geographicCoverage>
      <language>en</language>
      <geographicCoverageControlled>PT</geographicCoverageControlled>
    </geographicCoverage>
    <geographicCoverage>
      <language>en</language>
      <geographicCoverageControlled>SK</geographicCoverageControlled>
    </geographicCoverage>
    <geographicCoverage>
      <language>en</language>
      <geographicCoverageControlled>SI</geographicCoverageControlled>
    </geographicCoverage>
    <geographicCoverage>
      <language>en</language>
      <geographicCoverageControlled>ES</geographicCoverageControlled>
    </geographicCoverage>
    <geographicCoverage>
      <language>en</language>
      <geographicCoverageControlled>SE</geographicCoverageControlled>
    </geographicCoverage>
    <geographicCoverage>
      <language>de</language>
      <geographicCoverageControlled>DE</geographicCoverageControlled>
      <freetext>berlin</freetext>
      <geoLocationPoint>52.000000 69.000000</geoLocationPoint>
    </geographicCoverage>
  </geographicCoverages>
  <temporalCoverages>
    <temporalCoverage>
      <language>en</language>
      <temporalCoverageFormal>
        <startDate>
          <year>2012</year>
        </startDate>
      </temporalCoverageFormal>
    </temporalCoverage>
    <temporalCoverage>
      <language>de</language>
      <temporalCoverageFormal>
        <startDate>
          <year>2012</year>
        </startDate>
      </temporalCoverageFormal>
    </temporalCoverage>
  </temporalCoverages>
  <relations>
    <relation>
      <identifier>10.1787/hsinc-table-2012-1-fr</identifier>
      <identifierType>DOI</identifierType>
      <relationType>17</relationType>
    </relation>
  </relations>
</resource>
"""
    
    return xml
        




