from django.contrib.auth.models import User


class Member(User):
    pass
    # add additional fields in here

    def __str__(self):
        return self.username
