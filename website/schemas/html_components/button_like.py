from pydantic import BaseModel
from typing import Optional
from enum import IntEnum

class buttonLikeVariant(IntEnum):
    PRIMARY = 0
    SECONDARY = 1
    TERTIARY = 2
    GLASS = 3

class buttonLike(BaseModel):
    href: Optional[str] = None
    href_config: Optional[str] = None
    inner_text: str
    img_static_location: str
    variant: buttonLikeVariant
    

class buttonLikes(BaseModel):
    contact: buttonLike = buttonLike(
        inner_text = 'Contact',
        img_static_location = 'images/assets/icons/contact.svg',
        variant = buttonLikeVariant.TERTIARY
    )
    
    call: buttonLike = buttonLike(
        inner_text = 'Text Me',
        img_static_location = 'images/assets/icons/phone.svg',
        variant = buttonLikeVariant.PRIMARY,
        href="tel:954-882-8507"
    )

    resume: buttonLike = buttonLike(
        inner_text = 'Resume',
        href = 'docs/BarreraAlexanderResume21.pdf',
        href_config = 'download',
        img_static_location = 'images/assets/icons/resume.svg',
        variant = buttonLikeVariant.SECONDARY,
    )

    available: buttonLike = buttonLike(
        inner_text = 'Available',
        img_static_location = 'images/assets/icons/bolt.svg',
        variant = buttonLikeVariant.GLASS
    )
