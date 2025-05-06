from django.shortcuts import render,get_object_or_404
from rest_framework.generics import ListAPIView,RetrieveAPIView,GenericAPIView,CreateAPIView
from .models import User,GlucoseTableLvels
from .serializers import UserSerializer,GlucoseLevelsSerializer
from .filters import GlucoseLevelsFilter
from django_filters.rest_framework import DjangoFilterBackend
# Create your views here.
class UsersCreateView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UsersListView(ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetailsView(RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class GlucoseLevelsCreateView(CreateAPIView):
    queryset = GlucoseTableLvels.objects.all()
    serializer_class = GlucoseLevelsSerializer

class GlucoseLevelsListView(ListAPIView):
    serializer_class = GlucoseLevelsSerializer
    filter_backends =[DjangoFilterBackend]
    filterset_class =GlucoseLevelsFilter
    def get_queryset(self):
        user_id = self.kwargs.get("user_id")
        user = User.objects.get(user_id=user_id)
        return GlucoseTableLvels.objects.filter(user=user)

class GlucoseLevelsDetailsView(RetrieveAPIView):
    serializer_class = GlucoseLevelsSerializer
    def get_object(self):
        user_id = self.kwargs.get("user_id")
        pk = self.kwargs.get("pk")
        user = User.objects.get(user_id=user_id)

        return get_object_or_404(GlucoseTableLvels,user=user,pk=pk)


