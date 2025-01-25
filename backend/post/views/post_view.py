from post.logic.post_logic import PostLogic
from rest_framework.views import APIView
from rest_framework.response import Response
from post.serializers import PostSerializer


class PostServices(APIView):
    post_logic = PostLogic()

    def get(self, request):

        posts = self.post_logic.get_all_posts_active()

        serializer = PostSerializer(posts, many=True)

        return Response(serializer.data, status=200)
    

    def post(self, request):
        
        # NOTE: Si se extendiera este código, llevarlo a un archivo de Servicio
        # para mantener la vista lo más limpio posible y poder ocupar en cualquier otro lugar
        serializer = PostSerializer(data=request.data)

        if serializer.is_valid():
            name = serializer.data['name']
            description = serializer.data['description']
            post_created = self.post_logic.create_post(name, description)
            return Response({
                'id': post_created.id,
                'name': name,
                'description': description
            }, status=200)
        
        return Response(serializer.errors, status=400)
    
    def delete(self, request, id):

        post_deleted = self.post_logic.delete_post(id)

        if post_deleted:
            return Response({
                'message': 'Post deleted',
                'id': post_deleted.id
            }, status=200)
        
        return Response({
            'message': 'Post not found'
        }, status=404)
    


