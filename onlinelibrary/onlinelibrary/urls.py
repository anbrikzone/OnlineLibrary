from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import SimpleRouter
from rest_framework_simplejwt.views import TokenObtainPairView
from books.views import (BookView, 
                         BookDetailView, 
                         AuthorBookView,
                         UserViewSet, 
                         ReviewView, 
                         ReviewDetailView
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
]

urlpatterns += router.urls