let projects = document.querySelectorAll('.project')
if (projects){
    for (let project of projects){
        project.addEventListener('mouseover', run_slide, false)
    }
}

function run_slide(){
    let img = this.querySelector('.img_ctnr img')
    if (img.dataset.src_active==1){
        // img.src = img.dataset.src_1
    } else if (img.dataset.src_active==2){
        // img.src = img.dataset.src_2
    } else if (img.dataset.src_active==3) {
        // img.src = img.dataset.src_3        
    } else if (img.dataset.src_active==4){
        // img.dataset.src_active = 1
        // img.src = img.dataset.src_4        
        // img.dataset.src_active = 1
    }

}