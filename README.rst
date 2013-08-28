
Django Fineuploader
===================

A simple (and useless) django integration with fineuploader_

.. important::

    This app was created just for fun. Please read the code before use.

.. _fineuploader: http://fineuploader.com/

Usage
-----

This is just a example, please read the code to see what really happens.

.. code:: python

    # models.py #####################################################
    from django.db import models
    from django.core.urlresolvers import reverse


    class Picture(models.Model):
        image = models.ImageField(upload_to='profiles')
        slug = models.SlugField(blank=True)

        def __unicode__(self):
            return self.image.name

        def get_absolute_url(self):
            return reverse('images_list', args=[])

    # forms.py ######################################################
    from django.forms import ModelForm
    from fineuploader.widgets import FineUploderWidget

    from .models import Picture


    class PictureForm(ModelForm):
        class Meta:
            model = Picture
            widgets = {
                'image': FineUploderWidget(),
            }

    # views.py ######################################################
    from django.views.generic import ListView
    from fineuploader.views import FineUploaderView

    from .forms import PictureForm
    from .models import Picture


    # NOTE: Fineuploader inherits from CreateView
    class PictureView(FineUploaderView):
        model = Picture
        form_class = PictureForm


    class PictureListView(ListView):
        queryset = Picture.objects.all()

    # urls.py #######################################################
    from django.conf.urls import patterns, url

    from .views import PictureView, PictureListView

    urlpatterns = patterns('',
        url(r'^upload/', PictureView.as_view(), name='upload_image'),
        url(r'^images/', PictureListView.as_view(), name='images_list'),
    )
