let nav = document.getElementById('nav');
window.addEventListener("scroll", function(event) {
            if(window.pageYOffset>100){

                nav.style.background = "#007bff";

            }
            else{
                nav.style.background = "transparent";
            }
        });