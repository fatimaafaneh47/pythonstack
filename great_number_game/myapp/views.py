from multiprocessing import context
from unittest import result
from django.shortcuts import render ,redirect
import random 

def display(request):
        request.session['random'] = random.randint(1, 100) 
        request.session.save()
        return render(request,'index.html')


def Process(request):
	randonNum = random.randint(1, 100)
	request.session['random']= randonNum

	enterdNumber = request.POST['guess']
	userNumber = int(enterdNumber)   # to convert string or text to intger
		
	if(randonNum > userNumber):
		print("too low")
		result = 1
	elif(randonNum < userNumber):
		print("too high ")
		result = 2
	else:
		result = 3
		print ('True')
	context={
	'result': result
	}
	return render(request,'show.html',context)


   


