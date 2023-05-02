from django.shortcuts import render
from django.views.generic import TemplateView, ListView, View
from django.contrib.auth.mixins import LoginRequiredMixin
from fanapp.models import *
from django.http import  HttpResponseRedirect
class IndexView(LoginRequiredMixin, View):
    def get(self, request):
        myreply = UsersReplys.objects.filter(reciever = self.request.user )
        
        newReplys = Reply.objects.filter(ad__author = self.request.user, accept="")
        print(myreply)
        data ={
            'replys': myreply,
            'newReplys':newReplys,
        }


        return render(request, 'mypage.html', data)
    
    def post(self, request, *args, **kwargs):
        if request.POST.get('delete_by_id'):
            print('deleting')
            id = request.POST.get("delete_by_id")
            Reply.objects.get(id=id).delete()
        elif request.POST.get('add_by_id'):
            id = request.POST.get("add_by_id")
            replyObj = Reply.objects.get(id=id)
            replyObj.changeReply()
            user =User.objects.get(username = self.request.user.username)
            print(user)
            print(replyObj)
            UsersReplys.objects.create(reciever=user, reply=replyObj)
        return HttpResponseRedirect("")
    
    