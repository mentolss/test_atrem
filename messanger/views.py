from django.shortcuts import render
from .forms import FeedbackForm


def feedback_page(request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = FeedbackForm()
    return render(request, 'feedback_page.html', {'form': form})
