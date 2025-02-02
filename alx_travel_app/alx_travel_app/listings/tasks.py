from celery import shared_task
from django.core.mail import send_mail
from django.conf import settings

@shared_task
def send_booking_confirmation_email(booking_id):
    from .models import Booking  # Import inside the function to avoid circular imports
    booking = Booking.objects.get(id=booking_id)
    subject = 'Booking Confirmation'
    message = f'Thank you for booking {booking.listing.title}. Your booking ID is {booking.id}.'
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [booking.user.email,]
    send_mail(subject, message, email_from, recipient_list)