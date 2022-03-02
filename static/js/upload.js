function readURL(input) {

    if (input.files && input.files[0]) {
        var reader = new FileReader();
        reader.onload = function (e) {
            $('#blah2').attr('src', e.target.result);
        }
        reader.readAsDataURL(input.files[0]);
    }


}

let today = new Date();
let year = today.getFullYear();
let month = ('0' + (today.getMonth() + 1)).slice(-2);
let day = ('0' + today.getDate()).slice(-2);
let hours = ('0' + today.getHours()).slice(-2);
let minutes = ('0' + today.getMinutes()).slice(-2);
let seconds = ('0' + today.getSeconds()).slice(-2);
let timeString = year + month  + day + hours + '_' + minutes + '_' + seconds;

function filter_k() {
    $('#hidden_area').empty()
    let title = 'kan' + timeString
    let file = $('#uploaded_file')[0].files[0]
    let form_data = new FormData()

    form_data.append("key", title)
    form_data.append("img", file)
    $.ajax({
        type: "POST",
        url: "http://nst10-dev.ap-northeast-2.elasticbeanstalk.com/api/v1/nsts/",
        dataType: 'json',
        data: form_data,
        cache: false,
        contentType: false,
        processData: false,
        success: function (response) {
            let urls = response['file_url']

            $('#card-cadin-select1').attr('src', urls)

            let temp_html = `<textarea type=text id="api" class="form-control" placeholder="" name = 'url_api'>${urls}</textarea>`
            $('#hidden_area').append(temp_html)
            $('#hidden_area').hide()
        }
    })
}
function filter_mosa() {
     $('#hidden_area').empty()
    let title = 'mosa' + timeString
    let file = $('#uploaded_file')[0].files[0]
    let form_data = new FormData()

    form_data.append("key", title)
    form_data.append("img", file)
    $.ajax({
        type: "POST",
        url: "http://nst10-dev.ap-northeast-2.elasticbeanstalk.com/api/v1/nsts/mosaic",
        dataType: 'json',
        data: form_data,
        cache: false,
        contentType: false,
        processData: false,
        success: function (response) {
            let urls = response['file_url']

            $('#card-cadin-select1').attr('src', urls)

            let temp_html = `<textarea type=text id="api" class="form-control" placeholder="" name = 'url_api'>${urls}</textarea>`
            $('#hidden_area').append(temp_html)
            $('#hidden_area').hide()
        }
    })
}
function filter_pi() {
    $('#hidden_area').empty()
    let title = 'pica' + timeString
    let file = $('#uploaded_file')[0].files[0]
    let form_data = new FormData()

    form_data.append("key", title)
    form_data.append("img", file)
    $.ajax({
        type: "POST",
        url: "http://nst10-dev.ap-northeast-2.elasticbeanstalk.com/api/v1/nsts/piccasso",
        dataType: 'json',
        data: form_data,
        cache: false,
        contentType: false,
        processData: false,
        success: function (response) {
            let urls = response['file_url']

            $('#card-cadin-select1').attr('src', urls)

            let temp_html = `<textarea type=text id="api" class="form-control" placeholder="" name = 'url_api'>${urls}</textarea>`
            $('#hidden_area').append(temp_html)
            $('#hidden_area').hide()
        }
    })
}
function filter_monet() {
     $('#hidden_area').empty()
    let title = 'monet' + timeString
    let file = $('#uploaded_file')[0].files[0]
    let form_data = new FormData()

    form_data.append("key", title)
    form_data.append("img", file)
    $.ajax({
        type: "POST",
        url: "http://nst10-dev.ap-northeast-2.elasticbeanstalk.com/api/v1/nsts/monet",
        dataType: 'json',
        data: form_data,
        cache: false,
        contentType: false,
        processData: false,
        success: function (response) {
            let urls = response['file_url']

            $('#card-cadin-select1').attr('src', urls)

            let temp_html = `<textarea type=text id="api" class="form-control" placeholder="" name = 'url_api'>${urls}</textarea>`
            $('#hidden_area').append(temp_html)
            $('#hidden_area').hide()
        }
    })
}



function close_box() {
    $('#blank').hide()
    $('#card-cadin-select1').show()
}

function close_box2() {
    $('#blank2').hide()
    $('#blah2').show()
    $('#hidden_area').empty()
    $('#card-cadin-select1').hide()
    $('#blank').show()
    $('.button_show').show()


}
