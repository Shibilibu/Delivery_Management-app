
The Delivery Management App is a web-based application designed to streamline the process of managing deliveries for a delivery service. It allows users to log in, capture delivery details including photos, view delivery details, and reset passwords if needed.

Features
User Authentication: Users can log in securely using their username and password.
Capture Delivery Details: Users can capture delivery details including ticket name, type of photo (item or invoice), and upload corresponding photos.
View Delivery Details: Admin users can view all delivery details including ticket name, delivery date, image type, and image file.
Password Reset: Users can reset their passwords by providing their email address.
Technologies Used
Frontend: HTML, CSS, JavaScript
Backend: Django (Python web framework)
Database: SQLite (default for Django development)
File Structure
Admin/AdminHomePage.html: HTML template for the admin homepage.
Admin/Delivery_Details_view.html: HTML template for viewing delivery details in the admin panel.
User/UserHomePage.html: HTML template for the user homepage.
Forget_password.html: HTML template for the password reset page.
static/:
style.css: CSS file for styling common elements.
capture_style.css: CSS file for styling the capture photo form.
details.css: CSS file for styling the delivery details view.
capture.png: Image used as a capture button.
Homepage.html: HTML template for the landing page.
login_to_app: Django view function for user authentication.
signup_form: Django view function for user registration.
store_captured: Django view function for storing captured delivery details.
password_change_page: Django view function for rendering the password reset page.
forget_pswd: Django view function for handling password reset requests.
Setup Instructions
Clone the repository to your local machine.
Navigate to the project directory.
Install the required dependencies using pip install -r requirements.txt.
Run the Django development server using python manage.py runserver.
Access the application through your web browser at http://localhost:8000.
Usage
Visit the login page and log in with your username and password.
Capture delivery details by filling out the form and uploading photos.
View delivery details in the admin panel.
Reset your password if needed by providing your email address.
Contributors
Muhammed Shibile PP - Developer
License
This project is licensed under the MIT License.

