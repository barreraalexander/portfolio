import { GLTFLoader } from 'three/addons/loaders/GLTFLoader.js';

const aloader = new GLTFLoader();

export function modelLoader(url) {
    return new Promise((resolve, reject) => {
      aloader.load(url, data=> resolve(data), null, reject);
    });
  }

// export function loadMoon(moon_link, scene){
//     let moon;
//     let loader = new GLTFLoader();

//     loader.load(
//         moon_link,
//         function ( gltf ) {
//             moon = gltf.scene;
//             moon.position.set(1, 5, 8)
//             scene.add( moon );
//             console.log(moon)
//             return moon
//         },
//     )
// }

// export function loadMoon(moon_link, scene){
//     let moon;
//     let  loader = new GLTFLoader();

//     loader.load(
//         moon_link,
//         function ( gltf ) {
//             moon = gltf.scene;
//             moon.position.set(1, 5, 8)
//             scene.add( moon );
//             console.log(moon)
//             return moon
//         },
//     )
// }

