from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView
from .models import Question
from .forms import QuestionForm
from django.views.generic.edit import FormMixin
from answers.forms import AnswerForm
from answers.models import Answer

class IndexView(ListView):
    model = Question
    template_name = 'questions/index.html'
    context_object_name = 'questions'


class CreateView(CreateView):
    template_name = 'questions/create.html'
    form_class = QuestionForm
    success_url = reverse_lazy('questions:index')

    def form_valid(self, form):
      question = form.save(commit=False)
      question.save()
      return super().form_valid(form)

class DetailView(DetailView, FormMixin):
    model = Question
    template_name = 'questions/detail.html'
    form_class = AnswerForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        answers = Answer.objects.filter(question=self.object)
        context['answers'] = answers
        context['form'] = self.get_form()
        return context
