# # # from django.shortcuts import render

# # # # Create your views here.
# # # from django.http import JsonResponse
# # # from django.views.decorators.csrf import csrf_exempt
# # # from .models import Patient, Doctor, Report, APIKey
# # # import json

# # # @csrf_exempt
# # # def register_patient(request):
# # #     if request.method == "POST":
# # #         data = json.loads(request.body)
# # #         patient = Patient.objects.create(**data)
# # #         return JsonResponse({"message": "Patient registered successfully", "id": patient.id})

# # # @csrf_exempt
# # # def register_doctor(request):
# # #     if request.method == "POST":
# # #         data = json.loads(request.body)
# # #         doctor = Doctor.objects.create(**data)
# # #         return JsonResponse({"message": "Doctor registered successfully", "id": doctor.id})

# # # @csrf_exempt
# # # def upload_report(request):
# # #     if request.method == "POST" and request.FILES:
# # #         patient_id = request.POST.get("patient_id")
# # #         report_file = request.FILES["report"]
# # #         patient = Patient.objects.get(id=patient_id)
# # #         report = Report.objects.create(patient=patient, report_file=report_file)
# # #         return JsonResponse({"message": "Report uploaded successfully", "id": report.id})

# # # @csrf_exempt
# # # def generate_api_key(request):
# # #     if request.method == "POST":
# # #         api_key = APIKey.objects.create()
# # #         return JsonResponse({"api_key": str(api_key.key)})

# # from django.http import JsonResponse
# # from django.shortcuts import render
# # from django.views.decorators.csrf import csrf_exempt
# # from .models import Patient, Doctor, Report, APIKey
# # import json


# # @csrf_exempt
# # def register_patient(request):
# #     if request.method == "POST":
# #         data = json.loads(request.body)
# #         patient = Patient.objects.create(**data)
# #         return JsonResponse({"message": "Patient registered successfully", "id": patient.id})

# # @csrf_exempt
# # def register_doctor(request):
# #     if request.method == "POST":
# #         data = json.loads(request.body)
# #         doctor = Doctor.objects.create(**data)
# #         return JsonResponse({"message": "Doctor registered successfully", "id": doctor.id})

# # @csrf_exempt
# # def upload_report(request):
# #     if request.method == "POST" and request.FILES:
# #         patient_id = request.POST.get("patient_id")
# #         report_file = request.FILES["report"]
# #         patient = Patient.objects.get(id=patient_id)
# #         report = Report.objects.create(patient=patient, report_file=report_file)
# #         return JsonResponse({"message": "Report uploaded successfully", "id": report.id})
# #     return JsonResponse({"error": "Invalid request"}, status=400)

# # @csrf_exempt
# # def generate_api_key(request):
# #     if request.method == "POST":
# #         api_key = APIKey.objects.create()
# #         return JsonResponse({"api_key": str(api_key.key)})
    
# # def list_api_keys(request):
# #     api_keys = APIKey.objects.values("id", "key", "created_at")
# #     return JsonResponse({"api_keys": list(api_keys)})


# # # def home(request):
# # #     return render(request, 'home.html')

# # from django.shortcuts import render

# # def home(request):
# #     return render(request, 'home.html')

# # def register_patient_view(request):
# #     return render(request, 'register_patient.html')

# # def upload_report_view(request):
# #     return render(request, 'upload_report.html')

# # def api_section_view(request):
# #     return render(request, 'api_section.html')

# from django.http import JsonResponse
# from django.shortcuts import render, get_object_or_404
# from django.views.decorators.csrf import csrf_exempt
# from .models import Patient, Doctor, Report, APIKey
# import json
# import uuid

# @csrf_exempt
# def register_patient(request):
#     if request.method == "POST":
#         try:
#             data = json.loads(request.body)
#             required_fields = ["name", "age", "gender", "contact_number", "email", "address", "problem"]

#             # Check if all required fields are present
#             if not all(field in data for field in required_fields):
#                 return JsonResponse({"error": "Missing required fields"}, status=400)

#             # Create the patient
#             patient = Patient.objects.create(**data)
#             return JsonResponse({"message": "Patient registered successfully", "id": patient.id})
        
#         except json.JSONDecodeError:
#             return JsonResponse({"error": "Invalid JSON data"}, status=400)

