# main/forms.py

from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile
from .models import EmployerProfile

from .models import Comment
from .models import Reply

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']
        widgets = {
            'content': forms.Textarea(attrs={'rows': 3, 'placeholder': 'Enter your comment...',
            'style': 'width: 100%; max-width: 800px;'}),
        }
        labels = {
            'content': ''
        }

class ReplyForm(forms.ModelForm):
    class Meta:
        model = Reply
        fields = ['content']
        widgets = {
            'content': forms.Textarea(attrs={
                'rows': 2,
                'placeholder': 'Write your reply...',
                'style': 'width: 100%;'
            }),
        }
class RegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

EDUCATION_LEVEL_CHOICES = [
    ('', '-- Select --'),
    ('No formal education', 'No formal education'),
    ('Primary', 'Primary'),
    ('Secondary', 'Secondary'),
    ('College/University', 'College/University'),
    ('Vocational', 'Vocational'),
    ('Others', 'Others'),
]
OCCUPATION_CHOICES = [
    ('', '-- Select --'),
    ('student', 'Student'),
    ('homemaker', 'Homemaker'),
    ('others', 'Others'),
]
INTEREST_CHOICES = [
    ('', '-- Select --'),
    ('Health & Wellness', 'Health & Wellness'),
    ('Education & Learning', 'Education & Learning'),
    ('Career & Jobs', 'Career & Jobs'),
    ('Entrepreneurship', 'Entrepreneurship'),
    ('Personal Growth', 'Personal Growth'),
    ('Community Support', 'Community Support'),
]
GOAL_CHOICES = [
    ('', '-- Select --'),
    ('Learn new skills', 'Learn new skills'),
    ('Find a job', 'Find a job'),
    ('Start a business', 'Start a business'),
    ('Join support communities', 'Join support communities'),
    ('Get health or legal advice', 'Get health or legal advice'),
    ('Others', 'Others'),
]
COMPANY_TYPE_CHOICES = [
    ("", "-- Select --"),
    ("privatecompany", "Private Company"),
    ("startup", "Startup"),
    ("ngo", "NGO"),
    ("recruiter", "Individual Recruiter"),
]

class ProfileUpdateForm(forms.ModelForm):
    education_level = forms.ChoiceField(
        choices=EDUCATION_LEVEL_CHOICES,
        widget=forms.Select(attrs={'class': 'form-control'}),
        required=True
    )
    occupation = forms.ChoiceField(
        choices=OCCUPATION_CHOICES,
        widget=forms.Select(attrs={'class': 'form-control'}),
        required=True
    )
    interests = forms.ChoiceField(
        choices=INTEREST_CHOICES,
        widget=forms.Select(attrs={'class': 'form-control'}),
        required=True
    )
    goals = forms.ChoiceField(
        choices=GOAL_CHOICES,
        widget=forms.Select(attrs={'class': 'form-control'}),
        required=True
    )

    class Meta:
        model = Profile
        fields = ['profilepic', 'full_name', 'bio', 'date_of_birth',
            'city', 'occupation', 'education_level', 'interests', 'goals']
        widgets = {
            'full_name': forms.TextInput(attrs={'class': 'form-control'}),
            'bio': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'date_of_birth': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'city': forms.TextInput(attrs={'class': 'form-control'})
        }

class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username','email']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control', 'readonly': 'readonly'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
        }

class EmployerProfileUpdateForm(forms.ModelForm):
    companytype = forms.ChoiceField(
    choices=COMPANY_TYPE_CHOICES,
    widget=forms.Select(attrs={'class': 'form-control'}),
    required=True
    )
    class Meta:
        model = EmployerProfile
        fields = ['profilepic','managername', 'compname', 'companytype', 'desc', 'city']
        widgets = {
            #'profilepic': forms.ClearableFileInput(attrs={'class': 'form-control mt-2'}),
            'managername': forms.TextInput(attrs={'class': 'form-control'}),
            'compname': forms.TextInput(attrs={'class': 'form-control'}),
            'desc': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'city': forms.TextInput(attrs={'class': 'form-control'}),
        }

class HealthSurveyForm(forms.Form):
    CHOICES = [
        ('physical-health', 'Physical Health'),
        ('mental-health', 'Mental Health'),
        ('spiritual-health', 'Spiritual Health'),
        ('nutrition-health', 'Nutrition & Wellness')
    ]

    concern = forms.ChoiceField(
        choices=CHOICES,
        widget=forms.RadioSelect,
        label="What aspect of your health would you like to focus on today?"
    )
class PhysicalHealthForm(forms.Form):
    CHOICES=[
        ('exercise', 'Exercise & Fitness'),
        ('hygiene', 'Personal Hygiene'),
        ('sleep', 'Sleep Health'),
        ('healthyhabits', 'Healthy Habits')
        ]
    physical_concern = forms.ChoiceField(
        choices=CHOICES,
        widget=forms.RadioSelect,
        label="What aspect of your Physical Health would you like to focus on today?"
    )
class MentalHealthForm(forms.Form):
    CHOICES=[
        ('stress', 'Stress Management'),
        ('emotions', 'Emotional Well-Being'),
        ('meditation', 'Meditation'),
        ('disorders', 'Mental Health Disorders')
        ]
    mental_concern = forms.ChoiceField(
        choices=CHOICES,
        widget=forms.RadioSelect,
        label="What aspect of your Mental Health would you like to focus on today?"
    )
class SpiritualHealthForm(forms.Form):
    CHOICES=[
        ('peace', 'Inner Peace'),
        ('goal', 'Goal Setting'),
        ('nature', 'Nature Walks'),
        ('practices', 'Spiritual Practices')
        ]
    spiritual_concern = forms.ChoiceField(
        choices=CHOICES,
        widget=forms.RadioSelect,
        label="What aspect of your Spiritual Health would you like to focus on today?"
    )
class NutritionHealthForm(forms.Form):
    CHOICES=[
        ('diet', 'Balanced Diet'),
        ('foods', 'Superfoods & Foods'),
        ('eatinghabits', 'Healthy Eating Habits'),
        ('selfcare', 'Self-Care Routines')
        ]
    nutrition_concern = forms.ChoiceField(
        choices=CHOICES,
        widget=forms.RadioSelect,
        label="What aspect of your Nutrition & Wellness would you like to focus on today?"
    )
class ExerciseForm(forms.Form):

    PHYSICAL_ACTIVITY_CHOICES = [
        ('yes', 'Yes'),
        ('no', 'No'),
    ]
    EXERCISE_FREQUENCY_CHOICES = [
        ('daily', 'Daily'),
        ('3-4_times', '3-4 times a week'),
        ('once_week', 'Once a week'),
        ('rarely', 'Rarely/Never'),
    ]
    EXERCISE_TYPE_CHOICES = [
        ('cardio', 'Cardio (running, cycling, swimming)'),
        ('strength', 'Strength training (weights, bodyweight)'),
        ('flexibility', 'Flexibility exercises (yoga, pilates, stretching)'),
        ('daily_activity', 'Daily activity (walking, chores)'),
    ]
    FITNESS_PLAN_CHOICES = [
        ('yes', 'Yes'),
        ('no', 'No'),
        ('planning', 'Planning to start soon'),
    ]
    FITNESS_GOAL_CHOICES = [
        ('weight_loss', 'Weight loss'),
        ('weight_gain', 'Weight gain'),
        ('strength', 'Build strength'),
        ('stress', 'Reduce stress'),
        ('stay_active', 'Just stay active'),
    ]
    TRACK_PROGRESS_CHOICES = [
        ('yes', 'Yes'),
        ('no', 'No'),
    ]
    WORKOUT_STYLE_CHOICES = [
        ('group', 'Group fitness sessions'),
        ('personal', 'Personal training'),
        ('solo', 'Solo workouts'),
    ]
    ALTERNATIVE_ACTIVITIES_CHOICES = [
        ('yes', 'Yes'),
        ('no', 'No'),
    ]
    STRENGTH_TRAINING_CHOICES = [
        ('never', 'Never'),
        ('sometimes', 'Sometimes'),
        ('regularly', 'Regularly'),
    ]
    MENSTRUAL_DISCOMFORT_CHOICES = [
        ('yes', 'Yes'),
        ('no', 'No'),
    ]
    # Fields
    physical_activity = forms.ChoiceField(
        label="Do you engage in any physical activity (walking, running, yoga, gym etc)?",
        choices=PHYSICAL_ACTIVITY_CHOICES,
        widget=forms.RadioSelect
    )
    workout_frequency = forms.ChoiceField(
        label="How often do you exercise?",
        choices=EXERCISE_FREQUENCY_CHOICES,
        widget=forms.RadioSelect
    )
    workout_type = forms.ChoiceField(
        label="What type of exercise do you prefer?",
        choices=EXERCISE_TYPE_CHOICES,
        widget=forms.RadioSelect
    )

    fitness_plan = forms.ChoiceField(
        label="Are you currently following any fitness routine or plan?",
        choices=FITNESS_PLAN_CHOICES,
        widget=forms.RadioSelect
    )

    fitness_goal = forms.ChoiceField(
        label="What is your primary goal with physical activity?",
        choices=FITNESS_GOAL_CHOICES,
        widget=forms.RadioSelect
    )
    track_progress = forms.ChoiceField(
        label="Do you track your fitness progress through a journal, wearable device, or app?",
        choices=TRACK_PROGRESS_CHOICES,
        widget=forms.RadioSelect
    )

    workout_style = forms.ChoiceField(
        label="Do you prefer group fitness sessions, personal training, or solo workouts?",
        choices=WORKOUT_STYLE_CHOICES,
        widget=forms.RadioSelect
    )

    alternative_activities = forms.ChoiceField(
        label="Have you explored alternative physical activities like dance, Zumba, martial arts, or trekking for fitness?",
        choices=ALTERNATIVE_ACTIVITIES_CHOICES,
        widget=forms.RadioSelect
    )
    strength_training = forms.ChoiceField(
        label="Do you include strength training (bodyweight exercises, resistance bands, or weights) in your routine? If yes, how often?",
        choices=STRENGTH_TRAINING_CHOICES,
        widget=forms.RadioSelect
    )

    menstrual_discomfort = forms.ChoiceField(
        label="Are you currently facing any menstrual-related discomforts (like cramps, bloating, fatigue) that affect your physical activity?",
        choices=MENSTRUAL_DISCOMFORT_CHOICES,
        widget=forms.RadioSelect
    )
 

