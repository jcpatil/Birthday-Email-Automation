import smtplib
import pandas as pd
from datetime import datetime
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage

# Load employee data from CSV file
def load_employee_data():
    return pd.read_csv('/home/vmukti/employees/dob1.csv')  # Path to your CSV file

# Send email function
def send_email(to_email, subject, body, is_birthday_email=False):
    sender_email = "enter sender mail address"  # Your email address
    sender_password = "enter app password"  # Your email app password

    try:
        msg = MIMEMultipart('related')  # Use 'related' to support embedded images in the email body
        msg['From'] = sender_email
        msg['To'] = to_email
        msg['Subject'] = subject

        # Create the MIMEText object for the email body
        html_part = MIMEText(body, 'html')
        msg.attach(html_part)

        # If it's the birthday email, embed the image in the email body
        if is_birthday_email:
            with open('/path/to/your/birthday_image.jpg', 'rb') as img:
                img_data = img.read()
                image = MIMEImage(img_data, name="birthday_image.jpg")
                # Assign a content ID to the image so we can reference it in the HTML
                image.add_header('Content-ID', '<birthday_image.jpg>')
                msg.attach(image)

        # Sending the email
        with smtplib.SMTP('smtp.gmail.com', 587) as server:
            server.starttls()  # Secure the connection
            server.login(sender_email, sender_password)
            server.send_message(msg)
            print(f"Email sent to {to_email}")
    except Exception as e:
        print(f"Failed to send email to {to_email}: {e}")

# Check birthdays and send emails
def check_and_send_birthday_emails():
    today = datetime.now().strftime('%m/%d')
    data = load_employee_data()
    sent_birthday_emails = []
    found_birthday = False

    for _, row in data.iterrows():
        try:
            # Ensure the 'Date of Birth' is treated as a string and parse it
            dob_str = str(row['Date of Birth']).strip()
            if not dob_str or pd.isna(dob_str):
                print(f"Skipping record for {row['Name']}: Date of Birth is missing or invalid")
                continue

            birthday = datetime.strptime(dob_str, '%m/%d/%Y').strftime('%m/%d')
        except (ValueError, TypeError) as e:
            print(f"Error processing record for {row['Name']}: {e}")
            continue

        if birthday == today:
            found_birthday = True
            # Prepare the HTML birthday email content with embedded image
            birthday_email_body = f"""
                <html>
                    <body style="font-family: Arial, sans-serif; color: #333;">
                        <h1 style="color: #ff6347;">🎉 Happy Birthday, {row['Name']}! 🎂</h1>
                        <p style="font-size: 20px; font-weight: bold;">Wishing you a wonderful day filled with love, joy, and laughter. 🎈</p>
                        <p style="font-size: 18px;">May this year bring you lots of happiness and success!</p>
                        <img src="cid:birthday_image.jpg" alt="Birthday Cake" style="max-width: 100%; height: auto; border: 0;"/>
                        <p style="font-size: 16px; color: #555;">Best wishes from all of us at the company! 🎉</p>
                    </body>
                </html>
            """
            send_email(
                row['Email'],
                "🎂 Happy Birthday!",
                birthday_email_body,
                is_birthday_email=True
            )
            sent_birthday_emails.append(row['Email'])

            # Notify other employees
            others = data[data['Email'] != row['Email']]
            for _, other in others.iterrows():
                # Prepare the HTML notification email content
                notification_email_body = f"""
                    <html>
                        <body style="font-family: Arial, sans-serif; color: #333;">
                            <h2 style="color: #4682b4;">🎉 Birthday Notification</h2>
                            <p style="font-size: 18px;">Today is {row['Name']}'s birthday! Don't forget to wish them!</p>
                            <p style="font-size: 16px;">Let's make their day special! 🎈</p>
                        </body>
                    </html>
                """
                send_email(
                    other['Email'],
                    "🎉 Birthday Alert!",
                    notification_email_body
                )
                
    if sent_birthday_emails:
        print(f"Birthday emails sent to: {', '.join(sent_birthday_emails)}")
    else:
        if not found_birthday:
            print("No birthdays today.")
        else:
            print("All birthday emails sent successfully.")

# Main function
if __name__ == "__main__":
    check_and_send_birthday_emails()

