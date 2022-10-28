from django.test import TestCase

from datetime import datetime

t = datetime.now().time()
seconds = (t.hour * 60 + t.minute) * 60 + t.second

r = datetime(2000,2,3,4,5,23)
print(r)



# .total_seconds() / 60
#
# print(seconds)

from datetime import datetime

datetimeobj= datetime(2000,2,3,4,5,23)
total4 = int(datetimeobj.timestamp())
print ("Method #4: datetime timestamp")
print ("Before: %s" % datetimeobj)
print ("Seconds: %s " % total4)
print ("After: %s" % datetime.fromtimestamp(total4))