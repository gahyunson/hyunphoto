from django.http import HttpRequest
from django.http.response import HttpResponseBase
from django.middleware.common import CommonMiddleware
from django.middleware.http import ConditionalGetMiddleware

class CustomMiddleware(CommonMiddleware):
    def process_response(self, request, response):
        response = super().process_response(request, response)

        content_length = response.headers['Content-Length']
        print('response content_length is ',content_length)
        return response

    # def process_response(self, request: HttpRequest, response: HttpResponseBase) -> HttpResponseBase:
    #     print(response.headers["Content-Length"])
    #     return super().process_response(request, response)