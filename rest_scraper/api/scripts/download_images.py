# from api.serv.download_image import download_image
# from api.serv.download_html import download_html
from api.tasks import add,download_text_images
#
#
download_text_images.delay('http://allegro.pl')


#download_html('http://allegro.pl')