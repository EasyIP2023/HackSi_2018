// This is a manifest file that'll be compiled into application.js, which will include all the files
// listed below.
//
// Any JavaScript/Coffee file within this directory, lib/assets/javascripts, or any plugin's
// vendor/assets/javascripts directory can be referenced here using a relative path.
//
// It's not advisable to add code directly here, but if you do, it'll appear at the bottom of the
// compiled file. JavaScript code in this file should be added after the last require_* statement.
//
// Read Sprockets README (https://github.com/rails/sprockets#sprockets-directives) for details
// about supported directives.
//
//= require jquery
//= require jquery.turbolinks
//= require bootstrap-sprockets
//= require rails-ujs
//= require activestorage
//= require turbolinks
//= require hacksi_web_app
//= require_tree .

function addOurMerdianImg() {
  var x = document.createElement("IMG");
  x.setAttribute("src", "https://github.com/jkolecr/HackSi_2018/blob/master/IMG_20181103_193819.jpg");
  x.setAttribute("width", "1000");
  x.setAttribute("height", "800");
  x.setAttribute("alt", "Our Merdian Img");
  document.body.appendChild(x);
}

function addMerdianImg() {
  var x = document.createElement("IMG");
  x.setAttribute("src", "https://survivinskyrim.files.wordpress.com/2015/11/morc16-8.jpg");
  x.setAttribute("width", "1000");
  x.setAttribute("height", "700");
  x.setAttribute("alt", "Merdian Img");
  document.body.appendChild(x);
}