# @csrf_exempt
# def register_doctor(request):
#     if request.method == "POST":
#         try:
#             data = json.loads(request.body)
#             required_fields = ["name", "age", "gender", "contact_number", "email", "address", "specialization", "experience"]

#             if not all(field in data for field in required_fields):
#                 return JsonResponse({"error": "Missing required fields"}, status=400)

#             doctor = Doctor.objects.create(**data)
#             return JsonResponse({"message": "Doctor registered successfully", "id": doctor.id})
        
#         except json.JSONDecodeError:
#             return JsonResponse({"error": "Invalid JSON data"}, status=400)

# @csrf_exempt
# def upload_report(request):
#     if request.method == "POST":
#         patient_id = request.POST.get("patient_id")
        
#         if not patient_id:
#             return JsonResponse({"error": "Patient ID is required"}, status=400)

#         report_file = request.FILES.get("report")
#         if not report_file:
#             return JsonResponse({"error": "No report file uploaded"}, status=400)

#         # Get patient and handle the case if not found
#         patient = get_object_or_404(Patient, id=patient_id)

#         # Create report entry
#         report = Report.objects.create(patient=patient, report_file=report_file)
#         return JsonResponse({"message": "Report uploaded successfully", "id": report.id})

#     return JsonResponse({"error": "Invalid request"}, status=400)

# @csrf_exempt
# def generate_api_key(request):
#     if request.method == "POST":
#         api_key = APIKey.objects.create(key=str(uuid.uuid4()))
#         return JsonResponse({"api_key": api_key.key})

# def list_api_keys(request):
#     api_keys = APIKey.objects.values("id", "key", "created_at")
#     return JsonResponse({"api_keys": list(api_keys)})

# # Views for rendering HTML pages
# def home(request):
#     return render(request, 'home.html')

# def register_patient_view(request):
#     return render(request, 'register_patient.html')

# def upload_report_view(request):
#     return render(request, 'upload_report.html')

# def api_section_view(request):
#     return render(request, 'api_section.html')

from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from .models import Patient, Doctor, Report, APIKey
import uuid

def home(request):
    return render(request, 'home.html')


def base(request):
    return render(request, 'base.html')


def patient(request):
    return render(request, 'register_patient.html')


def doctor(request):
    return render(request, 'register_doctor.html')


def report(request):
    return render(request, 'upload_reports.html')


def api(request):
    return render(request, 'api_section.html')

# Register patient with form submission
def register_patient_view(request):
    if request.method == "POST":
        name = request.POST.get("name")
        age = request.POST.get("age")
        gender = request.POST.get("gender")
        contact_number = request.POST.get("contact_number")
        email = request.POST.get("email")
        address = request.POST.get("address")
        problem = request.POST.get("problem")

        if not all([name, age, gender, contact_number, email, address, problem]):
            return render(request, "register_patient.html", {"error": "All fields are required."})

        # Save patient to the database
        Patient.objects.create(
            name=name, age=age, gender=gender, contact_number=contact_number, 
            email=email, address=address, problem=problem
        )

        return redirect("home")  # Redirect to home page after successful registration

    return render(request, "register_patient.html")


# Register doctor with form submission
def register_doctor_view(request):
    if request.method == "POST":
        name = request.POST.get("name")
        age = request.POST.get("age")
        gender = request.POST.get("gender")
        contact_number = request.POST.get("contact_number")
        email = request.POST.get("email")
        address = request.POST.get("address")
        specialization = request.POST.get("specialization")
        experience = request.POST.get("experience")

        if not all([name, age, gender, contact_number, email, address, specialization, experience]):
            return render(request, "register_doctor.html", {"error": "All fields are required."})

        # Save doctor to the database
        Doctor.objects.create(
            name=name, age=age, gender=gender, contact_number=contact_number, 
            email=email, address=address, specialization=specialization, experience=experience
        )

        return redirect("home")  # Redirect to home page after successful registration

    return render(request, "register_doctor.html")


# Upload report from HTML form
def upload_report_view(request):
    if request.method == "POST":
        patient_id = request.POST.get("patient_id")
        report_file = request.FILES.get("report")

        if not patient_id or not report_file:
            return render(request, "upload_report.html", {"error": "Patient ID and report file are required."})

        patient = get_object_or_404(Patient, id=patient_id)
        
        # Save report to database
        Report.objects.create(patient=patient, report_file=report_file)

        return redirect("home")  # Redirect to home page after successful upload

    return render(request, "upload_report.html")


