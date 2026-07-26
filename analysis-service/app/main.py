from fastapi import FastAPI

from app.routes import health, analysis

app = FastAPI(
    title='Reverse Engineering Analysis Service',
    description='Backend service responsible for executable analysis'
)


app.include_router(health.router)
app.include_router(analysis.router)


@app.get("/")
def root():
    return {'message': 'Reverse Engineering Analysis Service'}