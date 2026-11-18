
# Student Task Manager

A Python-based console application designed to help students organize and manage their academic tasks.

## Features

- Add new tasks
- Display all tasks
- Validate task titles
- Mark tasks as completed
- Delete tasks using task IDs
- Handle invalid user input
- Automated unit testing
- GitHub Actions CI workflow

## Technologies Used

- Python 3
- Git
- GitHub
- Python unittest
- GitHub Actions

## Project Structure

```text
studenttaskmanager/
│
├── main.py
├── tests/
│   └── test_main.py
├── docs/
│   └── userguide.md
├── .github/
│   └── workflows/
│       └── python-tests.yml
├── README.md
├── .gitignore
└── LICENSE
```

## Setup Instructions

1. Clone the repository:

   git clone https://github.com/Hamza1889763/studenttaskmanager.git

2. Open the project directory:

   cd studenttaskmanager

3. Run the application:

   python main.py

## Usage

Choose an option from the console menu:

1. Add Task
2. Display Tasks
3. Exit
4. Complete Task
5. Delete Task

Enter the relevant task ID when completing or deleting a task.

## Running Tests

Run the following command:

python -m unittest discover -s tests -v

The tests verify task creation, completion, and deletion.

## GitHub Actions

GitHub Actions automatically executes the unit tests when changes are pushed to the main branch or when a Pull Request targets main.

## License

This project is licensed under the MIT License.
