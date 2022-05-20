from django.contrib import messages
from django.contrib.auth.decorators import login_required, permission_required
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect

# Create your views here.
from movies.forms import MovieForm
from movies.models import Movie


@login_required
def index(request):
    movies = Movie.objects.all()
    cnt = movies.count()
    return render(request, 'movies/index.html', {'movies': movies, 'cnt': cnt})


@login_required
def detail(request, pk):
    movie = get_object_or_404(Movie, pk=pk)
    director = movie.director
    return render(request, 'movies/detail.html', {'movie': movie, 'director': director})


@login_required
def search(request):
    movie_name = request.GET.get('movie_name')
    cleaned_name = str(movie_name).strip()
    try:
        movie = Movie.objects.get(name=cleaned_name)
    except Movie.DoesNotExist:
        messages.error(request, f'沒有關於「{cleaned_name}」的介紹，請搜尋其他電影')
        return redirect('/movies/')
    return render(request, 'movies/query.html', {'movie': movie})


@login_required
@permission_required('movies.add', raise_exception=True)
def add(request):
    if request.method == 'POST':
        form = MovieForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/movies/')
    else:
        form = MovieForm()
    return render(request, 'movies/form.html', {'form': form, 'title': '新增電影介紹'})


@login_required
@permission_required('movies.edit', raise_exception=True)
def edit(request, pk):
    movie = get_object_or_404(Movie, pk=pk)
    if request.method == 'POST':
        form = MovieForm(request.POST, instance=movie)
        if form.is_valid():
            form.save()
            messages.success(request, '編輯成功')
            return redirect(f'/movies/{pk}/')
    else:
        form = MovieForm(instance=movie)
    return render(request, 'movies/form.html', {'form': form, 'title': '編輯電影介紹'})


@login_required
@permission_required('movies.delete', raise_exception=True)
def delete(request, pk):
    movie = get_object_or_404(Movie, pk=pk)
    if request.method == 'POST':
        movie.delete()
        messages.success(request, '刪除成功')
        return redirect('/movies/')
    else:
        return render(request, 'movies/delete.html', {'movie': movie})


