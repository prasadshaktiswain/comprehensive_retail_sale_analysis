# Use an official Python runtime as a parent image
FROM python:3.11-slim

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Copy the CSV file into the container
COPY comprehensive_retail_sale_analysis/SampleSuperstore.csv  /app/comprehensive_retail_sale_analysis/SampleSuperstore.csv

# Install any needed packages specified in requirements.txt
RUN pip install -r requirements.txt

# Make port 80 available to the world outside this container
EXPOSE 80

# Run innovative_byte.py when the container launches
CMD ["python", "innovative_byte.py"]