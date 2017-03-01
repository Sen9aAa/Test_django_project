from .models import RequestHistory

class RequestHistoryMiddleware():
    def process_request(self,request):
        instanse = RequestHistory.objects.create(request_method = request.method,request_link = request.META.get('HTTP_REFERER',None))
        instanse_filter = RequestHistory.objects.order_by('-request_time')
        for c in range(len(instanse_filter)):
        	if c>=10:
        		instanse_filter[c].delete()
        return None