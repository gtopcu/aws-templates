
# https://github.com/marshmallow-code/marshmallow

from datetime import date
from pprint import pprint

from marshmallow import Schema, fields


class ArtistSchema(Schema):
    name = fields.Str()


class AlbumSchema(Schema):
    title = fields.Str()
    release_date = fields.Date()
    artist = fields.Nested(ArtistSchema())


bowie = dict(name="David Bowie")
album = dict(artist=bowie, title="Hunky Dory", release_date=date(1971, 12, 17))

schema = AlbumSchema()
result = schema.dump(album)
pprint(result, indent=2)
# { 'artist': {'name': 'David Bowie'},
#   'release_date': '1971-12-17',
#   'title': 'Hunky Dory'}



# https://circleci.com/blog/object-validation-and-conversion-with-marshamallow/
# class BookMarkSchema(ma.Schema):
#     title = fields.String(
#         metadata={
#             "required": True,
#             "allow_none": False,
#             "validate": must_not_be_blank
#         }
#     )
#     url = fields.URL(
#         metadata={
#             "relative": True,
#             "require_tld": True,
#             "error": "invalid url representation",
#         }
#     )
#     description = fields.String(metadata={"required": False, "allow_none": True})
#     created_at = fields.DateTime(metadata={"required": False, "allow_none": True})
#     updated_at = fields.DateTime(metadata={"required": False, "allow_none": True})