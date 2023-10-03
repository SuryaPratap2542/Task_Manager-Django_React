# Task Manager Web Application

A simple Task Manager web application built with Django and React.

<img width="960" alt="image" src="https://github.com/SuryaPratap2542/Task_Manager-Django_React/assets/89827931/c6e22a32-2097-4f0a-8067-9a09b5fb09ff">
- main page displaying tasks.


## Overview

Task Manager is a web application that allows users to manage their tasks and to-do lists. It provides a user-friendly interface for creating, editing, and deleting tasks, as well as marking tasks as completed or incompleted. The backend is built with Django, which provides RESTful API endpoints for interacting with tasks, while the frontend is built with React.


<img width="960" alt="image" src="https://github.com/SuryaPratap2542/Task_Manager-Django_React/assets/89827931/8c1dff9b-5160-44c4-9e05-bd3fc5e641f9">
- "Add Task" feature.


<img width="960" alt="image" src="https://github.com/SuryaPratap2542/Task_Manager-Django_React/assets/89827931/c431abe7-164d-4d8c-835f-38aec1f9926e">
- completed tasks.


<img width="954" alt="image" src="https://github.com/SuryaPratap2542/Task_Manager-Django_React/assets/89827931/59b1ad8b-6982-47f6-969e-4a373ee255da">
- incompleted tasks.


## Features

- Create, Read, Update, and Delete tasks.
- Mark tasks as completed or incompleted.
- Filter tasks by completion status (completed/incompleted).
- User-friendly and responsive design.
- Seamless integration of Django and React.

## Getting Started

1. **Clone the repository:**

   ```bash
   git clone https://github.com/your-username/task-manager.git
   cd task-manager
   ```

2. **Backend (Django):**

   ```bash
   cd backend
   pip install -r requirements.txt
   python manage.py migrate
   python manage.py runserver
   ```

   The Django server should now be running at `http://localhost:8000`.

3. **Frontend (React):**

   ```bash
   cd frontend
   npm install
   npm start
   ```

   The React development server should now be running at `http://localhost:3000`.


## Usage

1. Access the web application by opening your web browser and navigating to `http://localhost:3000`.

2. Create a new task by clicking the "Add Task" button.

3. Edit or delete tasks using the provided buttons.

4. Mark tasks as completed or incompleted by clicking on them.

## API Endpoints

The backend Django server provides the following API endpoints:

- `GET /api/task/`: Get a list of all tasks.
- `POST /api/task/`: Create a new task.
- `GET /api/task/<task_id>/`: Get details of a specific task.
- `PUT /api/task/<task_id>/`: Update a specific task.
- `DELETE /api/task/<task_id>/`: Delete a specific task.

You can use these endpoints to interact with the task data programmatically.

## Contributing

Contributions are welcome! If you'd like to contribute to this project, please follow these guidelines:

1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Make your changes and commit them.
4. Push your changes to your forked repository.
5. Submit a pull request with a detailed description of your changes.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

