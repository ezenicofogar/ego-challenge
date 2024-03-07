from rest_framework.generics import ListAPIView, RetrieveAPIView
from .models import Vehicle
from .serializers import VehicleSerializer, VehicleDetailSerializer

# Create your views here.
class VehicleListAPIView(ListAPIView):
    queryset = Vehicle.objects.all()
    serializer_class = VehicleSerializer

    def get_queryset(self):
        query = super().get_queryset()
        try:
            filters: str = self.request.query_params.get('filter').split(',')
            for key in filters:
                query = query.filter(categories__name__iexact=key)
        except:
            pass
        
        return query

class VehicleDetailAPIView(RetrieveAPIView):
    queryset = Vehicle.objects.all()
    serializer_class = VehicleDetailSerializer