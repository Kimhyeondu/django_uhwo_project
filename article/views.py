from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from user.models import UserModel
from .models import post, postcommant, photo
from django.http import JsonResponse
from django.views import View


# 로그인 안한사람이 이 요청을 수행하면 작동 안함, signin페이지나 봐라
@login_required(login_url='signin')
def main(request):
    username=request
    user = request.user.is_authenticated
    # like_list=post.objects.filter(like=request.user).last()
    userprofile = UserModel.objects.get(username=request.user).fro_image
    if user:
        pos = post.objects.all()
        return render(request, 'main.html', {"post": pos, "username": username, "image": userprofile})
    else:
        return redirect("/sign-in")

def upload(request):
    username = request
    if request.method == 'GET':
        return render(request, 'article/upload.html',{"username":username})

    if request.method == 'POST':
        writes = post.objects.create(
            author=request.user,
            main_image=request.POST['url_api'],
            img_des=request.POST['des'],
            title=request.POST['title'],


        )
        return redirect('/', writes.pk)
    else:
        return redirect(request, "article/upload.html")



# def new(request):
#     if request.method =='POST':
#         writes = Write.objects.create(
#             author=request.user,
#             main_image=request.FILES['imgs'],
#             img_des=request.POST['des']
#         )
#         return redirect('/', writes.pk)
#     else:
#         return render(request, "article/upload.html")


def detail_view(request, id):
    my_tweet = post.objects.get(id=id)
    like = post.objects.filter(like=request.user)
    user=request.user
    return render(request, 'article/detail.html',{"tweet": my_tweet,"user":user})
    # , '
#
# # @login_required  # 로그인이 되어있어야 실행가능
# def write_comment(request, id):
#     if request.method == "POST":
#         T_comment = tweetcommant()
#
#         T_comment.comment = request.POST.get("comment", '')  ##post로 name이 comment인 html의 요소안에서 텍스트를 가져온다
#         # if T_comment.comment == '':
#         #     return redirect(request, f"/detail/{id}",{"error":"글자를 적으시오"})
#         T_comment.tweet = tweetmodel.objects.get(id=id)  ## 댓글창 열기전 트위터 개시물 아이디
#         T_comment.author = request.user  ## 로그인한 유저
#
#         T_comment.save()
#         return redirect(f"/detail/{id}")  # 선택한 트위터의 댓글달기 창으로 다시 돌려줌
#
# # @login_required  # 로그인이 되어있어야 실행가능
# def delete_comment(request, id):
#     tweet_comment = tweetcommant.objects.get(id=id)
#
#     current_tweet = tweet_comment.tweet.id  ## 지우기전에 트위터에 해당하는 id를 빼온다
#
#     tweet_comment.delete()
#     return redirect(f'/detail/{current_tweet}')
#
def comment_like(request,id):
    me =request.user
    click_rasi = post.objects.get(id=id)
    if me in click_rasi.like.all():
        click_rasi.like.remove(request.user)
    else:
        click_rasi.like.add(request.user)
    return redirect(f'/detail/{id}')
#
#
#
# def mypage(request):
#
#     like=tweetmodel.objects.filter(like =request.user)
#
#     td=[]
#     for a in like:
#         # like_count = tweetmodel.objects.filter(like=a.id)
#         td+={a}
#         # ff=[]
#         # ff+={like_count}
#         print("----------")
#         # print(ff)
#         print(td)
#
#     return render(request, 'mypage.html',{"like": td})