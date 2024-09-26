

from rest_framework.response import Response
from .models import Stream
from .serializers import StreamSerializer
from rest_framework.decorators import api_view
from rest_framework import status

@api_view(['GET'])
def view_streams(request):
    try:
        streams = Stream.objects.all()
        serializer = StreamSerializer(streams, many=True)
        return Response(serializer.data)
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
 