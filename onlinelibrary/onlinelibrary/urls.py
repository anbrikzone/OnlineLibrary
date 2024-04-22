from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import SimpleRouter
from rest_framework_simplejwt.views import TokenObtainPairView
from books.views import (BookView, 
                         BookDetailView, 
                         AuthorBookView,
                         UserViewSet, 
                         ReviewView, 
                         ReviewDetailView)

router = SimpleRouter()
router.register('authors', AuthorBookView)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('rest_framework.urls')),
    path('books/', BookView.as_view(), name='Books'),
    path('books/<pk>/', BookDetailView.as_view(), name='books'),
    path('books/<int:pk>/review/', ReviewView.as_view()),
    path('books/<int:pk>/review/<int:id>/', ReviewDetailView.as_view()),
    path('register/', UserViewSet.as_view()),
    path('login/', TokenObtainPairView.as_view(), name='login'),
]

urlpatterns += router.urls