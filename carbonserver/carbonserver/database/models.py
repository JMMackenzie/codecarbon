from carbonserver.database.database import Base

from sqlalchemy import Boolean, Column, DateTime, Float, ForeignKey, Integer, String
from sqlalchemy.orm import relationship


class Run(Base):
    __tablename__ = "runs"
     
    id = Column(Integer, primary_key=True, index=True) 
    timestamp = Column(DateTime)
    experiment_id = Column(Integer, ForeignKey("experiments.id"))
    experiment = relationship("Experiment", back_populates="runs")
    emission_id = Column(Integer,ForeignKey("emissions.id"))
    emission = relationship("Emission", back_populates="runs")
    
  
class Emission(Base):
    __tablename__ = "emissions"

    id = Column(Integer, primary_key=True, index=True)
    timestamp = Column(DateTime)
    # experiment_id = Column(Integer)
    duration = Column(Float)
    emissions = Column(Float)
    energy_consumed = Column(Float)
    experiment_id = Column(Integer, ForeignKey("experiments.id"))
    experiment = relationship("Experiment", back_populates="emissions")


class Experiment(Base):
    __tablename__ = "experiments"

    id = Column(Integer, primary_key=True, index=True)
    timestamp = Column(DateTime)
    name = Column(String)
    description = Column(String)
    is_active = Column(Boolean, default=True)
    ########################
    country_name = Column(String)
    country_iso_code = Column(String)
    region = Column(String)
    on_cloud = Column(Boolean, default=False)
    cloud_provider = Column(String)
    cloud_region = Column(String)
    emission_id = Column(Integer,ForeignKey("emission.id"))
    project_id = Column(Integer, ForeignKey("projects.id"))
    #########################
    emissions = relationship("Emission", back_populates="experiment")
    project = relationship("Project", back_populates="experiments")


class Project(Base):
    __tablename__ = "projects"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    description = Column(String)
    team_id = Column(Integer, ForeignKey("teams.id"))
    experiments = relationship("Experiment", back_populates="project")
    team = relationship("Team", back_populates="projects")


class Team(Base):
    __tablename__ = "teams"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    description = Column(String)
    organization_id = Column(Integer, ForeignKey("organizations.id"))
    projects = relationship("Project", back_populates="team")
    organization = relationship("Organization", back_populates="teams")


class Organization(Base):
    __tablename__ = "organizations"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    description = Column(String)
    teams = relationship("Team", back_populates="organization")


class User(Base):
    __tablename__ = "users"

    user_id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    email = Column(String, unique=True, index=True)
    password = Column(String)
    api_key = Column(String)
    is_active = Column(Boolean, default=True)
    # TODO: Associate user with his entities
