from django.contrib.auth import get_user_model
from django.db import models

state_choices = [
    ('AL', 'Alabama'), ('AK', 'Alaska'), ('AZ', 'Arizona'), ('AR', 'Arkansas'), ('CA', 'California'), ('CO', 'Colorado'), ('CT', 'Connecticut'), ('DE', 'Delaware'), ('DC', 'District of Columbia'), ('FL', 'Florida'), ('GA', 'Georgia'), ('HI', 'Hawaii'), ('ID', 'Idaho'), ('IL', 'Illinois'), ('IN', 'Indiana'), ('IA', 'Iowa'), ('KS', 'Kansas'), ('KY', 'Kentucky'), ('LA', 'Louisiana'), ('ME', 'Maine'), ('MD', 'Maryland'), ('MA', 'Massachusetts'), ('MI', 'Michigan'), ('MN', 'Minnesota'), ('MS', 'Mississippi'), ('MO', 'Missouri'), ('MT', 'Montana'), ('NE', 'Nebraska'), ('NV', 'Nevada'), ('NH', 'New Hampshire'), ('NJ', 'New Jersey'), ('NM', 'New Mexico'), ('NY', 'New York'), ('NC', 'North Carolina'), ('ND', 'North Dakota'), ('OH', 'Ohio'), ('OK', 'Oklahoma'), ('OR', 'Oregon'), ('PA', 'Pennsylvania'), ('RI', 'Rhode Island'), ('SC', 'South Carolina'), ('SD', 'South Dakota'), ('TN', 'Tennessee'), ('TX', 'Texas'), ('UT', 'Utah'), ('VT', 'Vermont'), ('VA', 'Virginia'), ('WA', 'Washington'), ('WV', 'West Virginia'), ('WI', 'Wisconsin'), ('WY', 'Wyoming')
]

gender_choices = (
    ('M',"Male"), ('F',"Female"), ('TG', "Transgender"), ('NB', "Non-binary"), ('Other', "Other"), ('None Selected', "None Selected")
)

partner_preference_choices = (
    ('M',"Male"), ('F',"Female"), ('TG', "Transgender"), ('NB', "Non-binary"), ('Other', "Other"), ('None Selected', "None Selected")
)

zodiac_choices = (
    ('Sag',"Sagittarius"), ('Ari',"Aries"), ('Tau',"Taurus"), ('Gem', "Gemini"), ('Can', "Cancer"), ('Leo', "Leo"), ('Vir', "Virgo"), ('Lib', "Libra"), ('Sco', "Scorpio"), ('Cap', "Capricorn"), ('Aqu', "Aquarius"), ('Pis', "Pisces"), ('None Selected', "None Selected")
    )

class Profile(models.Model):
    name = models.CharField(max_length=256)
    age = models.IntegerField(default = "None Selected")
    gender = models.CharField(
        max_length = 256, choices = gender_choices, default='None Selected'
        )
    city = models.CharField(max_length=256)
    state = models.CharField(
        max_length=256, choices = state_choices, default="None Selected"
    )
    partner_preferences = models.CharField(
        max_length = 256, choices = partner_preference_choices, default="None Selected"
        )
    description = models.CharField(max_length=3000)
    hobbies_interests = models.CharField(max_length=3000)
    zodiac = models.CharField(
        max_length = 256, choices = zodiac_choices, default = "None Selected"
        )
    owner = models.ForeignKey(
        get_user_model(), on_delete=models.CASCADE, null=True, blank=True
    )
    description = models.TextField(default="", null=True, blank=True)

    def __str__(self):
        return self.name
