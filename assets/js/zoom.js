// Initialize medium zoom.
$(document).ready(function() {
  medium_zoom = mediumZoom('[data-zoomable]', {
<<<<<<< HEAD
    margin: 100,
=======
>>>>>>> 6e01a61a4ac1f39a8cef41d8bc249c54ef5187c5
    background: getComputedStyle(document.documentElement)
        .getPropertyValue('--global-bg-color') + 'ee',  // + 'ee' for trasparency.
  })
});
