from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Post, Star
from .serializers import PostSerializer, StarSerializer

@api_view(['GET', 'POST'])
def post_list_create_view(request):
    if request.method == 'POST':
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(author=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    posts = Post.objects.all().order_by('-created_at')
    serializer = PostSerializer(posts, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def give_star_view(request, post_id):
    try:
        post = Post.objects.get(id=post_id)
    except Post.DoesNotExist:
        return Response({'error': 'Post not found'}, status=status.HTTP_404_NOT_FOUND)

    if Star.objects.filter(user=request.user, post=post).exists():
        return Response({'error': 'You have already given a star to this post.'}, status=status.HTTP_400_BAD_REQUEST)

    Star.objects.create(user=request.user, post=post)
    return Response({'message': 'Star given successfully'}, status=status.HTTP_201_CREATED)

@api_view(['GET'])
def post_detail_view(request, post_id):
    try:
        post = Post.objects.get(id=post_id)
    except Post.DoesNotExist:
        return Response({'error': 'Post not found'}, status=status.HTTP_404_NOT_FOUND)

    serializer = PostSerializer(post)
    return Response(serializer.data)
