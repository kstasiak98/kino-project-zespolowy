from rest_framework import serializers
from backend.models import (Film, Bilet, Seans, Sala, ZajeteMiejsca,
                            Klient, Zamowienie, Cennik)


class FilmSerializer(serializers.ModelSerializer):

    class Meta:
        model = Film
        fields = "__all__"


class BiletSerializer(serializers.ModelSerializer):

    class Meta:
        model = Bilet
        fields = "__all__"


class SeansSerializer(serializers.ModelSerializer):

    class Meta:
        model = Seans
        fields = "__all__"


class SalaSerializer(serializers.ModelSerializer):

    class Meta:
        model = Sala
        fields = "__all__"


class ZajeteMiejscaSerializer(serializers.ModelSerializer):

    class Meta:
        model = ZajeteMiejsca
        fields = "__all__"


class KlientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Klient
        fields = "__all__"


class ZamowienieSerializer(serializers.ModelSerializer):

    class Meta:
        model = Zamowienie
        fields = "__all__"


class CennikSerializer(serializers.ModelSerializer):

    class Meta:
        model = Cennik
        fields = "__all__"
