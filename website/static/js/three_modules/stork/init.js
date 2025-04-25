import * as THREE from 'three';
import { OrbitControls } from 'three/addons/controls/OrbitControls.js';
import { modelLoader } from '../planets/elements/asyncModelLoader.js';

let stork, stork_animation_mixer;

const tablet_bp  = 767;
const desktop_bp  = 1400;

const $landing_section = $('#landing_section')
const $stork_container = $landing_section.find('.stork_container')
if ($landing_section.length > 0){
    // alert('good')    
    const stork_model_link = $landing_section[0].dataset.stork_model

    const landing_scene = new THREE.Scene();
    
    const landing_camera = new THREE.PerspectiveCamera(
        75,
        $stork_container.innerWidth()/$stork_container.innerHeight(),
        0.1,
        1000
        )
        
    // landing_camera.position.x = 15
    // landing_camera.position.y = 80
    // landing_camera.position.z = 140

    landing_camera.position.set(15, 80, 140)


    const landing_renderer = new THREE.WebGLRenderer({
        antialias: true,
        alpha: true,
    })

    landing_renderer.setClearColor(
        new THREE.Color('#f8f8f8'),
        0
    )


    landing_renderer.setSize(
        $stork_container.innerWidth(),
        $stork_container.innerHeight()
    )

    window.addEventListener('resize', ()=> {
        landing_renderer.setSize($stork_container.innerWidth(), $stork_container.innerHeight());
        landing_camera.aspect = $stork_container.innerWidth()/$stork_container.innerHeight();
        landing_camera.updateProjectionMatrix()
    })

    
    landing_renderer.toneMapping = THREE.CineonToneMapping;

    $stork_container.append(landing_renderer.domElement)

    const controls = new OrbitControls(
        landing_camera,
        landing_renderer.domElement
    );

    controls.maxPolarAngle = Math.PI * 0.495;
    controls.minDistance = 80.0;
    controls.maxDistance = 300.0;

    controls.update();


    const hemi_light = new THREE.HemisphereLight(
        new THREE.Color('#ffffff'),
        new THREE.Color('#c8c8c8'),
        10
    );


    landing_scene.add(hemi_light)

    const stork_gltf = await modelLoader(
        stork_model_link
    )
    
    stork = stork_gltf.scene;
    // stork.scale.set(.25, .25, .25);
    stork.position.set(0, 0, -20);
    landing_scene.add(stork);



    stork_animation_mixer = new THREE.AnimationMixer(stork)
    const clips = stork_gltf.animations
    // console.log(stork_gltf)
    // console.log(clips)

    const clip = THREE.AnimationClip.findByName(clips, 'storkFly_B_')
    const action = stork_animation_mixer.clipAction(clip)

    action.play();


    const clock = new THREE.Clock();



    var landing_render = function (){
        const delta = clock.getDelta();
        requestAnimationFrame(landing_render)

        // let elasped_time = clock.getElapsedTime()
        controls.update()


        if (stork){
            stork.rotation.y += .004;
            if (window.innerWidth < desktop_bp){
                stork.scale.set(1, 1, 1)

                // controls.enableRotate = false;            
                // controls.update()
                
            } else if (window.innerWidth > tablet_bp) {
                // controls.enableRotate = true;            
                // controls.update()

                
            } else if (window.innerWidth > desktop_bp){
                stork.scale.set(1.25, 1.25, 1.25)
    
            }
            

        }

        if (stork_animation_mixer){
            stork_animation_mixer.update(delta)

        }

        landing_renderer.domElement.id = 'stork_canvas';
        
        landing_renderer.render(
            landing_scene,
            landing_camera
        )

    }
    landing_render();


}