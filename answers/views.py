from django.shortcuts import render, redirect
from django.views import View
from .forms import AnswerForm

class AnswerCreateView(View):
  def post(self, request, *args, **kwargs):
    form = AnswerForm(request.POST)
    if form.is_valid():
      answer = form.save(commit=False)
      answer.question_id = kwargs['pk']
      answer.save()
      return redirect('questions:detail', pk=answer.question_id)
    else:
      return render(request, 'questions:detail', {'form': form, 'pk': answer.question_id})