from django.shortcuts import render, redirect, HttpResponse
import csv
from .forms import CSVUploadForm
from .models import Employee

def handle_uploaded_csv(csv_file):
    decoded_file = csv_file.read().decode('utf-8').splitlines()
    csv_reader = csv.reader(decoded_file)

    # Assuming your CSV file has headers (first row)
    headers = next(csv_reader) # [headers]
    print(headers)
    for row in csv_reader: # 10
        employee_data = dict(zip(headers, row)) # {"first_name": "aa", "last_name": "bb", "email": "aa@gmail.com"}  #In Python, the zip function is used to combine two or more iterables (lists, tuples, etc.) element-wise into tuples
        print("employee_data:-  ", employee_data)
        Employee.objects.create(**employee_data)


def upload_csv(request):   #first argumanet is always request in view.py
    if request.method == 'POST':
        form = CSVUploadForm(request.POST, request.FILES)
        if form.is_valid():
            
             # Process the uploaded file
            handle_uploaded_csv(request.FILES['csv_file'])
            return HttpResponse("File uploaded successfully..!") 
    else:
        form = CSVUploadForm()
    return render(request, 'upload_csv.html', {'form': form})


def download_csv(request):
     # Query the Employee model to get all records
    employees = Employee.objects.all()

    # Create the HttpResponse object with CSV content
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="employee_data.csv"'

    # Create the CSV writer and write the header
    csv_writer = csv.writer(response)
    csv_writer.writerow(['first_name', 'last_name', 'email'])  # CSV header

    # Write data rows
    for employee in employees:
        csv_writer.writerow([employee.first_name, employee.last_name, employee.email])

    return response