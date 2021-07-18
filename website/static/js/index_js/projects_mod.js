let projects = document.querySelectorAll('.project')
if (projects){
    for (let project of projects){
        project.addEventListener('click', run_slide, false)
    }
}


function run_slide(event){
    let img = this.querySelector('img')
    img.dataset.src_active = parseInt(img.dataset.src_active)+1
    if (img.dataset.src_active == 5){
        img.dataset.src_active = 1
    }
    // img.classList.add('dissipation')
    // setTimeout(function(){
    //     img.classList.remove('dissipation')
    // }, 2000)
    img.src = img.getAttribute(`data-src_${img.dataset.src_active}`)
    // img.classList.remove('dissipation')

}


const slideshow_clock = new THREE.Clock()
let clocking = function(){

    setTimeout(function(){
        requestAnimationFrame(clocking);
        for (let project of projects){

            // project.click()
        }
    }, 5000)
    
    // let elapsed = slideshow_clock.getElapsedTime()
    // let elapsed = slideshow_clock.elapsedTime
    // if (elapsed==5){
    //     console.log(elapsed)
    // }
}
clocking();
// console.log(clock)




// let check_time = clock.getElapsedTime() 
// console.log(check_time)

