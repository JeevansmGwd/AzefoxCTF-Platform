## Use official Python image as base
#FROM python:3.10
#
## Set the working directory
#WORKDIR /app
#
## Copy project files to the container
#COPY . /app
#
## Install dependencies
#RUN pip install --no-cache-dir -r requirements.txt
#
## Expose the port Django runs on
#EXPOSE 8000
#
## Run Django server
#CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
#
# Use an official Nginx image  git checkout -b front-end-templates

FROM nginx:latest

# Set the working directory inside the container
#WORKDIR /usr/share/nginx/html

# Copy the default Nginx configuration file (optional)
COPY nginx.conf /etc/nginx/nginx.conf

# Expose port 80 to access the site
EXPOSE 80

# Start Nginx
CMD ["nginx", "-g", "daemon off;"]
