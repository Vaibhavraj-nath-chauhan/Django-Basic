from django.http import HttpResponse

def studens(request):
    work = ["Ram","Raj","Work","vaibhav","Task"]
    html = "<center><h1>My Task</h1></center>"
    for i in work:
        html += f"<li><a href='http://127.0.0.1:8000/details/{work.index(i)}' target ='_blank'>{i}<a></li>"
    return HttpResponse(html)

def dynamic(request,my_details):
    work = ["Ram", "Raj", "Work", "vaibhav", "Task"]
    len_data = len(work)-1
    if len_data >= my_details:
        html= f"<h1>you want to know details {work[my_details]}</h1>"
        return HttpResponse(html)
    else:
        return HttpResponse("Data Not Exists....:(")