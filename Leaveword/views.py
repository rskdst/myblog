from django.shortcuts import render,redirect
from django.http import HttpResponse
import json
from .models import *
from Userinfo.models import *
# Create your views here.
def leaveword(req):
    data = []
    messages = UserMessage.objects.filter(reply_id=None).order_by("-created_date").values("message_id","user__username","content","created_date")
    for msg in messages:
        count = UserMessage.objects.filter(parent_id=msg["message_id"]).count()
        msg["count"] = count
        data.append(msg)
    return render(req,"leave_word.html",locals())

def ajax(req):
    data = {}
    message_id = int(req.POST.get("message_id"))
    print(message_id)
    message = UserMessage.objects.filter(parent_id=message_id).values("parent_id","message_id","parent_id","user__username","reply__user__username","content","created_date")
    html = "<div id=%s>\n"%message_id
    for msg in message:
        message_id = msg["message_id"]
        username = msg["user__username"]
        reply_username = msg['reply__user__username']
        content = msg["content"]
        created_date = msg['created_date'].strftime('%Y-%m-%d %H:%M:%S')
        html += "<div class='child-comment' style='margin-left: 50px;font-size:20px;>\n<p class='username' style='font-size: 20px'>{}&nbsp;<span>回复:&nbsp;{}</span><span class='created_date' style='padding-left: 200px'>时间:{}</span></p>\n<p class='content' style='font-size: 20px'>{}</p>\n<a id={} class='reply' style='font-size: 20px'><span class='content_count' style='padding-left: 400px'>回复</span></a>\n</div>\n".format(username,reply_username,created_date,content,message_id,)
    html += "</div>"
    data["html"] = html
    data["parent_id"] = message[0]["parent_id"]
    v = json.dumps(data)
    return HttpResponse(v)

def ajax_submit(req):
    username = req.POST.get("username")
    user_one = UserInfo.objects.filter(username=username).first()
    content = req.POST.get("content")
    user = UserMessage()
    user.content = content
    user.user = user_one
    user.save()
    return HttpResponse("123")