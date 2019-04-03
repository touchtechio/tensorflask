import datetime

from django.test import TestCase
from django.utils import timezone
from django.urls import reverse



from .models import Image


class ImagesModelTests(TestCase):

    def test_was_published_recently_with_future_image(self):
        time = timezone.now() + datetime.timedelta(days=30)
        future_image = Image(pub_date=time)
        self.assertIs(future_image.was_published_recently(), False)

    def test_was_published_recently_with_old_image(self):
        """
        was_published_recently() returns False for images whose pub_date
        is older than 1 day.
        """
        time = timezone.now() - datetime.timedelta(days=1, seconds=1)
        old_image = Image(pub_date=time)
        self.assertIs(old_image.was_published_recently(), False)

    def test_was_published_recently_with_recent_image(self):
        """
        was_published_recently() returns True for images whose pub_date
        is within the last day.
        """
        time = timezone.now() - datetime.timedelta(hours=23, minutes=59, seconds=59)
        recent_image = Image(pub_date=time)
        self.assertIs(recent_image.was_published_recently(), True)


def create_image(filename, days):
    """
    Create a image with the given `image_text` and published the
    given number of `days` offset to now (negative for images published
    in the past, positive for images that have yet to be published).
    """
    time = timezone.now() + datetime.timedelta(days=days)
    return Image.objects.create(filename=filename, pub_date=time)


class ImageIndexViewTests(TestCase):
    def test_no_images(self):
        """
        If no images exist, an appropriate message is displayed.
        """
        response = self.client.get(reverse('images:index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "No images are available.")
        self.assertQuerysetEqual(response.context['latest_image_list'], [])

    def test_past_image(self):
        """
        Images with a pub_date in the past are displayed on the
        index page.
        """
        create_image(filename="Past image.", days=-30)
        response = self.client.get(reverse('images:index'))
        self.assertQuerysetEqual(
            response.context['latest_image_list'],
            ['<Image: Past image.>']
        )

    def test_future_image(self):
        """
        Images with a pub_date in the future aren't displayed on
        the index page.
        """
        create_image(filename="Future image.", days=30)
        response = self.client.get(reverse('images:index'))
        self.assertContains(response, "No images are available.")
        self.assertQuerysetEqual(response.context['latest_image_list'], [])

    def test_future_image_and_past_image(self):
        """
        Even if both past and future images exist, only past images
        are displayed.
        """
        create_image(filename="Past image.", days=-30)
        create_image(filename="Future image.", days=30)
        response = self.client.get(reverse('images:index'))
        self.assertQuerysetEqual(
            response.context['latest_image_list'],
            ['<Image: Past image.>']
        )

    def test_two_past_images(self):
        """
        The images index page may display multiple images.
        """
        create_image(filename="Past image 1.", days=-30)
        create_image(filename="Past image 2.", days=-5)
        response = self.client.get(reverse('images:index'))
        self.assertQuerysetEqual(
            response.context['latest_image_list'],
            ['<Image: Past image 2.>', '<Image: Past image 1.>']
        )