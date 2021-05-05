let lastKnownScrollPosition = 0;
let ticking = false;

function doSomething(scrollPos) {
    // console.log(scrollPos)
    if (90 <= scrollPos <= 100){
        // alert('passed')
    } else if (1200 <= scrollPos <= 1250){
        // alert('passed')
    }
    // positions: at scrollPos 100, remove opaque of class="clips"
    // positions: at scrollPos 1236, remove opaque of class="technologies_ctnr"
    // heartbeat your image from grayscale to color
}

document.addEventListener('scroll', function(e) {
  lastKnownScrollPosition = window.scrollY;

  if (!ticking) {
    window.requestAnimationFrame(function() {
      doSomething(lastKnownScrollPosition);
      ticking = false;
    });

    ticking = true;
  }
});