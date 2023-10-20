from django.shortcuts import render, get_object_or_404
from django.views import generic, View
from .models import Game, Review, Comment

# Create your views here.

class GameList(generic.ListView):
    model = Game
    queryset = Game.objects.all()   # .order_by('-rating')
    template_name = 'index.html'
    paginate_by = 6


class GameReviews(generic.ListView):    # Site, where all Reviews are listed
    model = Review
    #slug = Game.slug                      # --> TO BE EDITED!
    queryset = Review.objects.all()        #(slug=slug)      # filter() #all() # Review.objects.filter(slug=game.title)
    template_name = 'reviews.html'       #for every game there is a different slug (URL)
    paginate_by = 6



class GameDetail(View):   #Früher: ReviewDetail
    
    def get(self, request, slug, *args, **kwargs):
        #review = Review,
        queryset = Review.objects.filter(status=1)     #  
        game = get_object_or_404(Game, slug=slug)
        reviews = game.review_set.filter(status=1).order_by('-created_on') # Get all reviews related to the game
        #comments = review.comments.filter(approved=True).order_by('created_on') # in walktrough: comments.filter(approved=True).order_by
        liked = False
        if request.user.is_authenticated:
            if reviews.filter(likes=request.user).exists():
                liked = True
        #if review.likes.filter(id=self.request.user.id).exists():
        #    liked = True

        return render(
            request,
            "game_detail.html",
            {   
                "game": game,
                "reviews": reviews,     # Pass the reviews related to the game to the context
                #"comments": comments,
                #"commented": True,
                "liked": liked,

                #"comment_form": CommentForm(),
            },
        )
    
class ReviewDetail(View):
    def get(self, request, slug, *args, **kwargs):
        queryset = Review.objects.filter(status=1)
        game = get_object_or_404(Game, slug=slug)
        review = get_object_or_404(queryset, slug=slug)
        #reviews = game.review_set.filter(status=1).order_by('-created_on') # Get all reviews related to the game
        #comments = review.comments.filter(approved=True).order_by('created_on') # in walktrough: comments.filter(approved=True).order_by
        liked = False
        if review.likes.filter(id=self.request.user.id).exists():
            liked = True
        #if review.likes.filter(id=self.request.user.id).exists():
        #    liked = True

        return render(
            request,
            "review_detail.html",
            {
                "review": review,
                "liked": liked,
            }
        )