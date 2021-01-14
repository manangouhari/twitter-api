from neomodel import StructuredNode, StringProperty, DateTimeProperty, Relationship


class User(StructuredNode):
    email = StringProperty()
    

class Tweet(StructuredNode):
    body = StringProperty()
    tweeted_on = DateTimeProperty(default_now=True)
    poster = Relationship('User', 'TWEETED_BY')
    liked_by = Relationship('User', 'LIKED_BY')
    comment_on = Relationship('Tweet', 'COMMENT_ON')

