"""
Database Schemas for Office Fitout Website

Each Pydantic model represents a MongoDB collection. Collection name is the
lowercase of the class name (e.g., Inquiry -> "inquiry").
"""

from pydantic import BaseModel, Field, EmailStr
from typing import Optional, Literal

class Inquiry(BaseModel):
    """
    Lead capture for website enquiries
    Collection: "inquiry"
    """
    name: str = Field(..., description="Full name of the person enquiring")
    email: EmailStr = Field(..., description="Contact email address")
    phone: Optional[str] = Field(None, description="Phone number")
    company: Optional[str] = Field(None, description="Company name")
    service: Optional[str] = Field(None, description="Service of interest (e.g., Office Fitout, Design, Refurbishment)")
    budget: Optional[str] = Field(None, description="Approximate budget range")
    timeframe: Optional[str] = Field(None, description="Desired timeline")
    message: Optional[str] = Field(None, description="Additional details about the project")
    source: Optional[str] = Field(None, description="Lead source or campaign tag")
    page: Optional[str] = Field(None, description="Page URL where the form was submitted")
    consent_marketing: Optional[bool] = Field(False, description="Whether the user consents to marketing communications")

class Testimonial(BaseModel):
    """
    Client testimonials
    Collection: "testimonial"
    """
    client_name: str
    company: Optional[str] = None
    role: Optional[str] = None
    quote: str
    rating: Optional[int] = Field(None, ge=1, le=5)

class Project(BaseModel):
    """
    Past project highlights
    Collection: "project"
    """
    title: str
    location: Optional[str] = None
    sector: Optional[str] = None
    cover_image_url: Optional[str] = None
    description: Optional[str] = None
    slug: Optional[str] = None
