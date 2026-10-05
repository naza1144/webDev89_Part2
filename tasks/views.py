from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from .models import Task

PAGE_SIZE = 5


def get_task_page(user, status="all", q="", page_number=1, per_page=PAGE_SIZE):
    tasks = Task.objects.filter(owner=user)
    if status == "pending":
        tasks = tasks.filter(done=False)
    elif status == "done":
        tasks = tasks.filter(done=True)

    if q:
        tasks = tasks.filter(title__icontains=q)

    paginator = Paginator(tasks, per_page)
    return paginator.get_page(page_number)


class TaskListView(LoginRequiredMixin, ListView):
    model = Task
    template_name = "tasks/task_list.html"
    context_object_name = "tasks"

    def get_queryset(self):
        return Task.objects.filter(owner=self.request.user)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        page = get_task_page(self.request.user, status="all", q="", page_number=1)
        context["page"] = page
        context["status"] = "all"
        context["q"] = ""
        return context


@login_required
def task_filter_view(request):
    status = request.GET.get("status", "all")
    q = request.GET.get("q", "").strip()
    page = get_task_page(request.user, status=status, q=q, page_number=1)
    return render(
        request,
        "tasks/partials/task_page_rows.html",
        {"page": page, "status": status, "q": q},
    )


@login_required
def task_load_more_view(request):
    status = request.GET.get("status", "all")
    q = request.GET.get("q", "").strip()
    page_number = request.GET.get("page", 1)
    page = get_task_page(request.user, status=status, q=q, page_number=page_number)
    return render(
        request,
        "tasks/partials/task_page_rows.html",
        {"page": page, "status": status, "q": q},
    )


@login_required
def task_add_view(request):
    if request.method == "POST":
        title = request.POST.get("title", "").strip()
        if title:
            Task.objects.create(owner=request.user, title=title)

    page = get_task_page(request.user, status="all", q="", page_number=1)
    return render(
        request,
        "tasks/partials/task_page_rows.html",
        {"page": page, "status": "all", "q": ""},
    )


@login_required
def task_toggle_view(request, pk):
    task = get_object_or_404(Task, pk=pk, owner=request.user)
    if request.method in ["POST", "PATCH"]:
        task.done = not task.done
        task.save()
    return render(request, "tasks/partials/task_row.html", {"task": task})


@login_required
def task_edit_form_view(request, pk):
    task = get_object_or_404(Task, pk=pk, owner=request.user)
    return render(request, "tasks/partials/task_edit_form.html", {"task": task})


@login_required
def task_edit_view(request, pk):
    task = get_object_or_404(Task, pk=pk, owner=request.user)
    if request.method in ["POST", "PUT", "PATCH"]:
        title = request.POST.get("title", "").strip()
        if title:
            task.title = title
            task.save()
        return render(request, "tasks/partials/task_row.html", {"task": task})
    return render(request, "tasks/partials/task_edit_form.html", {"task": task})


@login_required
def task_cancel_view(request, pk):
    task = get_object_or_404(Task, pk=pk, owner=request.user)
    return render(request, "tasks/partials/task_row.html", {"task": task})


@login_required
def task_delete_view(request, pk):
    task = get_object_or_404(Task, pk=pk, owner=request.user)
    if request.method in ["POST", "DELETE"]:
        task.delete()
        return HttpResponse("")
    return HttpResponse("Method Not Allowed", status=405)