from django.contrib import admin
from django.urls import path, include
from loja.models import Item, Carrinho_Item
from rest_framework.routers import DefaultRouter
from loja.views import ItemViewSet, Carrinho_itemViewSet
from django.conf import settings
from django.conf.urls.static import static

from uploader.router import router as uploader_router

router = DefaultRouter()
router.register(r"itens", ItemViewSet)
router.register(r"carrinho_itens", Carrinho_itemViewSet)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include(router.urls)),
    path("api/media/", include(uploader_router.urls)),
]

urlpatterns += static(settings.MEDIA_ENDPOINT, document_root=settings.MEDIA_ROOT)
