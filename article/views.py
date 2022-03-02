from django.shortcuts import render, redirect

from user.models import UserModel
from .models import post, postcommant, photo
from django.http import JsonResponse
from django.views import View

def main(request):
    username=request
    # user = request.user.is_authenticated
    # like_list=post.objects.filter(like=request.user).last()
    # if user:
    #     all_tweet = post.objects.all()
    #
    #
    #     return render(request, 'main.html', {"tweet": all_tweet})
    # else:
    #     return redirect("/sign-in")
    user = request.user.is_authenticated
    userprofile= UserModel.objects.get(username=request.user).fro_image
    print(userprofile)



    pos=post.objects.all()
    return render(request, 'main.html',{"post":pos,"username":username,"image":userprofile})


# def detail_view(request, id):
#     my_tweet = post.objects.get(id=id)
#     all_comment = tweetcommant.objects.filter(tweet_id=id)
#     user=request.user.username
#     if request.method == "GET":
#         taglist =""
#         tags=my_tweet.tag
#         list(tags)
#         for i in range(0, 4):
#             tag = tags.split(",")[i]
#             print(tag)
#             if tag != "전체":
#                 taglist = taglist + " " + tag
#                 print("-----")
#                 print(taglist)
#
#         return render(request, 'detail.html',{"tweet": my_tweet,"tag":taglist,"comment": all_comment,"user":user})
#     # , '
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
# def comment_like(request,id):
#     me =request.user
#     click_rasi = tweetmodel.objects.get(id=id)
#
#     if me in click_rasi.like.all():
#         click_rasi.like.remove(request.user)
#     else:
#         click_rasi.like.add(request.user)
#     return redirect(f'/detail/{id}')
#
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