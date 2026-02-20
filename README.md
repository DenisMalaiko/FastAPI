### Run Server
```uvicorn app.main:app --reload```

### Crete __init__.py
```touch app/models/__init__.py```

### Generate Migrations
```alembic revision --autogenerate -m "add name to users"```

### Run Migrations
```alembic upgrade head```