class HygieneForm(forms.Form):
    SANITARY_PRODUCT_CHANGE_CHOICES = [
        ('every_4_hours', 'Every 4 hours'),
        ('every_6_hours', 'Every 6 hours'),
        ('twice_daily', 'Twice a day'),
        ('once_daily', 'Once a day'),
    ]

    CLEANING_METHOD_CHOICES = [
        ('ph_balanced_wash', 'pH-balanced intimate wash'),
        ('plain_water', 'Plain water'),
        ('both', 'Both'),
        ('none', 'None of the above'),
    ]

    REUSABLE_PRODUCT_CLEANING_CHOICES = [
        ('boiling_water', 'Sterilize with boiling water'),
        ('mild_soap_water', 'Wash with mild soap and water'),
        ('disinfectant_solution', 'Use disinfectant solution'),
        ('dont_use', 'I don’t use reusable products'),
    ]

    HAND_WASHING_CHOICES = [
        ('always', 'Always, before and after'),
        ('only_after', 'Only after'),
        ('rarely', 'Rarely'),
    ]

    HAIR_WASH_FREQUENCY_CHOICES = [
        ('daily', 'Daily'),
        ('alternate_days', 'Every alternate day'),
        ('twice_week', 'Twice a week'),
        ('weekly', 'Once a week'),
    ]

    UNDERGARMENT_HABITS_CHOICES = [
        ('always_fresh', 'Yes, fresh daily and breathable fabrics'),
        ('sometimes_skip', 'Sometimes skip or wear tight/synthetic fabrics'),
        ('rarely_care', 'Rarely care about it'),
    ]

    GYNE_VISIT_FREQUENCY_CHOICES = [
        ('every_6_months', 'Every 6 months'),
        ('yearly', 'Yearly'),
        ('only_when_symptoms', 'Only when symptoms appear'),
        ('never', 'Never'),
    ]

    INFECTION_AWARENESS_CHOICES = [
        ('yes', 'Yes'),
        ('no', 'No'),
    ]

    GROOMING_TOOL_HYGIENE_CHOICES = [
        ('always_sterilize', 'Yes, always before use'),
        ('sometimes', 'Sometimes'),
        ('never', 'Never'),
    ]

    ITEM_REPLACEMENT_FREQUENCY_CHOICES = [
        ('monthly', 'Monthly'),
        ('every_3_months', 'Every 3 months'),
        ('rarely', 'Rarely/Only when visibly worn out'),
    ]

    # Fields

    sanitary_product_change = forms.ChoiceField(
        label="How often do you change sanitary pads/tampons/menstrual cups during your period?",
        choices=SANITARY_PRODUCT_CHANGE_CHOICES,
        widget=forms.RadioSelect
    )

    cleaning_method = forms.ChoiceField(
        label="Do you use pH-balanced intimate wash or plain water for cleaning your intimate area?",
        choices=CLEANING_METHOD_CHOICES,
        widget=forms.RadioSelect
    )

    reusable_product_cleaning = forms.ChoiceField(
        label="How do you clean reusable menstrual products like cups or cloth pads?",
        choices=REUSABLE_PRODUCT_CLEANING_CHOICES,
        widget=forms.RadioSelect
    )

    hand_washing = forms.ChoiceField(
        label="Do you wash your hands before and after using the restroom or changing sanitary products?",
        choices=HAND_WASHING_CHOICES,
        widget=forms.RadioSelect
    )

    hair_wash_frequency = forms.ChoiceField(
        label="How frequently do you wash your hair based on your scalp type and activity levels?",
        choices=HAIR_WASH_FREQUENCY_CHOICES,
        widget=forms.RadioSelect
    )

    undergarment_habits = forms.ChoiceField(
        label="Do you wear fresh undergarments every day and avoid tight or synthetic fabrics?",
        choices=UNDERGARMENT_HABITS_CHOICES,
        widget=forms.RadioSelect
    )

    gyne_visit_frequency = forms.ChoiceField(
        label="How often do you visit a gynecologist for routine check-ups, regardless of symptoms?",
        choices=GYNE_VISIT_FREQUENCY_CHOICES,
        widget=forms.RadioSelect
    )

    infection_awareness = forms.ChoiceField(
        label="Are you aware of the early signs of vaginal infections (unusual discharge, itching, burning)?",
        choices=INFECTION_AWARENESS_CHOICES,
        widget=forms.RadioSelect
    )

    grooming_tool_hygiene = forms.ChoiceField(
        label="Do you sterilize grooming tools (like razors, nail cutters) before use?",
        choices=GROOMING_TOOL_HYGIENE_CHOICES,
        widget=forms.RadioSelect
    )

    item_replacement_frequency = forms.ChoiceField(
        label="How often do you replace personal hygiene items like toothbrushes, loofahs, or towels?",
        choices=ITEM_REPLACEMENT_FREQUENCY_CHOICES,
        widget=forms.RadioSelect
    )
class SleepForm(forms.Form):

    SLEEP_HOURS_CHOICES = [
        ('less_than_4', 'Less than 4 hours'),
        ('4_6', '4-6 hours'),
        ('6_8', '6-8 hours'),
        ('8_plus', 'More than 8 hours'),
    ]

    CONSISTENT_SCHEDULE_CHOICES = [
        ('yes', 'Yes, regularly'),
        ('sometimes', 'Sometimes'),
        ('no', 'No, not really'),
    ]

    CONSUMPTION_BEFORE_BED_CHOICES = [
        ('never', 'Never'),
        ('rarely', 'Rarely'),
        ('sometimes', 'Sometimes'),
        ('often', 'Often'),
    ]

    SLEEP_DIFFICULTY_CHOICES = [
        ('falling_asleep', 'Falling asleep'),
        ('staying_asleep', 'Staying asleep'),
        ('waking_early', 'Waking up too early'),
        ('none', 'No issues'),
    ]

    FREQUENCY_CHOICES = [
        ('never', 'Never'),
        ('rarely', 'Rarely'),
        ('sometimes', 'Sometimes'),
        ('often', 'Often'),
        ('always', 'Always'),
    ]

    STRESS_SLEEP_CHOICES = FREQUENCY_CHOICES

    NIGHT_SWEATS_CHOICES = [
        ('yes', 'Yes'),
        ('no', 'No'),
        ('sometimes', 'Sometimes'),
    ]

    RELAXATION_TECHNIQUES_AWARENESS_CHOICES = [
        ('yes', 'Yes, I’m aware and practice them'),
        ('aware_no_practice', 'I’m aware but don’t practice'),
        ('no', 'No, I’m not aware'),
    ]

    PROFESSIONAL_HELP_CHOICES = [
        ('yes', 'Yes'),
        ('no', 'No'),
        ('planning', 'Planning to seek help'),
    ]

    sleep_hours = forms.ChoiceField(
        label="On average, how many hours of sleep do you usually get per night?",
        choices=SLEEP_HOURS_CHOICES,
        widget=forms.RadioSelect
    )

    consistent_schedule = forms.ChoiceField(
        label="Do you follow a consistent sleep schedule (like limiting screen time, relaxation techniques)?",
        choices=CONSISTENT_SCHEDULE_CHOICES,
        widget=forms.RadioSelect
    )

    consumption_before_bed = forms.ChoiceField(
        label="Do you consume caffeine, alcohol, or heavy meals before bedtime?",
        choices=CONSUMPTION_BEFORE_BED_CHOICES,
        widget=forms.RadioSelect
    )

    sleep_difficulty = forms.ChoiceField(
        label="Do you struggle with falling asleep, staying asleep, or waking up too early?",
        choices=SLEEP_DIFFICULTY_CHOICES,
        widget=forms.RadioSelect
    )

    frequency_difficulty = forms.ChoiceField(
        label="How often does this happen?",
        choices=FREQUENCY_CHOICES,
        widget=forms.RadioSelect
    )

    stress_sleep = forms.ChoiceField(
        label="How often do stress or anxiety about family, work, or personal issues interfere with your sleep?",
        choices=STRESS_SLEEP_CHOICES,
        widget=forms.RadioSelect
    )

    night_sweats = forms.ChoiceField(
        label="Have you ever experienced night sweats or hot flashes that disrupt your sleep?",
        choices=NIGHT_SWEATS_CHOICES,
        widget=forms.RadioSelect
    )

    relaxation_techniques_awareness = forms.ChoiceField(
        label="Are you aware of relaxation techniques such as deep breathing, progressive muscle relaxation, or meditation for improving sleep quality?",
        choices=RELAXATION_TECHNIQUES_AWARENESS_CHOICES,
        widget=forms.RadioSelect
    )

    professional_help = forms.ChoiceField(
        label="Have you ever sought professional help or therapy for persistent sleep issues?",
        choices=PROFESSIONAL_HELP_CHOICES,
        widget=forms.RadioSelect
    )

