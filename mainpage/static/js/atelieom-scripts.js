/* 
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
function openModal() {
  document.getElementById('myModal').style.display = "block";
}

function closeModal() {
  document.getElementById('myModal').style.display = "none";
}

var slideIndex = 1;
showSlides(slideIndex);

function plusSlides(n) {
  showSlides(slideIndex = Number(slideIndex)+parseInt(n));
}

function currentSlide(n) {
  showSlides(slideIndex = parseInt(n));
}

function showSlides(n) {
  var i;
  var slides = document.getElementsByClassName("modalSlides");
  if (n > slides.length) {slideIndex = 1;}
  if (n < 1) {slideIndex = slides.length;}
  for (i = 0; i < slides.length; i++) {
      slides[i].style.display = "none";
  }
  slides[slideIndex-1].style.display = "block";
 
}

