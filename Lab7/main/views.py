from spyne import Application, rpc, ServiceBase, Iterable, Integer, Unicode
from spyne.protocol.soap import Soap11
from spyne.server.django import DjangoApplication
from django.http import HttpResponse
from .models import Object
from django.views.decorators.csrf import csrf_exempt

class SoapService(ServiceBase):
    @rpc(Integer, _returns=Iterable(Unicode))
    def get_object_info(ctx, object_id):
        try:
            obj = Object.objects.get(id=object_id)
            yield f"Name: {obj.name}"
            yield f"Description: {obj.description}"
            yield f"Category: {obj.category}"
            # Add more fields as needed
        except Object.DoesNotExist:
            yield "Object not found"

application = Application([SoapService],
                          tns='http://example.com/objects',
                          in_protocol=Soap11(validator='lxml'),
                          out_protocol=Soap11())

django_soap_app = csrf_exempt(DjangoApplication(application))

