from rest_framework.generics import ListAPIView, RetrieveAPIView
from .models import Vehicle
from .serializers import VehicleSerializer, VehicleDetailSerializer

# Create your views here.
class VehicleListAPIView(ListAPIView):
    queryset = Vehicle.objects.all()
    serializer_class = VehicleSerializer

    def get_queryset(self):
        fullSet = super().get_queryset()
        if ('filter' in self.request.GET):
            filteredSet = fullSet.all()
            filters = self.request.query_params.get('filter').split(',')
            for idx in range(len(filters)):
                if not len(filters[idx]): continue # skip empty filter
                if not idx:
                    filteredSet = fullSet.filter(categories__name__iexact=filters[idx])
                else:
                    filteredSet = filteredSet.union(fullSet.filter(categories__name__iexact=filters[idx]))
            fullSet = filteredSet
        if ('order' in self.request.GET):
            if self.request.GET['order'] == 'year':
                fullSet = fullSet.order_by('model_year')
            if self.request.GET['order'] == 'price':
                fullSet = fullSet.order_by('price')
        if ('reverse' in self.request.GET):
            fullSet = fullSet.reverse()
        return fullSet

class VehicleDetailAPIView(RetrieveAPIView):
    queryset = Vehicle.objects.all()
    serializer_class = VehicleDetailSerializer
