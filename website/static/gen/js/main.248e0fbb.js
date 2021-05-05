let lastKnownScrollPosition=0;let ticking=false;function doSomething(scrollPos){if(90<=scrollPos<=100){}else if(1200<=scrollPos<=1250){}
}
document.addEventListener('scroll',function(e){lastKnownScrollPosition=window.scrollY;if(!ticking){window.requestAnimationFrame(function(){doSomething(lastKnownScrollPosition);ticking=false;});ticking=true;}});var world_ctnr=document.querySelector('#world_ctnr')
if(world_ctnr){var scene=new THREE.Scene();var camera=new THREE.PerspectiveCamera(75,window.innerWidth/window.innerHeight,0.1,1000)
camera.position.z=5
var renderer=new THREE.WebGLRenderer({antialias:true})
renderer.setClearColor("#000");renderer.setSize(window.innerWidth,window.innerHeight)
document.body.querySelector('#world_ctnr').appendChild(renderer.domElement)
window.addEventListener('resize',()=>{renderer.setSize(window.innerWidth,window.innerHeight);camera.aspect=window.innerWidth/window.innerHeight;camera.updateProjectionMatrix()})
var geometry=new THREE.SphereBufferGeometry(1,20,20);var material=new THREE.MeshLambertMaterial({color:0x77FFC0});material.metalness=0.7
material.roughness=0.7
var mesh1=new THREE.Mesh(geometry,material)
mesh1.position.y=1;mesh1.position.x=1;mesh1.position.z=.5;scene.add(mesh1)
var geometry=new THREE.SphereBufferGeometry(.5,15,15);var material=new THREE.MeshLambertMaterial({color:0xBCBCBC});var mesh2=new THREE.Mesh(geometry,material)
mesh2.position.x=2.5;mesh2.position.y=2.5;mesh2.position.z=-.5;scene.add(mesh2)
var light1=new THREE.PointLight(0xFFFFFF,1,1000)
light1.position.set(1,1,0);scene.add(light1)
var light2=new THREE.PointLight(0xFFFFFF,1,1000)
light2.position.set(-1,-1,5);scene.add(light2)
const particleGeometry=new.THREE.BufferGeometry;var render=function(){requestAnimationFrame(render)
mesh1.rotation.y+=0.01;mesh2.rotation.x+=0.01;renderer.domElement.id='globe_canvas';renderer.render(scene,camera)
}
render();}