(function () {
    var takePicture = document.querySelector("#take-picture"),
        showPicture = document.querySelector("#show-picture");

    if (takePicture && showPicture) {
        // Set events
        takePicture.onchange = function (event) {
            // Get a reference to the taken picture or chosen file
            var files = event.target.files,
                file;
            if (files && files.length > 0) {
                file = files[0];
                {
                    //upload
                    var xhr = new XMLHttpRequest();
                    xhr.open('POST', 'upload');
                    xhr.onload = function () {
                      if (xhr.status === 200) {
                        console.log('all done: ' + xhr.status);
                      } else {
                        console.log('Something went terribly wrong...');
                      }
                    };
                    var formData = new FormData();
                    formData.append('csrfmiddlewaretoken', csrf_token);
                    formData.append('file', file);
                    xhr.send(formData);
                }
                try {
                    // Create ObjectURL
                    var imgURL = window.URL.createObjectURL(file);

                    showPicture.addEventListener("load",
                                                  function (evt) {
                                                    URL.revokeObjectURL(imgURL);
                                                  })
                    showPicture.setAttribute("src", imgURL);
                }
                catch (e) {
                    try {
                        // Fallback if createObjectURL is not supported
                        var fileReader = new FileReader();
                        fileReader.onload = function (event) {
                            showPicture.src = event.target.result;
                        };
                        fileReader.readAsDataURL(file);
                    }
                    catch (e) {
                        //
                        var error = document.querySelector("#error");
                        if (error) {
                            error.innerHTML = "Neither createObjectURL or FileReader are supported";
                        }
                    }
                }
            }
        };
    }
})();