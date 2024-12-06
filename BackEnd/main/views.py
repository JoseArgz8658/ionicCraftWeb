from django.shortcuts import render
from django_user_agents.utils import get_user_agent

def index(request):
    user_agent = get_user_agent(request)
    
    apk_url = request.build_absolute_uri('/static/apk/IonicCraft.apk')
    
    context = {'mobile': user_agent.is_mobile, 'apk_url': apk_url}
    return render(request, 'index.html', context)