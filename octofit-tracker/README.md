# OctoFit Tracker

## Overview

The OctoFit Tracker is a fitness application designed to help users track their activities, manage teams, and receive personalized workout suggestions. The app includes features such as user authentication, activity logging, competitive leaderboards, and more.

## Project Structure

The project is organized into two main directories: `backend` and `frontend`.

### Backend

The backend is built using Django and includes the following components:

- **venv/**: Contains the Python virtual environment for the backend.
- **octofit_tracker/**: The main Django application directory.
  - **\_\_init\_\_.py**: Marks the directory as a Python package.
  - **settings.py**: Contains Django settings, including database configurations and installed apps.
  - **urls.py**: Defines URL routing for the application.
  - **asgi.py**: Entry point for ASGI-compatible web servers.
  - **wsgi.py**: Entry point for WSGI-compatible web servers.
- **manage.py**: Command-line utility for interacting with the Django project.
- **requirements.txt**: Lists the required Python packages for the project.

### Frontend

The frontend is built using React and includes the following components:

- **src/**: Contains the source code for the React application.
  - **App.jsx**: The main application component.
  - **index.jsx**: Entry point for the React application.
- **package.json**: Configuration file for the frontend project, including dependencies and scripts.
- **README.md**: Documentation for the frontend part of the project.

## Getting Started

To get started with the OctoFit Tracker project, follow these steps:

1. **Clone the repository**:
   ```bash
   git clone <repository-url>
   cd octofit-tracker
   ```

2. **Set up the backend**:
   - Create a Python virtual environment:
     ```bash
     python3 -m venv backend/venv
     ```
   - Activate the virtual environment:
     ```bash
     source backend/venv/bin/activate
     ```
   - Install the required packages:
     ```bash
     pip install -r backend/requirements.txt
     ```

3. **Run the backend server**:
   ```bash
   python backend/manage.py runserver
   ```

4. **Set up the frontend**:
   - Navigate to the frontend directory and install dependencies:
     ```bash
     cd frontend
     npm install
     ```

5. **Run the frontend application**:
   ```bash
   npm start
   ```

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements or features you'd like to add.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.