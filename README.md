# Birthday-Email-Automation
Sends personalized HTML birthday emails with embedded images to employees celebrating their birthday. Notifies other employees about the birthday.


Features
Birthday Greeting

Sends a personalized HTML email to employees on their birthday with an embedded image.
Colleague Notification

Notifies other employees about the birthday so they can wish their colleague.
Error Handling

Handles missing or invalid date formats gracefully, ensuring no interruptions.


CSV File Format
The dob1.csv file should contain the following columns:

Column Name	Description	Example
Name	Employee name	John Doe
Email	Employee email address	john.doe@email.com
Date of Birth	Birthdate (MM/DD/YYYY format)	01/01/1990


Requirements
Python 3.7 or above
Internet connection for email sending
Dependencies
Install the required Python libraries:
pip install pandas


Setup Instructions
Download the Script

Place the script (birthday_email_automation.py) in your project directory.
Prepare Employee Data

Create a dob1.csv file in the employees/ folder with employee details.
Add a Birthday Image

Save an image (birthday_image.jpg) in the employees/ folder. This will be embedded in the birthday emails.
Configure Email Credentials

Update the following variables in the script:
sender_email: Your email address
sender_password: Your email app password (Get App Password)

How to Run the Script
Open a terminal or command prompt.
Navigate to the directory containing the script.
Run the following command:
python birthday_email_automation.py



How It Works
Step 1: Reads employee data from dob1.csv.
Step 2: Checks today's date against employees' dates of birth.
Step 3: Sends personalized birthday emails if a match is found.
Step 4: Notifies other employees about the birthday.
If no birthdays are found, it logs a message: "No birthdays today."

Customization Options
Email Content:
Edit the HTML content in the send_email function to personalize the email message.
File Paths:
Update the paths for dob1.csv and birthday_image.jpg if they are in a different directory.


How to Get a Gmail App Password
Follow these steps to generate an App Password for your Gmail account. This password will allow the script to send emails securely without exposing your main Gmail password.

Steps:
Enable 2-Step Verification
App passwords are only available if 2-Step Verification is enabled. To enable it:

**Go to your Google Account Security Page ???** 
Scroll down to the "Signing in to Google" section.
Click on "2-Step Verification" and follow the instructions to set it up.
Access the App Passwords Page

After enabling 2-Step Verification, return to the "Security" section of your Google Account.
Under "Signing in to Google," look for "App Passwords" and click on it.
Generate an App Password

You may need to re-enter your Google account password.
In the "Select app" dropdown, choose "Mail."
In the "Select device" dropdown, choose "Other (Custom name)" and type a name like Birthday Script.
Click "Generate."
Copy the App Password

A 16-character password will appear in a yellow box.
Copy this password. You will need to paste it into the sender_password variable in the script.
Save the Password Securely

Keep the App Password private and avoid sharing it.
Use it only in the script to authenticate the email-sending process.

