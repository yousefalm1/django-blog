from django.shortcuts import render, get_object_or_404
from django.views import generic, View
from .models import Post


class PostList(generic.ListView):
    model = Post
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'index.html'
    paginate_b = 6


class PostDetail(View):

    def get(self, request, slug, *args, **kwargs):
        # Get all posts with status=1
        queryset = Post.objects.filter(status=1)

        # Get the specific post with the provided slug or return a 404 if not found
        post = get_object_or_404(queryset, slug=slug)

        # Get approved comments for the post, ordered by creation date
        comments = post.comments.filter(approved=True).order_by('created_on')

        # Check if the current user has liked the post
        liked = False
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True

        # Render the post_detail.html template with post details, comments, and liked status
        return render(
            request,
            "post_detail.html",
            {
                "post": post,
                "comments": comments,
                "liked": liked
            },
        )
