// Update the URL below with the server-side script URL that handles image processing and caption generation.
const serverURL = "http://127.0.0.1:8000/uploadfile/";

// Function to read and display the selected image
function readURL(input) {
    if (input.files && input.files[0]) {
        const reader = new FileReader();

        reader.onload = function (e) {
            // Hide the initial upload UI
            $('.image-upload-wrap').hide();
            // Set the source of the image preview to the selected image
            $('.file-upload-image').attr('src', e.target.result);
            // Show the image preview
            $('.file-upload-content').show();
        };

        // Read the selected image file
        reader.readAsDataURL(input.files[0]);
    }
}

// Trigger the file input dialog on button click
$('.file-upload-btn').on('click', function () {
    $('.file-upload-input').trigger('click');
    // e.preventDefault();
    // let token = sessionStorage.getItem('token');
    // let formdata = new FormData();
    // formdata.append('in_file', document.getElementById("media").files[0]); 
    // fetch('http://127.0.0.1:8000/uploadfile/', {
    //   method: 'POST',
    //   body: formdata,
      // headers: {
      //   'content-type': 'multipart/form-data'
      // }
    // })
    // .then(res => res.json())
    // .then(data => {
    //   console.log(data)
    // })
});

// Handle image upload and caption generation
$('.file-upload-input').on('change', function () {
    const fileInput = this;
    const file = fileInput.files[0];

    if (file) {
        const formData = new FormData();
        console.log(file);
        formData.append("in_file", file);

        // Send image file to the server for processing
        fetch("http://localhost:8000/uploadfile", {
            method: "POST",
            body: formData,
            // headers: {
            //   'accept': 'application/json',
            //   'Content-Type': 'undefined'
            // }
        })
        .then(response => response.json())
        .then(data => {
            console.log(data);
            const captions = data.captions;
            const captionList = document.getElementById("caption-list");
            captionList.innerHTML = "";

            // Display generated captions
            captions.forEach(caption => {
                const listItem = document.createElement("li");
                listItem.textContent = caption;
                listItem.className = "list-group-item";
                captionList.appendChild(listItem);
            });

            // Show the caption container
            document.getElementById("caption-container").style.display = "block";
        })
        .catch(error => console.error("laudaaaaaaaaa"));
    }
});