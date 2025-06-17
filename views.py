# In your views.py
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from .models import Profile
from .models import EmployerProfile
from .models import JobPost,JobApplication
from django.core.files.storage import FileSystemStorage
from django.db import migrations
from django.conf import settings
from datetime import date
from .forms import HealthSurveyForm,PhysicalHealthForm,MentalHealthForm,SpiritualHealthForm,NutritionHealthForm
from .forms import ExerciseForm,HygieneForm,SleepForm,HealthyHabitsForm
from .forms import StressManagementForm,EmotionalWellbeingForm,MeditationMindfulnessForm,MentalHealthDisordersForm
from .forms import InnerPeaceForm,GoalSettingForm,NatureForm,SpiritualityForm
from .forms import BalancedDietForm,SuperfoodsForm,MindfulEatingForm,SelfCareForm
from .forms import EducationSurveyForm
from .forms import ITForm,BusinessForm,HealthcareWellnessForm,ArtDesignForm,EducationTeachingForm,PersonalDevelopmentForm
from .forms import JobSearchForm,CandidateSearchForm


from django.views import View

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth import logout
from django.contrib.auth.models import User
from django.contrib import messages
from django.urls import reverse

from django.shortcuts import get_object_or_404, redirect
from .models import Comment, Reply
from .forms import CommentForm
from .forms import ReplyForm
from .forms import RegisterForm,UserUpdateForm,ProfileUpdateForm
from .forms import EmployerProfileUpdateForm

import re
from django.db import IntegrityError
from .models import EmailVerificationCode
import random
from django.core.mail import send_mail

def get_month_number(month_name):
    month_map = {
        'January': 1,
        'February': 2,
        'March': 3,
        'April': 4,
        'May': 5,
        'June': 6,
        'July': 7,
        'August': 8,
        'September': 9,
        'October': 10,
        'November': 11,
        'December': 12
    }
    return month_map.get(month_name, 1)  # default to 1 if invalid

def index(request):
    return render(request, 'main/index.html')

#def login(request):
    #return render(request, 'main/login1.html')

#def signup_view(request):
   # return render(request, 'main/signup.html')

#def loga(request):
    #return render(request, 'main/loga.html')

def job(request):
    return render(request, 'main/job.html')

def rainbow(request):
    return render(request, 'main/rainbow.html')

'''def create_default_user(apps, schema_editor):
    # Use the User model from the 'auth' app
    User = apps.get_model('auth', 'User')  # Correct capitalization of 'User'
    
    # Check if a user with the username 'nas' already exists
    if not User.objects.filter(username='nas').exists():
        # Create the default superuser
        User.objects.create_superuser(
            username='nas',           # Default username
            email='nas@example.com',  # Default email
            password='123'            # Default password
        )
class Migration(migrations.Migration):
    dependencies = [
        ('your_app_name', 'previous_migration_file'),
    ]

    operations = [
        migrations.RunPython(create_default_user),
    ]'''


def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            #if user.is_superuser:
            auth_login(request, user)
            # Set session flag for login type
            request.session['login_type'] = 'user'
            return redirect("two_factor_email")
            #else:
                #messages.error(request, 'You do not have permission to log in.')
        else:
            messages.error(request, 'Invalid credentials. Please signup first.')
            return redirect('login1')
        
    return render(request, 'main/login1.html')

def emplogin_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            #if user.is_superuser:
            auth_login(request, user)
            # Set session flag for login type
            request.session['login_type'] = 'employer'
            return redirect("two_factor_email")
            #else:
                #messages.error(request, 'You do not have permission to log in.')
        else:
            messages.error(request, 'Invalid credentials. Please signup first.')
            return redirect('emplogin1')
        
    return render(request, 'main/emplogin1.html')


def logout_view(request):
    logout(request)
    messages.success(request, "You have been logged out.")
    return redirect('index')

@login_required
def welcome_view(request):
    return render(request, 'main/welcome.html', {'username': request.user.username})

@login_required
def manage_account_redirect_view(request):
    if request.session.get('login_type') == 'employer':
        # If EmployerProfile doesn't exist, create it
        EmployerProfile.objects.get_or_create(user=request.user)
        return redirect('empmanageaccount')
    else:
        # For normal users (if you have that)
        Profile.objects.get_or_create(user=request.user)
        return redirect('manageaccount')

@login_required
def manage_account(request):
    if request.method == 'POST':
        user_form = UserUpdateForm(request.POST, instance=request.user)
        profile_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request,'Your profile has been updated successfully.')
            return redirect('manageaccount')
    else:
        user_form = UserUpdateForm(instance=request.user)
        profile_form = ProfileUpdateForm(instance=request.user.profile)

    return render(request, 'main/manageaccount.html', {
        'user_form': user_form,
        'profile_form': profile_form
    })

@login_required
def empmanage_account(request):
    #employer_profile = get_object_or_404(EmployerProfile, user=request.user)
    if request.method == 'POST':
        user_form = UserUpdateForm(request.POST, instance=request.user)
        empprofile_form = EmployerProfileUpdateForm(request.POST, request.FILES, instance=request.user.employerprofile)
        if user_form.is_valid() and empprofile_form.is_valid():
            user_form.save()
            # Handle clear checkbox
            '''if 'profilepic-clear' in request.POST:
                if employer_profile.profilepic:
                    employer_profile.profilepic.delete(save=False)
                employer_profile.profilepic = None
                empprofile_form.cleaned_data['profilepic'] = None  # <--- add this'''    
            empprofile_form.save()
            #request.user.EmployerProfile.refresh_from_db()
            messages.success(request, 'Your employer profile has been updated successfully.')
            return redirect('empmanageaccount')
    else:
        user_form = UserUpdateForm(instance=request.user)
        empprofile_form = EmployerProfileUpdateForm(instance=request.user.employerprofile)

    return render(request, 'main/empmanageaccount.html', {
        'user_form': user_form,
        'empprofile_form': empprofile_form
    })


#def register(request):
    #if request.method == 'POST':
        #form = RegisterForm(request.POST)
       # if form.is_valid():
            #user = form.save()
            #login(request, user)  # Log the user in after registration
            #return redirect('health')  # Redirect to health page or another URL after registration
    #else:
        #form = RegisterForm()
    #return render(request, 'main/register.html', {'form': form})


#def register_view(request):
    #if request.method == 'POST':
        #username = request.POST['username']
        #email = request.POST['email']
        #password = request.POST['password']
        #if User.objects.filter(username=username).exists():
            #messages.error(request, 'Username already exists')
        #else:
            #User.objects.create_user(username=username, email=email, password=password)
            #messages.success(request, 'Registration successful')
            #return redirect('login')
    #return render(request, 'main/register.html')

def service(request):
    return render(request, 'main/service.html')

def health1(request):
    return render(request, 'main/health1.html')

def education(request):
    return render(request, 'main/education.html')

def empsignup_view(request):
    return render(request, 'main/empsignup.html')

#def user_login(request):
    #if request.method == 'POST':
        #username = request.POST['username']
        #password = request.POST['password']
        #user = authenticate(request, username=username, password=password)
        #if user is not None:
            #login(request, user)
            #return redirect('home')
        #else:
            #messages.error(request, 'Invalid credentials')
    #return redirect('index')

#def register(request):
    #if request.method == 'POST':
        #username = request.POST['username']
        #email = request.POST['email']
        #password = request.POST['password']
        #if User.objects.filter(username=username).exists():
            #messages.error(request, 'Username already exists')
        #else:
            #User.objects.create_user(username=username, email=email, password=password)
            #messages.success(request, 'Registration successful')
    #return redirect('index')

# main/views.py

