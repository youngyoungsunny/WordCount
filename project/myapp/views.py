from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def result(request):
    textname = request.GET['textname']
    textlist = textname.split()
    text_dic = {}

    for word in textlist:
        if word in text_dic:
            text_dic[word]+=1
        else:
            text_dic[word]=1

    return render(request, 'result.html', {'textname' : textname, 'textcount' : len(textlist), 'text_dic' : text_dic.items()})