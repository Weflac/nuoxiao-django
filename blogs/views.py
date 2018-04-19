from django.shortcuts import render
from django.http import HttpResponse
from blogs.models import Users, Garden, Blogs, Commons
from django.http import Http404
from django.urls import reverse
from django.shortcuts import redirect

# 博客首页
def index(request):
    context = {'hello': 'nuo xiao & 诺晓', 'primary': 'nuo xiao', 'slide': '诺晓，你的精神庄园', 'product': '诺晓 Product By ObjectBin'}
    return render(request,'blog/index.html',context)

# 园子
def garden(request):
    try:
        garden = Garden.objects.all().values('id','name','introduce','description','author','dateTime')
        garden =list(garden)

        blogs = list(Blogs.objects.values('id', 'title', 'subtitle', 'introduction', 'imgurl'))

        context = {'list':garden,'blogs': blogs, 'hello': 'nuoxiao & 诺晓'}
    except Garden.DoesNotExist:
        raise Http404

    return render(request,'blog/garden.html', context)

# 园子-列表
def garden_list(request,type):
    try:
        gardenId = type
        garden = Garden.objects.values('id','name','introduce','description','author','dateTime').get(id=str(type))
        gardens = list(Garden.objects.all().values('id','name','introduce','description','author','dateTime'))
        blogs = list(Blogs.objects.filter(garden_id=type).values('id', 'title', 'subtitle', 'introduction', 'imgurl'))

        context = {'currentId': gardenId, 'garden': garden , 'list':gardens, 'blogs' :  blogs, 'hello': 'nuoxiao & 诺晓'}

    except Garden.DoesNotExist:
        raise Http404

    return render(request,'blog/garden-list.html',context)

# 园子详情
def detail(request, id):
    try:
        blog = Blogs.objects.values('id', 'title', 'subtitle', 'introduction','description','imgurl','dateTime','author').get(id=str(id))
        comments = Commons.objects.values('id','parentId','contnet','references','replys','dateTime','links','author','blogs').filter(blogs_id=id)

        context = {'num': id, 'blog': blog, 'comments': comments, 'counts': len(comments) }

    except Blogs.DoesNotExist:
        return redirect(reverse('notfound'))
        # raise Http404

    return render(request,'blog/detail.html', context)



# 添加 用户
def add_user(request):
    user = Users()
    user.name = 'nuoxiao'
    user.dateTime = '2018-03-31'
    user.save()

    return HttpResponse('<div>ok! add user.</div>')

# 添加 园子
def add_garden(request):
    garden = Garden()
    garden.name = '神经院子'
    garden.cover_url = 'http://www.nuoxiao.com/blog/dist/images/demo/stock-photos/3.jpg'
    garden.introduce = '不同的角度 同样的神经'
    garden.description = '添加数据是否通过'
    garden.author = Users.objects.get(name='nuoxiao')
    garden.dateTime = '2018-04-10'
    garden.save()

    return  HttpResponse('<div>ok! name=神经院子</div>')

