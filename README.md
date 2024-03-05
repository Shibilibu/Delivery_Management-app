# Delivery Management App

The Delivery Management App is a web-based application designed to streamline the process of managing deliveries for a delivery service. It provides various features such as user authentication, capturing delivery details, viewing delivery details, and resetting passwords.

## Features
1. **User Authentication**: Users can securely log in using their username and password.
2. **Capture Delivery Details**: Users can capture delivery details, including ticket name, type of photo (item or invoice), and upload corresponding photos.
3. **View Delivery Details**: Admin users can view all delivery details, including ticket name, delivery date, image type, and image file.
4. **Password Reset**: Users can reset their passwords by providing their email address.

## Technologies Used
- **Frontend**: HTML, CSS, JavaScript
- **Backend**: Django (Python web framework)
- **Database**: SQLite (default for Django development)

## File Structure
- **Admin/**
  - `AdminHomePage.html`: HTML template for the admin homepage.
  - `Delivery_Details_view.html`: HTML template for viewing delivery details in the admin panel.
- **User/**
  - `UserHomePage.html`: HTML template for the user homepage.
- `Forget_password.html`: HTML template for the password reset page.
- **static/**
  - `style.css`: CSS file for styling common elements.
  - `capture_style.css`: CSS file for styling the capture photo form.
  - `details.css`: CSS file for styling the delivery details view.
  - `capture.png`: Image used as a capture button.
- `Homepage.html`: HTML template for the landing page.
- `login_to_app.py`: Django view function for user authentication.
- `signup_form.py`: Django view function for user registration.
- `store_captured.py`: Django view function for storing captured delivery details.
- `password_change_page.py`: Django view function for rendering the password reset page.
- `forget_pswd.py`: Django view function for handling password reset requests.

## Setup Instructions
1. Clone the repository to your local machine.
2. Navigate to the project directory.
3. Install the required dependencies using `pip install -r requirements.txt`.
4. Run the Django development server using `python manage.py runserver`.
5. Access the application through your web browser at `http://localhost:8000`.

## Usage
1. Visit the login page and log in with your username and password.
2. Capture delivery details by filling out the form and uploading photos.
3. View delivery details in the admin panel.
4. Reset your password if needed by providing your email address.

## Contributors
-Muhammed Shibile PP - Developer

## License
This project is licensed under the MIT License.
