from django.shortcuts import render, redirect
from django.contrib import messages
import random
import string
import smtplib
from django.contrib import messages
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import ssl
from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model
from django.contrib import messages
from django.core.exceptions import ValidationError
from django.db.utils import IntegrityError
from .models import CustomUser  # Import your model here
from .forms import CustomUserForm  # Ensure this points to the correct form class
from django.utils import timezone
from django.shortcuts import render, redirect

from django.contrib import messages
from django.core.exceptions import ValidationError
from django.db.utils import IntegrityError

from django.shortcuts import render, redirect

from django.contrib import messages
from django.db.utils import IntegrityError
from django.core.exceptions import ValidationError
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login
from django.contrib import messages
from django.urls import reverse
from django.urls import reverse_lazy

# views.py
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import CustomUserForm , CustomUserFormWarehouse
from .models import CustomUser
import pytz
def get_ist_now():
    ist = pytz.timezone('Asia/Kolkata')
    utc_now = timezone.now()  # Get current time in UTC
    ist_now = utc_now.astimezone(ist)  # Convert to IST
    print(ist_now)
    return ist_now
@login_required
def manufacturing_details_view(request):
    current_user = request.user

    if request.method == 'POST':
        form = CustomUserForm(request.POST, instance=current_user)
        if form.is_valid():
            # Extract cleaned data
            CompanyName_MCU = form.cleaned_data.get('CompanyName_MCU')
            MCANumber_MCU = form.cleaned_data.get('MCANumber_MCU')
            GSTNumber_MCU = form.cleaned_data.get('GSTNumber_MCU')
            PanNumber_MCU = form.cleaned_data.get('PanNumber_MCU')
            Emailid_MCU = form.cleaned_data.get('Emailid_MCU')
            Contact_MCU = form.cleaned_data.get('Contact_MCU')
            Address_MCU = form.cleaned_data.get('Address_MCU')
            form.instance.Manufacturing_cu = 1
            form.instance.MCU_CreatedOn = get_ist_now() 
            # Print specific columns
            print('Company Name:', CompanyName_MCU)
            print('MCANumber_MCU:', MCANumber_MCU)
            print('GST Number:', GSTNumber_MCU)
            print('PAN Number:', PanNumber_MCU)
            print('Emailid_MCU:', Emailid_MCU)
            print('Contact Details:', Contact_MCU)
            print('Address:', Address_MCU)

            # Save the form data
            form.save()
            return redirect('accounts:MCU_profile')
    else:
        form = CustomUserForm(instance=current_user)

    return render(request, 'manufacturerDetails.html', {'form': form})

def MCU_profile(request):
    return render(request, 'MCU_profile.html')

def warehouse_details_view(request):
    current_user = request.user
    print(current_user)  # For debugging purposes

    if request.method == 'POST':
        print("post")
        form = CustomUserFormWarehouse(request.POST, instance=current_user)
        if form.is_valid():
            print("inside")
            # Extract cleaned data from the form
            WDRANumber_WCU = form.cleaned_data.get('WDRANumber_WCU')
            AadharNumber_WCU = form.cleaned_data.get('AadharNumber_WCU')
            CompanyName_WCU = form.cleaned_data.get('CompanyName_WCU')
            PanNumber_WCU = form.cleaned_data.get('PanNumber_WCU')
            Emailid_WCU = form.cleaned_data.get('Emailid_WCU')
            Contact_WCU = form.cleaned_data.get('Contact_WCU')
            Address_WCU = form.cleaned_data.get('Address_WCU')

            # Example of how to set additional fields
            form.instance.Warehouse_cu = 1  
            # Update the instance's field directly
            form.instance.WCU_CreatedOn = get_ist_now() 
            print("over")
            # Print specific columns for debugging
            print('WDRANumber WCU:', WDRANumber_WCU)
            print('Aadhar Number WCU:', AadharNumber_WCU)
            print('Company Name WCU:', CompanyName_WCU)
            print('PAN Number WCU:', PanNumber_WCU)
            print('Email ID WCU:', Emailid_WCU)
            print('Contact WCU:', Contact_WCU)
            print('Address WCU:', Address_WCU)

            # Save the form data
            form.save()
            return redirect('accounts:WCU_profile')  # Ensure this URL name is correct
        else:
            print('Form errors:', form.errors)  # Print form errors if validation fails
    else:
        form = CustomUserFormWarehouse(instance=current_user)

    # Render the template with the form
    return render(request, 'WarehouseDetails.html', {'form': form})
from Warehouse_Management.forms import WarehouseDetailsForm

def WCU_profile(request):
    if request.method == 'POST':
        print("POST request received")
        form = WarehouseDetailsForm(request.POST, request.FILES)
        print("Form created")

        # Print request data for debugging
        print("Request POST data:", request.POST)
        print("Request FILES data:", request.FILES)
        if form.is_valid():
            print("Form is valid")
            cleaned_data = form.cleaned_data
            print("Warehouse Name:", form.cleaned_data.get('warehouse_name'))
            print("Warehouse Location:", form.cleaned_data.get('warehouse_location'))
            print("Floor Type:", form.cleaned_data.get('floor_type'))
            print("Ground Floor Square Feet:", form.cleaned_data.get('ground_floor_square_feet'))
            print("First Floor Square Feet:", form.cleaned_data.get('first_floor_square_feet'))
            print("Warehouse Square Feet:", form.cleaned_data.get('warehouse_square_feet'))
            print("Warehouse Amount:", form.cleaned_data.get('warehouse_amount'))
            print("Additional Amount:", form.cleaned_data.get('additional_amount'))
         
            prohibited_items = request.POST.get('hiddenInput.value', '')
            print("Prohibited Items:", prohibited_items.split(','))
            print("Permitted Items:", form.cleaned_data.get('permitted_items'))
            print("Prohibited Items:", form.cleaned_data.get('prohibited_items'))
            print("Warehouse Types:", form.cleaned_data.get('warehouse_types'))
            print("Facilities:", form.cleaned_data.get('facilities'))
            # Save the form data
            form.save()
            return redirect('success_page')  # Redirect to a success page or another view
    else:
        form = WarehouseDetailsForm()

    return render(request, 'WCU_profile.html', {'form': form})

