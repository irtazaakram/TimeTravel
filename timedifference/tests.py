from datetime import datetime, timedelta, timezone

from django.test import TestCase
from freezegun import freeze_time

from timedifference.models import TimeModel
from timedifference.serializer import TimeSerializer

# Create your tests here.
TEST_TIME = datetime(2020, 8, 29, 2, 14, tzinfo=timezone(offset=timedelta(hours=-4)))


@freeze_time(TEST_TIME, tz_offset=-4)
class TimeSerializerTest(TestCase):
    test_user_id_1 = 'Alice'
    timestamp = '2020-08-29T02:14:00-04:00'

    def setUp(self):
        super().setUp()

        self.test_time_model = TimeModel.create_model(self.test_user_id_1)

    def test_serialize_time(self):
        context = {'user_id': self.test_user_id_1}
        expected_output = {
            'owner_id': self.test_user_id_1,
            'created_at': self.timestamp,
        }

        assert TimeSerializer(self.test_time_model, context=context).data == expected_output
