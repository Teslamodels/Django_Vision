from django.urls import path
from .views import (Articlehome,
                    Detail,
                    Update, 
                    Delete,
                    Create,
                    )

urlpatterns = [
    path('<int:pk>/update/', Update.as_view(), name='update'),
    path('<int:pk>/', Detail.as_view(), name='detail'),
    path('<int:pk>/delete/', Delete.as_view(), name='delete'),
    path('new/', Create.as_view(), name='create'),
    path('', Articlehome.as_view(), name='article'),
]