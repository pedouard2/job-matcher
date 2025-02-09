"""Job posting model for storing job listings with company and posting details."""

from datetime import datetime
from typing import Annotated
from sqlmodel import Field, Session, SQLModel, create_engine, select
from fastapi import Depends, FastAPI, HTTPException, Query
from sqlalchemy import JSON, Column


class Job(SQLModel, table=True):

    id: Annotated[
        str,
        Field(
            primary_key=True, description="Primary key identifier for the job posting"
        ),
    ]
    role: Annotated[str, Field(description="Job title or role name")]
    company_name: Annotated[str, Field("Name of the hiring company")]
    company_num_employees: Annotated[
        int | None, Field("Number of employees at the company, if available")
    ]
    employment_type: Annotated[
        str | None, Field("Type of employment (e.g., full-time, part-time, contract)")
    ]
    location: Annotated[str | None, Field(description="Physical location of the job")]
    remote: Annotated[bool, Field(description="Whether the position is remote")]
    logo: Annotated[
        str | None, Field(description="URL or path to the company logo image")
    ]
    url: Annotated[str, Field(description="Link to the original job posting")]
    text: Annotated[str, Field(description="Full text description of the job posting")]
    date_posted: Annotated[datetime, Field(description="When the job was posted")]
    keywords: Annotated[
        list[str], Field(sa_column=Column(JSON), description="When the job was posted")
    ]
    source: Annotated[
        str, Field(description="Platform or website where the job was posted")
    ]
