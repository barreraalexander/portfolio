import * as THREE from 'three';

export function loadStars(scene){

    //star system
    const particles_geomtery = new THREE.BufferGeometry;
    const particles_count = 10000/2;

    const position_array = new Float32Array(particles_count * 3)

    for (let i = 0; i < particles_count * 3; i++){
        position_array[i] = (Math.random() - 0.5) * 70
    }

    particles_geomtery.setAttribute('position', new THREE.BufferAttribute(position_array, 3))

    const particle_material = new THREE.PointsMaterial({
        // size: 0.010,
        size: 0.005,
        color: 'white',
    })
    const particles_mesh = new THREE.Points(particles_geomtery, particle_material)
    scene.add(particles_mesh)

}