import datetime
import smtplib
from email.mime.text import MIMEText

from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse
from django.shortcuts import render, redirect

from DeliveryApp.models import login, DeliveryPerson_Profile, Delivery, Photo


def login_page(request):
    return render(request,'Homepage.html')


def login_to_app(request):
    if request.method == 'POST':
        username=request.POST['usernm']
        password=request.POST['psswd']
        res = login.objects.filter(Username=username,Password=password)
        if res.exists():
            data = res[0]
            if data.UserType == 'Admin':
                return HttpResponse("<script>alert('Successfully LoggedIn');window.location='/admin_page'</script>")
            elif data.UserType == 'User':
                request.session['lid'] = data.id
                return HttpResponse("<script>alert('Successfully LoggedIn');window.location='/capture_page'</script>")

        else:
            return HttpResponse("<script>alert('Invalid User');window.location='/'</script>")

############################################Admin###################################################################

def admin_page(request):
    return render(request,'Admin/AdminHomePage.html')

def details_view(request):
    res=Photo.objects.all()
    return render(request,'Admin/Delivery_Details_view.html',{'data':res})

############################################User##################################################################

def delivery_per(request):
    return render(request,'Homepage.html')


def signup_form(request):
    usnm = request.POST['usnms']
    email =request.POST['eml']
    passwrd = request.POST['pswd']
    if request.session['lid'] == None:
        return HttpResponse("<script>alert('Session Expired Login Again!');window.location='/'</script>")
    else:

        loginobj = login()
        loginobj.Username = email
        loginobj.Password = passwrd
        loginobj.UserType="Pending"
        loginobj.save()

        person_obj = DeliveryPerson_Profile()
        person_obj.Username =usnm
        person_obj.Email = email
        person_obj.LOGIN = loginobj
        person_obj.save()
        return HttpResponse("<script>alert('Registered Successfully');window.location='/'</script>")


def capture_page(request):
    return render(request,'User/UserHomePage.html')

def capture(request):
    return render(request,'User/capture.html')

def store_captured(request):
    if request.session['lid'] == None:
        return HttpResponse("<script>alert('Session Expired Login Again!');window.location='/'</script>")
    else:
        tkt_name = request.POST['tkt']
        type_ = request.POST['type_of_photos']
        import datetime
        dt = datetime.datetime.now().strftime("%Y-%m-%d-%H:%M:%S")
        captured_img = request.FILES['image']
        fs =FileSystemStorage()

        d = datetime.datetime.now().strftime("%Y-%m-%d-%H%M%S")

        fs.save(r"C:\Users\shibil\PycharmProjects\DeliveryManagement\DeliveryApp\static\Files\\" + d + '.jpg', captured_img)
        CapturedFile ="/static/Files/" + d + '.jpg'

        stored_obj = Delivery()
        stored_obj.ticket_name = tkt_name
        stored_obj.delivery_date = dt
        stored_obj.user_profile = DeliveryPerson_Profile.objects.get(LOGIN=request.session['lid'])
        stored_obj.save()

        image_obj = Photo()
        image_obj.image_type =type_
        image_obj.image_file = CapturedFile
        image_obj.delivery = stored_obj
        image_obj.save()

        return HttpResponse("<script>alert('Delivery Details Added Successfully');window.location='/capture_page'</script>")



def password_change_page(request):
    return render(request,'Forget_password.html')

def forget_pswd(request):
    if request.method =="POST":
        username = request.POST['emlusnm']
        data = login.objects.filter(Username=username)


        if data.exists():
            pswd = data[0].Password
            try:
                gmail = smtplib.SMTP('smtp.gmail.com',587)
                gmail.ehlo()
                gmail.starttls()
                gmail.login('muhammadshibilepp@gmail.com','mxeleohzrhobqpel')


                msg = MIMEText("Your Password is" +  pswd)
                msg['Subject'] = 'Verification'
                msg['To'] = username
                msg['From'] ='uhammadshibilepp@gmail.com'
                gmail.send_message(msg)
                gmail.quit()
                return  render(request,'Forget_password.html',{'success_message':'Mail sent successfully'})
            except Exception as e:
                print("COULDN'T SEND EMAIL", str(e))
                return render(request,'Forget_password.html',{'error_message':'Filed to send email'})
        else:
            return render(request,'Forget_password.html',{'error_message':'User not found'})
    else:
        return render(request,'Forget_password.html')












