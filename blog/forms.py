from django import forms
from .models import Post
from .models import UploadFile
from django.contrib.auth.models import User

class PostForm(forms.ModelForm):

	class Meta:
		model = Post
		fields = ('title', 'text',)

	def __init__(self, *args, **kwargs):
		super(PostForm, self).__init__(*args, **kwargs)
		self.name = "Post"


class UploadFileForm(forms.ModelForm):

	class Meta:
		model = UploadFile
		fields = ('title', 'file')

	def __init__(self, *args, **kwargs):
		super(UploadFileForm, self).__init__(*args, **kwargs)
		# self.fields['file'].required = False
		self.name = "File"

class UserForm(forms.ModelForm):

	class Meta:
		model = User
		fields = ['username', 'email', 'password']

class LoginForm(forms.ModelForm):

	class Meta:
		model = User
		fields = ['username', 'password']