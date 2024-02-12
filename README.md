# Lost and Found Flask Web Application

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Technologies Used](#technologies-used)
- [Project Structure](#project-structure)
- [Getting Started](#getting-started)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Overview

The Lost and Found Flask Web Application is a web-based platform designed to facilitate the reporting of lost or found items. It provides a simple and intuitive interface for users to report items they have lost or found, browse the latest reported items, and view detailed information about individual items.

## Features

- **Report Lost Items**: Users can report items they have lost by providing details such as the item's name, location where it was lost, date, description, and their contact information. They can also upload a photo of the lost item.
- **Report Found Items**: Similarly, users can report items they have found by providing details such as the item's name, location where it was found, date, description, and their contact information. They can also upload a photo of the found item.
- **View Latest Items**: The application displays the latest reported lost and found items on the home page, allowing users to quickly browse through them to see if any match their lost or found items.
- **View Item Details**: Users can click on individual items to view detailed information about them, including the item's name, location, date, description, contact information, and photo (if available).

## Technologies Used

The Lost and Found Flask Web Application is built using the following technologies:

- **Flask**: Python-based web application framework used for building the backend of the application.
- **MySQL**: Relational database management system used for storing and managing data about lost and found items.
- **SQLAlchemy**: Python SQL toolkit and Object-Relational Mapping (ORM) library used for interacting with the MySQL database.
- **HTML/CSS**: Frontend languages used for designing the user interface and styling the web pages.
- **Bootstrap**: Frontend framework used for enhancing the design and responsiveness of the web pages.

## Project Structure

The project follows a typical Flask application structure, organized into the following main components:

- **app.py**: Main application file containing the Flask routes and logic for handling requests.
- **database.py**: File containing the database configuration and functions for interacting with the MySQL database.
- **templates/**: Directory containing HTML templates for different pages of the web application.
