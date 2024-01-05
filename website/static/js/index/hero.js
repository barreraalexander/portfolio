const hero_section_tl = gsap.timeline()

hero_section_tl.to(
    $('.hero_ctnr'),
    {
        duration: 1,
        y: '-2em',
        clipPath: 'polygon(0 0, 100% 0, 100% 100%, 0 100%)',
    },
), 1


hero_section_tl.to(
    $('#night_ctnr'),
    {
        duration: 1,
        filter: 'blur(0px)',
        ease: Sine.easeInOut,
    },
), 1




// function mod_text(event){
//     document.removeEventListener('scroll', mod_text)
//     hero_section_tl.to(
//         $('#hero_section'),
//         {
//             duration: .1,
//             y: '-2em',
//             filter: 'blur(0px)',
//             ease: Sine.easeInOut,
//         },
//     ), 1
// }
