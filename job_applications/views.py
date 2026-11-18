from django.shortcuts import render,redirect,get_object_or_404
from .models import JobApplication
from .forms import JobApplicationForm


def job_list(request):
    query = request.GET.get('q','')
    status_filter = request.GET.get('status','')

    jobs = JobApplication.objects.all().order_by('-applied_date')

    if query:
        jobs = jobs.filter(company_name__icontains=query)
    if status_filter:
        jobs = jobs.filter(status=status_filter)

    context = {
        'jobs':jobs,
        'query':query,
        'status_filter':status_filter,
    }

    return render(request,'job_list.html',context)

def add_job(request):
    if request.method == 'POST':
        form = JobApplicationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('job_list')
    else:
        form = JobApplicationForm()
    return render(request,'job_form.html',{'form':form,'title':'Add Job Application'})

def edit_job(request,pk):
    job = get_object_or_404(JobApplication, pk=pk)

    if request.method == 'POST':
        form = JobApplicationForm(request.POST, instance=job)
        if form.is_valid():
            form.save()
            return redirect('job_list')
    else:
        form = JobApplicationForm(instance=job)
        return render(request,'job_form.html',{'form':form,'title':'Edit Job Application'})

def delete_job(request,pk):
    job = get_object_or_404(JobApplication,pk=pk)
    if request.method == 'POST':
        job.delete()
        return redirect('job_list')
    return render(request,'job_confirm_delete.html',{'job':'job'})




