from django.db.models import Q
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from base.models import OmurInitials

from base.serializers import (
    OmurInitialsSerializer
)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_initials(request):
    initials = OmurInitials.objects.all()
    serializer = OmurInitialsSerializer(initials, many=True)
    return Response(serializer.data)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_initial(request):
    user = request.user
    data = request.data

    inital = OmurInitials.objects.create(
        commenter=user,
        content=data["content"],
    )
    serializer = OmurInitialsSerializer(inital, many=False)
    return Response(serializer.data)


@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def delete_initial(request, id):
    initial = OmurInitials.objects.get(id=id)
    initial.delete()
    return Response(id)