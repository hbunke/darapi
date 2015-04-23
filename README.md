darapi
======

Small client library for uploading metadata, and DOI registration with the API
of [da|ra](http://www.da-ra.de/)

Very basic class for talking with da|ra API (well, actually the API is very
basic, as well ;-). Submits XML via POST, dara returns HTTP Status Codes and
--if you are lucky-- a more or less helpful message. 
See [da|ra API reference](http://www.da-ra.de/fileadmin/media/da-ra.de/PDFs/dara_API_reference_v1.pdf).

NOTE: this does not check for valid XML. Your calling code will be
responsible for that. You will also need to provide user and password.

    :param login: the username for the account at da|ra
    :param password: password for the account at da|ra
    :param xml: the XML string to post to da|ra, *without* the <?xml ... ?>
                instruction. XML must validate against the dara XSD-Schema
    :param test: if True connects to dara production server, otherwise it uses
                the test-server (default: False)
    :param register: register a DOI. Note that the test server cannot register
                    DOI. If you try it will return an additional message
                    (default: False)

call() will only return da|ra response http codes:
    
    201 Created operation successful, returned if a new dataset created

    200 OK operation successful, returned if an existing dataset updated

    400 Bad Request - request body must be valid xml

    401 Unauthorized - no or wrong login

    500 Internal Server Error - server internal error, try later and if
    problem persists please contact da|ra

    '500' usually means that there's an error in your request.
    
Error 500 unfortunately also returns a huge chunk of html output. However,
it can be used for debugging. See commented code at bottom for saving
output.