def register(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        # Generate OTP
        otp = generate_otp()
        print(otp)
       
        # Example function to send OTP via email
        send_otp_email(email, otp)
        # Store email and OTP in session for verification
        request.session['otp_email'] = email
        request.session['otp'] = otp
        # Redirect to OTP verification page
        return redirect('verify_otp')
    # If GET request or after form submission
    return render(request, 'accounts/register.html')

def verify_otp(request):
    if request.method == 'POST':
        entered_otp = request.POST.get('otp')
        saved_otp = request.session.get('otp')
        if entered_otp == saved_otp:
            # Clear OTP data from session after successful verification
            email = request.session.get('otp_email')
            del request.session['otp_email']
            del request.session['otp']
            messages.success(request, 'OTP verified successfully. You can now create your account.')
            return redirect('create_account', email=email)
        else:
            messages.error(request, 'Invalid OTP. Please try again.')
    # If GET request or after form submission
    return render(request, 'accounts/verify_otp.html')



def create_account(request, email):
    if request.method == 'POST':
        print("POST request received")
        password = request.POST.get('password')

        if not password:
            print("Password is missing")
            messages.error(request, 'Password is required.')
            return render(request, 'accounts/create_account.html', {'email': email})

        User = get_user_model()  # Fetch the custom user model

        try:
            # Check if a user with this email already exists
            existing_user = User.objects.filter(email=email).first()

            if existing_user:
                # If the user exists, update their password
                print(f"Updating password for existing user with email: {email}")
                existing_user.set_password(password)
                existing_user.save()
                print("Password updated successfully")
                messages.success(request, 'Password updated successfully. You can now log in.')
            else:
                # Create a new user if no existing user is found
                print(f"Attempting to create user with email: {email}")
                user = User.objects.create_user(email=email, password=password)
                print("User created successfully")
                messages.success(request, 'Account created successfully. You can now log in.')

            return redirect('login')
        except IntegrityError:
            print("IntegrityError: An account with this email already exists.")
            messages.error(request, 'An account with this email already exists.')
        except ValidationError as e:
            print(f"ValidationError: {e}")
            messages.error(request, f'Error: {e}')
        except Exception as e:
            print(f"Unexpected error: {e}")
            messages.error(request, f'An unexpected error occurred: {e}')

    print("Rendering create_account.html")
    return render(request, 'accounts/create_account.html', {'email': email})


def generate_otp():
    length = 6  # Length of the OTP
    letters_and_digits = string.digits  # Using only digits for OTP
    return ''.join(random.choice(letters_and_digits) for i in range(length))

def send_otp_email(email, otp):
    smtp_server = 'smtpout.secureserver.net'
    smtp_port = 465  # For SSL
    sender_email = 'saravanan@ecosoftzolutions.com'
    receiver_email = email
    password = 'Ecosoft@12345'
    subject = 'OTP Verification'  # Subject with OTP
    body = f"""
    <html>
    <head></head>
    <body>
        <p>Hello,<br>
           This is an OTP email message.<br>
           Your OTP is: {otp}<br>
           Regards,<br>
           Sender
        </p>
    </body>
    </html>
    """

    message = MIMEMultipart()
    message['From'] = sender_email
    message['To'] = receiver_email
    message['Subject'] = subject
    print(receiver_email)
    message.attach(MIMEText(body, 'html'))

    # Send the email using SMTP with SSL
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(smtp_server, smtp_port, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message.as_string())

    print("Email sent successfully.")



def login(request):
    print(f"Request method: {request.method}")
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        print(f"Received username: {username}")
        # Note: Avoid printing passwords in a real application for security reasons.
        print(f"Received password: {'*' * len(password) if password else 'None'}")  # Mask password

        user = authenticate(request, username=username, password=password)

        if user is not None:
            auth_login(request, user)
            messages.success(request, 'You are now logged in.')
           # return redirect('http://127.0.0.1:8000/warehouse/search/')
            search_url = reverse('warehouse_management:search')
            return redirect(search_url)
        else:
            messages.error(request, 'Invalid username or password.')
    print("Rendering login page")
    return render(request, 'accounts/login.html')
def password_reset(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        print(f"Received password reset request for email: {email}")
        
        User = get_user_model()  # Fetch the custom user model

        try:
            user = User.objects.get(email=email)  # Use User model class directly
            print(f"User found: {user.email}")
            
            otp = generate_otp()  # Generate OTP
            request.session['otp_email'] = email
            request.session['otp'] = otp
            print(f"Generated OTP: {otp}")
            
            send_otp_email(email, otp)  # Send OTP email
            print(f"OTP sent to: {email}")
            
            messages.success(request, 'An OTP has been sent to your email address.')
        except User.DoesNotExist:
            print(f"Email address not found: {email}")
            messages.error(request, 'Email address not found.')
        except Exception as e:
            print(f"An error occurred: {e}")
            messages.error(request, f'An error occurred: {e}')
        
        return redirect('verify_otp')  # Redirect to prevent form resubmission

    return render(request, 'accounts/password_reset.html')