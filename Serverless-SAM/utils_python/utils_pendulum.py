import pendulum

now = pendulum.now()
print(now)

now = now.in_timezone('Asia/Tokyo')
print(now)
print(now.to_iso8601_string())

now = now.add(years=1).add(days=3).add(hours=2)
print(now)


