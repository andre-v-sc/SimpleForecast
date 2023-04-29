Here are the installation instructions in Markdown format:

---

## Installation Guide for SimpleForecast

Follow these steps to set up the SimpleForecast project on your local machine:

### 1. Install Python

Ensure that you have Python 3.7 or higher installed on your system. You can check your Python version by running the following command:

```
python --version
```

### 2. Create a virtual environment

Navigate to the SimpleForecast project directory and create a new virtual environment using the following command:

```
python -m venv venv
```

This will create a new virtual environment named `venv` inside the project directory.

### 3. Activate the virtual environment

Activate the virtual environment by running the appropriate command for your operating system:

- **Windows:**

  ```
  venv\Scripts\activate
  ```

- **macOS/Linux:**

  ```
  source venv/bin/activate
  ```

### 4. Install dependencies

Install the required packages from the `requirements.txt` file by running the following command:

```
pip install -r requirements.txt
```

### 5. Apply migrations

Apply the database migrations by running the following command:

```
python manage.py migrate
```

### 6. Run the development server

Start the Django development server by running the following command:

```
python manage.py runserver
```

Now you should be able to access the SimpleForecast application by navigating to `http://127.0.0.1:8000/` in your web browser.

---
