let job_span = document.querySelector('#job_span')



const job_span_clock = new THREE.Clock()

if (job_span){
    let job_span_clocking = function(){
        let curr_time = slideshow_clock.getElapsedTime()
        // job_span.classList.add('apply_shifting_span')
    
        if (curr_time < 3 && curr_time > 2){
            job_span_clock.start()
            // job_span.classList.remove('apply_shifting_span')
            // job_span.classList.add('apply_shifting_span_reverse')
            
        }
    
        requestAnimationFrame(job_span_clocking)
        // console.log('here')
    }
    
    
    // job_span_clocking();
    



}
