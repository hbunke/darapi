#!/bin/sh

curl -i -H 'Content-Type: application/xml;charset=UTF-8' \
    -d @clean.xml \
    --user demo:testdemo \
    --verbose \
    http://dara-test.gesis.org:8084/dara/study/importXML


    

