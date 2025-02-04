from fastapi import FastAPI
#from app.api.v1.routes import users, items

app = FastAPI(title="Fast API Services Template")

##include roting services for different Versions
#app.include_routes()


@app.get("/")
def read_root():
    return {"message":"Welcome to Fast API"}