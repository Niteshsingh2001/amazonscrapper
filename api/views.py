from django.views.generic.detail import DetailView
from django.shortcuts import render

from selectorlib import Extractor
import requests
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import JsonResponse

import json
e = Extractor.from_yaml_file('selectors.yml')


def scrape(url):
    headers = {
        'dnt': '1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-user': '?1',
        'sec-fetch-dest': 'document',
        'referer': 'https://www.amazon.com/',
        'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
    }

    # Download the page using requests
    print("Downloading %s" % url)
    r = requests.get(url, headers=headers)
    # Simple check to check if page was blocked (Usually 503)
    if r.status_code > 500:
        if "To discuss automated access to Amazon data please contact" in r.text:
            print(
                "Page %s was blocked by Amazon. Please try using better proxies\n" % url)
        else:
            print("Page %s must have been blocked by Amazon as the status code was %d" % (
                url, r.status_code))
        return None
    # Pass the HTML of the page and create
    return e.extract(r.text)


@api_view(['GET', 'POST'])
@csrf_exempt
def amazon_data(request):
    if request.method == "POST":
        data = scrape(request.data["link"])
        return Response(data)
        # return JsonResponse(json.dumps(

        #     {
        #         "id": 1,
        #         "author": "John Doe",
        #         "title": "Happy Birthday",
        #         "description": "20 years of ISS",
        #         "body": "Fancy content",
        #         "location": "Earth",
        #         "publication_date": "2020-06-11",
        #         "active": False
        #     }
        # ),safe=False)

    return JsonResponse({"Error": "dfsd"})


# class amazon_data(DetailView):
#     def post(self, request, *args, **kwargs):
#         A=request.data.get('A', None)
#         B=request.data.get('B', None)
#         return self.create(request, *args, **kwargs)
