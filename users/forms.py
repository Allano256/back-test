from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import User

class CustomUserCreationForm(UserCreationForm):
    """
    This handles creation of user
    """
    class Meta(UserCreationForm):
        model=User
        fields = ['email', 'first_name','last_name']
        error_class= 'error'
        

class CustomUserChangeForm(UserChangeForm):
    """
    This handles edit of user
    """
    class Meta(UserCreationForm):
        model=User
        fields = ['email', 'first_name','last_name']
        error_class= 'error'
        
