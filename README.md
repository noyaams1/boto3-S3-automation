📦 boto3 + S3 Automation Exercises
This project contains a series of Python automation exercises using the boto3 library to interact with Amazon S3. The exercises demonstrate various automation tasks such as file uploads, backups, and handling existing files on S3.

📁 Exercise 1: Automate One File Upload
Scenario:
You receive a daily image file (team_image.png) that needs to be uploaded to S3.

Script: exercise1.py

Features:

Connects to S3.

Creates a bucket named student-[yourname]-bucket.

Uploads team_image.png.

Lists the files in the bucket.

Prints a success message.


📂 Exercise 2: Upload Multiple Files Automatically
Scenario:
Backup all files from a local folder (daily_documents) to S3.

Script: exercise2.py

Features:

Creates a folder daily_documents with test .txt files.

Creates the bucket student-[yourname]-backup (if it doesn’t already exist).

Loops through the files and uploads them.

Prints the name of each file uploaded.


🚫 Exercise 3: Auto-Skip Already Uploaded Files
Scenario:
Skip uploading files that already exist in the S3 bucket.

Script: exercise3.py

Features:

Checks if each file already exists in S3.

Skips files that have already been uploaded.

Prints relevant status messages for each file.

🚀 How to Run
1. Install dependencies
bash
Copy
Edit
pip install boto3
2. Set up AWS credentials
Make sure your AWS credentials are configured. You can set them using the AWS CLI:

bash
Copy
Edit
aws configure
Or by manually editing the ~/.aws/credentials file.

3. Running the Exercises
Exercise 1:
Run the script to upload a single file to S3:

bash
Copy
Edit
python exercise1.py
Exercise 2:
Run the script to upload multiple files from the daily_documents folder:

bash
Copy
Edit
python exercise2.py
Exercise 3:
Run the script to skip already uploaded files during the upload process:

bash
Copy
Edit
python exercise3.py
⚙️ Requirements
Python 3.x

boto3 library

🔗 Links
GitHub Repository

AWS S3 Documentation

📝 More Features
📸 team_image.png
An image used in Exercise 1 to demonstrate a simple file upload to S3.

📑 exercises-screenshots.docx
Document containing screenshots from each automation exercise for visual reference.

📂 daily_documents
Folder with test .txt files used in Exercise 2 for simulating a backup process to S3.



