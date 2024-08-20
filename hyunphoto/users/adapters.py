from allauth.socialaccount.adapter import DefaultSocialAccountAdapter
from allauth.account.adapter import get_adapter as get_account_adapter

from .models import User

# class UserCustomAdapter(DefaultSocialAccountAdapter):
#     def save_user(self, request, sociallogin, form=None):
#         print(self.__dict__)
#         u = super().save_user(request, sociallogin, form)
#         print(u.__dict__)
#         # u = sociallogin.user 
#         # print(u.__dict__)
#         u.set_unusable_password()
#         print(u.__dict__)
#         # print('before password:', u.password)
#         # # u.password = None 
#         # try:
#         #     # del(u.password)
#         #     print('after password:', u.password)
#         # except User.DoesNotExist:
#         #     print('Dosenot exist')
            
#         # if form:
#         #     get_account_adapter().save_user(request, u, form)
#         # else:
#         #     get_account_adapter().populate_username(request, u)
#         # sociallogin.save(request)
#         return u