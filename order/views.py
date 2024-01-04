from rest_framework import viewsets
from .models import Printer, Check
from .serializers import PrinterSerializer, CheckSerializer
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.views import View
import os

class PrinterViewSet(viewsets.ModelViewSet):
    queryset = Printer.objects.all()
    serializer_class = PrinterSerializer


class CheckViewSet(viewsets.ModelViewSet):
    queryset = Check.objects.all()
    serializer_class = CheckSerializer



@method_decorator(csrf_exempt, name='dispatch')
class PollingView(View):
    def get(self, request):
        printer_id = request.GET.get('printer_id')
        checks = Check.objects.filter(printer_id=printer_id, status='rendered')
        response_data = []

        for check in checks:
            response_data.append({
                'id': check.id,
                'pdf_file': check.pdf_file.url
            })
        
        return JsonResponse(response_data, safe=False)

    def post(self, request):
        check_id = request.POST.get('check_id')
        check = Check.objects.get(id=check_id)
        check.status = 'printed'
        check.save()
        os.remove(check.pdf_file.path)
        return JsonResponse({'status': 'success'})
