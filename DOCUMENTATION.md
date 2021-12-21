## Steps to make your own YouTube Search

---

### Generate YouTube data API key

- Navigate to [Google Developer Console](https://console.developers.google.com/)
- Click on current project beside the Google Cloud Platform logo
- A modal pops up listing all your current projects
- Click on new project on the top and create a new project
- Name your project as per your preference and click on create project button
- Once the project is created, click on enable APIs and services tab in dashboard
- Search for YouTube data API and enable it
- Now go to credentials and create API key
- Generate as many as you want so that we'll use new once once the quota for one exhausts

### Setup Django environment and basic Setup

- Navigate to your preferred folder in either command prompt / your preferred terminal.
- Enter the below command to create a virtual environment. You can replace `myvenv` with your preferred name
  ```
  python -m venv myvenv
  ```
- Start the virutal environment using the command
  ```
  myvenv\Scripts\activate
  ```
  You can see your environment name to the left of command line if it's activated
- Upgrade pip if you're using older versions
  ```
  python -m pip install --upgrade pip
  ```
- Create a requirements.txt file in the same folder
- Add the following lines in requirements.txt

  ```
  Django~=4.0
  requests~=2.26.0
  djangorestframework~=3.13.1
  ```

- Install all required package using the following command in terminal
  ```
  pip install -r requirements.txt
  ```
- Create your Django project

  ```
  django-admin startproject ytsearchapi
  ```

- Now, move inside the project and create a new app for search
  ```
  cd ytsearchapi
  python manage.py startapp ytsearch
  ```
- Inside `settings.py` file of your ytsearch api add `rest_framework` and `ytsearch` inside the INSTALLED_APPS list.

- Inside the same file add the following lines to add REST_FRAMEWORK settings
  ```py
  REST_FRAMEWORK = {
    # Use Django's standard `django.contrib.auth` permissions,
    # or allow read-only access for unauthenticated users.
    'DEFAULT_PERMISSION_CLASSES': [
      'rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly'
    ]
  }
  ```
- Run the app using the following command
  ```
  python manage.py runserver
  ```
