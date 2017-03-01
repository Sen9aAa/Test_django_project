from .models import RequestHistory

class RequestHistoryMiddleware():
    def process_request(self,request):
        instance = RequestHistory.objects.create(request_method = request.method,request_link = request.META.get('HTTP_REFERER',''))
        instance_filter = RequestHistory.objects.order_by('-request_time')
        for c in range(len(instance_filter)):
        	if c>=10:
        		instance_filter[c].delete()
        return None