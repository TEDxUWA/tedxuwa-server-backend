from django.test import TestCase, Client
from events.models import Event, Talk

# Create your tests here.


class TestEventEndpoint(TestCase):
    fixtures = ["events/fixtures/events.json"]

    def setUp(self):
        self.c = Client()

    def test_endpoint(self):
        re = self.c.get("/api/events/")
        self.assertEqual(re.status_code, 200)
        self.assertEqual(re.json()["count"], Event.objects.count())

    def test_featured_only(self):
        # if ?featured is there, only get featured events
        Event.objects.all().update(featured=False)
        re = self.c.get("/api/events/?featured")
        self.assertEqual(re.status_code, 200)
        self.assertEqual(re.json()["count"], 0)
        # make everything featured
        Event.objects.all().update(featured=True)
        re = self.c.get("/api/events/?featured")
        self.assertEqual(re.status_code, 200)
        self.assertEqual(re.json()["count"], Event.objects.count())


class TestSpeakerEndpoint(TestCase):
    fixtures = ["events/fixtures/events.json",
                "events/fixtures/speakers.json"]

    def setUp(self):
        self.c = Client()
        self.event = Event.objects.first()

    def test_endpoint(self):
        re = self.c.get(f"/api/events/{self.event.id}/speakers/")
        self.assertEqual(re.status_code, 200)
        self.assertEqual(re.json()["count"], self.event.speakers.count())
        # non existent event
        re = self.c.get("/api/events/000/speakers/")
        self.assertEqual(re.status_code, 404)


class TestTalkEndpoint(TestCase):
    fixtures = ["events/fixtures/events.json",
                "events/fixtures/speakers.json",
                "events/fixtures/talks.json"]

    def setUp(self):
        self.c = Client()
        self.talk = Event.objects.first()

    def test_endpoint(self):
        re = self.c.get(f"/api/talks/")
        self.assertEqual(re.status_code, 200)
        self.assertEqual(re.json()["count"], Talk.objects.count())
        # non existent talk
        re = self.c.get("/api/talks/1111/")
        self.assertEqual(re.status_code, 404)
        # retrieve talk
        re = self.c.get("/api/talks/{}/".format(self.talk.id))
        self.assertEqual(re.status_code, 200)
