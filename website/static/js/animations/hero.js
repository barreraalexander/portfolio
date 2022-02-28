const hero_section = document.querySelector('#hero_section')
const three_d_ctnr = hero_section.querySelector('#night_ctnr')
const hero_ctnr = hero_section.querySelector('.hero_ctnr')


const hero_section_tl = gsap.timeline()



hero_section_tl.to(
    hero_ctnr,
    {
        duration: 1,
        y: '-2em',
        clipPath: 'polygon(0 0, 100% 0, 100% 100%, 0 100%)',
    },
), 1


hero_section_tl.to(
    three_d_ctnr,
    {
        duration: 1,
        ease: Sine.easeInOut,
        filter: 'blur(0px)',
    },
), 1


hero_section_tl.to(
    hero_ctnr,
    {
        duration: 2,
        delay: 3,
        ease: Sine.easeInOut,
        y: '2em',
        filter: 'blur(500px)',
    },
), 1



function mod_text(event){
    document.removeEventListener('scroll', mod_text)
    hero_section_tl.to(
        hero_ctnr,
        {
            duration: 2,
            ease: Sine.easeInOut,
            y: '2em',
            filter: 'blur(0px)',
        },
    ), 1
}

document.addEventListener('scroll', mod_text, false)