class HealthyHabitsForm(forms.Form):
    WATER_INTAKE_CHOICES = [
        ('yes_plain', 'Yes, plain water'),
        ('yes_infused', 'Yes, infused with lemon/mint etc.'),
        ('no', 'No, not regularly'),
    ]

    DIET_BALANCE_CHOICES = [
        ('very_balanced', 'Very balanced'),
        ('moderately_balanced', 'Moderately balanced'),
        ('needs_improvement', 'Needs improvement'),
    ]

    FOOD_LABEL_CHECK_CHOICES = [
        ('always', 'Always'),
        ('sometimes', 'Sometimes'),
        ('never', 'Never'),
    ]

    EMOTIONAL_EATING_CHOICES = [
        ('often', 'Often'),
        ('sometimes', 'Sometimes'),
        ('rarely_never', 'Rarely/Never'),
    ]

    IRON_FOODS_FREQUENCY_CHOICES = [
        ('daily', 'Daily'),
        ('3_4_times_week', '3-4 times a week'),
        ('rarely', 'Rarely'),
    ]

    STRESS_MANAGEMENT_CHOICES = [
        ('yes_regularly', 'Yes, regularly'),
        ('occasionally', 'Occasionally'),
        ('never', 'Never'),
    ]

    GUT_HEALTH_CHOICES = [
        ('yes_regularly', 'Yes, regularly'),
        ('sometimes', 'Sometimes'),
        ('unaware', 'I wasn’t aware'),
    ]

    DIGITAL_DETOX_CHOICES = [
        ('daily', 'Daily'),
        ('weekly', 'Weekly'),
        ('never', 'Never'),
    ]

    PERSONAL_GOALS_CHOICES = [
        ('yes_set', 'Yes, already set goals'),
        ('planning_to_set', 'Planning to set soon'),
        ('no_goals', 'No goals yet'),
    ]

    COMFORT_DISCUSS_HEALTH_CHOICES = [
        ('yes_doctor', 'Yes, with doctor'),
        ('yes_friend', 'Yes, with a friend/family'),
        ('yes_wellness_counselor', 'Yes, with a wellness counselor'),
        ('hesitant', 'Hesitant/Uncomfortable'),
    ]

    # Fields

    water_intake = forms.ChoiceField(
        label="Do you start your day with drinking water (plain or infused)?",
        choices=WATER_INTAKE_CHOICES,
        widget=forms.RadioSelect
    )

    diet_balance = forms.ChoiceField(
        label="How balanced is your daily diet in terms of proteins, vitamins, fiber, and good fats?",
        choices=DIET_BALANCE_CHOICES,
        widget=forms.RadioSelect
    )

    food_label_check = forms.ChoiceField(
        label="Do you regularly check food labels for sugar, preservatives, and calorie information?",
        choices=FOOD_LABEL_CHECK_CHOICES,
        widget=forms.RadioSelect
    )

    emotional_eating = forms.ChoiceField(
        label="Have you experienced emotional or binge eating tendencies during stress or periods?",
        choices=EMOTIONAL_EATING_CHOICES,
        widget=forms.RadioSelect
    )

    iron_foods_frequency = forms.ChoiceField(
        label="How often do you include iron-rich foods (like spinach, legumes, jaggery) in your meals?",
        choices=IRON_FOODS_FREQUENCY_CHOICES,
        widget=forms.RadioSelect
    )

    stress_management = forms.ChoiceField(
        label="Do you practice stress management activities like meditation, yoga, journaling, or hobbies?",
        choices=STRESS_MANAGEMENT_CHOICES,
        widget=forms.RadioSelect
    )

    gut_health_awareness = forms.ChoiceField(
        label="Are you aware of gut health and include probiotics (curd, fermented foods) in your diet?",
        choices=GUT_HEALTH_CHOICES,
        widget=forms.RadioSelect
    )

    digital_detox = forms.ChoiceField(
        label="Do you allocate daily or weekly screen-free hours for digital detox?",
        choices=DIGITAL_DETOX_CHOICES,
        widget=forms.RadioSelect
    )

    personal_goals = forms.ChoiceField(
        label="Have you set any personal fitness or mental health goals for the year?",
        choices=PERSONAL_GOALS_CHOICES,
        widget=forms.RadioSelect
    )

    comfort_discuss_health = forms.ChoiceField(
        label="Are you comfortable openly discussing your health issues with a doctor, friend, or wellness counselor?",
        choices=COMFORT_DISCUSS_HEALTH_CHOICES,
        widget=forms.RadioSelect
    )

class StressManagementForm(forms.Form):
    OVERWHELMED_FREQUENCY_CHOICES = [
        ('daily', 'Daily'),
        ('few_times_week', 'A few times a week'),
        ('rarely', 'Rarely'),
        ('never', 'Never'),
    ]

    STRESS_SOURCES_CHOICES = [
        ('work', 'Work'),
        ('relationships', 'Relationships'),
        ('finances', 'Finances'),
        ('health', 'Health'),
        ('caregiving', 'Caregiving'),
        ('studies', 'Studies'),
        ('other', 'Other'),
    ]

    COPING_METHODS_CHOICES = [
        ('talk', 'Talk to someone'),
        ('exercise', 'Exercise'),
        ('cry', 'Cry'),
        ('overthink', 'Overthink'),
        ('binge_eat', 'Binge-eat'),
        ('avoid', 'Avoid it'),
        ('other', 'Other'),
    ]

    PHYSICAL_SYMPTOMS_CHOICES = [
        ('yes', 'Yes'),
        ('no', 'No'),
        ('sometimes', 'Sometimes'),
    ]

    INTENTIONAL_BREAKS_CHOICES = [
        ('daily', 'Daily'),
        ('few_times_week', 'A few times a week'),
        ('rarely', 'Rarely'),
        ('never', 'Never'),
    ]

    SAY_NO_DIFFICULTY_CHOICES = [
        ('yes', 'Yes'),
        ('sometimes', 'Sometimes'),
        ('no', 'No'),
    ]

    IDENTIFY_TRIGGERS_CHOICES = [
        ('always', 'Always'),
        ('sometimes', 'Sometimes'),
        ('rarely', 'Rarely'),
        ('never', 'Never'),
    ]

    RELAXATION_TECHNIQUES_CHOICES = [
        ('yes_regularly', 'Yes, regularly'),
        ('occasionally', 'Occasionally'),
        ('never_tried', 'Never tried'),
    ]

    SUPPORT_SYSTEM_CHOICES = [
        ('yes', 'Yes'),
        ('partially', 'Somewhat'),
        ('no', 'No'),
    ]

    AWARENESS_STRESS_IMPACTS_CHOICES = [
        ('yes', 'Yes'),
        ('somewhat', 'Somewhat'),
        ('no', 'No'),
    ]

    # Fields

    overwhelmed_frequency = forms.ChoiceField(
        label="How often do you feel overwhelmed or emotionally exhausted in a typical week?",
        choices=OVERWHELMED_FREQUENCY_CHOICES,
        widget=forms.RadioSelect
    )

    stress_sources = forms.MultipleChoiceField(
        label="What are your primary sources of stress currently?",
        choices=STRESS_SOURCES_CHOICES,
        widget=forms.RadioSelect
    )

    coping_methods = forms.MultipleChoiceField(
        label="When you feel stressed, how do you usually cope with it?",
        choices=COPING_METHODS_CHOICES,
        widget=forms.RadioSelect
    )

    physical_symptoms = forms.ChoiceField(
        label="Do you experience physical symptoms when stressed (headaches, chest tightness, digestive issues, menstrual irregularities)?",
        choices=PHYSICAL_SYMPTOMS_CHOICES,
        widget=forms.RadioSelect
    )

    intentional_breaks = forms.ChoiceField(
        label="How often do you take intentional breaks from work, studies, or home duties for yourself?",
        choices=INTENTIONAL_BREAKS_CHOICES,
        widget=forms.RadioSelect
    )

    say_no_difficulty = forms.ChoiceField(
        label="Do you find it difficult to say 'no' when you're emotionally drained or overloaded with responsibilities?",
        choices=SAY_NO_DIFFICULTY_CHOICES,
        widget=forms.RadioSelect
    )

    identify_triggers = forms.ChoiceField(
        label="Are you able to identify your personal stress triggers quickly and address them?",
        choices=IDENTIFY_TRIGGERS_CHOICES,
        widget=forms.RadioSelect
    )

    relaxation_techniques = forms.ChoiceField(
        label="Have you learned or practiced any stress-relieving techniques (deep breathing, progressive muscle relaxation, creative hobbies)?",
        choices=RELAXATION_TECHNIQUES_CHOICES,
        widget=forms.RadioSelect
    )

    support_system = forms.ChoiceField(
        label="Do you have a personal support system (friends, family, mentor) you can turn to during difficult times?",
        choices=SUPPORT_SYSTEM_CHOICES,
        widget=forms.RadioSelect
    )

    awareness_stress_impacts = forms.ChoiceField(
        label="Are you aware of the long-term health impacts of unmanaged stress (hypertension, infertility, anxiety disorders)?",
        choices=AWARENESS_STRESS_IMPACTS_CHOICES,
        widget=forms.RadioSelect
    )
class EmotionalWellbeingForm(forms.Form):
    EMOTIONAL_STATE_CHOICES = [
        ('happy', 'Happy'),
        ('anxious', 'Anxious'),
        ('irritable', 'Irritable'),
        ('calm', 'Calm'),
        ('numb', 'Numb'),
        ('overwhelmed', 'Overwhelmed'),
    ]

    YES_NO_CHOICES = [
        ('yes', 'Yes'),
        ('no', 'No'),
        ('sometimes', 'Sometimes'),
    ]

    LONELINESS_FREQUENCY_CHOICES = [
        ('often', 'Often'),
        ('sometimes', 'Sometimes'),
        ('rarely', 'Rarely'),
        ('never', 'Never'),
    ]

    SELF_ESTEEM_ISSUES_CHOICES = [
        ('yes_currently', 'Yes, currently'),
        ('in_past', 'In the past'),
        ('no_never', 'No, never'),
    ]

    DAILY_HABITS_CHOICES = [
        ('yes', 'Yes'),
        ('no', 'No'),
        ('planning_to', 'Planning to start'),
    ]

    BOUNDARIES_SETTING_CHOICES = [
        ('very_well', 'Very well'),
        ('moderately', 'Moderately'),
        ('poorly', 'Poorly'),
        ('not_at_all', 'Not at all'),
    ]

    FORGIVENESS_CHOICES = [
        ('yes', 'Yes, I have forgiven myself'),
        ('working_on_it', 'I am working on it'),
        ('no', 'No, I still struggle with it'),
    ]

    TRIGGERS_AWARENESS_CHOICES = [
        ('yes', 'Yes'),
        ('somewhat', 'Somewhat'),
        ('no', 'Not really'),
    ]

    CELEBRATE_ACHIEVEMENTS_CHOICES = [
        ('always', 'Always'),
        ('sometimes', 'Sometimes'),
        ('rarely', 'Rarely'),
        ('never', 'Never'),
    ]

    # Fields

    emotional_state = forms.ChoiceField(
        label="How would you describe your current emotional state most of the time?",
        choices=EMOTIONAL_STATE_CHOICES,
        widget=forms.RadioSelect
    )

    express_emotions = forms.ChoiceField(
        label="Are you able to openly express your emotions without fear of judgment?",
        choices=YES_NO_CHOICES,
        widget=forms.RadioSelect
    )

    emotional_support = forms.ChoiceField(
        label="Do you feel emotionally supported by your family, friends, or workplace?",
        choices=YES_NO_CHOICES,
        widget=forms.RadioSelect
    )

    loneliness_frequency = forms.ChoiceField(
        label="How often do you experience feelings of loneliness or emotional disconnect?",
        choices=LONELINESS_FREQUENCY_CHOICES,
        widget=forms.RadioSelect
    )

    self_esteem_issues = forms.ChoiceField(
        label="Have you struggled with low self-esteem, body image issues, or feelings of unworthiness?",
        choices=SELF_ESTEEM_ISSUES_CHOICES,
        widget=forms.RadioSelect
    )

    daily_emotional_habits = forms.ChoiceField(
        label="Do you practice daily habits to nurture your emotional health (journaling, affirmations, hobbies)?",
        choices=DAILY_HABITS_CHOICES,
        widget=forms.RadioSelect
    )

    emotional_boundaries = forms.ChoiceField(
        label="How well do you set emotional boundaries in relationships — saying no, protecting your peace?",
        choices=BOUNDARIES_SETTING_CHOICES,
        widget=forms.RadioSelect
    )

    forgiveness_past = forms.ChoiceField(
        label="Have you forgiven yourself for past mistakes or regrets that affect your emotional wellbeing?",
        choices=FORGIVENESS_CHOICES,
        widget=forms.RadioSelect
    )

    emotional_triggers_awareness = forms.ChoiceField(
        label="Are you aware of your emotional triggers (criticism, neglect, rejection) and how you react to them?",
        choices=TRIGGERS_AWARENESS_CHOICES,
        widget=forms.RadioSelect
    )

    celebrate_achievements = forms.ChoiceField(
        label="Do you celebrate your personal achievements, no matter how small, as a way of validating your worth?",
        choices=CELEBRATE_ACHIEVEMENTS_CHOICES,
        widget=forms.RadioSelect
    )

