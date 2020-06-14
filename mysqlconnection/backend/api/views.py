from rest_framework import generics
from backend.models import (Film, Seans, Sala, Bilet,
                            ZajeteMiejsca, Klient, Zamowienie,
                            Cennik)
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from backend.api.serializers import (FilmSerializer, BiletSerializer,
                                     SalaSerializer, SeansSerializer,
                                     ZajeteMiejscaSerializer,
                                     KlientSerializer, ZamowienieSerializer,
                                     CennikSerializer)


class FilmListCreateAPIView(generics.ListCreateAPIView):
    queryset = Film.objects.all()
    serializer_class = FilmSerializer


class FilmDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Film.objects.all()
    serializer_class = FilmSerializer


class SeansListCreateAPIView(generics.ListCreateAPIView):
    queryset = Seans.objects.all()
    serializer_class = SeansSerializer


class SalaDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Sala.objects.all()
    serializer_class = SalaSerializer


class BiletListCreateAPIView(generics.ListCreateAPIView):
    queryset = Bilet.objects.all()
    serializer_class = BiletSerializer


class ZajeteMiejscaListCreateAPIView(generics.ListCreateAPIView):
    queryset = ZajeteMiejsca.objects.all()
    serializer_class = ZajeteMiejscaSerializer


class KlientListCreateAPIView(generics.ListCreateAPIView):
    queryset = Klient.objects.all()
    serializer_class = KlientSerializer


class ZamowienieListCreateAPIView(generics.ListCreateAPIView):
    queryset = Zamowienie.objects.all()
    serializer_class = ZamowienieSerializer


class CennikListCreateAPIView(generics.ListCreateAPIView):
    queryset = Cennik.objects.all()
    serializer_class = CennikSerializer

