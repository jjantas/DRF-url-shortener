# 🔗 Django REST URL Shortener API

Minimalistyczny backendowy projekt w Django REST Framework, umożliwiający skracanie długich linków oraz ich rozwijanie poprzez przekierowanie.

---

## Założenia projektowe

Celem było stworzenie prostego API działającego jak usługa typu TinyURL, bez zbędnych funkcji. Treść zadania kładła nacisk na minimalizm, więc projekt nie zawiera:

- systemu logowania/rejestracji,
- edycji/usuwania linków,
- statystyk, dat ważności itd.

---

## Funkcjonalność

- `POST /api/shorten/`  
  Przyjmuje długi URL, generuje (lub zwraca istniejący) skrót.

- `GET /shrt/<code>/`  
  Przekierowuje do oryginalnego URL-a na podstawie kodu.

---

## Przykłady działania

### 1. Skracanie URL-a

**Żądanie:**

```http
POST /api/shorten/
Content-Type: application/json

{
  "original_url": "https://example.com/very/long/link"
}
```

**Odpowiedź:**

```json
{
  "short_url": "http://localhost:8000/shrt/aB3kZ8/"
}
```

---

### 2. Rozwijanie URL-a (przekierowanie)

Wejście w przeglądarce pod adres:

```
http://localhost:8000/shrt/aB3kZ8/
```

Spowoduje przekierowanie do:

```
https://example.com/very/long/link
```

---

## Decyzje techniczne

- Jeśli użytkownik próbuje skrócić URL, który już istnieje w bazie, to nie jest tworzony nowy wpis, tylko zwracany jest istniejący `short_url`.
- Użyto funkcji `redirect()` Django, aby uzyskać rzeczywiste przekierowanie, a nie tylko zwracanie oryginalnego URL-a jako JSON.

---

## Technologie

- Python 
- Django
- Django REST Framework
- SQLite (domyślna baza Django)

---

## Uruchomienie lokalne

1. Klonowanie repozytorium:

```bash
git clone https://github.com/twoj-login/DRF-url-shortener.git
cd DRF-url-shortener
```

2. Wirtualne środowisko:

```bash
python -m venv venv
source venv/bin/activate  # lub venv\Scripts\activate w Windows
```

3. Instalacja zależności:

```bash
pip install -r requirements.txt
```

4. Migracje i uruchomienie:

```bash
python manage.py migrate
python manage.py runserver
```

---

## Struktura katalogów

```
DRF-url-shortener/
│
├── shortener/               # Aplikacja Django z logiką
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── serializers.py
│   ├── tests.py
│   ├── urls.py
│   ├── views.py
│   └── migrations/
│
├── url_shortener/           # Główny katalog projektu Django
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
├── .gitignore
├── db.sqlite3               # (w .gitignore)
├── manage.py
├── venv/                    # (w .gitignore)
├── requirements.txt
└── README.md
```


---

## Niejasności

- Nie było dla mnie jasne, czy rozwinięcie skróconego URLa ma być dostępne jako klasyczny endpoint API (zwracający JSON), czy jako przekierowanie.  
Zdecydowałem się na rozwiązanie z przekierowaniem po wejściu w /shrt/code, ponieważ to najbardziej przypomina sposób działania popularnych narzędzi typu TinyURL.
- Nie było określone, czy powtarzające się linki mają tworzyć nowe skróty – zdecydowałem, że lepiej nie duplikować, aby zaoszczędzić pamięć w bazie.

---

## Testy

Nie zawarto testów jednostkowych, ponieważ treść zadania sugerowała minimalną wersję produktu.  
Wersja testowa może być rozszerzeniem w przyszłości.  
Pomimo braku testów automatycznych, ręcznie weryfikowałem poprawność działania endpointów przy pomocy narzędzia Postman, co pozwoliło mi upewnić się, że API działa zgodnie z założeniami.

---
## Dodatkowe materiały

W repozytorium znajduje się również plik `zadanie.pdf` zawierający oryginalną treść zadania rekrutacyjnego, na podstawie którego powstał ten projekt.
Pozwala to lepiej zrozumieć wymagania i kontekst realizacji.

---

Projekt wykonany w ramach zadania rekrutacyjnego.  

