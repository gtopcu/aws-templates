
# https://pypi.org/project/Faker/
# pip install faker

from faker import Faker

"""
cmd:

faker [-h] [--version] [-o output]
      [-l {bg_BG,cs_CZ,...,zh_CN,zh_TW}]
      [-r REPEAT] [-s SEP]
      [-i {package.containing.custom_provider otherpkg.containing.custom_provider}]
      [fake] [fake argument [fake argument ...]]
"""


fake = Faker()
# fake = Faker('it_IT') # Italy
# fake = Faker(['it_IT', 'en_US', 'ja_JP']) # multiple locales

fake.name()
# 'Lucy Cechtelar'

for _ in range(10):
  print(fake.name())


fake.address()
# '426 Jordy Lodge
#  Cartwrightshire, SC 88120-6700'

fake.text()
# 'Sint velit eveniet. Rerum atque repellat voluptatem quia rerum. Numquam excepturi


# from faker.providers import internet
# fake = Faker()
# fake.add_provider(internet)
# print(fake.ipv4_private())