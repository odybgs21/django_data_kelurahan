from django.urls import path
# from .views import WargaListAPIView, WargaDetailAPIView
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import WargaViewSet, PengaduanViewSet

router = DefaultRouter()
router.register(r'warga', WargaViewSet, basename='warga')
router.register(r'pengaduan', PengaduanViewSet, basename='pengaduan')


urlpatterns = [
    # path('warga/', WargaListAPIView.as_view(), name='api-warga-list'),
    # path('warga/<int:warga_id>/', WargaDetailAPIView.as_view(), name='api-warga-detail'),
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]