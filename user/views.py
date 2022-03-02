from django.shortcuts import render, redirect
from django.contrib import auth
from django.contrib.auth.decorators import login_required
import re
from article.models import post

# Create your views here.
from user.models import UserModel


def mypage(request):
    username = request
    like = post.objects.filter(like=request.user)
    posts = post.objects.filter(author_id=request.user)

    td = []
    for a in like:
        # like_count = tweetmodel.objects.filter(like=a.id)

        td += {a}
        # ff=[]
        # ff+={like_count}
        print("----------")
        # print(ff)
        print(td)
    userprofile = UserModel.objects.get(username=request.user).fro_image

    return render(request, 'user/mypage.html', {"like": td, "post": posts, "username": username, "image": userprofile})


# Create your views here.
def signup(request):
    if request.method == 'POST':
        # form 태그 요청일때
        # 회원가입 + 로그인
        # 만약 아이디가 중복이면?
        email = request.POST.get('email', '')
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        password2 = request.POST.get('password2', '')
        fro_image = request.FILES['fro_image'] #한번 post씀. 끝

        found_user = UserModel.objects.filter(username=username)
        exist_email = UserModel.objects.filter(email=email)

        if len(found_user) > 0:
            return render(request, 'user/signup.html', {'error': '아이디가 이미 존재합니다.'})
        if len(exist_email) > 0:
            return render(request, 'user/signup.html', {'error': 'email이 이미 존재합니다.'})

        if email == '' or username == '' or password == '':
            return render(request, 'user/signup.html', {'error': '빈 칸에 내용을 입력해 주세요!'})

        else:
            if not (6 < len(password) < 21):
                return render(request, 'user/signup.html', {'error': 'password 길이는 7~20자 입니다.'})
            elif re.search('[0-9]+', password) is None or re.search('[a-zA-Z]+', password) is None:
                return render(request, 'user/signup.html', {'error': 'password 형식은 영문,숫자 포함 7~20자 입니다.'})
            elif password != password2:
                return render(request, 'user/signup.html', {'error': 'password가 서로 다릅니다'})

            else:
                UserModel.objects.create_user(email=email, username=username, password=password, fro_image=fro_image)
                # return render(request, 'user/signup.html', {'success': '회원가입 완료 !'})
                # return render(request, 'user/signin.html', {'success': '회원가입 완료 !'}) <- 하고싶은데 안됨
                return redirect('signin')

    else:
        # 그냥 링크타고 들어왔을 때
        # 회원가입 정보 입력하는 페이지를 보여줘
        return render(request, 'user/signup.html')


def signin(request):
    if request.method == 'POST':  # 데이터를 넘겨주는 경우는 :
        found_user = auth.authenticate(request,  # 유요한 유저인지 검사하는 장고기능
                                       username=request.POST['username'],
                                       password=request.POST['password']
                                       )
        print(request.POST)
        if found_user is not None:  # 유저가 있다면
            auth.login(request, found_user)  # 유효성검사를 한 found_user로 로그인해라.
            return redirect('main')

        else:  # 유효한 유저가 아니라면 :
            return render(request, 'user/signin.html', {'error': '유저가 존재하지 않습니다.'})
    elif request.method == 'GET':
        # 로그인정보 입력하는 페이지를 보여줘.
        return render(request, 'user/signin.html')


# 로그아웃
# 로그인 안한사람이 이 요청을 수행하면 작동 안함, signin페이지나 봐라
@login_required(login_url='signin')
def logout(request):
    auth.logout(request)  # 이거 쓰면 됨
    return redirect('signin')


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