class MeditationMindfulnessForm(forms.Form):
    YES_NO_CHOICES = [
        ('yes', 'Yes'),
        ('no', 'No'),
    ]

    MEDITATION_REASON_CHOICES = [
        ('stress_relief', 'Stress relief'),
        ('focus', 'Improved focus'),
        ('anxiety', 'Anxiety management'),
        ('spirituality', 'Spiritual connection'),
        ('sleep', 'Better sleep'),
        ('other', 'Other'),
    ]

    FREQUENCY_CHOICES = [
        ('daily', 'Daily'),
        ('2_3_week', '2–3 times a week'),
        ('occasionally', 'Occasionally'),
        ('never', 'Never'),
    ]

    MEDITATION_TYPE_CHOICES = [
        ('guided', 'Guided meditations'),
        ('breathing', 'Breathing exercises'),
        ('mantra', 'Mantra meditation'),
        ('yoga_nidra', 'Yoga Nidra'),
        ('spiritual', 'Spiritual/faith-based'),
        ('visualization', 'Visualization/imagery'),
    ]

    POSITIVE_EFFECTS_CHOICES = [
        ('yes', 'Yes, definitely'),
        ('somewhat', 'Somewhat'),
        ('no', 'Not really'),
        ('haven’t_tried_enough', 'Haven’t tried enough yet'),
    ]

    RESTLESSNESS_CHOICES = [
        ('often', 'Often'),
        ('sometimes', 'Sometimes'),
        ('rarely', 'Rarely'),
        ('never', 'Never'),
    ]

    INTERESTED_HORMONAL_BALANCE_CHOICES = [
        ('yes', 'Yes, very interested'),
        ('maybe', 'Maybe, I’d like to explore'),
        ('no', 'Not at this time'),
    ]

    USED_APPS_CHOICES = [
        ('yes', 'Yes'),
        ('no', 'No'),
        ('planning', 'Planning to try'),
    ]

    JOIN_CIRCLE_CHOICES = [
        ('yes_virtual', 'Yes, virtual'),
        ('yes_in_person', 'Yes, in-person'),
        ('maybe', 'Maybe in the future'),
        ('no', 'No'),
    ]

    AWARENESS_BENEFITS_CHOICES = [
        ('yes', 'Yes'),
        ('no', 'No, I wasn’t aware'),
    ]

    # Fields
    tried_meditation = forms.ChoiceField(
        label="Have you ever tried meditation or mindfulness practices?",
        choices=YES_NO_CHOICES,
        widget=forms.RadioSelect
    )

    meditation_reason = forms.ChoiceField(
        label="What’s your main reason for meditating?",
        choices=MEDITATION_REASON_CHOICES,
        widget=forms.RadioSelect
    )

    meditation_frequency = forms.ChoiceField(
        label="How frequently do you meditate or engage in quiet, mindful moments?",
        choices=FREQUENCY_CHOICES,
        widget=forms.RadioSelect
    )

    meditation_type = forms.ChoiceField(
        label="Which type of meditation appeals to you the most?",
        choices=MEDITATION_TYPE_CHOICES,
        widget=forms.RadioSelect
    )

    positive_effects = forms.ChoiceField(
        label="Do you notice any positive effects on your mood, focus, or sleep after meditation?",
        choices=POSITIVE_EFFECTS_CHOICES,
        widget=forms.RadioSelect
    )

    restlessness_experience = forms.ChoiceField(
        label="Do you feel restless, distracted, or impatient when trying to meditate?",
        choices=RESTLESSNESS_CHOICES,
        widget=forms.RadioSelect
    )

    interested_in_hormonal_meditation = forms.ChoiceField(
        label="Are you interested in learning meditation techniques designed specifically for women’s hormonal health and emotional balance?",
        choices=INTERESTED_HORMONAL_BALANCE_CHOICES,
        widget=forms.RadioSelect
    )

    used_meditation_apps = forms.ChoiceField(
        label="Have you used meditation apps or online sessions for guided practices?",
        choices=USED_APPS_CHOICES,
        widget=forms.RadioSelect
    )

    join_womens_circle = forms.ChoiceField(
        label="Would you like to join a women’s-only meditation circle (virtual or in-person) for shared healing and support?",
        choices=JOIN_CIRCLE_CHOICES,
        widget=forms.RadioSelect
    )

    aware_of_mindful_benefits = forms.ChoiceField(
        label="Are you aware that even 5–10 minutes of mindful breathing daily can improve menstrual discomfort, anxiety, and sleep quality?",
        choices=AWARENESS_BENEFITS_CHOICES,
        widget=forms.RadioSelect
    )
class MentalHealthDisordersForm(forms.Form):
    YES_NO_CHOICES = [
        ('yes', 'Yes'),
        ('no', 'No'),
    ]

    FREQUENCY_CHOICES = [
        ('often', 'Often'),
        ('sometimes', 'Sometimes'),
        ('rarely', 'Rarely'),
        ('never', 'Never'),
    ]

    AWARENESS_CHOICES = [
        ('yes', 'Yes'),
        ('somewhat', 'Somewhat'),
        ('no', 'No'),
    ]

    STIGMA_CHOICES = [
        ('yes', 'Yes, I avoid it'),
        ('no', 'No, I feel safe seeking help'),
        ('sometimes', 'Sometimes I hesitate'),
    ]

    FAMILIARITY_CHOICES = [
        ('very_familiar', 'Very familiar and have used them'),
        ('aware', 'Aware but haven’t used'),
        ('not_aware', 'Not aware'),
    ]

    WILLINGNESS_CHOICES = [
        ('yes', 'Yes, definitely'),
        ('maybe', 'Maybe, if needed'),
        ('no', 'No'),
    ]

    # Questions
    prolonged_sadness = forms.ChoiceField(
        label="Have you ever experienced prolonged sadness, irritability, or lack of interest in daily activities lasting over 2 weeks?",
        choices=YES_NO_CHOICES,
        widget=forms.RadioSelect
    )

    diagnosed_mental_health_condition = forms.ChoiceField(
        label="Have you ever been formally diagnosed with a mental health condition (anxiety, depression, PTSD, OCD, bipolar disorder)?",
        choices=YES_NO_CHOICES,
        widget=forms.RadioSelect
    )

    intrusive_thoughts_frequency = forms.ChoiceField(
        label="Do you experience frequent intrusive thoughts, excessive worry, or panic attacks?",
        choices=FREQUENCY_CHOICES,
        widget=forms.RadioSelect
    )

    social_withdrawal_due_to_mental_distress = forms.ChoiceField(
        label="Have you faced social withdrawal or avoided relationships due to mental distress?",
        choices=YES_NO_CHOICES,
        widget=forms.RadioSelect
    )

    awareness_postpartum_depression = forms.ChoiceField(
        label="Are you aware of postpartum depression and its early signs?",
        choices=AWARENESS_CHOICES,
        widget=forms.RadioSelect
    )

    thoughts_of_self_harm = forms.ChoiceField(
        label="Have you ever considered self-harm or had thoughts of ending your life during overwhelming times?",
        choices=YES_NO_CHOICES,
        widget=forms.RadioSelect
    )

    avoiding_mental_health_care = forms.ChoiceField(
        label="Do you avoid seeking mental health care because of stigma or fear of judgment?",
        choices=STIGMA_CHOICES,
        widget=forms.RadioSelect
    )

    familiarity_with_support_platforms = forms.ChoiceField(
        label="How familiar are you with online mental health support platforms and helplines available in your region?",
        choices=FAMILIARITY_CHOICES,
        widget=forms.RadioSelect
    )

    recognizing_physical_impact_of_mental_health = forms.ChoiceField(
        label="Do you recognize when your mental health symptoms begin affecting your sleep, appetite, or physical health?",
        choices=FREQUENCY_CHOICES,
        widget=forms.RadioSelect
    )

    willingness_to_consult_professional = forms.ChoiceField(
        label="Would you be willing to consult a mental health professional if recommended, for better emotional management and healing?",
        choices=WILLINGNESS_CHOICES,
        widget=forms.RadioSelect
    )
