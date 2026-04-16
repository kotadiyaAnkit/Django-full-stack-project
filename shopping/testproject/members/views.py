from django.http import HttpResponse
from django.template import loader
from django.shortcuts import redirect, render
from .models import Member
from django.shortcuts import render, redirect, get_object_or_404
from .models import Member
from .forms import MemberForm
from django.contrib.auth import logout
from django.contrib import messages

def members(request):
    form = MemberForm()
    return render(request, 'insert.html', {'form': form})   

# def members(request):
#   template = loader.get_template('insert.html')
  
#   return HttpResponse(template.render({}, request))

def submit_member(request):
    if request.method == 'POST':
        form = MemberForm(request.POST)
        if form.is_valid():
            print("============>no error")
            form.save()
            return redirect('show')   # Redirect to members list after submission
        else:
            # Re-render the form with errors
            print("============>error")
            return render(request, 'insert.html', {'form': form})
        
        # firstname = request.POST.get('firstname')
        # lastname = request.POST.get('lastname')
        # email = request.POST.get('email')

        # # Save to DB
        # Member.objects.create(firstname=firstname, lastname=lastname, email=email)

        # return redirect('show')   # Redirect to members list after submission
        # return render(request, 'your_form_template.html')
    return redirect('members')

def show_members(request):
    all_members = Member.objects.all()
    return render(request, 'display.html', {'members': all_members})

def update_member(request, id):
    member = get_object_or_404(Member, id=id)
    if request.method == 'POST':
        form = MemberForm(request.POST, instance=member)
        if form.is_valid():
            form.save()
            return redirect('show')
    else:
        form = MemberForm(instance=member)
    return render(request, 'update.html', {'form': form, 'member': member})


def delete_member(request, id):
    member = get_object_or_404(Member, id=id)
    member.delete()
    print(id,"========>id delete")
    return redirect('show')

def logout_view(request):
    logout(request)
    messages.success(request, "You have been logged out.")
    return redirect('submit_member')

# def member_create_view(request):
#     if request.method == 'POST':
#         form = MemberForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('success')  # redirect to success page
#     else:
#         form = MemberForm()
#     return render(request, 'members/member_form.html', {'form': form})