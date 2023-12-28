import http.client, urllib.request, urllib.parse, urllib.error, base64

headers = {
    # Request headers
    'Content-Type': 'application/json',
    'Ocp-Apim-Subscription-Key': '9be58914fc8a4cef8e49bd3d99ca2396',
}

params = urllib.parse.urlencode({
    # Request parameters
    'features': 'Read',
    'model-version': 'latest',
    'language': 'en',
    'smartcrops-aspect-ratios': '{array}',
    'gender-neutral-caption': 'False',
})

try:
    conn = http.client.HTTPSConnection('https://cs1-36408297.cognitiveservices.azure.com/')
    conn.request("POST", "/computervision/imageanalysis:analyze?api-version=2023-10-01&%s" % params, "{body}", headers)
    response = conn.getresponse()
    data = response.read()
    print(data)
    conn.close()
except Exception as e:
    print("[Errno {0}] {1}".format(e.errno, e.strerror))