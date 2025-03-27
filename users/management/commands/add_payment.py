from django.core.management.base import BaseCommand

from materials.models import Course, Lesson
from users.models import User, Payments



class Command(BaseCommand):
    help = 'Add test purchases to the database'

    def handle(self, *args, **kwargs):
        user = User.objects.get(pk=1)
        course_paid = Course.objects.get(pk=2)
        lesson_paid = Lesson.objects.get(pk=4)
        payment = Payments.objects.create(
            user=user,
            course_paid=course_paid,
            payment_date='2024-03-01',
            payment_amount=5000,
            payment_method='transfer',
            lesson_paid=lesson_paid,
        )
        payment.save()

