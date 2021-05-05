let lastKnownScrollPosition=0;let ticking=false;function doSomething(scrollPos){if(90<=scrollPos<=100){}else if(1200<=scrollPos<=1250){}
}
document.addEventListener('scroll',function(e){lastKnownScrollPosition=window.scrollY;if(!ticking){window.requestAnimationFrame(function(){doSomething(lastKnownScrollPosition);ticking=false;});ticking=true;}});var world_ctnr=document.querySelector('#world_ctnr')
if(world_ctnr){var scene=new THREE.Scene();var camera=new THREE.PerspectiveCamera(75,window.innerWidth/window.innerHeight,0.1,1000)
camera.position.z=5
var renderer=new THREE.WebGLRenderer({antialias:true})
renderer.setClearColor("#000");renderer.setSize(window.innerWidth,window.innerHeight)
document.body.querySelector('#world_ctnr').appendChild(renderer.domElement)
window.addEventListener('resize',()=>{renderer.setSize(window.innerWidth,window.innerHeight);camera.aspect=window.innerWidth/window.innerHeight;camera.updateProjectionMatrix()})
var geometry=new THREE.SphereBufferGeometry(1,20,20);var material=new THREE.MeshLambertMaterial({color:0x77FFC0});var textureLoader=new THREE.TextureLoader()
var normal_texture=textureLoader.load('../images/textures/moon_texture.png')
material.normalMap=normal_texture
var mesh1=new THREE.Mesh(geometry,material)
mesh1.position.y=1;mesh1.position.x=1;mesh1.position.z=.5;scene.add(mesh1)
var geometry=new THREE.SphereBufferGeometry(.5,15,15);var material=new THREE.MeshLambertMaterial({color:0xBCBCBC});var textureLoader=new THREE.TextureLoader()
var normal_texture=textureLoader.load('../images/textures/moon_texture.png')
material.normalMap=normal_texture
var mesh2=new THREE.Mesh(geometry,material)
mesh2.position.x=2.5;mesh2.position.y=2.5;mesh2.position.z=-.5;scene.add(mesh2)
var light1=new THREE.PointLight(0xFFFFFF,1,1000)
light1.position.set(1,1,0);scene.add(light1)
var light2=new THREE.PointLight(0xFFFFFF,1,1000)
light2.position.set(-1,-1,5);scene.add(light2)
var light3=new THREE.SpotLight(0xa165ff,1)
light3.position.set(-10.5,-10.5,2);scene.add(light3)
const particles_geomtery=new THREE.BufferGeometry;const particles_count=10000;const position_array=new Float32Array(particles_count*3)
for(let i=0;i<particles_count*3;i++){position_array[i]=(Math.random()-0.5)*8}
particles_geomtery.setAttribute('position',new THREE.BufferAttribute(position_array,3))
const particle_material=new THREE.PointsMaterial({size:0.005,color:'white',})
const particles_mesh=new THREE.Points(particles_geomtery,particle_material)
scene.add(particles_mesh)
var star_cluster_geometry=new THREE.SphereBufferGeometry(1.5,20,15);var star_cluster_material=new THREE.PointsMaterial({size:0.015,transparent:true,color:'white'})
var star_cluster_mesh=new THREE.Points(star_cluster_geometry,star_cluster_material)
star_cluster_mesh.position.x=-2.5;star_cluster_mesh.position.y=-1.5;star_cluster_mesh.position.z=-2;scene.add(star_cluster_mesh)
star_cluster_material.size=.05;var star_cluster_mesh2=new THREE.Points(star_cluster_geometry,star_cluster_material)
star_cluster_mesh2.position.x=-2.5;star_cluster_mesh2.position.y=-1.5;star_cluster_mesh2.position.z=-2;scene.add(star_cluster_mesh2)
document.addEventListener('mousemove',animateParticles)
let mouse_x=0
let mouse_y=0
function animateParticles(event){mouse_y=event.clientY
mouse_x=event.clientX}
const clock=new THREE.Clock()
var render=function(){requestAnimationFrame(render)
let elasped_time=clock.getElapsedTime()
mesh1.rotation.y+=0.01;mesh2.rotation.x+=0.01;star_cluster_mesh.rotation.x+=0.001;particles_mesh.rotation.y=(.0009*elasped_time)
particles_mesh.rotation.x=(.0009*-mouse_y)
particles_mesh.rotation.x=(.0009*-mouse_x)
renderer.domElement.id='globe_canvas';renderer.setClearColor(new THREE.Color('#000'))
renderer.render(scene,camera)
}
render();}