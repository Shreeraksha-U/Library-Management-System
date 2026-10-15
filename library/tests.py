from django.db import IntegrityError, transaction
from django.test import TestCase
from django.urls import reverse

from .models import Book, Borrow, Member


class ModelTests(TestCase):
    def setUp(self):
        self.member = Member.objects.create(
            name="Smitha", email="smitha@example.com", phone="1234567890"
        )
        self.book = Book.objects.create(
            title="Dune", author="Frank Herbert", isbn="9780441013593"
        )

    def test_string_representations(self):
        self.assertEqual(str(self.member), "Smitha")
        self.assertEqual(str(self.book), "Dune")

    def test_book_is_available_by_default(self):
        self.assertTrue(self.book.available)

    def test_duplicate_isbn_is_rejected(self):
        with self.assertRaises(IntegrityError), transaction.atomic():
            Book.objects.create(title="Other", author="Someone", isbn="9780441013593")

    def test_duplicate_member_email_is_rejected(self):
        with self.assertRaises(IntegrityError), transaction.atomic():
            Member.objects.create(name="Other", email="smitha@example.com", phone="999")

    def test_borrow_record(self):
        borrow = Borrow.objects.create(member=self.member, book=self.book)
        self.assertIsNotNone(borrow.borrow_date)  # set automatically
        self.assertIsNone(borrow.return_date)  # not returned yet
        self.assertEqual(str(borrow), "Smitha borrowed Dune")


class ViewTests(TestCase):
    def setUp(self):
        Member.objects.create(
            name="Smitha", email="smitha@example.com", phone="1234567890"
        )
        Book.objects.create(
            title="Dune", author="Frank Herbert", isbn="9780441013593"
        )

    def test_home_page_lists_books(self):
        response = self.client.get(reverse("home"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Dune")
        self.assertContains(response, "Frank Herbert")
        self.assertContains(response, "9780441013593")

    def test_members_page_lists_members(self):
        response = self.client.get(reverse("members"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Smitha")
        self.assertContains(response, "smitha@example.com")

    def test_pages_work_with_no_data(self):
        Book.objects.all().delete()
        Member.objects.all().delete()
        self.assertEqual(self.client.get(reverse("home")).status_code, 200)
        self.assertEqual(self.client.get(reverse("members")).status_code, 200)