class InnerPeaceForm(forms.Form):
    FREQUENCY_CHOICES = [
        ('daily', 'Daily'),
        ('several_times_week', 'Several times a week'),
        ('rarely', 'Rarely'),
        ('never', 'Never'),
    ]

    YES_NO_CHOICES = [
        ('yes', 'Yes'),
        ('no', 'No'),
    ]

    RESPONSE_CHOICES = [
        ('stay_calm', 'I try to stay calm and reflect'),
        ('express_emotions', 'I express emotions openly'),
        ('withdraw', 'I withdraw from the situation'),
        ('seek_support', 'I talk to someone or seek support'),
        ('overthink', 'I tend to overthink it'),
    ]

    DISCONNECTION_CHOICES = [
        ('often', 'Often'),
        ('sometimes', 'Sometimes'),
        ('rarely', 'Rarely'),
        ('never', 'Never'),
    ]

    ACTIVITY_CHOICES = [
        ('music', 'Listening to music'),
        ('reading', 'Reading'),
        ('journaling', 'Journaling'),
        ('prayer', 'Prayer/Spiritual practices'),
        ('nature', 'Spending time in nature'),
        ('exercise', 'Exercise/Yoga'),
        ('other', 'Other'),
    ]

    AWARENESS_CHOICES = [
        ('very_aware', 'Very aware'),
        ('somewhat', 'Somewhat aware'),
        ('not_aware', 'Not aware'),
    ]

    RECOGNITION_CHOICES = [
        ('yes', 'Yes, and I take action'),
        ('sometimes', 'Sometimes I notice it'),
        ('no', 'No, I tend to ignore it'),
    ]

    # Questions
    calm_frequency = forms.ChoiceField(
        label="How often do you experience a sense of calm and inner peace during your daily routine?",
        choices=FREQUENCY_CHOICES,
        widget=forms.RadioSelect
    )

    personal_space = forms.ChoiceField(
        label="Do you have a personal space, ritual, or activity where you disconnect and recharge mentally?",
        choices=YES_NO_CHOICES,
        widget=forms.RadioSelect
    )

    conflict_response = forms.ChoiceField(
        label="When faced with conflict or emotional distress, how do you usually regain your composure?",
        choices=RESPONSE_CHOICES,
        widget=forms.RadioSelect
    )

    gratitude_practice = forms.ChoiceField(
        label="Do you take time each day to reflect on things you’re grateful for?",
        choices=FREQUENCY_CHOICES,
        widget=forms.RadioSelect
    )

    self_forgiveness = forms.ChoiceField(
        label="Are you able to forgive yourself for past mistakes and let go of guilt or regrets?",
        choices=YES_NO_CHOICES,
        widget=forms.RadioSelect
    )

    emotional_disconnection = forms.ChoiceField(
        label="Do you ever feel disconnected from your own emotions and needs while managing others’ expectations?",
        choices=DISCONNECTION_CHOICES,
        widget=forms.RadioSelect
    )

    peace_activities = forms.MultipleChoiceField(
        label="What activities bring you the most peace and emotional clarity?",
        choices=ACTIVITY_CHOICES,
        widget=forms.RadioSelect
    )

    deep_breathing_practice = forms.ChoiceField(
        label="Have you ever consciously practiced deep breathing or mindfulness to calm your mind?",
        choices=YES_NO_CHOICES,
        widget=forms.RadioSelect
    )

    stress_awareness = forms.ChoiceField(
        label="Are you aware of how stress and inner turmoil can affect your physical health?",
        choices=AWARENESS_CHOICES,
        widget=forms.RadioSelect
    )

    recognizing_signs = forms.ChoiceField(
        label="Do you recognize signs in your body or emotions when you’re mentally unsettled, and take steps to address them?",
        choices=RECOGNITION_CHOICES,
        widget=forms.RadioSelect
    )
class GoalSettingForm(forms.Form):
    YES_NO_CHOICES = [
        ('yes', 'Yes'),
        ('no', 'No'),
    ]

    CLARITY_CHOICES = [
        ('very_clear', 'Very clear'),
        ('somewhat_clear', 'Somewhat clear'),
        ('not_clear', 'Not very clear'),
    ]

    ALIGNMENT_CHOICES = [
        ('fully_aligned', 'Fully aligned'),
        ('partially_aligned', 'Partially aligned'),
        ('not_aligned', 'Not at all aligned'),
    ]

    FREQUENCY_CHOICES = [
        ('weekly', 'Weekly'),
        ('monthly', 'Monthly'),
        ('rarely', 'Rarely'),
        ('never', 'Never'),
    ]

    FOCUS_CHOICES = [
        ('external', 'Primarily external achievements (career, status, possessions)'),
        ('internal', 'Primarily inner contentment and wellbeing'),
        ('balanced', 'A balance of both'),
    ]

    CELEBRATION_CHOICES = [
        ('always', 'Always'),
        ('sometimes', 'Sometimes'),
        ('never', 'Never'),
    ]

    BALANCE_CHOICES = [
        ('excellent', 'Excellent'),
        ('good', 'Good'),
        ('needs_work', 'Needs work'),
        ('struggling', 'Struggling to balance'),
    ]

    CONFIDENCE_SUPPORT_CHOICES = [
        ('strong_confidence', 'Yes, I feel confident and supported'),
        ('some_support', 'Somewhat — I have limited support'),
        ('no_support', 'No — I feel alone in pursuing my goals'),
    ]

    AWARENESS_CHOICES = [
        ('fully_aware', 'Fully aware'),
        ('somewhat_aware', 'Somewhat aware'),
        ('not_aware', 'Not aware at all'),
    ]

    # Questions
    set_goals = forms.ChoiceField(
        label="Do you regularly set personal, professional, or wellness goals for yourself?",
        choices=YES_NO_CHOICES,
        widget=forms.RadioSelect
    )

    clarity_values = forms.ChoiceField(
        label="How clear are you about what truly matters to you in life beyond social expectations?",
        choices=CLARITY_CHOICES,
        widget=forms.RadioSelect
    )

    lifestyle_alignment = forms.ChoiceField(
        label="Do you believe your current lifestyle aligns with your inner values and personal priorities?",
        choices=ALIGNMENT_CHOICES,
        widget=forms.RadioSelect
    )

    review_frequency = forms.ChoiceField(
        label="How often do you review your goals and adjust them according to your growth or changing needs?",
        choices=FREQUENCY_CHOICES,
        widget=forms.RadioSelect
    )

    vision_board = forms.ChoiceField(
        label="Have you ever created a personal vision board or written down your life goals?",
        choices=YES_NO_CHOICES,
        widget=forms.RadioSelect
    )

    goal_focus = forms.ChoiceField(
        label="Are your goals focused on external achievements or inner contentment and wellbeing?",
        choices=FOCUS_CHOICES,
        widget=forms.RadioSelect
    )

    celebrate_victories = forms.ChoiceField(
        label="Do you celebrate small personal victories, even if others don’t acknowledge them?",
        choices=CELEBRATION_CHOICES,
        widget=forms.RadioSelect
    )

    balance_personal_responsibilities = forms.ChoiceField(
        label="How well do you balance your personal desires with responsibilities like family, work, and caregiving?",
        choices=BALANCE_CHOICES,
        widget=forms.RadioSelect
    )

    confidence_support = forms.ChoiceField(
        label="Do you feel you have the confidence and support to pursue goals important to you?",
        choices=CONFIDENCE_SUPPORT_CHOICES,
        widget=forms.RadioSelect
    )

    goal_awareness = forms.ChoiceField(
        label="Are you aware that setting emotionally fulfilling goals contributes to mental peace and spiritual contentment?",
        choices=AWARENESS_CHOICES,
        widget=forms.RadioSelect
    )
class NatureForm(forms.Form):
    FREQUENCY_CHOICES = [
        ('daily', 'Daily'),
        ('weekly', 'Weekly'),
        ('occasionally', 'Occasionally'),
        ('rarely', 'Rarely'),
        ('never', 'Never'),
    ]

    YES_NO_CHOICES = [
        ('yes', 'Yes'),
        ('no', 'No'),
    ]

    AWARENESS_CHOICES = [
        ('fully_aware', 'Fully aware'),
        ('somewhat_aware', 'Somewhat aware'),
        ('not_aware', 'Not aware'),
    ]

    WALK_PREFERENCE_CHOICES = [
        ('solitary', 'Solitary walks'),
        ('with_friends_pets', 'With friends or pets'),
        ('either', 'Either — depends on mood'),
    ]

    INTEREST_CHOICES = [
        ('interested', 'Yes, very interested'),
        ('maybe', 'Maybe'),
        ('not_interested', 'Not interested'),
    ]

    # Questions
    time_in_nature = forms.ChoiceField(
        label="How often do you spend time in natural surroundings like parks, beaches, or gardens?",
        choices=FREQUENCY_CHOICES,
        widget=forms.RadioSelect
    )

    feel_lighter_outdoors = forms.ChoiceField(
        label="Do you feel emotionally lighter and calmer after spending time outdoors?",
        choices=YES_NO_CHOICES,
        widget=forms.RadioSelect
    )

    practiced_mindful_walking = forms.ChoiceField(
        label="Have you ever practiced mindful walking — observing your surroundings, sounds, and breath while walking in nature?",
        choices=YES_NO_CHOICES,
        widget=forms.RadioSelect
    )

    aware_sunlight_air_benefits = forms.ChoiceField(
        label="Are you aware of the mental health benefits of regular exposure to sunlight and fresh air?",
        choices=AWARENESS_CHOICES,
        widget=forms.RadioSelect
    )

    disconnect_during_nature = forms.ChoiceField(
        label="Do you intentionally disconnect from digital devices during nature walks or outdoor time?",
        choices=YES_NO_CHOICES,
        widget=forms.RadioSelect
    )

    nature_walk_preference = forms.ChoiceField(
        label="Would you prefer solitary nature walks, or walks with friends or pets for emotional support?",
        choices=WALK_PREFERENCE_CHOICES,
        widget=forms.RadioSelect
    )

    feel_spiritually_connected = forms.ChoiceField(
        label="Do you feel more spiritually connected or reflective while surrounded by natural landscapes?",
        choices=YES_NO_CHOICES,
        widget=forms.RadioSelect
    )

    schedule_outdoor_breaks = forms.ChoiceField(
        label="How often do you schedule weekend breaks, picnics, or outdoor hobbies to destress?",
        choices=FREQUENCY_CHOICES,
        widget=forms.RadioSelect
    )

    aware_walks_reduce_symptoms = forms.ChoiceField(
        label="Are you aware that regular nature walks can reduce symptoms of anxiety, depression, and fatigue?",
        choices=AWARENESS_CHOICES,
        widget=forms.RadioSelect
    )

    join_wellness_walks = forms.ChoiceField(
        label="Would you be interested in joining women’s wellness nature walks or community retreats for healing and bonding?",
        choices=INTEREST_CHOICES,
        widget=forms.RadioSelect
    )
