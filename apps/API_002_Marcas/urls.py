from django.urls import path, include
from .api import MarcaAPIView, MarcaDetailAPIView
from rest_framework import routers

"""router = routers.DefaultRouter()
router.register('marca', MarcaViewset)

urlpatterns = [
    path('marca/', include(router.urls)),
]"""

urlpatterns = [
    path('crear/', MarcaAPIView.as_view(), name='marca-list-create'),
    path('marca/<int:pk>/', MarcaDetailAPIView.as_view(), name='marca-detail')
]