from django.shortcuts import render

# 主页
def main(request):
    context = {}

    return render(request,'main.html',context)

# 首页
def index(request):
    context = {}
    context['primary'] = 'nuo xiao'
    context['slide'] = '诺晓，平凡世界的精神庄园'
    context['product'] = '诺晓 Product By ObjectBin'

    return render(request, 'index.html', context)