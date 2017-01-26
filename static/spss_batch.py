# coding utf-8
import pprint
import requests

def main():

    response = requests.get(
        'https://ibm-watson-ml.mybluemix.net/pm/v1/score/test1?accesskey=3pmpR/Rmw/E93jH25U9/dP6yciTZ+Gth0O3gDIJnpUvMOoVIgpPvg2+v3QyZPPnfHxGxQ3pIogjgEOjN0TGDTcL0h32gVzPkwMbmHXNpi+Hox+Mvwa+7GQ8vHAZW3CihtzIPylVCeA53o1U3j5CUNs2WmPAxFgfEYJlcc/bkHVg=',
        headers={'Content-Type': 'application/json'}
        )
    pprint.pprint(response.json())

if __name__== '__main__':
    main()