def health_view(request):
    comments = Comment.objects.all()
    reply_form = ReplyForm()
    if request.method == 'POST' and 'reply' in request.POST:
        if request.user.is_authenticated:
            reply_form = ReplyForm(request.POST)
            #form = CommentForm(request.POST)
            if reply_form.is_valid():
                reply = reply_form.save(commit=False)
                reply.user = request.user
                reply.comment_id = request.POST.get("comment_id")
                reply.save()
                #form.save()  # Save the new comment to the database
                return redirect('health')  # Redirect to the same page to see the new comment
        else:
            #form = CommentForm()
            # If the user is not authenticated, redirect to login page
            return redirect('login')  # Replace 'login' with the actual name of your login URL
    return render(request, 'main/health.html', {
        'comments': comments,
        'reply_form': reply_form,
    })
    
    # Retrieve all comments, ordered by creation date
    comments = Comment.objects.order_by('-created_at')
    return render(request, 'main/health.html', {'form': form, 'comments': comments})

@login_required
def like_comment(request, comment_id):
    comment = get_object_or_404(Comment, id=comment_id)
    comment.likes += 1
    comment.save()
    return redirect('health')

def signup_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        bio = request.POST.get("bio")
        email = request.POST.get("email")
        password = request.POST.get("password")
        profilepic = request.FILES.get("profilepic")
        full_name = request.POST.get("full_name")
        birth_day = request.POST.get("date_of_birth")
        birth_month = request.POST.get("birth_month")
        birth_year = request.POST.get("birth_year")
        city = request.POST.get("city")
        occupation = request.POST.get("occupation")
        education_level = request.POST.get("education_level")
        interests = request.POST.get("interests")
        goals = request.POST.get("goals")

        if not username or not email or not password:
            messages.error(request, "All fields are required.")
            return redirect("signup")
        
        if not full_name or not birth_day or not birth_month or not birth_year:
            messages.error(request, "Please complete your personal details.")
            return redirect("signup")
        
        if not city or not occupation or not education_level:
            messages.error(request, "Please complete your profile information.")
            return redirect("signup")

        if not re.match(r"^[\w\.-]+@gmail\.com$", email):
            messages.error(request, "Email must be in xyz@gmail.com format.")
            return redirect("signup")

        if len(password) < 8 or not any(char.isdigit() for char in password):
            messages.error(request, "Password must be at least 8 characters and contain digits.")
            return redirect("signup")

        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already taken.")
            return render(request, "main/signup.html", {'username_error': 'Username already exists.'})
        
        if User.objects.filter(email=email).exists():
            messages.error(request, "Email already registered.")
            return render(request, "main/signup.html",{'email_error': 'Email already registered.'})
        
        try:
            user = User.objects.create_user(username=username, email=email, password=password)
            user.save()

            # Convert birth date parts
            birth_day = int(birth_day)
            birth_month_num = get_month_number(birth_month)
            birth_year = int(birth_year)
            date_of_birth = date(birth_year, birth_month_num, birth_day)

            # Create Profile
            profile = Profile.objects.create(
                user=user,
                full_name=full_name,
                date_of_birth=date_of_birth,
                profilepic=profilepic,
                city=city,
                occupation=occupation,
                education_level=education_level,
                interests=interests,
                goals=goals,
                bio=bio
            )
            print("✅ Created profile for:", user.username)
            print("Full Name:", profile.full_name)
            print("Date of Birth:", profile.date_of_birth)
            print("City:", profile.city)

            # Save profile picture if uploaded
            '''user_profile = user.userprofile  # signals already create it
            if profilepic:
                user_profile.profilepic = profilepic
                user_profile.save()'''
            messages.success(request, "Account created successfully. Please login.")
            return redirect("index")
        except IntegrityError:
            messages.error(request, "An error occurred while creating your account.")
            return redirect("signup")

    return render(request, "main/signup.html")

def empsignup_view(request):
    if request.method == "POST":
        username = request.POST.get('username')
        managername = request.POST.get('managername')
        compname = request.POST.get('compname')
        companytype = request.POST.get('companytype')
        desc = request.POST.get('desc')
        city = request.POST.get('city')
        email = request.POST.get("email")
        password = request.POST.get("password")
        profilepic = request.FILES.get("profilepic")

        #if not username or not email or not password:
        if not (username and managername and compname and companytype and desc and city and email and password):
            messages.error(request, "All fields are required.")
            return redirect("empsignup")

        if not re.match(r"^[\w\.-]+@gmail\.com$", email):
            messages.error(request, "Email must be in xyz@gmail.com format.")
            return redirect("empsignup")

        if len(password) < 8 or not any(char.isdigit() for char in password):
            messages.error(request, "Password must be at least 8 characters and contain digits.")
            return redirect("empsignup")
        
        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already taken.")
            return render(request, "main/empsignup.html", {'username_error': 'Username already exists.'})
        
        if User.objects.filter(email=email).exists():
            messages.error(request, "Email already registered.")
            return render(request, "main/empsignup.html",{'email_error': 'Email already registered.'})
        
        try:
            user = User.objects.create_user(username=username, email=email,password=password)
            user.save()
           
           # Create EmployerProfile instance
            employer_profile = EmployerProfile.objects.create(
                user=user,
                managername=managername,
                compname=compname,
                companytype=companytype,
                desc=desc,
                city=city,
                profilepic=profilepic
            )
            employer_profile.save()
            messages.success(request, " Employer Account created successfully. Please login.")
            return redirect("index")
        except IntegrityError:
            messages.error(request, "An error occurred while creating your account.")
            return redirect("empsignup")

    return render(request, "main/empsignup.html")

def admin_login_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            messages.error(request, "Invalid email or password.")
            return redirect('loga')

        user = authenticate(request, username=user.username, password=password)

        if user is not None and user.is_superuser:
            auth_login(request, user)
            return redirect('/admin/')  # Django admin page
        else:
            messages.error(request, "You do not have permission to log in.")
            return redirect('loga')

    return render(request, 'main/loga.html')

def employer_signup1(request):
    if request.method == 'POST':
        company_name = request.POST['company_name']
        company_address = request.POST['company_address']
        email = request.POST['email']
        password = request.POST['password']

        if User.objects.filter(username=company_name).exists():
            messages.error(request, 'Company already registered.')
        else:
            user = User.objects.create_user(username=company_name, email=email, password=password)
            user.save()
            messages.success(request, 'Employer account created successfully.')
            return redirect('login1')  # Or wherever you want them to go after signup

    return render(request, 'main/employer_signup1.html')

def two_factor_email(request):
    return render(request, 'main/two_factor_email.html')

def enter_otp(request):
    return render(request, 'main/two_factor_otp.html')

