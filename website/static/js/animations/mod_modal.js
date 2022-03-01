const contact_modal_section = document.querySelector('#contact_modal_section')
const close_modal = contact_modal_section.querySelector('#close_modal')
const open_modal = document.querySelectorAll('.open_modal')

console.log(open_modal)

if (close_modal){
    close_modal.addEventListener('click', toggle_modal, false)

    for (let elem of open_modal){
        alert('here') 
        elem.addEventListener('click', toggle_modal, false)
    }

}

function toggle_modal(event){
    if (event.target==close_modal){
        contact_modal_section.dataset.status = "closed"
    } else {
        contact_modal_section.dataset.status = "open"
    }
}
