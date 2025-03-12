from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Customer, Visit, Satisfaction
#from .ml_model import ml_model   # todo i have  load the model here dont forget


@receiver(post_save)
def make_prediction(sender, instance, created, **kwargs):
    if created and sender.__name__ in ['Customer', 'Visit', 'Satisfaction']:
        # todo handle each model differently here. but ill depends on if max ill train the model for each use case
        input_data = [
            instance.feature1,  # todo retrieve the features to use with the model created by max... dont forget
            instance.feature2,
            instance.feature3,
        ]

        processed_data = [input_data]

        # prediction = ml_model.predict(processed_data)[0]

        # todo
        # save the prediction in a csv file or create and endpoint to view the result

