from celery.decorators import task
from api.serv.download_html import download_html,get_text_selectolax,get_list_image
from api.serv.download_image import serv_download_image
from api.models import Page
from django.utils.timezone import now



@task(name='url_task')
def create_url_task(url):
    pass


@task(name='download_text')
def download_text_images_task(page_id):
    """
    Celery Task for downloading text,starts downloading images from the list
    """
    page = Page.objects.get(pk=page_id)
    html_obj = download_html(page.url)
    page_text = get_text_selectolax(html_obj)
    page.text = page_text
    page.scraped_at = now()
    page.save()
    img_list = get_list_image(html_obj)
    if img_list:
        for image in img_list:
            download_image_task.delay(image,page_id)

@task(name='save_img')
def download_image_task(url, page_id):
    serv_download_image(url,page_id)