# Generate API Key
@csrf_exempt
def generate_api_key(request):
    if request.method == "POST":
        api_key = APIKey.objects.create(key=str(uuid.uuid4()))
        return JsonResponse({"api_key": api_key.key})
    else:
        redirect('generate_api_key')

# List API Keys
def list_api_keys(request):
    api_keys = APIKey.objects.values("id", "key", "created_at")
    return JsonResponse({"api_keys": list(api_keys)})

# Home Page
# def home(request):
#     return render(request, "base.html")  # Redirecting to base.html as the main page


from django.shortcuts import render
from .models import Report

def display_reports(request):
    reports = Report.objects.all()  # Fetch all reports from the database
    return render(request, 'display_reports.html', {'reports': reports})




from django.shortcuts import render, redirect
from django.http import JsonResponse
from .models import APIKey
import uuid

def generate_api_key_view(request):
    if request.method == "POST":
        user = request.POST.get("user")

        if not user:
            return JsonResponse({"error": "User field is required"}, status=400)

        # Generate and save API key
        api_key = APIKey.objects.create(user=user, key=str(uuid.uuid4()))

        return render(request, "api_key_success.html", {"api_key": api_key})

    return render(request, "generate_api_key.html")





from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.core.exceptions import ObjectDoesNotExist
from .models import APIKey, Patient
import json
from difflib import SequenceMatcher

def validate_api_key(api_key):
    """Check if API key is valid."""
    try:
        key_obj = APIKey.objects.get(key=api_key)
        return key_obj.user  # Return the user associated with the API key
    except APIKey.DoesNotExist:
        return None

def calculate_similarity_score(submitted_data, existing_patient):
    """Calculate similarity score between submitted data and existing patient records."""
    score = 0
    total_fields = 6  # Number of fields used for comparison

    # Check each field and increase score based on similarity
    if submitted_data.get("name") and existing_patient.name:
        score += SequenceMatcher(None, submitted_data["name"].lower(), existing_patient.name.lower()).ratio() * 100

    if submitted_data.get("age") == existing_patient.age:
        score += 100  # Exact match on age

    if submitted_data.get("gender") and existing_patient.gender:
        if submitted_data["gender"].lower() == existing_patient.gender.lower():
            score += 100  # Exact match on gender

    if submitted_data.get("contact_number") and existing_patient.contact_number:
        if submitted_data["contact_number"] == existing_patient.contact_number:
            score += 100  # Exact match on contact number

    if submitted_data.get("email") and existing_patient.email:
        if submitted_data["email"].lower() == existing_patient.email.lower():
            score += 100  # Exact match on email

    if submitted_data.get("problem") and existing_patient.problem:
        score += SequenceMatcher(None, submitted_data["problem"].lower(), existing_patient.problem.lower()).ratio() * 100

    return int(score / total_fields)  # Normalize the score

@csrf_exempt
def check_patient_record(request):
    """Check submitted patient details against database and return a match score."""
    if request.method != "POST":
        return JsonResponse({"error": "Invalid request method"}, status=405)

    try:
        data = json.loads(request.body)
    except json.JSONDecodeError:
        return JsonResponse({"error": "Invalid JSON data"}, status=400)

    api_key = request.headers.get("X-API-KEY")
    if not api_key:
        return JsonResponse({"error": "API key is required"}, status=400)

    user = validate_api_key(api_key)
    if not user:
        return JsonResponse({"error": "Invalid API key"}, status=403)

    # Extract patient details from the request
    patient_name = data.get("name")
    patient_age = data.get("age")
    patient_gender = data.get("gender")
    patient_contact = data.get("contact_number")
    patient_email = data.get("email")
    patient_problem = data.get("problem")

    if not (patient_name and patient_age and patient_gender and patient_contact and patient_email and patient_problem):
        return JsonResponse({"error": "All fields are required"}, status=400)

    # Try to find a matching patient in the database
    patients = Patient.objects.all()
    best_match_score = 0
    best_match_patient = None

    for patient in patients:
        score = calculate_similarity_score(data, patient)
        if score > best_match_score:
            best_match_score = score
            best_match_patient = patient

    # Return match score
    return JsonResponse({
        "message": "Patient record checked successfully",
        "submitted_by": user,
        "match_score": best_match_score,
        "best_match_patient": best_match_patient.name if best_match_patient else "No match found"
    })

