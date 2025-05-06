from .views import UserDetailsView,UsersListView,GlucoseLevelsDetailsView,GlucoseLevelsListView,UsersCreateView,GlucoseLevelsCreateView


from django.urls import path,include

urlpatterns = [
   path("users/",UsersListView.as_view()),
   path("register-user/",UsersCreateView.as_view()),
   path("users/<uuid:pk>",UserDetailsView.as_view()),
   path("levels/add-glucose-logs/",GlucoseLevelsCreateView.as_view()),
   path("levels/<slug:user_id>/",GlucoseLevelsListView.as_view()),
   path("levels/<str:user_id>/<int:pk>/",GlucoseLevelsDetailsView.as_view())
]