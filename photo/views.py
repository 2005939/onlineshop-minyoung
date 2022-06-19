from django.shortcuts import render, redirect

from .models import Photo
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic import DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.list import ListView


# Create your views here.

def photo_list(request):
  photos = Photo.objects.all()
  return render(request, 'photo/list.html', {'photos': photos})


class PhotoUploadView(LoginRequiredMixin, CreateView):
    model = Photo
    fields = ['photo', 'text']
    template_name = 'photo/upload.html'

    def form_valid(self, form):
        form.instance.author_id = self.request.user.id  # 현재 로그인 한 사용자로 설정
        if form.is_valid():  # 입력된 값 검증
            form.instance.save()  # 이상이 없다면, 데이터베이스에 저장하고,
            return redirect('photo:photo_list')  # 메인 페이지로 이동
        else:
            return self.render_to_response({'form': form})  # 이상이 있다면, 작성된 내용을 그대로 작성 페이지에 표시


class PhotoDeleteView(LoginRequiredMixin, DeleteView):
    model = Photo
    success_url = '/'  # site 메인 의미
    template_name = 'photo/delete.html'


class PhotoUpdateView(LoginRequiredMixin, UpdateView):
    model = Photo
    fields = ['photo', 'text']
    template_name = 'photo/update.html'


class PhotoDetailView(LoginRequiredMixin, DetailView):
    model = Photo
    template_name = 'photo/detail.html'


class Mypage(LoginRequiredMixin, ListView):
    model = Photo
    template_name = 'photo/mypage.html'
