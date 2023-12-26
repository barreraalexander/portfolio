from pydantic import BaseModel, constr

class websiteLanguage(BaseModel):
    variant: int = 2


class contactAttribute(BaseModel):
    text: str

class contactLanguage(BaseModel):
    phone: contactAttribute = contactAttribute(text='+19548828507')
    email: contactAttribute = contactAttribute(text='barreraalexander93@gmail.com')
    

class metaAttribute(BaseModel):
    text: constr(strip_whitespace=True)


class metaLanguage(BaseModel):
    description: metaAttribute = metaAttribute(text=
        """
        Barrera Portfolio is a website used to
        showcase the web development experience
        of Alexander Barrera. He is a freelancing
        fullstack web developer from south Florida.        
        """
    )
    keywords: metaAttribute = metaAttribute(text=
        """
        fullstack engineer, web developer, programmer, web freelancer, web developer south florida, python engineer, database manager, coder, python flask, API manager, web designer 
        """
    )
    domain: metaAttribute = metaAttribute(text=
        "www.barrera-port.co"
    )
    domain_name: metaAttribute = metaAttribute(text=
        "Barrera Portfolio"
    )
    


class socialMediaAttribute(BaseModel):
    link: str

class socialMediaLinks(BaseModel):
    github: socialMediaAttribute = socialMediaAttribute(link='https://github.com/barreraalexander')
    linkedin: socialMediaAttribute = socialMediaAttribute(link='https://www.linkedin.com/in/abarrera-tech/')
    upwork: socialMediaAttribute = socialMediaAttribute(link='https://www.upwork.com/freelancers/~0120837e444852e684')