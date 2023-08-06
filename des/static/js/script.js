var videoOverlay = document.querySelector(".video-overlay");
var video = videoOverlay.querySelector("video");

video.loop = true;

videoOverlay.addEventListener("mouseover", function () {
  video.play();
});

videoOverlay.addEventListener("mouseout", function () {
  video.pause();
  video.currentTime = 0;
});
