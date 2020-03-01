# REST SCRAPER
Aplikacja wspierającego pracę programistów zajmujących się uczeniem maszynowym. 
System ma pomóc w gromadzeniu i udostępnianiu informacji pobranych z sieci. 
Główną funkcjonalnością systemu jest pobieranie tekstu oraz obrazków ze stron internetowych.


## Uruchamianie
Po pobraniu repozytorium aplikacje uruchamiamy przy pomocy docker-compose.
```
docker-compose build
docker-compose up -d
```

Aplikacja w domyślnym configu pojawi się na porcie 1337

http://127.0.0.1:1337/api/v1/



## ENDPOINTS

### Dodawanie zadania:

__/api/v1/page_create/__ - POST aby dodać zadanie

Request POST
```json
{
    "url": "https://www.dorotasmakuje.com/2016/11/jak-uprazyc-slonecznik/"
}
```

Response:
```json
{
    "url": "https://www.dorotasmakuje.com/2016/11/jak-uprazyc-slonecznik/",
    "scraped": false
    "id": 1
}
```

### Status zadania

__/api/v1/page_create/?url={url}__ - sprawdzanie statusu zadania<br>
Status:
- scraped: true oznacza ukończenie zadania
- scraped: false oznacza zadanie do wykonania

Response:
```
{
    "url":"https://www.dorotasmakuje.com/2016/11/jak-uprazyc-slonecznik/",
    "scraped":true
    "id": 1
}
```
### Pobieranie zdjęć dla adresu URL
__/api/v1/picture_list/?page={page_id}__ - pobranie listy zdjęć dla konkrentej strony.<br>
Parametr __page_id__ (id adresu url) pobrać można wpisując adres URL w zasobie do sprawdzania statusu zadania ('id')


Response:

```
[
    {
        "picture":"http://127.0.0.1:1337/media/wyciskara_philips9_wnIB143.jpg",
        "page":1
    },
    {
        "picture":"http://127.0.0.1:1337/media/kulinarne_tricki_ktore_warto_znac_LQQQpxr.jpg",
        "page":1
    },
    {
        "picture":"http://127.0.0.1:1337/media/siemie_lniane_jajko_BjEjeFk.jpg",
        "page":1
    },
    {
        "picture":"http://127.0.0.1:1337/media/kasza_jaglana_jak_pozby_sie_goryczki_J9cfULS.jpg",
        "page":1
    },
    {
        "picture":"http://127.0.0.1:1337/media/jak_uprazyc_slonecznik_jof2eq0.jpg",
        "page":1
     },
    {
        "picture":"http://127.0.0.1:1337/media/patelnia_woll_Q8S4SYG.jpg",
        "page":1
    },
    {
        "picture":"http://127.0.0.1:1337/media/jak_uprazyc_slonecznik_OoiB0Fk.jpg",
        "page":1
    }
]
```

### Pobieranie tekstu z pobranej strony
__/api/v1/page_create/{page_id}/__ - pobieranie tekstu na podstawie parametry page_id
Jeżeli strona posiada status scraped = True, mamy możliwość pobrania tekstu z danej strony 
```
{
    "url": "https://www.dorotasmakuje.com/2016/11/jak-uprazyc-slonecznik/",
    "scraped": true,
    "id": 1,
    "text": "Słonecznik jest znakomitym dodatkiem do surówek, sałatek, zup, makaronów, kasz a nawet deserów 
    (pyszny z lodami). Prażenie słonecznika znacznie wzmacnia jego smak, dlatego warto poświęcić na to chwilkę zanim 
    dodamy ziarno do dania. Prażenie słonecznika to bardzo łatwa sprawa, ale trzeba tu pozostać czujnym – słonecznik 
    łatwo przypalić i wtedy zamiast pysznego orzechowego smaku otrzymamy gorzki.
}
```


##Requirements


```
asgiref==3.2.3
certifi==2019.11.28
chardet==3.0.4
Django==3.0.3
django-extensions==2.2.8
djangorestframework==3.11.0
django-filter==2.2.0
idna==2.9
Pillow==7.0.0
psycopg2-binary==2.8.4
pytz==2019.3
requests==2.23.0
six==1.14.0
sqlparse==0.3.0
urllib3==1.25.8
redis
celery==4.3.0
kombu==4.6.3
selectolax==0.2.3

```


##TODO:
Rzeczy do wykonania

###Pobieranie treści:
 - Rozbudowa pobierania treści włączając semantyke HTML - np. pobieranie zawartosci samych tagów article
 - Możliwość wykluczania większej ilości tagów html
 
 
 ###Pobieranie obrazów:
 - Rozbudowa o możliwość wykluczanai bardzo małych obrazów
 - Rozbudowa o możliwość pobierania obrazów z CSS background
 - Weryfikacja contentu zdjęcia
 - Hashowanie contentu zdjęć
 
 ### Testy
 - wykonanie dodatkowych testów widoków
 - wykonanie dodatkowych testów api
 
 ## Co do zmiany
 Do aktualizacji proces deploymentu oraz testów. Aktualnie testy odpalane są przy uruchomieniu docker-compose