# CTF Platform

This project is a Django-based Capture The Flag (CTF) platform designed for users to participate in various challenges. It includes user authentication and a dedicated challenges page where users can view and join challenges.

## Features

- **User Authentication**: A secure login and registration system for users.
- **Challenges Page**: A dedicated page displaying various challenges with descriptions and participation options.
- **Dockerized Environment**: The application can be easily deployed using Docker.

## Prerequisites

- Python 3.x
- Django 5.1.6
- MySQL database
- Docker (for containerization)

## Installation and Setup

### Setting Up a Virtual Environment
1. Create a virtual environment:

   ```bash
   python -m venv venv
   ```

2. Activate the virtual environment:
   - On Windows:
     ```bash
     venv\Scripts\activate
     ```
   - On macOS/Linux:
     ```bash
     source venv/bin/activate
     ```

### Installation
1. Clone the repository:

   ```bash
   git clone https://github.com/JeevansmGwd/CTF_Platform
   cd CTF_Platform
   ```

2. Install the required packages:

   ```bash
   pip install -r requirements.txt
   ```

3. Set up the database in `backend/settings.py` with your MySQL credentials.

4. Create a MySQL database and user:
   ```sql
   CREATE DATABASE mydatabase;
   CREATE USER 'myuser'@'localhost' IDENTIFIED BY 'mypassword';
   GRANT ALL PRIVILEGES ON mydatabase.* TO 'myuser'@'localhost';
   FLUSH PRIVILEGES;
   ```

5. Run the migrations:

   ```bash
   python manage.py migrate
   ```

6. Start the development server:

   ```bash
   python manage.py runserver
   ```

7. Access the application by navigating to `http://localhost:8000` in your browser.

## Django Framework
Django is a high-level Python web framework that encourages rapid development and clean, pragmatic design. It provides built-in features such as an admin panel, ORM, and security features.

## MySQL Database
MySQL is a widely used relational database management system. It is known for its reliability and performance. Users will need to create a database and user for the application.

## Contributing

### Pro Tips for Installing Docker
1. **Installing Docker**:
   - Ensure that your system meets the [Docker installation requirements](https://docs.docker.com/get-docker/).
   - Follow the official installation guide for your operating system (Windows, macOS, or Linux).

2. **Setting Up Docker**:
   - After installation, verify that Docker is running by executing `docker --version` in your terminal.
   - Use `docker-compose` for easier management of multi-container applications. Ensure it is installed alongside Docker.

3. **Common Errors and Solutions**:
   - **Error: "Cannot connect to the Docker daemon"**: Ensure that Docker is running. On Windows, you may need to start Docker Desktop.
   - **Error: "Permission denied"**: This may occur when trying to run Docker commands without sufficient permissions. On Linux, consider adding your user to the `docker` group with `sudo usermod -aG docker $USER`.
   - **Error: "Image not found"**: Ensure that the image name is correct and that you have built the image before running the container.

Contributions are welcome! Please feel free to fork the repository, make your changes, and submit a pull request.

## 🚀 About Me

Motivated developer with a focus on testing, validating, and securing software applications. I’m passionate about making development processes more efficient, delivering high-quality and secure results. Eager to bring skills, security expertise, and fresh ideas to a dynamic team while continuing to improve my software development and cybersecurity expertise.

## 🔗 Links

[![linkedin](https://img.shields.io/badge/linkedin-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](www.github.com/JeevansmGwd)
[![twitter](https://img.shields.io/badge/twitter-1DA1F2?style=for-the-badge&logo=twitter&logoColor=white)](www.x.com/Jeevansm_Gowda)

## Other Common Github Profile Sections

🔭 I’m currently working on Aiml-Based Insider Threat Detection

🌱 I’m currently learning Automation using Python

👯 I’m looking to collaborate on Security Related and Development Projects

🤝 I’m looking for help with Development Projects

👨‍💻 All of my projects are available at www.github.com/JeevansmGwd

💬 Ask me about Security, Development

📫 How to reach me jeevansm99@gmail.com

📄 Know about my experiences www.linkedin.com/in/jeevansmgwd
