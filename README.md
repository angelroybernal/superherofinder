# Superhero Finder app

### How to:

First install requirements using:

```sh
python -m pip install -r requirements.txt
```

Then run the database using:

```sh
cd database && docker-compose up
```

Now load the data to database by running:

```sh
python cargar_datos.py
```

Finally, let's run the app:

```sh
streamlit run app.py
```