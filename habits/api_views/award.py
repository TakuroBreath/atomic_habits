from rest_framework.exceptions import PermissionDenied
from rest_framework.generics import ListAPIView, CreateAPIView, UpdateAPIView, DestroyAPIView
from rest_framework.permissions import IsAuthenticated

from habits.models import Award
from habits.permissions import IsOwner, IsSuperUser
from habits.serializers.award import AwardSerializer


class AwardListAPIView(ListAPIView):
    serializer_class = AwardSerializer
    queryset = Award.objects.all()
    permission_classes = [IsAuthenticated | IsOwner | IsSuperUser]

    def get_queryset(self):
        user = self.request.user
        if user.is_authenticated and user.is_superuser:
            return Award.objects.all()
        elif user.is_authenticated:
            return Award.objects.filter(user=user)
        else:
            raise PermissionDenied("You are not authenticated.")


class AwardCreateAPIView(CreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = AwardSerializer

    def perform_create(self, serializer):
        serializer.validated_data['user'] = self.request.user
        serializer.save()


class AwardUpdateAPIView(UpdateAPIView):
    serializer_class = AwardSerializer
    queryset = Award.objects.all()
    permission_classes = [IsOwner | IsSuperUser]


class AwardDestroyAPIView(DestroyAPIView):
    queryset = Award.objects.all()
    permission_classes = [IsOwner | IsSuperUser]
