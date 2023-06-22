from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Info
import random
from django.contrib import messages

class LevelScoreInfo:
    score=0
    level=1
    def __init(self):
        self.score=0
        self.level=0

    def inc(self):
        self.score+=1
        return  self.score
    def dec(self):
        self.score-=1
        return  self.score
    def givescore(self):
        return self.score
    def setScore(self):
        self.score=0

    def incLevel(self):
        if self.score%2==0 and self.score !=0:
            self.level+=1
    
    def giveLevel(self):
        return self.level
    
    def setLevel(self):
        self.level=1



sc=LevelScoreInfo()

def play(request):
        records=Info.objects.all()
        n=len(records)
        i=random.randrange(0,n,1)
        name=str(records[i].word).strip() 
        des=str(records[i].des_word).strip() 
        id=records[i].id

        # makes hiding word string
        length_of_word=len(records[i].word)
        hiding_word=str()
        k=0
        half=int(length_of_word/2)
        inc=random.randrange(0,half)
        while len(hiding_word)!=length_of_word/2 and k<length_of_word:
            hiding_word+=name[k]
            k+=2
            if len(hiding_word)==0:
                k=0
        sc.incLevel()
        context={'des':des,'name':name,'id':id,'hide':hiding_word ,'score':sc.givescore(),'level':sc.giveLevel()}
        return render(request,"game.html",context )
        # return HttpResponse(records[0].word)

def validate(request):
       if request.method=='POST':
        word1=str(request.POST['word'])
        id=request.POST['key']
        records=Info.objects.filter(id=id)
    #    here condtion becomes true when the user input word present in data base irreprective of we given the word
        flag=True 
        for rec in records:
            if( str(rec).strip().upper() == word1.strip().upper()):
                messages.success(request,"Nice..! correct word ")
                flag=False
                sc.inc()
                return redirect('Game/play')
        if flag:
            messages.error(request,"Sorry..! wrong word ")
            context1={'context':records ,'score':sc.givescore(),'setscore':sc.setScore(),'level':sc.giveLevel(),'setlevel':sc.setLevel()}
            return render(request,'playground.html',context1)
