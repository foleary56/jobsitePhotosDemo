from django.shortcuts import render, redirect
from .forms import PhotoUploadForm

def upload_photo(request):
    if request.method == 'POST':
        form = PhotoUploadForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('upload_success')
    else:
        form = PhotoUploadForm()
    return render(request, 'upload_photo.html', {'form': form})

def upload_success(request):
    return render(request, 'upload_success.html')
