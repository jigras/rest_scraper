import requests
import tempfile
from django.core import files
from api.models import Picture


def download_image():
    image_urls = [
        'https://i.wpimg.pl/O/644x430/d.wpimg.pl/58127322-34588805/shutterstock_Michal%20Ludwiczak.jpg',
    ]

    for image_url in image_urls:
        # Steam the image from the url
        request = requests.get(image_url, stream=True)

        # Was the request OK?
        if request.status_code != requests.codes.ok:
            # Nope, error handling, skip file etc etc etc
            continue

        # Get the filename from the url, used for saving later
        file_name = image_url.split('/')[-1]

        # Create a temporary file
        lf = tempfile.NamedTemporaryFile()

        # Read the streamed image in sections
        for block in request.iter_content(1024 * 8):

            # If no more file then stop
            if not block:
                break

            # Write image block to temporary file
            lf.write(block)

        # Create the model you want to save the image to
        image = Picture(page_id=1)

        # Save the temporary image to the model#
        # This saves the model so be sure that is it valid
        image.picture.save(file_name, files.File(lf))