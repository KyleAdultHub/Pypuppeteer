# encoding: utf-8


class Request(object):

    def __init__(self, request):
        self.request = request

    def get_failure_text(self):
        return self.request.failure()

    def get_headers(self):
        return self.request.headers

    def get_method(self):
        return self.request.method()

    def get_post_data(self):
        return self.request.postData()

    def get_redirect_chain(self):
        """
        A redirectChain is a chain of requests initiated to fetch a resource.
        If the website https://google.com has no redirects, then the chain will be empty
        :return:
        """
        return self.request.redirectChain()

    def get_response(self):
        """
         A matching Response object, or null if the response has not been received yet.
        :return:
        """
        return self.request.response()

    def get_request_url(self):
        return self.request.url()
