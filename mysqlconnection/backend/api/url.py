from django.urls import path
from backend.api.views import (FilmListCreateAPIView, FilmDetailAPIView,
                               SeansListCreateAPIView, BiletListCreateAPIView, SalaDetailAPIView,
                               ZajeteMiejscaListCreateAPIView, KlientListCreateAPIView,
                               ZamowienieListCreateAPIView, CennikListCreateAPIView)


urlpatterns = [
    path("films/",
         FilmListCreateAPIView.as_view(),
         name="film-list"),

    path("films/<int:pk>/",
         FilmDetailAPIView.as_view(),
         name="film-detail"),

    path("seans/",
         SeansListCreateAPIView.as_view(),
         name="seans-list"),


    path("ticket/",
         BiletListCreateAPIView.as_view(),
         name="tickets"),

    path("sall/<int:pk>/",
         SalaDetailAPIView.as_view(),
         name="sall-detail"),

    path("reserved/",
         ZajeteMiejscaListCreateAPIView.as_view(),
         name="reserved"),

    path("client/",
         KlientListCreateAPIView.as_view(),
         name="client-lis"),

    path("orders/",
         ZamowienieListCreateAPIView.as_view(),
         name="order-list"),

    path("prizes/",
         CennikListCreateAPIView.as_view(),
         name="order-list"),

]