class SpiritualityForm(forms.Form):
    YES_NO_CHOICES = [
        ('yes', 'Yes'),
        ('no', 'No'),
    ]

    IMPORTANCE_CHOICES = [
        ('very_important', 'Very important'),
        ('somewhat_important', 'Somewhat important'),
        ('not_important', 'Not important'),
    ]

    FREQUENCY_CHOICES = [
        ('daily', 'Daily'),
        ('weekly', 'Weekly'),
        ('occasionally', 'Occasionally'),
        ('rarely', 'Rarely'),
        ('never', 'Never'),
    ]

    BELIEF_CHOICES = [
        ('private', 'A private, personal experience'),
        ('shared', 'Shared with a supportive community'),
        ('both', 'A mix of both'),
    ]

    OPENNESS_CHOICES = [
        ('very_open', 'Very open'),
        ('somewhat_open', 'Somewhat open'),
        ('not_open', 'Not open'),
    ]

    AWARENESS_CHOICES = [
        ('fully_aware', 'Fully aware'),
        ('somewhat_aware', 'Somewhat aware'),
        ('not_aware', 'Not aware'),
    ]

    # Questions
    regular_spiritual_practice = forms.ChoiceField(
        label="Do you follow any regular spiritual practices (prayer, meditation, reading scriptures, affirmations)?",
        choices=YES_NO_CHOICES,
        widget=forms.RadioSelect
    )

    spirituality_importance = forms.ChoiceField(
        label="How important is spirituality in your personal and family life?",
        choices=IMPORTANCE_CHOICES,
        widget=forms.RadioSelect
    )

    explored_other_spiritual_paths = forms.ChoiceField(
        label="Have you explored spiritual practices from different cultures or faiths that resonate with you personally?",
        choices=YES_NO_CHOICES,
        widget=forms.RadioSelect
    )

    frequency_spiritual_upliftment = forms.ChoiceField(
        label="How frequently do you engage in practices that make you feel spiritually uplifted?",
        choices=FREQUENCY_CHOICES,
        widget=forms.RadioSelect
    )

    use_affirmations_gratitude = forms.ChoiceField(
        label="Do you use affirmations or gratitude exercises as part of your spiritual or self-care routine?",
        choices=YES_NO_CHOICES,
        widget=forms.RadioSelect
    )

    aware_spiritual_support = forms.ChoiceField(
        label="Are you aware of how spiritual practices can support recovery from emotional trauma or grief?",
        choices=AWARENESS_CHOICES,
        widget=forms.RadioSelect
    )

    participated_healing_therapies = forms.ChoiceField(
        label="Have you ever participated in spiritual healing therapies like Reiki, sound therapy, or group meditation sessions?",
        choices=YES_NO_CHOICES,
        widget=forms.RadioSelect
    )

    belief_spirituality_community = forms.ChoiceField(
        label="Do you believe spirituality should be a private, personal experience or shared with a supportive community?",
        choices=BELIEF_CHOICES,
        widget=forms.RadioSelect
    )

    differentiate_rituals_practices = forms.ChoiceField(
        label="How do you differentiate between religious rituals and personal spiritual practices in your life?",
        choices=[
            ('clearly_different', 'I view them as clearly different'),
            ('somewhat_overlapping', 'They overlap for me'),
            ('not_thought_about', 'I haven’t thought about it much'),
        ],
        widget=forms.RadioSelect
    )

    open_to_nonreligious_techniques = forms.ChoiceField(
        label="Would you be open to learning about non-religious mindfulness and self-awareness techniques for inner growth?",
        choices=OPENNESS_CHOICES,
        widget=forms.RadioSelect
    )
class BalancedDietForm(forms.Form):
    FREQUENCY_CHOICES = [
        ('daily', 'Daily'),
        ('most_days', 'Most days'),
        ('occasionally', 'Occasionally'),
        ('rarely', 'Rarely'),
        ('never', 'Never'),
    ]

    YES_NO_CHOICES = [
        ('yes', 'Yes'),
        ('no', 'No'),
    ]

    BREAKFAST_SKIP_REASON_CHOICES = [
        ('lack_of_time', 'Lack of time'),
        ('no_appetite', 'No appetite in the morning'),
        ('habit', 'It has become a habit'),
        ('dieting', 'Dieting/fasting reasons'),
        ('never_skip', 'I never skip breakfast'),
    ]

    PROCESSED_FOOD_CONSUMPTION = [
        ('daily', 'Daily'),
        ('few_times_week', 'Few times a week'),
        ('once_week', 'Once a week'),
        ('rarely', 'Rarely'),
        ('never', 'Never'),
    ]

    WATER_INTAKE_CHOICES = [
        ('less_than_1L', 'Less than 1 liter'),
        ('1_to_2L', '1–2 liters'),
        ('2_to_3L', '2–3 liters'),
        ('more_than_3L', 'More than 3 liters'),
    ]

    CURRENT_DIET_CHOICES = [
        ('vegetarian', 'Vegetarian'),
        ('vegan', 'Vegan'),
        ('keto', 'Keto'),
        ('intermittent_fasting', 'Intermittent fasting'),
        ('gluten_free', 'Gluten-free'),
        ('balanced_normal', 'Balanced/normal diet'),
        ('other', 'Other'),
        ('no_special_diet', 'No specific diet plan'),
    ]

    DEFICIENCY_SIGNS_CHOICES = [
        ('low_energy', 'Low energy levels'),
        ('brittle_nails', 'Brittle nails'),
        ('hair_fall', 'Hair fall'),
        ('frequent_infections', 'Frequent infections'),
        ('none', 'None'),
    ]

    # Questions
    include_all_five_groups = forms.ChoiceField(
        label="How often do you include all five essential food groups (grains, fruits, vegetables, proteins, dairy/alternatives) in your daily meals?",
        choices=FREQUENCY_CHOICES,
        widget=forms.RadioSelect
    )

    plan_meals_for_balance = forms.ChoiceField(
        label="Do you consciously plan your meals to maintain a balance of proteins, carbs, and healthy fats?",
        choices=YES_NO_CHOICES,
        widget=forms.RadioSelect
    )

    skip_breakfast_reason = forms.ChoiceField(
        label="How frequently do you skip breakfast, and what’s usually the reason?",
        choices=BREAKFAST_SKIP_REASON_CHOICES,
        widget=forms.RadioSelect
    )

    aware_nutritional_needs = forms.ChoiceField(
        label="Are you aware of your daily nutritional needs based on your age, activity level, and reproductive health (menstruation, pregnancy, menopause)?",
        choices=YES_NO_CHOICES,
        widget=forms.RadioSelect
    )

    check_food_labels = forms.ChoiceField(
        label="Do you check food labels for calorie, sugar, and fat content before purchasing packaged foods?",
        choices=YES_NO_CHOICES,
        widget=forms.RadioSelect
    )

    consume_processed_food = forms.ChoiceField(
        label="How often do you consume processed foods, instant meals, or packaged snacks?",
        choices=PROCESSED_FOOD_CONSUMPTION,
        widget=forms.RadioSelect
    )

    daily_water_intake = forms.ChoiceField(
        label="Do you regularly drink enough water (at least 2–3 liters per day)?",
        choices=WATER_INTAKE_CHOICES,
        widget=forms.RadioSelect
    )

    current_diet = forms.ChoiceField(
        label="Are you currently following any specific diet (vegetarian, keto, intermittent fasting, gluten-free, etc.)? If yes, why?",
        choices=CURRENT_DIET_CHOICES,
        widget=forms.RadioSelect
    )

    recurring_deficiencies = forms.MultipleChoiceField(
        label="Do you notice any recurring deficiencies (low energy, brittle nails, hair fall) related to your dietary habits?",
        choices=DEFICIENCY_SIGNS_CHOICES,
        widget=forms.CheckboxSelectMultiple,
        required=False
    )

    open_to_nutritionist_consult = forms.ChoiceField(
        label="Would you be open to consulting a certified nutritionist for a personalized women’s nutrition plan?",
        choices=YES_NO_CHOICES,
        widget=forms.RadioSelect
    )
class SuperfoodsForm(forms.Form):
    YES_NO_CHOICES = [
        ('yes', 'Yes'),
        ('no', 'No'),
    ]

    FREQUENCY_CHOICES = [
        ('daily', 'Daily'),
        ('few_times_week', 'Few times a week'),
        ('occasionally', 'Occasionally'),
        ('rarely', 'Rarely'),
        ('never', 'Never'),
    ]

    # Questions
    familiar_superfoods = forms.ChoiceField(
        label="Are you familiar with superfoods like chia seeds, flax seeds, quinoa, avocados, and moringa?",
        choices=YES_NO_CHOICES,
        widget=forms.RadioSelect
    )

    antioxidant_foods_frequency = forms.ChoiceField(
        label="How often do you include antioxidant-rich foods (berries, turmeric, green tea) in your diet?",
        choices=FREQUENCY_CHOICES,
        widget=forms.RadioSelect
    )

    iron_foods_frequency = forms.ChoiceField(
        label="Do you consume iron-rich foods regularly to manage menstrual health and energy levels?",
        choices=FREQUENCY_CHOICES,
        widget=forms.RadioSelect
    )

    aware_hormone_balancing_foods = forms.ChoiceField(
        label="Are you aware of foods that naturally support hormonal balance (pumpkin seeds, walnuts, dark leafy greens)?",
        choices=YES_NO_CHOICES,
        widget=forms.RadioSelect
    )

    omega3_foods_frequency = forms.ChoiceField(
        label="How frequently do you consume omega-3 rich foods (fish, flax seeds, walnuts) for heart and brain health?",
        choices=FREQUENCY_CHOICES,
        widget=forms.RadioSelect
    )

    immunity_boosting_herbs = forms.ChoiceField(
        label="Have you ever tried immunity-boosting herbs or ingredients (ginger, garlic, tulsi, cinnamon)?",
        choices=YES_NO_CHOICES,
        widget=forms.RadioSelect
    )

    healthy_dessert_alternatives = forms.ChoiceField(
        label="Do you replace high-sugar desserts with healthy alternatives like fruit bowls, yogurt parfait, or dates?",
        choices=YES_NO_CHOICES,
        widget=forms.RadioSelect
    )

    aware_calcium_vitaminD = forms.ChoiceField(
        label="Are you aware of calcium and vitamin D rich foods necessary for bone health, especially after 30?",
        choices=YES_NO_CHOICES,
        widget=forms.RadioSelect
    )

    include_probiotics = forms.ChoiceField(
        label="Do you include probiotics (yogurt, fermented foods) for gut health and digestion?",
        choices=FREQUENCY_CHOICES,
        widget=forms.RadioSelect
    )

    interested_in_superfoods_plan = forms.ChoiceField(
        label="Would you like to receive a superfoods meal plan customized for women’s hormonal, skin, and energy needs?",
        choices=YES_NO_CHOICES,
        widget=forms.RadioSelect
    )
