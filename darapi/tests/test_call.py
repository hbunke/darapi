import unittest
from darapi import DaraClient

# trivial test case

class DarapiTest(unittest.TestCase):
    """
    we only do checks for calling the server, not for valid XML or whatever
    kind of http code return. That's mainly because da|ra does not have 
    an official test server or something, so we would need to give account
    information here.
    """

    def test_call(self):
        """
        """
        #we are faking xml and user/password here
        xml_string = u"<xml><invalid>";
        client = DaraClient('user', 'pass', xml_string, test=True,
                register=False)
        dara = client.call()
        self.assertEqual(dara, 401)

if __name__ == '__main__':
    unittest.main()
        


