from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.contrib.contenttypes.models import ContentType
from django.http import HttpResponseRedirect, HttpResponseForbidden
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.views import generic
from django.views.generic.edit import CreateView, FormMixin

from blog.forms import CommentForm
from .forms import UpdateProfileForm
from .models import Movie, Anime, Book, Software, Profile, Comment


# Create your views here.

# the home page view
def index(request):
    num_movies = Movie.objects.all().count()
    num_anime = Anime.objects.all().count()
    num_books = Book.objects.all().count()
    num_softwares = Software.objects.all().count()
    user = request.user

    context = {
        'num_movies': num_movies,
        'num_anime': num_anime,
        'num_books': num_books,
        'num_softwares': num_softwares,
    }

    if user.is_authenticated:
        user_profile = Profile.objects.get_or_create(user=user)
        user_profile1 = user_profile[0]
        user_following = user_profile1.following.all()
        context['user_profile1'] = user_profile1
        context['user_following'] = user_following

    return render(request, 'index.html', context=context)


# models listing view
class MovieListView(generic.ListView):
    model = Movie


class AnimeListView(generic.ListView):
    model = Anime


class BookListView(generic.ListView):
    model = Book


class SoftwareListView(generic.ListView):
    model = Software


class MovieDetailView(generic.DetailView, FormMixin):
    model = Movie
    form_class = CommentForm

    def get_success_url(self):
        return reverse('Movies-detail', kwargs={'pk': self.object.pk})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = self.get_form()
        comments_for_post = Comment.objects.all().filter(comment_author=self.request.user)
        context['comments_for_post'] = comments_for_post
        return context

    def post(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return HttpResponseForbidden()
        self.object = self.get_object()
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        # Here, we would record the user's interest using the message
        # passed in form.cleaned_data['message']
        stuff_pk = self.object.pk
        Comment.objects.create(comment_author=self.request.user,
                               content_type=ContentType.objects.get_for_model(self.model),
                               comment_text=form.cleaned_data['comment'], object_id=stuff_pk)
        return super().form_valid(form)


class AnimeDetailView(generic.DetailView):
    model = Anime


class SoftwareDetailView(generic.DetailView):
    model = Software


class BookDetailView(generic.DetailView):
    model = Book


# models creation views. Allows user to add movies,anime,etc

# create movies
class MovieCreate(LoginRequiredMixin, CreateView):
    model = Movie
    fields = ['title', 'magnetic_link', 'cover_img_link', 'movie_quality', 'movie_size', 'movie_genre']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


# create anime
class AnimeCreate(LoginRequiredMixin, CreateView):
    model = Anime
    fields = ['title', 'magnetic_link', 'cover_img_link', 'anime_video_quality', 'anime_video_size']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


# create softwares
class SoftwareCreate(LoginRequiredMixin, CreateView):
    model = Software
    fields = ['title', 'magnetic_link', 'cover_img_link', 'software_os', 'software_size']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


# crea book
class BookCreate(LoginRequiredMixin, CreateView):
    model = Book
    fields = ['title', 'book_author', 'magnetic_link', 'cover_img_link', 'book_format']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


# registration views
def register(request):  # not working
    if request.method == 'POST':
        f = UserCreationForm()
        if f.is_valid():
            f.save()
            messages.success(request, 'Account created Successfully')
            return HttpResponseRedirect('Movies')

    else:
        f = UserCreationForm()

    return render(request, 'registration/signup.html', {'form': f})


@login_required
def user_list(request):
    users = User.objects.exclude(username=request.user.username)
    context = {
        'users': users
    }
    return render(request, 'account/user/list.html', context=context)


@login_required
def user_detail(request, username):
    user = get_object_or_404(User, username=username)
    user_profile = Profile.objects.get_or_create(user=user)
    user_profile1 = user_profile[0]
    user_followers = user_profile1.followers.all()
    context = {
        'user_profile1': user_profile1,
        'user_followers': user_followers,
        'user': user,
    }
    print(user_followers)
    return render(request, 'account/user/detail.html', context)


@login_required
def follow(request, username):
    user_following = request.user
    user_followed = get_object_or_404(User, username=username)
    profile_user_following = Profile.objects.get_or_create(user=user_following)
    profile_user_followed = Profile.objects.get_or_create(user=user_followed)
    profile_user_followed[0].followers.add(profile_user_following[0])

    return render(request, 'users/follow/successfull.html')


def UpdateProfile(request):
    if request.method == 'POST':
        form = UpdateProfileForm(request.POST)
        if form.is_valid():
            # process the data
            # form.save(commit=False)
            current_user_profile = Profile.objects.get_or_create(user=request.user)
            # current_user_profile=request.user.Profile
            current_user_profile[0].dc_username = form.cleaned_data['dc_username']
            current_user_profile[0].something = form.cleaned_data['something']
            current_user_profile[0].save()
            print(current_user_profile[0].something)
            profile_url = reverse('user_detail', kwargs={'username': request.user.username})
            return HttpResponseRedirect(profile_url)

    else:
        form = UpdateProfileForm()

    return render(request, 'users/update_profile.html', {'form': form})