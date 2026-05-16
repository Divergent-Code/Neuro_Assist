from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, DateTime, Text
from sqlalchemy.orm import declarative_base, relationship
from datetime import datetime, timezone

Base = declarative_base()


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, nullable=False)
    email = Column(String, unique=True, nullable=False, index=True)
    hashed_password = Column(String, nullable=False)
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime, default=lambda: datetime.now(timezone.utc))

    profiles = relationship("UserProfile", back_populates="user", cascade="all, delete-orphan")
    learning_materials = relationship("LearningMaterial", back_populates="user", cascade="all, delete-orphan")
    job_listings = relationship("JobListing", back_populates="user", cascade="all, delete-orphan")
    routine_tasks = relationship("RoutineTask", back_populates="user", cascade="all, delete-orphan")
    mental_health_entries = relationship("MentalHealthEntry", back_populates="user", cascade="all, delete-orphan")


class UserProfile(Base):
    __tablename__ = "user_profiles"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    full_name = Column(String, nullable=True)
    bio = Column(String, nullable=True)
    interests = Column(String, nullable=True)

    user = relationship("User", back_populates="profiles")


class LearningMaterial(Base):
    __tablename__ = "learning_materials"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    title = Column(String, nullable=False)
    description = Column(String, nullable=True)
    content_url = Column(String, nullable=False)
    created_at = Column(DateTime, default=lambda: datetime.now(timezone.utc))
    entry_text = Column(Text, nullable=False)

    user = relationship("User", back_populates="learning_materials")

    def dict(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
            "title": self.title,
            "description": self.description,
            "content_url": self.content_url,
            "entry_text": self.entry_text,
            "created_at": self.created_at.isoformat() if self.created_at else None
        }


class JobListing(Base):
    __tablename__ = "job_listings"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    title = Column(String, nullable=False)
    company = Column(String, nullable=False)
    location = Column(String, nullable=False)
    description = Column(String, nullable=True)
    created_at = Column(DateTime, default=lambda: datetime.now(timezone.utc))
    entry_text = Column(Text, nullable=False)

    user = relationship("User", back_populates="job_listings")

    def dict(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
            "title": self.title,
            "company": self.company,
            "location": self.location,
            "description": self.description,
            "entry_text": self.entry_text,
            "created_at": self.created_at.isoformat() if self.created_at else None
        }


class RoutineTask(Base):
    __tablename__ = "routine_tasks"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    task_name = Column(String, nullable=False)
    schedule_time = Column(DateTime, nullable=False)
    entry_text = Column(Text, nullable=False)

    user = relationship("User", back_populates="routine_tasks")

    def dict(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
            "task_name": self.task_name,
            "schedule_time": self.schedule_time.isoformat() if self.schedule_time else None,
            "entry_text": self.entry_text
        }


class MentalHealthEntry(Base):
    __tablename__ = "mental_health_entries"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    mood = Column(String, nullable=False)
    notes = Column(String, nullable=True)
    created_at = Column(DateTime, default=lambda: datetime.now(timezone.utc))
    entry_text = Column(Text, nullable=False)

    user = relationship("User", back_populates="mental_health_entries")

    def dict(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
            "mood": self.mood,
            "notes": self.notes,
            "entry_text": self.entry_text,
            "created_at": self.created_at.isoformat() if self.created_at else None
        }
