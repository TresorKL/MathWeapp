from multiprocessing import context
from unittest import result
from django.shortcuts import render

def getInputs(request):
    return render(request,'getnumbers.html')

def determineResult(request):
    
    if request.method == 'POST':
        num1 = request.POST.get("num1")
        num2 = request.POST.get("num2")
        result= int(num1) + int(num2)
        
        context={"num1":num1, "num2": num2, "result":result}
        
    return render(request, 'result.html',context)



