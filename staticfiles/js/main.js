function myFunction() {
    var navIcon = document.getElementById("menu-trigger");
    navIcon.classList.toggle("menu-clicked");
    var sideBar = document.getElementById("side");
    sideBar.classList.toggle("slide-in");
    var mainContent = document.getElementById("main");
    mainContent.classList.toggle("slide-content");
  }