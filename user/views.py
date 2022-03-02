from django.shortcuts import render

from article.models import post


# Create your views here.
from user.models import UserModel


def mypage(request):
    username = request
    like=post.objects.filter(like =request.user)
    posts=post.objects.filter(author_id=request.user)

    td=[]
    for a in like:
        # like_count = tweetmodel.objects.filter(like=a.id)

        td+={a}
        # ff=[]
        # ff+={like_count}
        print("----------")
        # print(ff)
        print(td)
    userprofile = UserModel.objects.get(username=request.user).fro_image


    return render(request, 'user/mypage.html',{"like": td,"post":posts,"username":username,"image":userprofile})