def send_verification_code(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            messages.error(request, 'Email not registered.')
            return redirect('two_factor_email')

        code = str(random.randint(100000, 999999))
        EmailVerificationCode.objects.create(user=user, code=code)

        send_mail(
            'Your Verification Code',
            f'Your 6-digit code is {code}',
            settings.EMAIL_HOST_USER,
            [email],
            fail_silently=False,
        )

        request.session['verification_user_id'] = user.id
        messages.success(request, 'A verification code was sent to your email.')
        return redirect('enter_otp')

    return redirect('two_factor_email')

def verify_code(request):
    if request.method == 'POST':
        otp = request.POST.get('otp')
        user_id = request.session.get('verification_user_id')

        if not user_id:
            messages.error(request, 'Session expired. Please try again.')
            return redirect('two_factor_email')

        user = User.objects.get(id=user_id)
        code_entry = EmailVerificationCode.objects.filter(user=user, code=otp, is_verified=False).order_by('-created_at').first()

        if code_entry:
            if code_entry.is_expired():
                messages.error(request, 'Code expired. Request a new one.')
                return redirect('enter_otp')

            code_entry.is_verified = True
            code_entry.save()

            #Check login type and redirect accordingly
            login_type = request.session.get('login_type')
            if login_type == 'user':
                return redirect('index')  # your user home page
            elif login_type == 'employer':
                return redirect('empjob_page')  # your employer job portal page

            # Do your post-login redirect here
            messages.success(request, 'Verification successful. Welcome!')
            return redirect('index')  # replace with your dashboard/home page URL

        messages.error(request, 'Invalid code. Try again.')
        return redirect('enter_otp')

    return redirect('two_factor_email')

def resend_code(request):
    user_id = request.session.get('verification_user_id')
    if not user_id:
        messages.error(request, 'Session expired. Please try again.')
        return redirect('two_factor_email')

    user = User.objects.get(id=user_id)
    code = str(random.randint(100000, 999999))
    EmailVerificationCode.objects.create(user=user, code=code)

    send_mail(
        'Your New Verification Code',
        f'Your new 6-digit code is {code}',
        settings.EMAIL_HOST_USER,
        [user.email],
        fail_silently=False,
    )

    messages.success(request, 'A new verification code was sent.')
    return redirect('enter_otp')

def health_page(request):
    if request.method == 'POST':
        form = HealthSurveyForm(request.POST)
        physical_form = PhysicalHealthForm(request.POST)
        mental_form = MentalHealthForm(request.POST)
        spiritual_form = SpiritualHealthForm(request.POST)
        nutrition_form = NutritionHealthForm(request.POST)
        if form.is_valid():
            choice = form.cleaned_data['concern']
            # Redirect to corresponding section on health1 page
            return redirect(f'/health_page#{choice}')
        if physical_form.is_valid():
            choice = physical_form.cleaned_data['physical_concern']
            if choice == 'exercise':
                return redirect('/exercise_questions')
            elif choice == 'hygiene':
                return redirect('/hygiene_questions')
            elif choice == 'sleep':
                return redirect('/sleep_questions')
            elif choice == 'healthyhabits':
                return redirect('/healthyhabits_questions')
            else:
                return redirect('/health_page')
            # Redirect to corresponding section on health1 page
            #return redirect(f'/health_page#{choice}')
        
        if mental_form.is_valid():
            choice = mental_form.cleaned_data['mental_concern']
            if choice == 'stress':
                return redirect('/stress_questions')
            elif choice == 'emotions':
                return redirect('/emotions_questions')
            elif choice == 'meditation':
                return redirect('/meditation_questions')
            elif choice == 'disorders':
                return redirect('/disorders_questions')
            else:
                return redirect('/health_page')
            # Redirect to corresponding section on health1 page
            #return redirect(f'/health_page#{choice}')
        if spiritual_form.is_valid():
            choice = spiritual_form.cleaned_data['spiritual_concern']
            if choice == 'peace':
                return redirect('/peace_questions')
            elif choice == 'goal':
                return redirect('/goal_questions')
            elif choice == 'nature':
                return redirect('/nature_questions')
            elif choice == 'practices':
                return redirect('/practices_questions')
            else:
                return redirect('/health_page')
            # Redirect to corresponding section on health1 page
            #return redirect(f'/health_page#{choice}')
        if nutrition_form.is_valid():
            choice = nutrition_form.cleaned_data['nutrition_concern']
            if choice == 'diet':
                return redirect('/diet_questions')
            elif choice == 'foods':
                return redirect('/foods_questions')
            elif choice == 'eatinghabits':
                return redirect('/eatinghabits_questions')
            elif choice == 'selfcare':
                return redirect('/selfcare_questions')
            else:
                return redirect('/health_page')
            # Redirect to corresponding section on health1 page
            #return redirect(f'/health_page#{choice}')
        
    else:
        form = HealthSurveyForm()
        physical_form = PhysicalHealthForm()
        mental_form = MentalHealthForm()
        spiritual_form = SpiritualHealthForm()
        nutrition_form = NutritionHealthForm()

    return render(request, 'main/health_page.html', 
                  {'form': form,
                  'physical_form': physical_form,
                  'mental_form': mental_form,
                  'spiritual_form': spiritual_form,
                  'nutrition_form': nutrition_form,
                  })

''' # Redirect based on concern
            if concern == 'physical-health':
                return redirect('/health_page/#physical-health')
            elif concern == 'sleep':
                return redirect('/health1#sleep')
            elif concern == 'hydrate':
                return redirect('/health1#hydrate')
            elif concern == 'exercise':
                return redirect('/health1#exercise')
            elif concern == 'mental':
                return redirect('/health1#mental')
            elif concern == 'meditate':
                return redirect('/health1#meditate')
            else:
                return redirect('/health1')
        else:
            return render(request, 'health_page.html', {'form': form})'''
        
def exercise_questionsview(request):
    if request.method == 'POST':
        exercise_form = ExerciseForm(request.POST)
        if exercise_form.is_valid():
            # Save form data in session
            request.session['exercise_data'] = exercise_form.cleaned_data
            return redirect('exercise_results')  # URL name of results page
        
            # Redirect to corresponding section on health1 page
            return redirect(f'/exercise_questions#{choice}')
            '''activity = form.cleaned_data['physical_activity']
            frequency = form.cleaned_data['workout_frequency']
            types = form.cleaned_data['workout_type']

            # Logic for customized advice
            if frequency == 'never':
                advice = "Start with 10 minutes of walking daily."
            elif frequency == 'daily':
                advice = "Keep up your daily routine — try adding variety!"
            elif activity == 'yes':
                advice = "Start with 10 minutes of walking daily."


            return render(request, 'main/exercise_results.html', {'advice': advice, 'types': types})'''
    else:
        exercise_form = ExerciseForm()
    return render(request, 'main/exercise_questions.html', {'exercise_form': exercise_form})

def exercise_results(request):
    exercise_data = request.session.get('exercise_data')
    if not exercise_data:
        # No data, redirect back to form page
        return redirect('exercise_questions')

    # Example: logic based on user's physical_activity and fitness_goal
    physical_activity = exercise_data.get('physical_activity')
    fitness_goal = exercise_data.get('fitness_goal')
    workout_frequency = exercise_data.get('workout_frequency')
    workout_type = exercise_data.get('workout_type')
    fitness_plan = exercise_data.get('fitness_plan')
    fitness_goal = exercise_data.get('fitness_goal')
    track_progress = exercise_data.get('track_progress')
    workout_style = exercise_data.get('workout_style')
    alternative_activities = exercise_data.get('alternative_activities')
    strength_training = exercise_data.get('strength_training')
    menstrual_discomfort = exercise_data.get('menstrual_discomfort')

    messages = []

    # Physical activity
    if physical_activity == 'no':
        messages.append("Starting some physical activity, even light walking or stretching, can greatly improve your health.")
    else:
        messages.append("Great that you engage in physical activity! Keep it up.")

    # Workout frequency advice
    if workout_frequency in ['rarely', 'once_week']:
        messages.append("Try to increase your exercise frequency to at least 3 times a week for better results.")
    elif workout_frequency == '3-4_times':
        messages.append("Good job maintaining a solid workout schedule!")
    elif workout_frequency == 'daily':
        messages.append("Exercising daily is excellent but ensure you include rest days as needed to avoid burnout.")

    # Workout type recommendations
    if workout_type == 'cardio':
        messages.append("Cardio exercises are great for heart health and weight management.")
    elif workout_type == 'strength':
        messages.append("Strength training helps build muscle and improve metabolism.")
    elif workout_type == 'flexibility':
        messages.append("Flexibility exercises improve mobility and reduce injury risk.")
    elif workout_type == 'daily_activity':
        messages.append("Including daily activities like walking or chores is a good way to stay active.")

    # Fitness plan
    if fitness_plan == 'no':
        messages.append("Consider following a fitness routine or plan to stay motivated and consistent.")
    elif fitness_plan == 'planning':
        messages.append("Planning to start a fitness routine soon is a great step!")

    # Fitness goals
    if fitness_goal == 'weight_loss':
        messages.append("Focus on combining cardio and strength training for effective weight loss.")
    elif fitness_goal == 'weight_gain':
        messages.append("Strength training combined with a calorie surplus diet helps in gaining weight.")
    elif fitness_goal == 'strength':
        messages.append("Regular strength training sessions are key to building strength.")
    elif fitness_goal == 'stress':
        messages.append("Activities like yoga, pilates, or light cardio can help reduce stress.")
    elif fitness_goal == 'stay_active':
        messages.append("Maintaining regular moderate activity helps keep your body healthy and active.")

    # Tracking progress
    if track_progress == 'yes':
        messages.append("Tracking your progress is a great habit to stay motivated.")
    else:
        messages.append("Try tracking your fitness progress through apps or journals for better results.")

    # Workout style
    if workout_style == 'group':
        messages.append("Group fitness sessions can boost motivation and make workouts fun.")
    elif workout_style == 'personal':
        messages.append("Personal training offers tailored guidance for your goals.")
    else:
        messages.append("Solo workouts provide flexibility and independence.")

    # Alternative activities
    if alternative_activities == 'yes':
        messages.append("Exploring different activities like dance or martial arts keeps fitness exciting!")
    else:
        messages.append("Trying new physical activities can be refreshing and beneficial.")

    # Strength training frequency
    if strength_training == 'never':
        messages.append("Incorporating some strength training can improve overall fitness.")
    elif strength_training == 'sometimes':
        messages.append("Increasing strength training sessions could help you see better results.")
    else:
        messages.append("Regular strength training supports muscle growth and endurance.")

    # Menstrual discomfort impact
    if menstrual_discomfort == 'yes':
        messages.append("Listen to your body during menstrual discomfort and adjust your workouts accordingly.")
    else:
        messages.append("It's great that menstrual discomfort isn't affecting your activity!")

    # Join all messages for display
    final_message = " ".join(messages)

    context = {
        'exercise_data': exercise_data,
        'message': final_message,
    }
    return render(request, 'main/exercise_results.html', context)

def hygiene_questionsview(request):
    if request.method == 'POST':
        hygiene_form = HygieneForm(request.POST)
        if hygiene_form.is_valid():
            request.session['hygiene_data'] = hygiene_form.cleaned_data
            return redirect('hygiene_results')  
    else:
        hygiene_form = HygieneForm()
    return render(request, 'main/hygiene_questions.html', {'hygiene_form': hygiene_form})

def hygiene_results(request):
    # Assume data is stored in session (as you'd need to save form data after POST)
    hygiene_data = request.session.get('hygiene_data')

    if not hygiene_data:
        return redirect('hygiene_questionsview')  # if no data, send user back to form

    # Extract values
    sanitary_product_change = hygiene_data.get('sanitary_product_change')
    cleaning_method = hygiene_data.get('cleaning_method')
    reusable_product_cleaning = hygiene_data.get('reusable_product_cleaning')
    hand_washing = hygiene_data.get('hand_washing')
    hair_wash_frequency = hygiene_data.get('hair_wash_frequency')
    undergarment_habits = hygiene_data.get('undergarment_habits')
    gyne_visit_frequency = hygiene_data.get('gyne_visit_frequency')
    infection_awareness = hygiene_data.get('infection_awareness')
    grooming_tool_hygiene = hygiene_data.get('grooming_tool_hygiene')
    item_replacement_frequency = hygiene_data.get('item_replacement_frequency')

    # Result message logic
    result_messages = []

    # Sanitary product hygiene
    if sanitary_product_change in ['once_daily', 'twice_daily']:
        result_messages.append("👉 Consider changing your sanitary products more frequently (every 4-6 hours) to prevent infections and rashes.")
    else:
        result_messages.append("✅ Great job maintaining proper menstrual hygiene by changing products frequently.")

    # Cleaning method
    if cleaning_method == 'none':
        result_messages.append("⚠️ It's important to clean your intimate area daily with plain water or a pH-balanced wash to avoid infections.")
    else:
        result_messages.append("✅ Good hygiene routine for intimate area cleaning.")

    # Reusable product cleaning
    if reusable_product_cleaning == 'dont_use':
        result_messages.append("✔️ If you ever opt for reusable menstrual products, ensure proper sterilization for safety.")
    elif reusable_product_cleaning in ['boiling_water', 'disinfectant_solution']:
        result_messages.append("✅ Excellent method for sterilizing reusable products.")
    else:
        result_messages.append("⚠️ Consider sterilizing reusable menstrual products with boiling water or a disinfectant solution.")

    # Hand washing
    if hand_washing != 'always':
        result_messages.append("⚠️ Always wash your hands both before and after changing sanitary products to prevent infections.")
    else:
        result_messages.append("✅ Good hand hygiene practice.")

    # Hair washing
    if hair_wash_frequency in ['weekly']:
        result_messages.append("📝 Washing hair only once a week might lead to scalp issues, especially in humid climates or after workouts.")
    else:
        result_messages.append("✅ Balanced hair washing routine.")

    # Undergarment habits
    if undergarment_habits == 'rarely_care':
        result_messages.append("⚠️ Consider switching to breathable, clean undergarments daily for better hygiene.")
    else:
        result_messages.append("✅ Good undergarment hygiene.")

    # Gyne visit frequency
    if gyne_visit_frequency in ['only_when_symptoms', 'never']:
        result_messages.append("⚠️ It's advisable to schedule routine gynecologist check-ups at least once a year, even without symptoms.")
    else:
        result_messages.append("✅ Great job staying proactive with routine health checks.")

    # Infection awareness
    if infection_awareness == 'no':
        result_messages.append("💡 Educating yourself about early signs of infections can help you take timely action.")
    else:
        result_messages.append("✅ Good awareness about potential signs of infections.")

    # Grooming tool hygiene
    if grooming_tool_hygiene != 'always_sterilize':
        result_messages.append("⚠️ Always sterilize grooming tools like razors and nail cutters before use to prevent infections.")
    else:
        result_messages.append("✅ Safe grooming tool hygiene.")

    # Item replacement
    if item_replacement_frequency == 'rarely':
        result_messages.append("⚠️ Regularly replace personal hygiene items like toothbrushes and loofahs every 1-3 months for optimal hygiene.")
    else:
        result_messages.append("✅ Good practice of replacing hygiene items.")

    # Final overall message
    final_summary = "Here's a personalized hygiene report based on your answers. Stay consistent with good habits and make small changes where needed to support your health and comfort."

    context = {
        'hygiene_data': hygiene_data,
        'result_messages': result_messages,
        'final_summary': final_summary,
    }

    return render(request, 'main/hygiene_results.html', context)

def sleep_questionsview(request):
    if request.method == 'POST':
        sleep_form = SleepForm(request.POST)
        if sleep_form.is_valid():
             choice = sleep_form.cleaned_data['sleep_hours']
             return redirect(f'/sleep_questions#{choice}')      
    else:
        sleep_form = SleepForm()
    return render(request, 'main/sleep_questions.html', {'sleep_form': SleepForm})

def healthyhabits_questionsview(request):
    if request.method == 'POST':
        healthyhabits_form = HealthyHabitsForm(request.POST)
        if healthyhabits_form.is_valid():
            choice = healthyhabits_form.cleaned_data['water_intake']
            return redirect(f'/healthyhabits_questions#{choice}')   
    else:
        healthyhabits_form = HealthyHabitsForm()
    return render(request, 'main/healthyhabits_questions.html', {'healthyhabits_form': healthyhabits_form})

def stress_questionsview(request):
    if request.method == 'POST':
        stress_form = StressManagementForm(request.POST)
        if stress_form.is_valid():
            choice = stress_form.cleaned_data['overwhelmed_frequency']
            return redirect(f'/stress_questions#{choice}')   
    else:
        stress_form = StressManagementForm()
    return render(request, 'main/stress_questions.html', {'stress_form': stress_form})

def emotions_questionsview(request):
    if request.method == 'POST':
        emotions_form = EmotionalWellbeingForm(request.POST)
        if emotions_form.is_valid():
            choice = emotions_form.cleaned_data['emotional_state']
            return redirect(f'/emotions_questions#{choice}')   
    else:
        emotions_form = EmotionalWellbeingForm()
    return render(request, 'main/emotions_questions.html', {'emotions_form': emotions_form})

def meditation_questionsview(request):
    if request.method == 'POST':
        meditation_form = MeditationMindfulnessForm(request.POST)
        if meditation_form.is_valid():
            # Save form responses to session
            request.session['meditation_data'] = meditation_form.cleaned_data
            return redirect('meditation_results')
    else:
        meditation_form = MeditationMindfulnessForm()
    return render(request, 'main/meditation_questions.html', {'meditation_form': meditation_form})

def meditation_results(request):
    data = request.session.get('meditation_data')

    if not data:
        return redirect('meditation_questionsview')

    # Initialize result messages
    recommendations = []
    resources = []

    # Tried meditation?
    if data['tried_meditation'] == 'yes':
        recommendations.append("Fantastic that you’ve tried meditation! Consistency can deepen its mental, emotional, and physical benefits.")
    else:
        recommendations.append("Consider starting with 5 minutes of mindful breathing daily — it's a gentle, effective way to begin.")

    # Main reason for meditation
    reason = data['meditation_reason']
    if reason == 'stress_relief':
        recommendations.append("For stress relief, guided meditations and breathing techniques are highly effective. Try Calm or Insight Timer apps.")
        resources.append("🎥 [10-Minute Guided Meditation for Stress](https://www.youtube.com/watch?v=MIr3RsUWrdo)")
    elif reason == 'focus':
        recommendations.append("To improve focus, try morning meditation or short mindfulness breaks during work. Pomodoro + breathing works wonders.")
        resources.append("🎥 [5-Minute Focus Boosting Meditation](https://www.youtube.com/watch?v=inpok4MKVLM)")
    elif reason == 'anxiety':
        recommendations.append("For anxiety, progressive muscle relaxation and mantra meditation can calm racing thoughts.")
        resources.append("🎥 [Anxiety Relief Meditation](https://www.youtube.com/watch?v=ZToicYcHIOU)")
    elif reason == 'spirituality':
        recommendations.append("For a spiritual connection, explore Yoga Nidra or visualization meditations under soft music.")
        resources.append("🎥 [Spiritual Meditation - Peaceful Connection](https://www.youtube.com/watch?v=84z8VUGCPno)")
    elif reason == 'sleep':
        recommendations.append("For better sleep, practice Yoga Nidra or gentle guided sleep meditations before bed.")
        resources.append("🎥 [Yoga Nidra for Sleep](https://www.youtube.com/watch?v=1o3uo2LOtJk)")
    else:
        recommendations.append("Experiment with different styles to discover what resonates most with you.")

    # Meditation frequency
    freq = data['meditation_frequency']
    if freq == 'daily':
        recommendations.append("Daily practice is excellent! Keep going — even 10 minutes a day rewires the brain for calm and focus.")
    elif freq == '2_3_week':
        recommendations.append("Try aiming for short daily sessions — consistency matters more than duration.")
    elif freq == 'occasionally':
        recommendations.append("Great start! Making it a regular part of your week will enhance your emotional resilience.")
    elif freq == 'never':
        recommendations.append("No worries! Starting small — 2 minutes of deep breathing — can still shift your mood.")

    # Preferred meditation type
    preferred_type = data['meditation_type']
    recommendations.append(f"Since you prefer {preferred_type.replace('_', ' ').title()}, consider exploring guided sessions on YouTube or Insight Timer in this style.")

    # Positive effects
    if data['positive_effects'] == 'yes':
        recommendations.append("Wonderful that you’ve felt noticeable benefits! Track your mood and sleep to notice long-term changes.")
    elif data['positive_effects'] == 'somewhat':
        recommendations.append("That’s a good start — increasing frequency or trying new techniques might amplify the effects.")
    elif data['positive_effects'] == 'no':
        recommendations.append("It’s normal early on. Try different types like breathing or visualization, and stay patient.")
    else:
        recommendations.append("Give it a fair shot for a couple of weeks — consistency reveals real benefits.")

    # Restlessness
    restlessness = data['restlessness_experience']
    if restlessness in ['often', 'sometimes']:
        recommendations.append("Feeling restless is natural. Start with 2–5 minute sessions and use guided audios to stay focused.")
    else:
        recommendations.append("Great that you feel calm — you’re naturally tuned to mindfulness!")

    # Interested in hormonal meditation
    if data['interested_in_hormonal_meditation'] == 'yes':
        recommendations.append("Explore hormone-balancing Yoga Nidra or guided breathwork designed for PMS, menopause, and hormonal mood swings.")
    elif data['interested_in_hormonal_meditation'] == 'maybe':
        recommendations.append("Worth exploring — hormonal balancing meditation practices are gentle and can uplift mood and regulate cycles.")
    else:
        recommendations.append("No pressure — but keep it in mind if emotional health needs shift.")

    # Used apps
    if data['used_meditation_apps'] == 'no':
        recommendations.append("Consider beginner-friendly apps like Medito (free), Insight Timer, or Calm for guided sessions.")
    elif data['used_meditation_apps'] == 'planning':
        recommendations.append("Awesome — start with a few 5-minute guided sessions for focus or stress relief.")
    else:
        recommendations.append("Great that you’re using apps — track your streak and progress!")

     # App recommendations
    app_suggestions = [
        "📱 **Medito** (Free, beginner-friendly guided meditations)",
        "📱 **Insight Timer** (Huge library, free meditations by category)",
        "📱 **Smiling Mind** (Great for emotional well-being and stress management)"
    ]
    recommendations.append("💡 Helpful apps to try:")
    recommendations.extend(app_suggestions)

    # Joining women’s circle
    join_circle = data['join_womens_circle']
    if join_circle in ['yes_virtual', 'yes_in_person']:
        recommendations.append("Joining a women’s meditation circle can offer emotional support and create a nurturing, understanding space.")
    elif join_circle == 'maybe':
        recommendations.append("Stay open — connecting with like-minded women can be a wonderful boost to your emotional wellness journey.")

    # Awareness of benefits
    if data['aware_of_mindful_benefits'] == 'no':
        recommendations.append("Even 5–10 minutes of mindful breathing a day improves anxiety, mood, sleep, and menstrual discomfort. Science-backed and easy to start!")

    # Final motivation
    recommendations.append("✨ Remember: Meditation isn’t about emptying your mind, but gently returning to your breath when thoughts wander.")

    return render(request, 'main/meditation_results.html', {
        'data': data,
        'recommendations': recommendations,
        'resources': resources
    })

def disorders_questionsview(request):
    if request.method == 'POST':
        disorders_form = MentalHealthDisordersForm(request.POST)
        if disorders_form.is_valid():
            choice = disorders_form.cleaned_data['prolonged_sadness']
            return redirect(f'/disorders_questions#{choice}')   
    else:
        disorders_form = MentalHealthDisordersForm()
    return render(request, 'main/disorders_questions.html', {'disorders_form': disorders_form})

def peace_questionsview(request):
    if request.method == 'POST':
        peace_form = InnerPeaceForm(request.POST)
        if peace_form.is_valid():
            choice = peace_form.cleaned_data['recognizing_signs']
            return redirect(f'/peace_questions#{choice}')   
    else:
        peace_form = InnerPeaceForm()
    return render(request, 'main/peace_questions.html', {'peace_form': peace_form})

def goal_questionsview(request):
    if request.method == 'POST':
        goal_form = GoalSettingForm(request.POST)
        if goal_form.is_valid():
            choice = goal_form.cleaned_data['prolonged_sadness']
            return redirect(f'/goal_questions#{choice}')   
    else:
        goal_form = GoalSettingForm()
    return render(request, 'main/goal_questions.html', {'goal_form': goal_form})

def nature_questionsview(request):
    if request.method == 'POST':
        nature_form = NatureForm(request.POST)
        if nature_form.is_valid():
            choice = nature_form.cleaned_data['prolonged_sadness']
            return redirect(f'/nature_questions#{choice}')   
    else:
        nature_form = NatureForm()
    return render(request, 'main/nature_questions.html', {'nature_form': nature_form})

def practices_questionsview(request):
    if request.method == 'POST':
        practices_form = SpiritualityForm(request.POST)
        if practices_form.is_valid():
            choice = practices_form.cleaned_data['prolonged_sadness']
            return redirect(f'/practices_questions#{choice}')   
    else:
        practices_form = SpiritualityForm()
    return render(request, 'main/practices_questions.html', {'practices_form': practices_form})

def diet_questionsview(request):
    if request.method == 'POST':
        diet_form = BalancedDietForm(request.POST)
        if diet_form.is_valid():
            choice = diet_form.cleaned_data['prolonged_sadness']
            return redirect(f'/diet_questions#{choice}')   
    else:
        diet_form = BalancedDietForm()
    return render(request, 'main/diet_questions.html', {'diet_form': diet_form})

def foods_questionsview(request):
    if request.method == 'POST':
        foods_form = SuperfoodsForm(request.POST)
        if foods_form.is_valid():
            choice = foods_form.cleaned_data['prolonged_sadness']
            return redirect(f'/foods_questions#{choice}')   
    else:
        foods_form = SuperfoodsForm()
    return render(request, 'main/foods_questions.html', {'foods_form': foods_form})

def eatinghabits_questionsview(request):
    if request.method == 'POST':
        eatinghabits_form = MindfulEatingForm(request.POST)
        if eatinghabits_form.is_valid():
            choice = eatinghabits_form.cleaned_data['prolonged_sadness']
            return redirect(f'/eatinghabits_questions#{choice}')   
    else:
        eatinghabits_form = MindfulEatingForm()
    return render(request, 'main/eatinghabits_questions.html', {'eatinghabits_form': eatinghabits_form})

def selfcare_questionsview(request):
    if request.method == 'POST':
        selfcare_form = SelfCareForm(request.POST)
        if selfcare_form.is_valid():
            choice = selfcare_form.cleaned_data['prolonged_sadness']
            return redirect(f'/selfcare_questions#{choice}')   
    else:
        selfcare_form = SelfCareForm()
    return render(request, 'main/selfcare_questions.html', {'selfcare_form': selfcare_form})

def education_page(request):
    if request.method == 'POST':
        education_form = EducationSurveyForm(request.POST)
        if education_form.is_valid():
            choice = education_form.cleaned_data['preferred_education_field']
            if choice == 'information_technology':
                return redirect('/it_questions')
            elif choice == 'business':
                return redirect('/business_questions')
            elif choice == 'healthcare_wellness':
                return redirect('/healthcare_wellness_questions')
            elif choice == 'art_design':
                return redirect('/art_design_questions')
            elif choice == 'education_teaching':
                return redirect('/education_teaching_questions')
            elif choice == 'personal_development':
                return redirect('/personal_development_questions')
            else:
                return redirect('/education_page')

            # Redirect to corresponding section on health1 page
           # return redirect(f'/education_page#{choice}'   
    else:
        education_form = EducationSurveyForm()

    return render(request, 'main/education_page.html', 
                  {'education_form': education_form,
                  })
def it_questionsview(request):
    if request.method == 'POST':
        it_form = ITForm(request.POST)
        if it_form.is_valid():
            request.session['it_data'] = it_form.cleaned_data
            return redirect('it_results')   
    else:
        it_form = ITForm()
    return render(request, 'main/it_questions.html', {'it_form': it_form})

def it_results(request):
    data = request.session.get('it_data', None)
    if not data:
        return redirect('it_questionsview')  # fallback if accessed directly

    recommendations = []
    resources = []

    skills_to_learn = data.get('it_skills_to_learn', [])
    tried_learning = data.get('tried_learning_online')
    interested_job = data.get('interested_in_it_job')
    preferred_platform = data.get('preferred_learning_platform')
    want_roadmap = data.get('it_skill_roadmap_interest')

    # --- Skill-specific suggestions ---
    if 'basic_computer_skills' in skills_to_learn:
        recommendations.append("💻 Start with fundamentals like MS Office, email, and internet browsing.")
        resources.append('<a href="https://www.youtube.com/watch?v=5k-N_2b9tjQ" target="_blank">Basic Computer Skills Tutorial</a>')
        recommendations.append("Practice typing using free tools like TypingClub or Ratatype.")

    if 'graphic_design' in skills_to_learn:
        recommendations.append("🎨 Learn Canva for easy design, then explore Adobe Photoshop and Illustrator basics.")
        resources.append('<a href="https://www.youtube.com/watch?v=K1s6V4yjsPk" target="_blank">Photoshop Beginner Tutorial</a>')
        resources.append('<a href="https://www.canva.com/" target="_blank">Canva Online Design Tool</a>')

    if 'web_development' in skills_to_learn:
        recommendations.append("🌐 Start with HTML, CSS, and JavaScript basics.")
        recommendations.append("Build simple projects like personal websites or portfolios.")
        resources.append('<a href="https://www.freecodecamp.org/learn/" target="_blank">FreeCodeCamp Web Development</a>')
        resources.append('<a href="https://www.youtube.com/watch?v=UB1O30fR-EE" target="_blank">HTML Full Course for Beginners</a>')

    if 'mobile_app_development' in skills_to_learn:
        recommendations.append("📱 Explore app development with beginner-friendly platforms like MIT App Inventor or Flutter.")
        recommendations.append("Try building simple apps focusing on practical use cases.")
        resources.append('<a href="https://appinventor.mit.edu/" target="_blank">MIT App Inventor</a>')
        resources.append('<a href="https://flutter.dev/docs/get-started/install" target="_blank">Flutter Installation Guide</a>')

    if 'social_media_marketing' in skills_to_learn:
        recommendations.append("📢 Learn about content creation, analytics, and ads on platforms like Facebook and Instagram.")
        recommendations.append("Understand target audiences and scheduling tools like Buffer or Hootsuite.")
        resources.append('<a href="https://www.youtube.com/watch?v=3V3G1lPl-84" target="_blank">Social Media Marketing for Beginners</a>')
        resources.append('<a href="https://buffer.com/" target="_blank">Buffer Social Media Scheduler</a>')

    if 'data_entry' in skills_to_learn:
        recommendations.append("🗂️ Practice accuracy and speed with tools like Microsoft Excel and Google Sheets.")
        recommendations.append("Learn keyboard shortcuts and basic formulas for efficiency.")
        resources.append('<a href="https://www.youtube.com/watch?v=FtjE8jJfs9I" target="_blank">Excel for Beginners</a>')

    if 'cybersecurity_basics' in skills_to_learn:
        recommendations.append("🔒 Understand fundamental cybersecurity concepts and safe internet practices.")
        recommendations.append("Explore beginner courses on network security and password management.")
        resources.append('<a href="https://www.cybrary.it/course/introduction-to-it-and-cybersecurity/" target="_blank">Intro to Cybersecurity - Cybrary</a>')
        resources.append('<a href="https://www.youtube.com/watch?v=O6xx6hfcEjQ" target="_blank">Cybersecurity Basics</a>')

    if 'none' in skills_to_learn or len(skills_to_learn) == 0:
        recommendations.append("💡 Consider exploring some basic IT skills; they open many opportunities.")
        recommendations.append("Start with free tutorials and see what sparks your interest.")

    # --- Learning experience ---
    if tried_learning == 'yes':
        recommendations.append("👍 Great! Keep building consistency and set small goals for each learning session.")
    else:
        recommendations.append("🚀 Start with beginner-friendly platforms like YouTube or free apps to ease into IT learning.")

    # --- Interest in IT job from home ---
    if interested_job == 'yes':
        recommendations.append("🏠 Working from home in IT is possible! Skills like data entry, content moderation, and web development are in demand.")
        recommendations.append("Try freelancing platforms like Upwork or Fiverr to find projects.")
        resources.append('<a href="https://www.upwork.com/" target="_blank">Upwork Freelance Platform</a>')
        resources.append('<a href="https://www.fiverr.com/" target="_blank">Fiverr Freelance Platform</a>')
    elif interested_job == 'maybe':
        recommendations.append("🤔 Explore part-time or freelance IT gigs to understand what fits your schedule and interests.")
    else:
        recommendations.append("🔍 IT skills can be useful for personal projects, family, or community help even if you don't want a job.")

    # --- Preferred learning platform ---
    if preferred_platform == 'youtube_tutorials':
        recommendations.append("📺 YouTube has lots of free tutorials – subscribe to channels like FreeCodeCamp, The Net Ninja, or Simplilearn.")
        resources.append('<a href="https://www.youtube.com/c/Freecodecamp" target="_blank">FreeCodeCamp YouTube Channel</a>')
        resources.append('<a href="https://www.youtube.com/c/TheNetNinja" target="_blank">The Net Ninja YouTube Channel</a>')
    elif preferred_platform == 'online_course_apps':
        recommendations.append("🎓 Platforms like Coursera and Udemy offer structured courses with certificates.")
        resources.append('<a href="https://www.coursera.org/" target="_blank">Coursera</a>')
        resources.append('<a href="https://www.udemy.com/" target="_blank">Udemy</a>')
    elif preferred_platform == 'community_workshops':
        recommendations.append("👩‍💻 Community workshops are great for hands-on learning and networking. Check local NGOs or libraries.")
    else:
        recommendations.append("💡 Try mixing different platforms to find what works best for you.")

    # --- Roadmap interest ---
    if want_roadmap == 'yes':
        recommendations.append("🗺️ We'll send you a beginner-friendly IT skill roadmap to your email with step-by-step milestones.")
    else:
        recommendations.append("🔔 Feel free to ask anytime if you want a personalized roadmap later.")

    context = {
        'recommendations': recommendations,
        'resources': resources,
    }

    return render(request, 'main/it_results.html', context)

def business_questionsview(request):
    if request.method == 'POST':
        business_form = BusinessForm(request.POST)
        if business_form.is_valid():
            choice = business_form.cleaned_data['prolonged_sadness']
            return redirect(f'/business_questions#{choice}')   
    else:
        business_form = BusinessForm()
    return render(request, 'main/business_questions.html', {'business_form': business_form})

def healthcare_wellness_questionsview(request):
    if request.method == 'POST':
        healthcare_wellness_form = HealthcareWellnessForm(request.POST)
        if healthcare_wellness_form.is_valid():
            choice = healthcare_wellness_form.cleaned_data['prolonged_sadness']
            return redirect(f'/healthcare_wellness_questions#{choice}')   
    else:
        healthcare_wellness_form = HealthcareWellnessForm()
    return render(request, 'main/healthcare_wellness_questions.html', {'healthcare_wellness_form': healthcare_wellness_form})

def art_design_questionsview(request):
    if request.method == 'POST':
        art_design_form = ArtDesignForm(request.POST)
        if art_design_form.is_valid():
            request.session['art_design_data'] = art_design_form.cleaned_data
            return redirect('artndesign_results')  
    else:
        art_design_form = ArtDesignForm()
    return render(request, 'main/art_design_questions.html', {'art_design_form': art_design_form})

def artndesign_results(request):
    data = request.session.get('art_design_data', None)
    if not data:
        return redirect('art_design_questionsview')  # fallback if accessed directly

    recommendations = []
    resources = []

    interests = data.get('creative_skills_interest', [])
    sell_online = data.get('sell_creative_work_online')
    learn_graphic_video = data.get('learn_graphic_video_editing')
    join_community = data.get('art_community_participation')
    learning_pref = data.get('art_learning_preference')

    # === Interest-based detailed suggestions ===
    if 'drawing_painting' in interests:
        recommendations.append("🎨 Join sketch challenges like #Inktober or #DrawThisInYourStyle on Instagram to improve skills and connect with artists.")
        recommendations.append("Use apps like Procreate (iPad) or Krita (free desktop) to explore digital painting.")
        resources.append('<a href="https://www.youtube.com/watch?v=2VHZei2PpTo" target="_blank">Watercolor Techniques for Beginners</a>')
        resources.append('<a href="https://procreate.art/" target="_blank">Procreate App for Digital Painting</a>')

    if 'fashion_design' in interests:
        recommendations.append("👗 Practice sketching your own clothing designs and create mood boards on Pinterest.")
        recommendations.append("Try online pattern-making tools like Valentina or watch sewing tutorials to bring ideas to life.")
        resources.append('<a href="https://www.youtube.com/watch?v=0gW9QVoAAI8" target="_blank">Learn Fashion Illustration Basics</a>')
        resources.append('<a href="https://valentina-project.org/" target="_blank">Valentina Open-Source Pattern Design Software</a>')

    if 'craft_making' in interests:
        recommendations.append("✂️ Explore Etsy tutorials for popular handmade crafts and try selling your crafts locally or online.")
        recommendations.append("Participate in craft fairs or local maker markets to build connections.")
        resources.append('<a href="https://www.youtube.com/watch?v=PiCmgPpXLZ0" target="_blank">Easy DIY Craft Ideas for Beginners</a>')

    if 'jewelry_designing' in interests:
        recommendations.append("💍 Experiment with affordable DIY kits and learn wire wrapping techniques from YouTube channels like Beadaholique.")
        recommendations.append("Join Facebook groups dedicated to handmade jewelry to learn and sell.")
        resources.append('<a href="https://www.youtube.com/watch?v=LcLHFr0Q7YU" target="_blank">Wire Wrapping Jewelry Tutorial</a>')

    if 'graphic_designing' in interests:
        recommendations.append("🎨 Build your portfolio by taking daily logo or poster design challenges.")
        recommendations.append("Use Canva for quick social media graphics and advance to Adobe Illustrator or Photoshop.")
        recommendations.append("Sell templates on marketplaces like Creative Market or Etsy.")
        resources.append('<a href="https://www.youtube.com/watch?v=K1s6V4yjsPk" target="_blank">Photoshop Basics Tutorial</a>')
        resources.append('<a href="https://www.canva.com/" target="_blank">Canva Online Graphic Design Tool</a>')

    if 'photography' in interests:
        recommendations.append("📷 Practice photography using natural light and learn editing with Lightroom Mobile or Snapseed.")
        recommendations.append("Join photography contests like GuruShots for motivation.")
        resources.append('<a href="https://www.youtube.com/watch?v=WE27xjhCjO0" target="_blank">Mobile Photography Masterclass</a>')

    if 'content_creation' in interests:
        recommendations.append("📱 Start a content series on Instagram Reels or YouTube Shorts focusing on your art journey or tutorials.")
        recommendations.append("Use free tools like Canva and CapCut for editing content.")
        resources.append('<a href="https://www.youtube.com/watch?v=7WUudHWH1Qk" target="_blank">Content Creation Tips for Beginners</a>')
        resources.append('<a href="https://www.canva.com/" target="_blank">Canva for Content Creators</a>')
        resources.append('<a href="https://www.capcut.com/" target="_blank">CapCut Video Editor</a>')

    # === Selling creative work online ===
    if sell_online == 'yes':
        recommendations.append("🛍️ Open shops on platforms like Etsy, Redbubble, or Meesho to monetize your creations.")
        recommendations.append("Leverage Instagram Shops and Facebook Marketplace to reach local customers.")
        recommendations.append("Optimize your listings with good photos and SEO-friendly descriptions.")
        resources.append('<a href="https://www.youtube.com/watch?v=YB6v93WxK94" target="_blank">How to Sell Handmade Products Online</a>')
        resources.append('<a href="https://www.etsy.com/sell" target="_blank">Start Selling on Etsy</a>')

    elif sell_online == 'not_sure':
        recommendations.append("🤔 Explore success stories of women turning hobbies into businesses to get inspired.")
        recommendations.append("Try small-scale sales with friends and family before scaling up.")
        resources.append('<a href="https://www.youtube.com/watch?v=8NYW3v7FfNY" target="_blank">Hobby to Business Stories</a>')

    else:
        recommendations.append("💡 Even if you don't want to sell now, sharing your art on social media can build an audience for the future.")

    # === Learning preferences ===
    if learning_pref == 'youtube_tutorials':
        recommendations.append("📺 Follow curated beginner-friendly art and design playlists on YouTube.")
        resources.append('<a href="https://www.youtube.com/c/SkillshareArt" target="_blank">Skillshare Art Playlist</a>')
        resources.append('<a href="https://www.youtube.com/c/TheArtSherpa" target="_blank">The Art Sherpa - Acrylic Painting Tutorials</a>')

    elif learning_pref == 'free_online_courses':
        recommendations.append("🎓 Enroll in free courses on Coursera, Udemy free offerings, or Skillshare free trials.")
        resources.append('<a href="https://www.coursera.org/specializations/graphic-design" target="_blank">Graphic Design Specialization - CalArts</a>')
        resources.append('<a href="https://www.udemy.com/courses/search/?q=free%20art%20design" target="_blank">Free Art & Design Courses on Udemy</a>')

    elif learning_pref == 'paid_certification_programs':
        recommendations.append("📜 Invest in premium classes on Domestika or Skillshare for specialized certifications and mentorship.")
        resources.append('<a href="https://www.domestika.org/en/courses/category/7-art" target="_blank">Domestika Art Courses</a>')

    elif learning_pref == 'offline_classes':
        recommendations.append("🎨 Look for weekend or evening art workshops at local community centers or NGOs.")
        recommendations.append("Join group painting or craft sessions for hands-on learning and networking.")

    # === Art community participation ===
    if join_community == 'yes':
        recommendations.append("🌐 Join Facebook groups like 'Women Art Collective', Behance, and Dribbble to showcase work and gain feedback.")
        recommendations.append("Participate in online art challenges and virtual exhibitions.")
        resources.append('<a href="https://www.behance.net/" target="_blank">Behance Portfolio Platform</a>')
        resources.append('<a href="https://dribbble.com/" target="_blank">Dribbble Design Community</a>')

    elif join_community == 'no' and 'graphic_designing' in interests:
        recommendations.append("Even without active participation, submit designs anonymously on Dribbble or Pinterest to get feedback and stay motivated.")

    else:
        recommendations.append("Consider attending occasional art meetups or online webinars to stay inspired without heavy commitment.")

    context = {
        'recommendations': recommendations,
        'resources': resources,
    }

    return render(request, 'main/artndesign_results.html', context)

def education_teaching_questionsview(request):
    if request.method == 'POST':
        education_teaching_form = EducationTeachingForm(request.POST)
        if education_teaching_form.is_valid():
            choice = education_teaching_form.cleaned_data['prolonged_sadness']
            return redirect(f'/education_teaching_questions#{choice}')   
    else:
        education_teaching_form = EducationTeachingForm()
    return render(request, 'main/education_teaching_questions.html', {'education_teaching_form': education_teaching_form})

def personal_development_questionsview(request):
    if request.method == 'POST':
        personal_development_form = PersonalDevelopmentForm(request.POST)
        if personal_development_form.is_valid():
            choice = personal_development_form.cleaned_data['prolonged_sadness']
            return redirect(f'/personal_development_questions#{choice}')   
    else:
        personal_development_form = PersonalDevelopmentForm()
    return render(request, 'main/personal_development_questions.html', {'personal_development_form': personal_development_form})

def job_page(request):
    job_form = JobSearchForm()
    return render(request, 'main/job_page.html', {'job_form': job_form})

def apply_now_view(request):
    return render(request, 'main/apply_now_page.html')

def browse_jobs_view(request):
    return render(request, 'main/browse_jobs_page.html')

def empjob_page(request):
    emp_job_form = CandidateSearchForm()
    return render(request, 'main/empjob_page.html', {'emp_job_form': emp_job_form})

def post_job_view(request):
    return render(request, 'main/post_job_page.html')

def browse_candidates_view(request):
    return render(request, 'main/browse_candidates_page.html')

def post_job_view(request):
    if request.method == 'POST':
        jobtitle = request.POST.get('jobtitle')
        jobcategory = request.POST.get('jobcategory')
        jobtype = request.POST.get('jobtype')
        salary = request.POST.get('salary')
        jobdesc = request.POST.get('jobdesc')
        deadline = request.POST.get('deadline')
        compname = request.POST.get('compname')
        companytype = request.POST.get('companytype')
        desc = request.POST.get('desc')
        city = request.POST.get('city')
        email = request.POST.get('email')
        terms = request.POST.get('terms')

        # Check if email already exists for duplicate handling (optional)
        if JobPost.objects.filter(email=email, jobtitle=jobtitle).exists():
            email_error = "A job with this email and title already exists."
            return render(request, 'main/post_job_page.html', {'email_error': email_error})

        # Handle file upload
        if 'profilepic' in request.FILES:
            profilepic = request.FILES['profilepic']
            #fs = FileSystemStorage()
            #filename = fs.save(profilepic.name, profilepic)
            #uploaded_file_url = fs.url(filename)
        else:
            profilepic = None

        # Save to database
        job = JobPost(
            jobtitle=jobtitle,
            jobcategory=jobcategory,
            jobtype=jobtype,
            salary=salary,
            jobdesc=jobdesc,
            deadline=deadline,
            compname=compname,
            companytype=companytype,
            logo=profilepic,
            description=desc,
            city=city,
            email=email
        )
        job.save()

        messages.success(request, 'Job posted successfully!')
        return redirect('browse_jobs_page')  # redirect to your job listings page or another confirmation page

    return render(request, 'main/post_job_page.html')

def browse_jobs_view(request):
    jobs = JobPost.objects.all().order_by('-posted_on')
    form = JobSearchForm(request.GET or None)

    if form.is_valid():
        keyword = form.cleaned_data.get('keyword')
        location = form.cleaned_data.get('location')
        category = form.cleaned_data.get('category')

        if keyword:
            jobs = jobs.filter(jobtitle__icontains=keyword)
        if location:
            jobs = jobs.filter(city__icontains=location)
        if category:
            jobs = jobs.filter(jobcategory=category)

    return render(request, 'main/browse_jobs_page.html', {'jobs': jobs, 'form': form})

def job_detail_view(request, job_id):
    job = get_object_or_404(JobPost, id=job_id)
    return render(request, 'main/job_detail_page.html', {'job': job})

def apply_now_view(request):
    if request.method == 'POST':
        full_name = request.POST.get("full_name")
        email = request.POST.get("email")
        birth_day = request.POST.get("date_of_birth")
        birth_month = request.POST.get("birth_month")
        birth_year = request.POST.get("birth_year")
        profilepic = request.FILES.get("profilepic")
        resume = request.FILES.get("resume")
        city = request.POST.get("city")
        occupation = request.POST.get("occupation")
        education_level = request.POST.get("education_level")
        skills = request.POST.get("skills")
        position = request.POST.get("position")
        experience = request.POST.get("experience")
        terms = request.POST.get("terms")

        # Mandatory field checks
        if not full_name or not email or not birth_day or not birth_month or not birth_year:
            messages.error(request, "Please complete all personal details.")
            return redirect("apply_now_page")

        if not city or not occupation or not education_level or not skills or not position or not experience:
            messages.error(request, "Please fill in all required fields.")
            return redirect("apply_now_page")

        if not terms:
            messages.error(request, "You must agree to the Terms & Conditions.")
            return redirect("apply_now_page")

        # Email validation (like signup)
        if not re.match(r"^[\w\.-]+@gmail\.com$", email):
            messages.error(request, "Email must be in xyz@gmail.com format.")
            return redirect("apply_now_page")

        try:
            # Convert birth date parts
            birth_day = int(birth_day)
            birth_month_num = get_month_number(birth_month)
            birth_year = int(birth_year)
            date_of_birth = date(birth_year, birth_month_num, birth_day)

            # Create Application
            applications = JobApplication.objects.create(
                full_name=full_name,
                email=email,
                date_of_birth=date_of_birth,
                profilepic=profilepic,
                resume=resume,
                city=city,
                occupation=occupation,
                education_level=education_level,
                skills=skills,
                position=position,
                experience=experience
            )

            messages.success(request, "Application submitted successfully!")
            return redirect("browse_candidates_page")

        except IntegrityError:
            messages.error(request, "An error occurred while submitting your application.")
            return redirect("apply_now_page")

    return render(request, "main/apply_now_page.html")

def browse_candidates_page(request):
    applications = JobApplication.all()  # using related_name='applications'
    return render(request, 'main/browse_candidates_page.html', {'applications': applications})



