from django.db import models
from django.db.models.deletion import DO_NOTHING
from django.conf import settings
from django.contrib.auth.models import User

class countries(models.Model):
    country_code = models.IntegerField(primary_key=True)
    name = models.CharField(max_length = 200, null=True)	
    country_code_alpha= models.CharField(max_length=2, null=True)	
    country_code_alpha3	= models.CharField(max_length=3, null=True)
    name_long= models.CharField(max_length = 200, null=True)	
    latitude= models.FloatField(null=True)	
    longitude= models.FloatField(null=True)
    region = models.CharField(max_length=200, null=True)
    subregion =  models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']

class dim_roaster(models.Model):
    roaster_id = models.AutoField(primary_key=True, unique=True)
    name = models.CharField(max_length = 200, null=True)
    website = models.URLField(null=True, blank=True)

    def __str__(self):
        return self.name or ''

    class Meta:
        ordering = ['name']

class dim_notes(models.Model):
    flavor_notes = models.CharField(max_length = 200, null=True)

    def __str__(self):
        return self.flavor_notes

    class Meta:
        ordering = ['flavor_notes']

class dim_varietal(models.Model):
    varietal = models.CharField(max_length = 200, null=True)

    def __str__(self):
        return self.varietal

    class Meta:
        ordering = ['varietal']

class dim_coffee(models.Model):

    class coffeeProcess(models.TextChoices):
        WASHED = 'Washed', ('Washed')
        NATURAL = 'Natural', ('Natural')
        ANAEROBIC_NATURAL = 'Anaerobic Natural', ('Anaerobic Natural')
        NATURAL_PULP = 'Pulp Natural', ('Pulp Natural')
        HONEY = 'Honey', ('Honey')
        YELLOW_HONEY = 'Yellow Honey', ('Yellow Honey')
        HONEY_WASHED = 'Honey Washed', ('Honey Washed')
        HONEY_NATURAL = 'Honey Natural', ('Honey Natural')
        EA = 'EA Decaf', ('EA Decaf')
        SWISSWATER = 'Swiss Water Decaf', ('Swiss Water Decaf')
        MIXED = 'Mixed Process', ('Mixed Process')
        WET_HULLED = 'Wet-hulled', ('Wet-hulled')
        EXPERIMENTAL = 'Experimental', ('Experimental')

    coffee_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length = 200, null=True)
    roaster = models.ForeignKey(dim_roaster, to_field='roaster_id', null=True, on_delete=models.SET_NULL, related_name="coffees")
    farmer = models.CharField(max_length = 200, null = True, blank=True)
    country = models.ForeignKey(countries, to_field='country_code', null=True, on_delete=models.SET_NULL, related_name="coffees")
    # region = models.CharField(max_length = 50, null = True)
    varietals = models.ManyToManyField(dim_varietal, related_name = 'varieties', blank=True)
    process = models.CharField(
        max_length=100,
        choices=coffeeProcess.choices,
        null = True
    )
    elevation = models.IntegerField(null = True, blank=True)
    roaster_notes = models.ManyToManyField(dim_notes, related_name='notes')
    storage_path = models.CharField(max_length = 500, null = True, blank=True)
    tradeUrl = models.URLField(null = True, blank=True)

    def __str__(self):
        if self.name:
            return self.name or ' '
        return str("Coffee")+str(self.coffee_id)

    class Meta:
        ordering = ['name']

class ratings(models.Model):

    class ratings_scale(models.IntegerChoices):
        (1, '1')
        (2, '2')
        (3, '3')
        (4, '4')
        (5, '5')

    class coffeeRating (models.IntegerChoices):
        No = 1
        Tolerable = 2
        Good = 3
        Like = 4
        Love = 5

    class brewMethod(models.TextChoices):
        V60 = 'V60', ('V60')
        CHEMEX = 'Chemex', ('Chemex')
        KALITA = 'Kalita Wave', ('Kalita Wave')
        CLOVER = "Clover", ('Clover')
        AEROPRESS = 'AeroPress', ('AeroPress')
        FRENCHPRESS = 'French Press', ('French Press')
        DRIP = 'Drip', ('Drip')
        CUPPING = 'Cupping', ('Cupping')
        SIPHON = 'Siphon', ('Siphon')
        ESPRESSO = 'Espresso', ('Espresso')

    rating_id = models.AutoField(primary_key=True)
    coffee = models.ForeignKey(dim_coffee, null=True, on_delete=models.DO_NOTHING, to_field='coffee_id', related_name='ratings', related_query_name='ratings')
    brew_method = models.CharField(
        max_length=25,
        choices=brewMethod.choices,
        null = True
        )
    reaction = models.TextField(max_length=500, null=True)
    rating = models.IntegerField(
        choices = coffeeRating.choices, null=True
        )
    rating_date = models.DateField(null=True, editable=True)
    last_updated = models.DateTimeField(auto_now=True)
    user_id = models.ForeignKey(User, default='', null=True, blank=True, on_delete=models.SET_NULL)

    class Meta:
        ordering = ['-last_updated']

class recommendations(models.Model):
    rec_id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(User, default='', null=True, blank=True, on_delete=models.SET_NULL)
    recs_set = models.IntegerField(null = True, blank=True)
    rec_num = models.IntegerField(null = True, blank=True)
    coffee = models.ForeignKey(dim_coffee, null=True, on_delete=models.DO_NOTHING, to_field='coffee_id', related_name='recs', related_query_name='recs')
    score = models.FloatField(null = True, blank=True)
    last_updated = models.DateTimeField(auto_now=True)
    

