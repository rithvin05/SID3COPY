
document.querySelectorAll("img").forEach(img => {
  console.log("runs");
  img.onerror = function () {
    this.onerror = null;

    this.src = "../js/blankPic.webp";
    this.alt = "";
  };
  
});
