from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import SimpleRouter
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from books.views import (BookView, 
                         BookDetailView, 
                         AuthorBookView,
                         UserViewSet, 
                         ReviewView, 
                         ReviewDetailView
                        )

schema_view = get_schema_view(
    openapi.Info(
        title="My API",
        default_version='v1',
        description='My API Description',
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

router = SimpleRouter()
router.register('authors', AuthorBookView)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('rest_framework.urls')),
    path('books/', BookView.as_view({'get': 'list', 'post': 'create'}), name='Books'),
    path('books/<int:pk>/', BookDetailView.as_view({'get': 'list', 'put': 'update', 'delete': 'destroy'}), name='books'),
    path('books/<int:pk>/review/', ReviewView.as_view({'get': 'list', 'post': 'create'})),
    path('books/<int:pk>/review/<int:id>/', ReviewDetailView.as_view({'get': 'list', 'put': 'update', 'delete': 'destroy'})),
    path('register/', UserViewSet.as_view()),
    path('login/', TokenObtainPairView.as_view(), name='login'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]

urlpatterns += router.urls