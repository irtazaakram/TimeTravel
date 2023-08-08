from datetime import datetime, timedelta, timezone

from django.conf import settings
from django.utils.timezone import now
from freezegun import freeze_time
import pytz

settings.configure(
    TIME_ZONE="America/New_York",
    USE_TZ=True,
)

TEST_TIME = datetime(2020, 8, 29, 2, 14, tzinfo=timezone(offset=timedelta(hours=-4)))


@freeze_time(TEST_TIME, tz_offset=-4)
def print_time():
    print(now().isoformat())
    print(datetime.utcnow().replace(tzinfo=pytz.utc).isoformat())


print_time()
