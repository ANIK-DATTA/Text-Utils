# views.py file created by me

from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return  render(request, 'index.html')
    #return HttpResponse('''Hello World''')

def analyze(request):
    str = request.POST.get('textAreaData', 'default')
    
    removepunc = request.POST.get('removepunc', 'off')   
    uppercase = request.POST.get('uppercase', 'off')
    remspace = request.POST.get('remspace', 'off')
    reverse = request.POST.get('reverse', 'off')
    countChar = request.POST.get('countChar', 'off')

    analyzed = ""
    punctuations = ''' !()[]'";:. ?><,/\|!@#$%^&*-+=_{} '''
    title = ''
    if removepunc == "on":
        for char in str:
            if char not in punctuations:
                analyzed += char
        if title == '':             
            title +=  'Removed Punctuations'        
        params = {'purpose': title,
              'analyzed_text': analyzed}
        str = analyzed
        
    if (uppercase == "on"):
        analyzed= ""
        for char in str:
            analyzed += char.upper()
        if title == '': 
            title += 'Upper Case'
        else:
            title += ', Upper Case'
        params = {'purpose': title,
              'analyzed_text': analyzed}
        str = analyzed

    if remspace == "on":
        analyzed= "".join(str.split())
        if title == '':
            title += 'Remove Space'
        else:
            title += ', Remove Space'
        params = {'purpose': title,
              'analyzed_text': analyzed}
        str = analyzed

    if reverse == "on":
        analyzed = str[::-1]
        if title == '':
            title += 'Reverse String'
        else:
            title += ', Reverse String'
        params = {'purpose': title,
              'analyzed_text': analyzed}
        str = analyzed

    if countChar == 'on':
        count=0
        for ch in str:
            if not ch==" ":
               count += 1
        if title == '':
            title += 'Count'
        else:
            title += ', Count'
        params = {'purpose': title,
              'analyzed_text': count}
        str = analyzed

    if not (countChar == 'on' or reverse == "on" or remspace == "on" or uppercase == "on" or removepunc == "on"):
        return HttpResponse('<center><h1 style = "margin: 10%;">  Error  <h1></center>')

    return render(request, 'analyze.html', params)
    