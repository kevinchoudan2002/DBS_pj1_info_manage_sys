from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Student(models.Model):
    name = models.CharField(verbose_name="姓名", max_length=20)
    student_id = models.CharField(verbose_name="学号", max_length=15,unique=True)
    sex_choices = (
        (1, "男"),
        (2, "女"),
    )
    sex = models.SmallIntegerField(verbose_name="性别", choices=sex_choices)
    age = models.IntegerField(verbose_name="年龄")
    major = models.CharField(verbose_name="专业", max_length=50)
    #user = models.OneToOneField(User, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "学生"
        verbose_name_plural = verbose_name
        ordering = ['student_id']
        permissions = [
            ("can_view_student", "Can see available students"),
            ("can_view_course", "Can see available courses"),
            ("can_view_teacher", "Can see available teachers"),
            ("can_view_score", "Can see available scores"),
        ]

    def __str__(self):
        return self.name
    
    def create_student(self, name, student_id, sex, age, major, username):
        user = User.objects.get(username=username)
        student = self(name=name, student_id=student_id, sex=sex, age=age, major=major, user=user)
        student.save()
        return student


class Teacher(models.Model):
    name = models.CharField(verbose_name="姓名", max_length=20)
    teacher_id = models.CharField(verbose_name="工号", max_length=15, unique=True)
    age = models.IntegerField(verbose_name="年龄")
    sex_choices = (
        (1, "男"),
        (2, "女"),
    )
    sex = models.SmallIntegerField(verbose_name="性别", choices=sex_choices)
    school = models.CharField(verbose_name="学院", max_length=50)
    user = models.OneToOneField(User, on_delete=models.CASCADE)


    class Meta:
        verbose_name = "教师"
        verbose_name_plural = verbose_name
        ordering = ['teacher_id']
        permissions = [
            ("can_view_student", "Can see available students"),
            ("can_view_course", "Can see available courses"),
            ("can_view_teacher", "Can see available teachers"),
            ("can_view_score", "Can see available scores"),
            ("can_view_course_time", "Can see available course time"),
            ("can_change_score", "Can change scores"),
            ("can_add_score", "Can add scores"),

        ]

    def __str__(self):
        return self.name
    
    def create_teacher(self, name, teacher_id, sex, age, school, username):
        user = User.objects.get(username=username)
        teacher = self(name=name, teacher_id=teacher_id, sex=sex, age=age, school=school, user=user)
        teacher.save()
        return teacher
    

class Course(models.Model):
    name = models.CharField(verbose_name="课程名", max_length=80)
    course_id = models.CharField(verbose_name="课程号", max_length=50)
    teacher = models.ForeignKey(Teacher, verbose_name="教师", on_delete=models.CASCADE)

    class Meta:
        verbose_name = "课程"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name + " " + self.teacher.name
    
    def create_course(self, name, course_id, teacher_id):
        teacher = Teacher.objects.get(teacher_id=teacher_id)
        course = self(name=name, course_id=course_id, teacher=teacher)
        course.save()
        return course


class CourseScore(models.Model):
    course = models.ForeignKey(Course, verbose_name="课程", on_delete=models.CASCADE)
    student = models.ForeignKey(Student, verbose_name="学生", on_delete=models.CASCADE)
    score = models.IntegerField(verbose_name="成绩")

    class Meta:
        verbose_name = "学生成绩"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.course.name + " " + self.student.name + " " + str(self.score)
    
    def create_score(self, course_id, student_id, score):
        course = Course.objects.get(course_id=course_id)
        student = Student.objects.get(student_id=student_id)
        score = self(course=course, student=student, score=score)
        return score


class CourseTime(models.Model):
    course = models.ForeignKey(Course, verbose_name="课程", on_delete=models.CASCADE)
    weekday = models.IntegerField(verbose_name="星期")
    start = models.IntegerField(verbose_name="开始节")
    end = models.IntegerField(verbose_name="结束节")

    class Meta:
        verbose_name = "课程时间"
        verbose_name_plural = verbose_name
    def __str__(self):
        return self.course.name + " " + str(self.weekday) + " " + str(self.start) + " " + str(self.end)
    
    def create_time(self, course_id, weekday, start, end):
        course = Course.objects.get(course_id=course_id)
        time = self(course=course, weekday=weekday, start=start, end=end)
        return time


class Admin(models.Model):
    employee_id = models.CharField(verbose_name='工号', max_length=15, unique=True)
    name = models.CharField(verbose_name="姓名", max_length=32)
    age = models.IntegerField(verbose_name="年龄")
    gender_choices = (
        (1, "男"),
        (2, "女"),
    )
    sex = models.SmallIntegerField(verbose_name="性别", choices=gender_choices)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "教师"
        verbose_name_plural = verbose_name
        ordering = ['employee_id']
        permissions = [
            ("can_view_all", "Can view all"),
            ("can_change_all", "Can change all"),
            ("can_add_all", "Can add all"),
            ("can_delete_all", "Can delete all"),
        ]

    def __str__(self):
        return self.name
    
    def create_admin(self, name, employee_id, sex, age, username):
        user = User.objects.get(username=username)
        admin = self(name=name, employee_id=employee_id, sex=sex, age=age, user=user)
        return admin


