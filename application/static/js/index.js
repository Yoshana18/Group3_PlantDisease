function openPopup(popupId) {
    document.getElementById(popupId).style.display = "block";
}

function closePopup(popupId) {
    document.getElementById(popupId).style.display = "none";
}
function previewImage(event) {
        const file = event.target.files[0];
        const preview = document.getElementById('imagePreview');

        if (file) {
            const reader = new FileReader();
            reader.onload = function(e) {
                preview.src = e.target.result;
                preview.style.display = 'block';
            };
            reader.readAsDataURL(file);
        }
}

$(document).ready(function () {
    // Init
    $('#result').hide();

    $("#imageUpload").change(function (event) {
        $('#btn-predict').show();
        $('#result').text('');
        $('#result').hide();
        previewImage(event); });

    // Predict
    $('#btn-predict').click(function () {
        var form_data = new FormData($('#upload-file')[0]);

        // Make prediction by calling API /predict
        $.ajax({
            type: 'POST',
            url: '/predict',
            data: form_data,
            contentType: false,
            cache: false,
            processData: false,
            async: true,
            success: function (data) {
                $('#result').fadeIn(600);
                $('#result').text('Predicted Disease: ' + data);
            },
            error: function (xhr, status, error) {
                console.log("Error:", xhr.responseText);
            }
        });
    });
});

const predictButton = document.getElementById('btn-predict');

predictButton.onclick = async function() {
    try {
        const result = await makePrediction(); // Assuming makePrediction is your function
        console.log(result); // Output the result to the console
    } catch (error) {
        console.error("Error during prediction:", error);
    }
};