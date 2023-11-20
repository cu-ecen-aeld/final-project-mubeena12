# use the official Python image as the base image
From python:3.9

# Set the working directory in the container
WORKDIR /app

# Copy requirmrnts.txt file and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the current directory contents into the container at /app
COPY . .

# Expose the port the app runs on 
EXPOSE 5500

# Set environment variables
#ENV FLASK_APP=app.py
#ENV FLASK_RUN_HOST=0.0.0.0

# Run the Flask application
#CMD ["flask", "run"]
CMD ["python", "app.py"]
