from django.shortcuts import render

def comment_problem_page_view(request):
    return render(request, 'main/comments/comment.html')