from .models import RequestHistory

class RequestHistoryMiddleware():
    def process_request(self,request):
        instanse = RequestHistory.objects.create(request_method = request.method,request_link = request.META.get('HTTP_REFERER',None))
        return None