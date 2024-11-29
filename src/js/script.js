which image to display when the link is clicked.

javascript
Copy code
// Wait for the document to fully load
document.addEventListener('DOMContentLoaded', function () {
    // Get all the links with the 'update-link' class
    const links = document.querySelectorAll('.update-link');
    
    // Get the image display container and the image element
    const imageDisplay = document.getElementById('image-display');
    const displayedImage = document.getElementById('displayed-image');
    
    // Add an event listener to each link
    links.forEach(function (link) {
        link.addEventListener('click', function (event) {
            event.preventDefault(); // Prevent the default link behavior
            
            // Get the image source from the data-image attribute of the clicked link
            const imageSrc = link.getAttribute('data-image');
            
            // Set the src attribute of the displayed image
            displayedImage.src = imageSrc;
            
            // Make the image visible
            displayedImage.style.display = 'block';
        });
    });
});