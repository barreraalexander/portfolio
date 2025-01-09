
import * as THREE from 'three';
import { OrbitControls } from 'three/addons/controls/OrbitControls.js';

import {modelLoader} from './elements/asyncModelLoader.js'
import {loadStars} from './elements/loadStars.js'

let moon, ship, planet;
var night_ctnr = document.querySelector('#night_ctnr')
if (night_ctnr){
    let moon_link = night_ctnr.dataset.moon_model
    let ship_link = night_ctnr.dataset.ship_model
    let planet_link = night_ctnr.dataset.planet_model


    var scene = new THREE.Scene();
    var camera = new THREE.PerspectiveCamera(
        75,
        window.innerWidth/window.innerHeight,
        0.1,
        1000
        )
    camera.position.z = 30


    var renderer = new THREE.WebGLRenderer({
        antialias: true
    })

    renderer.setClearColor(new THREE.Color('#111'))

    renderer.setSize(window.innerWidth, window.innerHeight)
    renderer.toneMapping = THREE.CineonToneMapping;

    night_ctnr.appendChild(renderer.domElement)



    const controls = new OrbitControls( camera, renderer.domElement );
    controls.maxPolarAngle = Math.PI * 0.495;
    controls.target.set( 0, 10, 0 );
    controls.minDistance = 40.0;
    controls.maxDistance = 100.0;
    controls.enableZoom = false;

    controls.update();


    const hemi_light = new THREE.HemisphereLight( 0xFFFFFF, 10 );
    scene.add(hemi_light)



    loadStars(scene)


    const moon_gltf = await modelLoader(moon_link)
    moon = moon_gltf.scene;
    moon.scale.set(3, 3, 3)
    moon.position.set(1, 8, 8)
    scene.add(moon)

    const ship_gltf = await modelLoader(ship_link)
    ship = ship_gltf.scene;
    // ship.scale.set(1.5, 1.5, 1.5)
    ship.position.set(4, 4, 0)    
    scene.add(ship)


    // const planet_gltf = await modelLoader(planet_link)
    // planet = planet_gltf.scene;
    // planet.scale.set(8, 8, 8)
    // planet.position.set(4, 18, -20)
    // scene.add(planet)


    window.addEventListener('resize', ()=> {
        renderer.setSize(window.innerWidth, window.innerHeight);
        camera.aspect = window.innerWidth / window.innerHeight;
        camera.updateProjectionMatrix()
    })

    const clock = new THREE.Clock()
    // var loaded_components = false

    var orbitRadius = 25
    var orbitRate;


    var render = function (){
        requestAnimationFrame(render)

        let elasped_time = clock.getElapsedTime()
        controls.update()

        try {

            if (moon){
                moon.rotation.y += 0.003;

            }

            if (planet){
                planet.rotation.y += 0.002;
                planet.rotation.x += 0.001;
            }


            if (ship){

                orbitRate = Date.now() * -0.0005;
                ship.position.set(
                Math.cos(orbitRate) * orbitRadius,
                0,
                Math.sin(orbitRate) * orbitRadius
                );

                ship.rotation.y -= 0.003;
                ship.rotation.x += 0.003;

            }

            if (window.innerWidth > 1399){
                // controls.enableRotate = true;
                // controls.update()

                if (moon){
                    moon.position.set = (1, 8, 8)
                }

                if (point_light){
                    point_light.position.z = 16
                }

            } else {
                // controls.enableRotate = false;
                // controls.update()

                if (moon){
                    moon.position.set = (0, 100, 0)

                }
                point_light.position.z = 8
            }

        } catch (error) {
        }



        renderer.domElement.id = 'globe_canvas';
        renderer.render(scene, camera)

    }
    render();
}
















// this section handles controls and manipulation of the camera
// var index_hero_ctnr = document.querySelector('.hero_ctnr')
var hero_text = document.querySelector('.text_ctnr')
// var control_panel = document.querySelector('.controls_ctnr')
// var mountain = document.querySelector('#mountain')
// var control_sets = document.querySelectorAll('.control_set')
// var control_message = document.querySelector('#controls_ctnr_message')
// var control_buttons = document.querySelectorAll('.control_button')

const show_controls_tl = gsap.timeline({
    paused: true,  
})

// mountain.style.transition = "2s"
// mountain.style.opacity = 0

// show_controls_tl.to(
//     mountain,
//     {
//         opacity: 0,
//         duration: .15,
//         ease: Sine.easeInOut,
//         display: 'none',
//     },
//     1
// ), 1

show_controls_tl.to(
    hero_text,
    {
        opacity: 0,
        duration: .15,
        ease: Sine.easeInOut,
        display: 'none',
    },
    1
), 1

// show_controls_tl.to(
//     control_panel,
//     {
//         duration: 1,
//         left: '2em',
//         x: '-20em',    
//         ease: Sine.easeInOut,
//     }
// ), 1



// function handleKeyDown(event, custom_action=false){
//     if (custom_action){
//         var action = custom_action
//     } else {
//         var action = event.key.toLowerCase()
//     }
    

//     element = document.querySelector(`#${action}`)
//     console.log(element)

//     element.classList.add('apply_click_light')

//     // element.style.transition = '.5s'
//     // element.style.filter = 'brightness(2)'
//     // element.style.filter = 'none'



//     if (action==='w'){
//         camera.position.z -= 1
//     }

//     if (action==='s'){
//         camera.position.z += 1
//     }

//     if (action==='d'){
//         camera.position.x += 1
//     }
//     if (action==='a'){
//         camera.position.x -= 1
//     }

//     if (action==='q'){
//         camera.position.y += 1
//     }
//     if (action==='e'){
//         camera.position.y -= 1
//     }

//     setTimeout(function(){
//         element.classList.remove('apply_click_light')
//     }, 250)

// }

// function handleKeyUp(event){
//     let action = event.key.toLowerCase()

//     if (action==='enter'){
//         control_message.innerText = 'controls for the camera'
    
//         show_controls_tl.play()

  
//         for (let elem of control_sets){
//             elem.style.display = 'flex';
//         }

//         for (let elem of control_buttons){
//             elem.addEventListener('click', handleControlClick, false)
//         }


//         document.addEventListener('keydown', handleKeyDown)
//         document.removeEventListener('keyup', handleKeyUp)
//     }
// }

// document.addEventListener('keyup', handleKeyUp)


// function handleControlClick(event){
//     handleKeyDown(event, custom_action=event.target.id)
// }