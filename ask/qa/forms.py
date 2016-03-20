from django import forms
from .models import Question, Answer


class AskForm(forms.Form):
    title = forms.CharField(max_length=1000)
    text = forms.CharField(widget=forms.Textarea)

    def clean_title(self):
        title = self.cleaned_data.get('title')
        if len(title) < 3:
            raise forms.ValidationError('Title is a short. Min length 3')
        return title

    def clean_text(self):
        text = self.cleaned_data.get('text')
        if len(text) < 3:
            raise forms.ValidationError('Text is a short. Min length 3')
        return text

    def save(self):
        question = Question(**self.cleaned_data)
        question.save()
        return question


class AnswerForm(forms.Form):
    text = forms.CharField(widget=forms.Textarea)
    question = forms.IntegerField(widget=forms.HiddenInput)

    def clean_text(self):
        answer = self.cleaned_data.get('text')
        if not answer:
            raise forms.ValidationError('Answer text can\'t be blank.')
        return answer

    def clean_question(self):
        id = self.cleaned_data.get('question')
        try:
            question = Question.objects.get(pk=id)
        except Question.DoesNotExist:
            raise forms.ValidationError('Question not founded.')
        return question

    def save(self):
        answer = Answer(**self.cleaned_data)
        answer.save()
        return answer
