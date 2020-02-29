import requests
import tempfile
from django.core import files
from api.models import Picture


def serv_download_image(image_url,page_id):
    """
    Download image
    @param image_url: Full image URL
    @return: Temporary file for Django Image and file name
    """
    request = requests.get(url=image_url,stream=True)
    if request.status_code != requests.codes.ok:
        return False

    # Get the filename from the url,
    file_name = image_url.split('/')[-1]
    # Create a temporary file
    lf = tempfile.NamedTemporaryFile()

    # Read the streamed image in sections
    for block in request.iter_content(1024 * 8):
        if not block:
            break
        lf.write(block)
    image = Picture(page_id=page_id)
    image.picture.save(file_name, files.File(lf))

    return lf, file_name


# def serv_save_image(lf, file_name,page_id):
#     # Create the model you want to save the image to
#     image = Picture(page_id=page_id)
#
#     # Save the temporary image to the model#
#     # This saves the model so be sure that is it valid


