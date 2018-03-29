from django.shortcuts import render

# 博客首页
def index(request):
    context = {}
    context['hello'] = 'nuo xiao & 诺晓'

    return render(request,'blog/index.html',context)

# 园子
def garden(request):
    context = {}
    context['hello'] = 'nuo xiao & 诺晓'

    return render(request,'blog/garden.html',context)

# 园子详情
def detail(request, id):
    context = {}
    return render(request,'blog/detail.html', context)


# 主题
def theme(request):
    context = {}
    return render(request,'blog/theme.html', context)