from pydantic import BaseModel, EmailStr
from typing import Optional, List
from datetime import datetime


# Token Schemas
class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    email: Optional[str] = None


# User Schemas
class UserBase(BaseModel):
    username: str
    email: EmailStr


class UserCreate(UserBase):
    password: str


class UserLogin(BaseModel):
    email: EmailStr
    password: str


class UserResponse(UserBase):
    id: int
    is_active: bool
    created_at: datetime

    class Config:
        orm_mode = True


# User Profile Schemas
class UserProfileBase(BaseModel):
    full_name: Optional[str] = None
    bio: Optional[str] = None
    interests: Optional[str] = None


class UserProfileCreate(UserProfileBase):
    pass


class UserProfileResponse(UserProfileBase):
    id: int
    user_id: int

    class Config:
        orm_mode = True


# Learning Material Schemas
class LearningMaterialBase(BaseModel):
    user_id: int
    title: str
    description: Optional[str] = None
    content_url: str
    entry_text: str


class LearningMaterialCreate(LearningMaterialBase):
    pass


class LearningMaterialResponse(LearningMaterialBase):
    id: int
    created_at: datetime

    class Config:
        orm_mode = True


# Job Listing Schemas
class JobListingBase(BaseModel):
    user_id: int
    title: str
    company: str
    location: str
    description: Optional[str] = None
    entry_text: str


class JobListingCreate(JobListingBase):
    pass


class JobListingResponse(JobListingBase):
    id: int
    created_at: datetime

    class Config:
        orm_mode = True


# Routine Task Schemas
class RoutineTaskBase(BaseModel):
    user_id: int
    task_name: str
    schedule_time: datetime
    entry_text: str


class RoutineTaskCreate(RoutineTaskBase):
    pass


class RoutineTaskResponse(RoutineTaskBase):
    id: int

    class Config:
        orm_mode = True


# Mental Health Entry Schemas
class MentalHealthEntryBase(BaseModel):
    user_id: int
    mood: str
    notes: Optional[str] = None
    entry_text: str


class MentalHealthEntryCreate(MentalHealthEntryBase):
    pass


class MentalHealthEntryResponse(MentalHealthEntryBase):
    id: int
    created_at: datetime

    class Config:
        orm_mode = True