# 添加 博客
def add_blogs(request):
    blogs = Blogs()
    blogs.title = 'Facebook产品设计副总裁'
    blogs.subtitle = '产品从0到1，能否成功我只看这4点'
    blogs.introduction = """本周问题是这样的：“过去，我所有的工作，都是与成熟产品打交道。通过不断的改变和优化，
    为那些产品的进一步发展和成长提供支持。但最近，我进行了一些调整，加入了一支团队从零开始研发全新产品。
    虽然这样一来各方面的限制比较少，但想想未来可能会遇到的问题，还是让人不禁胆怯。因此，我想问，一款产品从无到有，在设计上都存在哪些注意事项？你是否能给我提供几点可行性的建议？”
    想要从零开始研发一款成功产品，在较大范围内为用户创造新价值，是一件比较困难的事情。这样一种产品在诞生之初，是不可能十全十美的，都需要不断完善优化。就像人一样，产品也要经历不同的生命阶段。
    与能够扩展升级的成熟产品相比，新产品在研发过程中需要采用不同的策略和流程。
    因此，为了在最大程度上研发一款能够对全世界产生影响的产品，你最好要搞清楚产品开发要经历的不同阶段，知道每一项目所处的具体阶段，并且了解在该阶段内最为重要的影响因素。
    """
    blogs.description = """Facebook 产品设计副总裁：
“过去，我所有的工作，都是与成熟产品打交道......”
　　本周问题是这样的：“过去，我所有的工作，都是与成熟产品打交道。通过不断的改变和优化，为那些产品的进一步发展和成长提供支持。但最近，我进行了一些调整，加入了一支团队从零开始研发全新产品。虽然这样一来各方面的限制比较少，但想想未来可能会遇到的问题，还是让人不禁胆怯。因此，我想问，一款产品从无到有，在设计上都存在哪些注意事项？你是否能给我提供几点可行性的建议？”

　　想要从零开始研发一款成功产品，在较大范围内为用户创造新价值，是一件比较困难的事情。这样一种产品在诞生之初，是不可能十全十美的，都需要不断完善优化。就像人一样，产品也要经历不同的生命阶段。与能够扩展升级的成熟产品相比，新产品在研发过程中需要采用不同的策略和流程。

　　因此，为了在最大程度上研发一款能够对全世界产生影响的产品，你最好要搞清楚产品开发要经历的不同阶段，知道每一项目所处的具体阶段，并且了解在该阶段内最为重要的影响因素。

　　第一阶段：定义目标用户、明确用户需求

　　所谓定义目标用户，就是要仔细考虑，如果你即将要研发的产品能够在大范围内取得成功，那目标客户的行为、理解和感受应该要有什么不同。在编写代码之前，首先要对自己的产品有一个清晰定位。而这样一种定位，则要以目标客户的需求为基础。

　　下面，介绍三种正确定义目标用户的方法：

　　第一，搞清楚所研发产品想要解决的问题。这个问题可以是一种需求、一个难题或者一个机遇，是普通人都能够理解或者都有可能遇到的问题。比如说，如何解决飞行旅途中的无聊或者不适问题，而不是一家企业如何提高客户留存率这种问题。

　　比较理想的目标问题，能够了解人们在日常生活中的需求，能够找到现有解决方案中比较欠缺甚至根本不起作用的地方。所以，验证产品希望解决目标问题的合适、正确与否，是一家公司最该关注的本质问题。现阶段，有哪些行为、环境、研究或者数据告诉你这是一个需要解决的问题？这是一个表层问题还是一个根源问题？

　　第二，初步确定产品的目标客户。哪些人最需要你的产品？哪些人最头疼这一亟需解决的问题，并且真正愿意尝试一些方法来解决这个问题？

　　保证自家产品的功能能够适用于大多数用户，这固然是好事。但那些成功产品在研发初期，都是以小部分人为目标受众，努力让这部分人爱上自家产品，随后再慢慢扩大受众范围。所以，不妨定一个小目标，那就是顺利找到 1000 位早期用户，让他们爱上你的产品。

　　第三，搞清楚目标受众可能出现的变化。也就是说，如果你的产品真能在大范围内取得成功，那他们在行为和认知上的表现，将会出现哪些不一样的变化？

　　你希望初期用户在使用你的产品时，都有哪些心智模型或者使用案例？如果你想要针对目标受众发起一场营销活动，那要如何向他们展示自家产品的价值？

　　第二阶段：顺利找到产品市场匹配

　　所谓找到产品市场匹配，就是指在有了产品原型之后，仍然不断重复和完善，直到顺利实现上述几点预先设定的目标。在这一阶段，最重要的就是，在正确假设的基础之上，以最快速度得出决定性的结论。

　　下面，介绍三种快速找到产品市场匹配的方法：

　　第一，针对部分目标受众提供独一无二的产品使用体验。首先，你需要找到 1000 位可能会喜欢上你的产品的早期用户。其次，你需要针对这些早期用户设计端对端的产品使用体验，在最大程度上满足他们的需求，为他们提供满意的服务。当然，目标受众范围较小，就意味着在产品研发过程中可能会出现偏执武断的情况，你或许会在设计流程等问题上走极端。

　　所以，针对部分目标受众提供的端对端产品使用体验，至少必须要是切实可行的。如果他们对产品功能并不了解，也不知道自己为什么要使用、如何使用你的产品，又或者使用过程中发现速度太慢、漏洞百出，那很明显，你是不可能针对产品假设得出什么决定性结论的。与此同时，千万不要一味追求标新立异，不要在那些根本不会影响产品成功与否的所谓的特色上浪费时间。比如说，跳过标准组成部分，去研究与众不同的新按钮或者新标签。

　　第二，设置一些明显的成功衡量指标，保证顺利实现预先设定的目标。这些指标的任务，就是告诉你产品是否按照预先设想那样为用户创造价值。其中，比较好的指标包括，使用某项功能的用户留存率保持在 30% 左右不变，以及使用某项功能的用户愿意与别人分享的概率增加了三倍。相反，比较差的指标，就是在头三个月中，使用某项功能的用户共有多少人。之所以说这个指标比较差，是因为像这种计算总量的指标，可以通过广告宣传这类漏斗顶部策略，来实现增加或减少。所以，在目前这个阶段，这些指标还不能发挥太大的作用。

　　总而言之，在设置衡量指标时，你可以多多考虑留存率。因为它可以告诉你，自己的产品是否足够具有价值，能够吸引用户重复使用。由于在研发初期，你的目标受众范围比较小，因此你还需要注意整个群体行为出现的阶跃函数变化。简单说来，就是关注用户愿意分享的概率的倍数变化，而不是百分比变化。除此之外，还要通过定性研究来关注该群体内部出现的积极情绪。

　　第三，假定自己会不断学习，而不是一味想着将产品推向全世界各个角落。在这个阶段，你的目标应该是验证自己的产品确实能够为部分目标受众提供满意的使用体验。或者，对之前的产品假设有一个全面清晰的认识，找到错误之处，吸取经验教训。这两种，都是比较理想的结果。那么，为什么要养成这样一种有益的思维模式呢？理由大致有两个：

　　首先，产品不能顺利进入发货阶段，并不一定就意味着失败。在一款产品从无到有的过程中，想要保证每一个产品假设的正确性，是基本不现实的。如果一支团队执行能力较强，能够在最短时间内找到某一产品假设不成立的深层次原因，那它就应该受到褒奖，即便团队成员给出的建议是转变项目研究方向甚至彻底叫停项目。如果你从一开始就坚定地认为，研发的每一款产品最后都要进入发货销售阶段，那视野范围就会受到限制，只能以保守叠加的方式研究产品，而不是完完全全的创新。

　　其次，能够尽量避免过早的产品优化。在展示产品价值之前，千万不要急着去考虑收益和投入产出平衡问题。另外，在这个阶段，你只需要专心某一项产品的研发，不要考虑能否与其他产品创意共同研发等问题。这是下一个阶段才需要考虑的问题。最后，也不要过早给产品定型，限制它进行任何可能的变动。

　　第三阶段：做好各方面的协调工作

　　恭喜你，到这个阶段，你的产品已经顺利针对部分目标受众找到了产品市场匹配。现在这个阶段，你需要做的就是，基于产品研发早期出现的各种冲突因素进行合理协调。在这之后，你才能考虑向更广受众推出自家产品。

　　下面，介绍三种有效协调各方面工作的方法：

　　第一，在范围更加广泛的系统中寻求平衡和优化。我们都经历过这样的阶段，即自家产品看上去大受欢迎，但实际却无法取得可观收益。或者，你一心想着让目标受众深入了解你的产品，但却在无意中发现了一个新的入口点。而这个新的入口点，由于无法实现扩展升级而引起了其他团队不满。再或者，你所研发的产品与另一团队正在测试的内容非常相似，那么究竟该重点关注并且发布哪一款产品，就成了一个大问题。

　　不管怎么说，这个阶段的工作非常难做，牵涉到大量的数据挖掘工作和频繁的交叉组别讨论等等。但重点是要记住，在用户眼中，你的公司并不是内部各款产品和各个团队的集合体，而是一个完整的整体。一旦你无法做好各方面的协调工作，那研发出来的产品也会比较复杂，甚至令人困惑。当然，如果你按照上述步骤操作，注意上述问题，那么到这一阶段，应该就已经能证实自家产品确实可以为部分目标受众提供满意的使用体验，这就能为产品在更广范围内的发展完善提供动力。

　　第二，搞清楚所研发的产品是否会给公司带来积极正面的影响。研发的新产品能够扩大整个蛋糕的尺寸，而非个人分得的蛋糕份额，这一点至关重要。如果新产品的研发损害了其他产品的利益，那这些加减正负最终结果如何？为公司和用户创造的价值大于带来的损害吗？这款产品未来是否能为我们提供一个可以长期使用的可靠平台？如果不能，那你需要做的，就是停下脚步、重新评估，而不是全然不顾继续将它推向全球。

　　第三，确保提供高质量的用户使用体验。因为在上一个产品市场匹配阶段，你已经达到了自己的最快发展速度。所以，在这个完善和优化阶段，产品的开发过程可能会选择抄近路。比如，设计师的水平可能参差不齐、各种按钮协作低效、出现拼写错误、页面加载速度较慢等等。所有这些问题，最好都要在这个协调阶段得到完美解决，保证各项事务高效有序运行。

　　第四阶段：产品增长

　　确保产品实现增长，就意味着你要清楚地知道，作出什么样的变动可以让产品为现有用户和潜在用户创造更多价值。通常情况下，大多数团队都会想直接从这个阶段开始。但看过这篇文章之后，你应该知道这其实是最后一个阶段，必需要在完成上述三个阶段之后才能着手推进。那么，究竟应该如何实现产品增长，提高漏斗中的用户数量呢？

　　下面，从三个方面介绍一个成功的产品增长模式：

　　第一，找到合适自家公司和产品的用户获取模式。在产品研发初期，你需要找到 1000 位用户。那么，接下来，应该如何再获取到 1000 位用户呢？你认为，还有哪些用户虽然尚未使用你的产品，但必将从你的产品中获益？为了为更多潜在用户创造更多价值，你需要向产品中添加哪些新功能？在不断向新用户扩展的过程中，你或许会有一种循环周期的感觉，似乎又回到了第一个阶段。但其实，在第一阶段的基础之上，你还需要做一些额外工作，针对全新的目标受众顺利找到全新的产品市场匹配。

　　第二，搞清楚应该如何提供用户互动效率。对于现有用户来说，你要针对产品及其功能作出什么样的改变，才能为他们创造更多价值呢？初次使用产品的用户，与经常使用产品的用户，在使用体验上会呈现出哪些不同和变化趋势？

　　第三，继续观察和控制漏斗效率。随着漏斗中用户数量的逐渐增加，你需要想办法证明去漏斗仍然能够正常运作。比如说，你要注意某一特定层级或步骤，是否会出现用户数量的急剧下降等等。
    """
    blogs.garden = Garden.objects.get(name='神经院子')
    blogs.author = Users.objects.get(name='nuoxiao')
    blogs.links = 0
    blogs.reads = 0
    blogs.imgurl = 'http://www.nuoxiao.com/blog/dist/images/demo/stock-photos/facebook.jpg'
    blogs.dateTime = '2018-04-10'
    blogs.save()

    return  HttpResponse('<div>ok! facebook=blogs chengwei</div>')

# 修改 博客
def update_blogs(request):
    # blogs = Blogs()
    # blogs.imgurl = 'http://www.nuoxiao.com/blog/dist/images/demo/stock-photos/chenwei.jpg'
    # blogs.save()

    Blogs.objects.filter(title='滴滴宣布公司架构调整').update(imgurl='http://www.nuoxiao.com/blog/dist/images/demo/stock-photos/chenwei.jpg')

    return  HttpResponse('<div>ok! update = blogs chengwei</div>')


# 主题
def theme(request):
    context = {  }
    return render(request,'blog/theme.html', context)


# 404
def notfound(request):
    context = {  }
    return render(request,'404.html', context)