class MindfulEatingForm(forms.Form):
    YES_NO_CHOICES = [
        ('yes', 'Yes'),
        ('no', 'No'),
    ]

    FREQUENCY_CHOICES = [
        ('daily', 'Daily'),
        ('few_times_week', 'Few times a week'),
        ('occasionally', 'Occasionally'),
        ('rarely', 'Rarely'),
        ('never', 'Never'),
    ]

    LAST_MEAL_CHOICES = [
        ('before_7', 'Before 7 PM'),
        ('7_to_9', '7–9 PM'),
        ('after_9', 'After 9 PM'),
    ]

    MEAL_COUNT_CHOICES = [
        ('1_2', '1–2'),
        ('3_regular', '3 regular meals'),
        ('5_small', '5 small meals'),
        ('varies', 'Varies'),
    ]

    # Questions
    mindful_eating_practice = forms.ChoiceField(
        label="Do you practice mindful eating (avoiding screens, eating slowly, focusing on food)?",
        choices=YES_NO_CHOICES,
        widget=forms.RadioSelect
    )

    number_of_meals = forms.ChoiceField(
        label="How many meals do you typically eat in a day?",
        choices=MEAL_COUNT_CHOICES,
        widget=forms.RadioSelect
    )

    eat_out_of_emotion = forms.ChoiceField(
        label="Do you tend to eat out of boredom, stress, or emotional triggers?",
        choices=YES_NO_CHOICES,
        widget=forms.RadioSelect
    )

    skip_meals_frequency = forms.ChoiceField(
        label="How often do you skip meals due to a busy schedule or intentional dieting?",
        choices=FREQUENCY_CHOICES,
        widget=forms.RadioSelect
    )

    meal_source = forms.ChoiceField(
        label="Are your meals usually prepared at home or ordered from outside?",
        choices=[('home', 'Prepared at home'), ('outside', 'Ordered from outside')],
        widget=forms.RadioSelect
    )

    fruits_vegetables_every_meal = forms.ChoiceField(
        label="Do you consume fruits and vegetables with every meal?",
        choices=YES_NO_CHOICES,
        widget=forms.RadioSelect
    )

    last_meal_time = forms.ChoiceField(
        label="How late is your last meal of the day?",
        choices=LAST_MEAL_CHOICES,
        widget=forms.RadioSelect
    )

    aware_caffeine_effects = forms.ChoiceField(
        label="Are you aware of how caffeine, alcohol, and sugary drinks affect women’s hormonal and bone health?",
        choices=YES_NO_CHOICES,
        widget=forms.RadioSelect
    )

    binge_eating_frequency = forms.ChoiceField(
        label="How often do you binge-eat unhealthy snacks while watching TV or working late?",
        choices=FREQUENCY_CHOICES,
        widget=forms.RadioSelect
    )

    interested_in_eating_challenge = forms.ChoiceField(
        label="Would you be interested in a guided 7-day healthy eating challenge for women on your wellness journey?",
        choices=YES_NO_CHOICES,
        widget=forms.RadioSelect
    )
class SelfCareForm(forms.Form):
    YES_NO_CHOICES = [
        ('yes', 'Yes'),
        ('no', 'No'),
    ]

    FREQUENCY_CHOICES = [
        ('daily', 'Daily'),
        ('few_times_week', 'Few times a week'),
        ('occasionally', 'Occasionally'),
        ('rarely', 'Rarely'),
        ('never', 'Never'),
    ]

    BREAK_FREQUENCY_CHOICES = [
        ('multiple_daily', 'Multiple times a day'),
        ('once_daily', 'Once a day'),
        ('few_times_week', 'Few times a week'),
        ('rarely', 'Rarely'),
        ('never', 'Never'),
    ]

    SELF_CARE_PRACTICES_CHOICES = [
        ('skincare', 'Skincare'),
        ('reading', 'Reading'),
        ('yoga', 'Yoga'),
        ('spa', 'Spa'),
        ('sleep_in', 'Sleep-in days'),
        ('creative_hobbies', 'Creative hobbies'),
        ('other', 'Other'),
    ]

    # Questions
    conscious_self_care_time = forms.ChoiceField(
        label="Do you consciously set aside time for self-care activities every week?",
        choices=YES_NO_CHOICES,
        widget=forms.RadioSelect
    )

    regular_self_care_practices = forms.MultipleChoiceField(
        label="What self-care practices do you regularly follow?",
        choices=SELF_CARE_PRACTICES_CHOICES,
        widget=forms.CheckboxSelectMultiple
    )

    aware_sleep_skin_digestion = forms.ChoiceField(
        label="Are you aware of how inadequate sleep, poor hydration, and stress impact your skin and digestion?",
        choices=YES_NO_CHOICES,
        widget=forms.RadioSelect
    )

    monitor_menstrual_cycle = forms.ChoiceField(
        label="Do you monitor your menstrual cycle and adjust your diet/self-care around it?",
        choices=YES_NO_CHOICES,
        widget=forms.RadioSelect
    )

    breaks_for_self_priority = forms.ChoiceField(
        label="How frequently do you take breaks from work or caregiving responsibilities to prioritize yourself?",
        choices=BREAK_FREQUENCY_CHOICES,
        widget=forms.RadioSelect
    )

    practicing_digital_detox = forms.ChoiceField(
        label="Are you practicing any digital detox routines to reduce screen fatigue and improve sleep?",
        choices=YES_NO_CHOICES,
        widget=forms.RadioSelect
    )

    treat_yourself_frequency = forms.ChoiceField(
        label="How often do you treat yourself to activities or meals that make you happy, guilt-free?",
        choices=FREQUENCY_CHOICES,
        widget=forms.RadioSelect
    )

    recognize_burnout_signs = forms.ChoiceField(
        label="Do you recognize the signs of burnout and take intentional steps to recharge?",
        choices=YES_NO_CHOICES,
        widget=forms.RadioSelect
    )

    consistent_night_routine = forms.ChoiceField(
        label="Are you following a consistent nighttime routine for better sleep and mental calmness?",
        choices=YES_NO_CHOICES,
        widget=forms.RadioSelect
    )

    interested_personalized_checklist = forms.ChoiceField(
        label="Would you like a personalized self-care checklist designed for modern, multitasking women?",
        choices=YES_NO_CHOICES,
        widget=forms.RadioSelect
    )
class EducationSurveyForm(forms.Form):
    EDUCATION_CHOICES = [
        ('information_technology', 'Information Technology'),
        ('business', 'Business'),
        ('healthcare_wellness', 'Healthcare and Wellness'),
        ('art_design', 'Art and Design'),
        ('education_teaching', 'Education & Teaching'),
        ('personal_development', 'Personal Development'),
    ]

    preferred_education_field = forms.ChoiceField(
        label="Which education field are you most interested in?",
        choices=EDUCATION_CHOICES,
        widget=forms.RadioSelect
    )
class ITForm(forms.Form):
    IT_SKILLS_CHOICES = [
        ('basic_computer_skills', 'Basic Computer Skills'),
        ('graphic_design', 'Graphic Design'),
        ('web_development', 'Web Development'),
        ('mobile_app_development', 'Mobile App Development'),
        ('social_media_marketing', 'Social Media Marketing'),
        ('data_entry', 'Data Entry'),
        ('cybersecurity_basics', 'Cybersecurity Basics'),
        ('none', 'None'),
    ]

    LEARNING_PLATFORM_CHOICES = [
        ('youtube_tutorials', 'YouTube Tutorials'),
        ('online_course_apps', 'Online Course Apps (Coursera, Udemy)'),
        ('community_workshops', 'Free Community Workshops'),
        ('none', 'None'),
    ]

    YES_NO_CHOICES = [
        ('yes', 'Yes'),
        ('no', 'No'),
    ]

    YES_NO_MAYBE_CHOICES = [
        ('yes', 'Yes'),
        ('no', 'No'),
        ('maybe', 'Maybe'),
    ]

    # Questions
    it_skills_to_learn = forms.MultipleChoiceField(
        label="Which IT skills would you like to learn?",
        choices=IT_SKILLS_CHOICES,
        widget=forms.CheckboxSelectMultiple
    )

    tried_learning_online = forms.ChoiceField(
        label="Have you ever tried learning IT skills through online videos or apps?",
        choices=YES_NO_CHOICES,
        widget=forms.RadioSelect
    )

    interested_in_it_job = forms.ChoiceField(
        label="Are you interested in working in an IT-related job from home?",
        choices=YES_NO_MAYBE_CHOICES,
        widget=forms.RadioSelect
    )

    preferred_learning_platform = forms.ChoiceField(
        label="Which digital platform would you prefer to learn through?",
        choices=LEARNING_PLATFORM_CHOICES,
        widget=forms.RadioSelect
    )

    it_skill_roadmap_interest = forms.ChoiceField(
        label="Would you be interested in receiving a beginner’s IT skill-building roadmap for women?",
        choices=YES_NO_CHOICES,
        widget=forms.RadioSelect
    )
class BusinessForm(forms.Form):
    BUSINESS_TOPICS_CHOICES = [
        ('starting_small_business', 'Starting a Small Business'),
        ('marketing_social_media', 'Marketing on Social Media'),
        ('money_accounts', 'Managing Money & Accounts'),
        ('selling_online', 'Selling Products Online'),
        ('baking_cooking', 'Baking/Cooking Business'),
        ('beauty_services', 'Beauty Services (Salon, Makeup)'),
        ('handicrafts', 'Handicrafts Business'),
        ('not_interested', 'Not interested right now'),
    ]

    YES_NO_CHOICES = [
        ('yes', 'Yes'),
        ('no', 'No'),
    ]

    LEARNING_PREFERENCE_CHOICES = [
        ('online_videos', 'Online Videos'),
        ('business_workshops', 'Women’s Business Workshops'),
        ('mentorship', 'Mentorship from successful women entrepreneurs'),
        ('not_interested', 'Not interested'),
    ]

    # Questions
    business_topics_interest = forms.MultipleChoiceField(
        label="What kind of business topics are you interested in?",
        choices=BUSINESS_TOPICS_CHOICES,
        widget=forms.CheckboxSelectMultiple
    )

    learn_selling_on_social_media = forms.ChoiceField(
        label="Would you like to learn how to sell products using social media?",
        choices=YES_NO_CHOICES,
        widget=forms.RadioSelect
    )

    manage_business_finances = forms.ChoiceField(
        label="Are you interested in managing your own business finances?",
        choices=YES_NO_CHOICES,
        widget=forms.RadioSelect
    )

    learn_customer_handling = forms.ChoiceField(
        label="Would you like to learn customer handling and business communication skills?",
        choices=YES_NO_CHOICES,
        widget=forms.RadioSelect
    )

    business_learning_preference = forms.ChoiceField(
        label="How would you prefer to learn business skills?",
        choices=LEARNING_PREFERENCE_CHOICES,
        widget=forms.RadioSelect
    )
