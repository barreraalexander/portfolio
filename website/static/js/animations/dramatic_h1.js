let dramatic_h1_ctnrs = document.querySelectorAll('.dramatic_h1_ctnr')

// alert('here')

const dramatic_h1_observer_options = {
    root: null,
    threshold: .4,
}


const dramatic_h1_observer = new IntersectionObserver(function(entries, dramatic_h1_observer){
    entries.forEach(entry => {
        if (entry.isIntersecting){
            console.log(entry.target)
        } else {
        }
    })
}, dramatic_h1_observer_options);


for (let elem of dramatic_h1_ctnrs){
    // console.log(elem)
    dramatic_h1_observer.observe(elem)
}

