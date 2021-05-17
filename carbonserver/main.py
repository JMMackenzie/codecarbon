from carbonserver.database.database import engine
from carbonserver.database import models
from carbonserver.api.dependencies import get_query_token
from carbonserver.api.routers import (
    emissions,
    runs,
    experiments,
    projects,
    organizations,
    teams,
    users,
)

from fastapi import Depends, FastAPI

models.Base.metadata.create_all(bind=engine)

app = FastAPI(dependencies=[Depends(get_query_token)])


app.include_router(emissions.router)
app.include_router(runs.router)
app.include_router(experiments.router)
app.include_router(projects.router)
app.include_router(teams.router)
app.include_router(organizations.router)
app.include_router(users.router)


@app.get("/")
def default():
    return {"docs": "Please go to /docs"}


@app.get("/status")
def status():
    return {"status": "OK"}