class HealthcareWellnessForm(forms.Form):
    HEALTHCARE_TOPICS_CHOICES = [
        ('womens_health', 'Women’s Health (Periods, Pregnancy, Menopause)'),
        ('nutrition', 'Nutrition and Healthy Eating'),
        ('first_aid', 'First Aid & Emergency Care'),
        ('yoga_meditation', 'Yoga & Meditation'),
        ('mental_health', 'Mental Health Awareness'),
        ('elderly_childcare', 'Caring for Elderly or Children'),
        ('none', 'None'),
    ]

    YES_NO_CHOICES = [
        ('yes', 'Yes'),
        ('no', 'No'),
    ]

    LEARNING_PREFERENCE_CHOICES = [
        ('online_courses', 'Online Courses'),
        ('local_workshops', 'Local Health Workshops'),
        ('wellness_apps', 'Wellness Apps'),
        ('books', 'Books'),
    ]
    PERSONAL_WELLNESS_GOAL_CHOICES = [
    ('daily_yoga', 'Start daily yoga practice'),
    ('improve_sleep', 'Improve sleep routine'),
    ('eat_more_greens', 'Eat more green vegetables'),
    ('daily_walks', 'Take 30-minute walks daily'),
    ('reduce_screen_time', 'Reduce screen time before bed'),
    ('practice_mindfulness', 'Practice mindfulness or meditation'),
    ('increase_water', 'Drink more water daily'),
    ('none', 'Not sure yet'),
]

    # Questions
    healthcare_topics_interest = forms.MultipleChoiceField(
        label="Which healthcare topics would you like to learn about?",
        choices=HEALTHCARE_TOPICS_CHOICES,
        widget=forms.CheckboxSelectMultiple
    )

    certified_yoga_trainer_interest = forms.ChoiceField(
        label="Are you interested in becoming a certified yoga instructor or fitness trainer?",
        choices=YES_NO_CHOICES,
        widget=forms.RadioSelect
    )

    learn_first_aid = forms.ChoiceField(
        label="Would you like to learn basic first-aid and emergency care for your family?",
        choices=YES_NO_CHOICES,
        widget=forms.RadioSelect
    )

    health_learning_preference = forms.ChoiceField(
        label="Where would you prefer learning health and wellness skills?",
        choices=LEARNING_PREFERENCE_CHOICES,
        widget=forms.RadioSelect
    )

    personal_wellness_goal = forms.ChoiceField(
    label="What is one health or wellness goal you wish to achieve this year?",
    choices=PERSONAL_WELLNESS_GOAL_CHOICES,
    widget=forms.RadioSelect
)

class ArtDesignForm(forms.Form):
    CREATIVE_SKILLS_CHOICES = [
        ('drawing_painting', 'Drawing & Painting'),
        ('fashion_design', 'Fashion Design'),
        ('craft_making', 'Craft Making'),
        ('jewelry_designing', 'Jewelry Designing'),
        ('graphic_designing', 'Graphic Designing (Canva, Photoshop)'),
        ('photography', 'Photography'),
        ('content_creation', 'Content Creation for Instagram/YouTube'),
        ('none', 'None'),
    ]

    YES_NO_NOTSURE_CHOICES = [
        ('yes', 'Yes'),
        ('no', 'No'),
        ('not_sure', 'Not sure'),
    ]

    YES_NO_CHOICES = [
        ('yes', 'Yes'),
        ('no', 'No'),
    ]

    LEARNING_PREFERENCE_CHOICES = [
        ('youtube_tutorials', 'YouTube Tutorials'),
        ('free_online_courses', 'Free Online Courses'),
        ('paid_certification_programs', 'Paid Certification Programs'),
        ('offline_classes', 'Offline Classes'),
    ]

    # Questions
    creative_skills_interest = forms.MultipleChoiceField(
        label="Which creative skills interest you the most?",
        choices=CREATIVE_SKILLS_CHOICES,
        widget=forms.CheckboxSelectMultiple
    )

    sell_creative_work_online = forms.ChoiceField(
        label="Would you like to sell your creative work online?",
        choices=YES_NO_NOTSURE_CHOICES,
        widget=forms.RadioSelect
    )

    learn_graphic_video_editing = forms.ChoiceField(
        label="Would you like to learn graphic designing or video editing?",
        choices=YES_NO_CHOICES,
        widget=forms.RadioSelect
    )

    art_community_participation = forms.ChoiceField(
        label="Are you open to participating in art exhibitions or online art communities?",
        choices=YES_NO_CHOICES,
        widget=forms.RadioSelect
    )

    art_learning_preference = forms.ChoiceField(
        label="How would you prefer to learn art and design skills?",
        choices=LEARNING_PREFERENCE_CHOICES,
        widget=forms.RadioSelect
    )
class EducationTeachingForm(forms.Form):
    TEACHING_AREAS_CHOICES = [
        ('school_subjects', 'Teaching School Subjects'),
        ('spoken_english', 'Spoken English'),
        ('life_skills', 'Life Skills & Health Education'),
        ('art_craft_classes', 'Art & Craft Classes'),
        ('yoga_dance', 'Yoga or Dance Classes'),
        ('online_tutoring', 'Online Tutoring'),
        ('none', 'None'),
    ]

    YES_NO_MAYBE_CHOICES = [
        ('yes', 'Yes'),
        ('no', 'No'),
        ('maybe', 'Maybe'),
    ]

    YES_NO_CHOICES = [
        ('yes', 'Yes'),
        ('no', 'No'),
    ]

    LEARNING_PREFERENCE_CHOICES = [
        ('online_video_classes', 'Online Video Classes'),
        ('educator_workshops', 'Women Educator Workshops'),
        ('mentorship_programs', 'Mentorship Programs'),
    ]

    # Questions
    teaching_areas_interest = forms.MultipleChoiceField(
        label="Which teaching areas would you like to explore?",
        choices=TEACHING_AREAS_CHOICES,
        widget=forms.CheckboxSelectMultiple
    )

    join_teaching_course = forms.ChoiceField(
        label="Would you like to join a course to improve your teaching skills?",
        choices=YES_NO_MAYBE_CHOICES,
        widget=forms.RadioSelect
    )

    become_online_tutor = forms.ChoiceField(
        label="Would you like to become an online tutor for school or skill-based subjects?",
        choices=YES_NO_CHOICES,
        widget=forms.RadioSelect
    )

    improve_public_speaking = forms.ChoiceField(
        label="Do you want to improve your public speaking and classroom presentation skills?",
        choices=YES_NO_CHOICES,
        widget=forms.RadioSelect
    )

    teaching_learning_preference = forms.ChoiceField(
        label="How would you like to learn teaching skills?",
        choices=LEARNING_PREFERENCE_CHOICES,
        widget=forms.RadioSelect
    )
class PersonalDevelopmentForm(forms.Form):
    PERSONAL_GROWTH_SKILLS_CHOICES = [
        ('public_speaking', 'Public Speaking'),
        ('confidence_building', 'Confidence Building'),
        ('time_management', 'Time Management'),
        ('financial_literacy', 'Financial Literacy'),
        ('goal_setting', 'Goal Setting & Planning'),
        ('stress_management', 'Stress Management'),
        ('none', 'None'),
    ]

    YES_NO_MAYBE_CHOICES = [
        ('yes', 'Yes'),
        ('no', 'No'),
        ('maybe', 'Maybe'),
    ]

    YES_NO_CHOICES = [
        ('yes', 'Yes'),
        ('no', 'No'),
    ]

    LEARNING_METHOD_CHOICES = [
        ('motivational_videos', 'Motivational Videos'),
        ('online_courses', 'Online Courses'),
        ('support_groups', 'Women’s Support Groups'),
        ('books', 'Books'),
    ]

    # Questions
    personal_growth_skills = forms.MultipleChoiceField(
        label="Which personal growth skills would you like to learn?",
        choices=PERSONAL_GROWTH_SKILLS_CHOICES,
        widget=forms.CheckboxSelectMultiple
    )

    attend_workshops = forms.ChoiceField(
        label="Would you attend workshops on personal development for women?",
        choices=YES_NO_MAYBE_CHOICES,
        widget=forms.RadioSelect
    )

    interested_in_stress_management = forms.ChoiceField(
        label="Are you interested in learning stress management techniques?",
        choices=YES_NO_CHOICES,
        widget=forms.RadioSelect
    )

    improve_leadership_skills = forms.ChoiceField(
        label="Would you like to improve your leadership and decision-making skills?",
        choices=YES_NO_CHOICES,
        widget=forms.RadioSelect
    )

    personal_growth_learning_method = forms.ChoiceField(
        label="How do you prefer learning personal growth topics?",
        choices=LEARNING_METHOD_CHOICES,
        widget=forms.RadioSelect
    )
LOCATIONS = [
    ('', 'Select Location'),
    ('delhi', 'Delhi'),
    ('mumbai', 'Mumbai'),
    ('bangalore', 'Bangalore'),
    # Add more locations here
]

CATEGORIES = [
    ('', 'Select Category'),
    ('it', 'IT'),
    ('sales', 'Design'),
    ('healthcare', 'Healthcare'),
    ('marketing', 'Marketing'),
    # Add more categories here
]

class JobSearchForm(forms.Form):
    keyword = forms.CharField(
        required=False, 
        widget=forms.TextInput(attrs={'placeholder': 'Search Keywords...'})
    )
    location = forms.ChoiceField(
        choices=LOCATIONS,
        required=False,
        widget=forms.Select()
    )
    category = forms.ChoiceField(
        choices=CATEGORIES,
        required=False,
        widget=forms.Select()
    )
LOCATIONS1 = [
    ('', 'Select Location'),
    ('delhi', 'Delhi'),
    ('mumbai', 'Mumbai'),
    ('bangalore', 'Bangalore'),
    # Add more locations here
]

CATEGORIES1 = [
    ('', 'Select Category'),
    ('tech', 'Technology'),
    ('design', 'Design'),
    ('marketing', 'Marketing'),
    # Add more categories here
]
class CandidateSearchForm(forms.Form):
    keyword1 = forms.CharField(
        required=False, 
        widget=forms.TextInput(attrs={'placeholder': 'Search Keywords...'})
    )
    location1 = forms.ChoiceField(
        choices=LOCATIONS1,
        required=False,
        widget=forms.Select()
    )
    category1 = forms.ChoiceField(
        choices=CATEGORIES1,
        required=False,
        widget=forms.Select()
    )
class JobSearchForm(forms.Form):
    keyword = forms.CharField(required=False, widget=forms.TextInput(attrs={'placeholder': 'Keyword', 'class': 'form-control'}))
    location = forms.CharField(required=False, widget=forms.TextInput(attrs={'placeholder': 'Location', 'class': 'form-control'}))
    category = forms.ChoiceField(
        choices=[('', 'Select Category'), ('it', 'IT'), ('sales', 'Design'), ('healthcare', 'Healthcare'), ('marketing', 'Marketing')],
        required=False,
        widget=forms.Select(attrs={'class': 'form-control'})
    )

