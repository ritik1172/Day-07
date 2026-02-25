from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny

# public view accessible by anyone
@api_view(['GET'])
@permission_classes([AllowAny])
def public(request):
    return Response({'message': 'This is a public view.'})


# private view accessible only by authenticated users
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def private(request):
    return Response({'message':f'Hello {request.user.username},'  'This is a private view.'})
