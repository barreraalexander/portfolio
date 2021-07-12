  let lastKnownScrollPosition = 0;
  let ticking = false;
  let run1 = false;
  let run2 = false;
  let run3 = false;
  let project1 = document.querySelector('#project1');
  let project2 = document.querySelector('#project2');
  let project3 = document.querySelector('#project3');


  let deg_min = 0
  function shift_digital(scrollPos) {
      let digital = document.querySelectorAll('.digital')
      let deg_max = 360
      if (scrollPos > 2380){
        for (let digi of digital){
          digi.style.transform = `rotate(${deg_min}deg)`
        }
        deg_min += 1
        if (deg_min > deg_max){
          deg_min = 0
        } 
      }
  }

  let filter_min = 100
  let img = document.querySelector('.img_of_me')
  function alter_image(scrollPos){
    let filter_max = 0
    if (scrollPos > 2500){
      if (filter_min > filter_max){
        img.style.filter = "grayscale("+ filter_min +"%)"
        filter_min -= 3;
      }
    } else if (scrollPos < 2000){
      img.style.filter = "grayscale(100%)"
      filter_min = 100
    }
  }


  let divider = document.querySelector('.shimmering_div')
  function dissolve_divider(scrollPos){
    if(scrollPos > 10){
      divider.classList.add("dissolving_div")
      setTimeout(function(){
        divider.style.display = "none"
      }, 400)
    }
  }

  function check_no_scroll(scrollPos){
    setTimeout(function(){
      divider.classList.add("enlarge_div")
      var scroll_alert = document.createElement("p")
      var alert_text = document.createTextNode("Please Scroll Down")
      scroll_alert.appendChild(alert_text)
      scroll_alert.classList.add("scroll_alert")
      divider.appendChild(scroll_alert)
    }, 6000)
  }

  if (divider){
    check_no_scroll()
  }


  document.addEventListener('scroll', function(e) {
    lastKnownScrollPosition = window.scrollY;
    if (!ticking) {
      window.requestAnimationFrame(function() {
        shift_digital(lastKnownScrollPosition);
        dissolve_divider(lastKnownScrollPosition);
        if (screen.width >= 1600){
          alter_image(lastKnownScrollPosition);
        }
        ticking = false;
      });
      ticking = true;
    }
  });