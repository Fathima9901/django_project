import datetime
from django.db import models
from django.contrib.auth.models import User

# Create your models here.


gender_choice = (
    ('M', 'Male'),
    ('F', 'Female'),
)

district_choices = (
    ('Alappuzha', 'Alappuzha'),
    ('Eranakulam', 'Eranakulam'),
    ('Kozhikode', 'Kozhikode'),
    ('Palakkad', 'Palakkad'),
    ('Kollam', 'Kollam'),
    ('Kannur', 'Kannur'),
    ('Kottayam', 'Kottayam'),
    ('Pathanamthitta', 'Pathanamthitta'),
    ('Kasaragod', 'Kasaragod'),
    ('Thiruvananthapuram', 'Thiruvananthapuram'),
    ('Idukki', 'Idukki'),
    ('Thrissur', 'Thrissur'),
    ('Malappuram', 'Malappuram'),
    ('Wayanad', 'Wayanad'),
)

branch_choices = (
    ('BCA', 'BCA'),
    ('BCA DS', 'BCA DS'),
)


class Register(models.Model):
    enrollment_no = models.CharField(max_length=22, unique=True, verbose_name='enrollment no')
    first_name = models.CharField(max_length=20, verbose_name='first name')
    last_name = models.CharField(max_length=20, verbose_name='last name')
    date_of_birth = models.DateField(verbose_name='date of birth', default=datetime.date.today)
    gender = models.CharField(max_length=1, choices=gender_choice, verbose_name='gender', blank=True, )
    branch = models.CharField(max_length=20, choices=branch_choices, verbose_name='Department', blank=True)
    mail_id = models.EmailField(max_length=40, unique=True, blank=True, verbose_name='mail id')
    college_mail = models.EmailField(max_length=40, unique=True, blank=True, verbose_name='College mail')
    phone_number = models.CharField(max_length=10, unique=True, verbose_name='phone number', blank=True)
    password = models.CharField(max_length=15, verbose_name='password')
    current_cgpa = models.FloatField(max_length=5, verbose_name='current cgpa')
    tenth = models.CharField(max_length=5, verbose_name='10th percentage', blank=True)
    twelfth = models.CharField(max_length=5, verbose_name='12th percentage', blank=True)
    address_name = models.CharField(max_length=45, verbose_name='House name')
    post_office = models.CharField(max_length=30, verbose_name='post office')
    city = models.CharField(max_length=25, verbose_name='city')
    district = models.CharField(max_length=25, choices=district_choices, verbose_name='district')
    pincode = models.IntegerField(verbose_name='pincode')
    father_name = models.CharField(max_length=20, verbose_name='father name')
    mother_name = models.CharField(max_length=20, verbose_name='mother name')

    def __str__(self):
        return self.first_name

    class Meta:
        verbose_name_plural = 'Registration Table'


# Create your models here.

class Skill(models.Model):
    student_id = models.ForeignKey(Register, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    skill = models.CharField(max_length=200)

    def __str__(self):
        return self.name


# Create your models here.

class Project(models.Model):
    project_id = models.AutoField(primary_key=True)
    student_id = models.ForeignKey(Register, on_delete=models.CASCADE)
    project_type = models.CharField(max_length=200)

    def __str__(self):
        return f"Project {self.project_id}"


# Create your models here.


class Company(models.Model):
    name = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    email = models.EmailField()
    company_type = models.CharField(max_length=200)
    package = models.IntegerField()
    role = models.CharField(max_length=200)

    def __str__(self):
        return self.name


# Create your models here.

class Coordinator(models.Model):
    coordinator_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    email = models.EmailField()
    contact_no = models.CharField(max_length=20)

    def __str__(self):
        return self.name


# Create your models here.

class Criteria(models.Model):
    cgpa = models.DecimalField(max_digits=3, decimal_places=2)
    backlogs = models.IntegerField()

    def __str__(self):
        return f"Criteria: CGPA - {self.cgpa}, Backlogs - {self.backlogs}"


# Create your models here.

class Drives(models.Model):
    company_name = models.CharField(max_length=50, verbose_name='Name', default='')
    salary_package = models.FloatField(max_length=10, verbose_name='CTC(LPA)', default='')
    description = models.TextField(blank=True, verbose_name='Job Role', default='')
    cgpa = models.FloatField(default='6', verbose_name='Required CGPA')
    backlog = models.IntegerField(default=0, verbose_name='Backlog Count')
    last_date = models.DateField(verbose_name='Last Date', default='')
    status = models.BooleanField(default=False, verbose_name='Accept Response')

    class Meta:
        verbose_name_plural = 'Drive Details'

    def _str_(self):
        return self.company_name


# Create your models here.

class ApplyDrive(models.Model):
    drive_name = models.ForeignKey(Drives, verbose_name='Drive Name', on_delete=models.CASCADE)
    user = models.ForeignKey(Register, verbose_name='Student Name', on_delete=models.CASCADE)
    applied_on = models.DateField(auto_now_add=True)
    status = models.BooleanField(default=False, verbose_name='Applied')

    def _str_(self):
        return "%s" % self.drive_name

    class Meta:
        verbose_name_plural = "Students Applied Drives"


# Create your models here.

class Notification(models.Model):
    student = models.ForeignKey(User, on_delete=models.CASCADE)
    email = models.EmailField()
    date_and_time = models.DateTimeField(auto_now_add=True)
    message = models.CharField(max_length=200)
    n_status = models.BooleanField(default=False)

    def __str__(self):
        return self.message


# Create your models here.

class Interview(models.Model):
    student = models.ForeignKey(Register, on_delete=models.CASCADE)
    date_and_time = models.DateTimeField()
    location = models.CharField(max_length=200)
    status = models.CharField(max_length=100)

    def __str__(self):
        return f"Interview {self.id} - Student: {self.student}, Date and Time: {self.date_and_time}, Location: {self.location}, Status: {self.status}"


# Create your models here.

class Result(models.Model):
    student = models.ForeignKey(Register, on_delete=models.CASCADE)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    interview_type = models.CharField(max_length=100)

    def __str__(self):
        return f"Result - Student: {self.student}, Company: {self.company}, Interview Type: {self.interview_type}"
