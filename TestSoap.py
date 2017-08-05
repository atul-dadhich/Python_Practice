import requests
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
assert response.status_code == 200, "Test Case Failed"
print 'Test Case Passed', response.content

