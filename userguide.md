
# Student Task Manager - User Guide

## Introduction

The Student Task Manager is a simple Python console application that helps students manage their academic activities.

## Starting the Application

Open the terminal inside the project directory and run:

python main.py

## Available Operations

### 1. Add Task
Select option 1 and enter a task title. Empty task titles are not accepted.

### 2. Display Tasks
Select option 2 to view all available tasks and their completion status.

### 3. Exit
Select option 3 to close the application.

### 4. Complete Task
Select option 4 and enter the ID of the task you want to mark as completed.

### 5. Delete Task
Select option 5 and enter the ID of the task you want to remove.

## Input Validation

The application rejects empty task titles and invalid task identifiers.

## Running Automated Tests

Execute:

python -m unittest discover -s tests -v

The test suite checks adding, completing, and deleting tasks.

## Conclusion

The application provides basic academic task management through a simple console interface.
