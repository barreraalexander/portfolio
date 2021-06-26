// var day_ctnr = document.querySelector('#day_ctnr')
// if (day_ctnr){
//     var day_scene = new THREE.Scene();
//     var day_camera = new THREE.PerspectiveCamera(
//         75,
//         window.innerWidth/window.innerHeight,
//         0.1,
//         1000
//         )
        
//     day_camera.position.z = 5


//     var day_renderer = new THREE.WebGLRenderer({
//         antialias: true
//     })

//     day_renderer.setClearColor(new THREE.Color('#94fcff'))


//     day_renderer.setSize(window.innerWidth, window.innerHeight)

//     document.body.querySelector('#day_ctnr').appendChild(day_renderer.domElement)
//     window.addEventListener('resize', ()=> {
//         day_renderer.setSize(window.innerWidth, window.innerHeight);
//         day_camera.aspect = window.innerWidth / window.innerHeight;
//         day_camera.updateProjectionMatrix()
//     })

//     var day_render = function (){
//         // requestAnimationFrame(render)

//         // let elasped_time = clock.getElapsedTime()   
//         // mesh1.rotation.y += 0.01;

//         // particles_mesh.rotation.y = (.0009 * elasped_time)
//         // particles_mesh.rotation.x = (.0009 * -mouse_y)
//         // particles_mesh.rotation.x = (.0009 * -mouse_x)

//         day_renderer.domElement.id = 'globe_canvas';
//         day_renderer.setClearColor(new THREE.Color('#94fcff'))
//         day_renderer.render(day_scene, day_camera)

//         //window.requestAnimationFrame()
//     }
//     day_render();


// }