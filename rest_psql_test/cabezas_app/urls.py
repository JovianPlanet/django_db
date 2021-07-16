from django.urls import include, path
from .views import PixCreate, PixList


urlpatterns = [
    path('create/', PixCreate.as_view(), name='create-cabeza'),
    path('', PixList.as_view()),
    #path('<int:pk>/', CustomerDetail.as_view(), name='retrieve-customer'),
    #path('update/<int:pk>/', CustomerUpdate.as_view(), name='update-customer'),
    # path('delete/<int:pk>/', CustomerDelete.as_view(), name='delete-customer')
]
