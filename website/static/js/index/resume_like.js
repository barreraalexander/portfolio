let resume_like = document.querySelector('#resume_like')
let comment_ctnrs = resume_like.querySelectorAll('.comment_ctnr')
// let split = resume_like.querySelector('hr')

const resume_tl = gsap.timeline({
    paused: true,
})


resume_tl.to(
    resume_like,
    {
        delay: .5,
        duration: 2,
        filter: 'grayscale(0%)',
        ease: Sine.easeInOut,
    }
), 0


resume_tl.to(
    comment_ctnrs,
    {
        duration: .25,
        // clipPath: 'polygon(0 0, 100% 0, 100% 100%, 0 100%)',
        // clipPath: 'polygon(20px 0px, 100% 0px, 90% 100%, 0px 100%)',
        y: "1em",
        ease: Sine.easeInOut,
    }
), 0


const resume_observer_options = {
    root: null,
    threshold: .01,
}

const resume_observer = new IntersectionObserver(function(entries, resume_observer){
    entries.forEach(entry => {
        if (entry.isIntersecting){
            resume_tl.play()
        } else {
            resume_tl.reverse()
        }
    })
}, resume_observer_options);


resume_observer.observe(resume_like)