from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.viewsets import ModelViewSet

from habits.permissions import IsSuperUser
from users.models import User
from users.permissions import IsOwner
from users.serializers.user import UserSerializer


class UserViewSet(ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()

    def get_permissions(self):
        if self.action == 'create':
            permission_classes = [AllowAny]
        elif self.action == 'list':
            permission_classes = [IsAuthenticated]
        elif self.action == 'update' or self.action == 'partial_update':
            permission_classes = [IsSuperUser | IsOwner]
        elif self.action == 'destroy':
            permission_classes = [IsSuperUser | IsOwner]
        elif self.action == 'retrieve':
            permission_classes = [IsSuperUser | IsOwner]
        else:
            permission_classes = [IsAuthenticated]
        return [permission() for permission in permission_classes]
