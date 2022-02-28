from django.contrib import auth
from django.shortcuts import render, redirect

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


def edit_user(request):
    username = request
    userprofile = UserModel.objects.get(username=request.user).fro_image
    if request.method == 'GET':
        return render(request, 'user/edit_profile.html',{"username":username,"image":userprofile})

    if request.method == 'POST':
        re_name = request.POST.get('title', '')
        img = request.FILES['imgs']
        user=UserModel.objects.get(username=request.user)
        if img and re_name is not None:
            user.fro_image = img
            user.username = re_name
            user.save()
            return redirect('/')
        else:
            return render(request, 'user/edit_profile.html', {'error2': ' ID 또는 패스워드를 확인해주세요!'})




    # true_user = auth.authenticate(request, username=username, password=password)
    # if true_user is not None:
    #     auth.login(request, true_user)
    #     return redirect('/main')
    # else:
    #     return render(request, 'user/edit_profile.html', {'error2': ' ID 또는 패스워드를 확인해주세요!'})
