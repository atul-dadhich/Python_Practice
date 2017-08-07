import requests
from xml.etree import ElementTree


url = "http://www.webservicex.com/currencyconvertor.asmx?WSDL"
# headers = {'content-type': 'application/soap+xml'}
headers = {'content-type': 'text/xml'}
body = """ <soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:web="http://www.webserviceX.NET/">
           <soapenv:Header/>
            <soapenv:Body>
                <web:ConversionRate>
                <web:FromCurrency>USD</web:FromCurrency>
                <web:ToCurrency>INR</web:ToCurrency>
                </web:ConversionRate>
            </soapenv:Body>
           </soapenv:Envelope> """


response = requests.post(url, data=body, headers=headers)
xmlresponse = ElementTree.fromstring(response.content)

for element in xmlresponse.iter('*'):
    print (element.tag, element.attrib)


assert response.status_code == 200, "Test Case Failed"

print '\n'
print 'Response Code \n', response.status_code
print '\n'
print 'Test Case Passed \n', response.content
