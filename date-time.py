from datetime import datetime

delta = datetime.now() - datetime(1900, 12, 31)
print(delta)
print(delta.days)
print(delta.seconds)
