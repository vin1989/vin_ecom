from django.core.exceptions import PermissionDenied
from .models import Post

def user_authenticate(function):
    def wrap(request,d):
        post=Post.objects.get(id=d)
        if post.created_by==request.user:
            return function(request,d)
        else:
            raise PermissionDenied

    return wrap        
