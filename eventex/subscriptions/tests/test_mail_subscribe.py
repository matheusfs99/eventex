from django.core import mail
from django.test import TestCase


class SubscribePostValid(TestCase):
    def setUp(self):
        data = dict(name='Matheus Farias', cpf='12345678901',
                    email='matheusfarias009@hotmail.com', phone='81-98545-1247')
        self.resp = self.client.post('/inscricao/', data)
        self.email = mail.outbox[0]

    def test_subscription_email_subject(self):
        expect = 'Confirmação de inscrição'

        self.assertEqual(expect, self.email.subject)

    def test_subscription_email_from(self):
        expect = 'matheusfarias009@hotmail.com'

        self.assertEqual(expect, self.email.from_email)

    def test_subscription_email_to(self):
        expect = ['matheusfarias009@hotmail.com', 'matheusfarias009@hotmail.com']

        self.assertEqual(expect, self.email.to)

    def test_subscription_email_body(self):
        contents = [
            'Matheus Farias',
            '12345678901',
            'matheusfarias009@hotmail.com',
            '81-98545-1247',
        ]
        for content in contents:
            with self.subTest():
                self.assertIn(content, self.email.body)
