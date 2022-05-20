from django.contrib import messages
from django.shortcuts import render, redirect


def not_found(request, exception):
    return render(request, 'errors/not_found.html', status=404)


def permission_denied(request, exception):
    messages.error(request, '沒有這個權限，無法進入畫面')
    return redirect('/movies/')