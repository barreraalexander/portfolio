from pydantic import BaseModel

class experience(BaseModel):
    description: str
    max_count: int

class experiences(BaseModel):
    contract: experience = experience(
        description="successfully completed contracts",
        max_count=18
    )

    technology: experience = experience(
        description="technologies mastered",
        max_count=21
    )

    year: experience = experience(
        description="years of experience",
        # maybe have this one be a delta of when I started
        # so that I don't have to update it
        max_count=6
    )
    