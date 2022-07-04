let editor;
// const element = document.getElementById("editor");
// console.log(element)
document.getElementById('editor').style.fontSize='16px';
window.onload = function() {
    editor = ace.edit("editor");
    editor.setTheme("ace/theme/twilight");
    editor.session.setMode("ace/mode/c_cpp");
}

console.log("Hello World!");


function changeLanguage() {

    let language = $("#languages").val();

    if(language == 'c' || language == 'cpp')editor.session.setMode("ace/mode/c_cpp");
    else if(language == 'python')editor.session.setMode("ace/mode/python");
    else if(language == 'javascipt')editor.session.setMode("ace/mode/javascript");
}


function executeCode() {

    $.ajax({

        url: "http://127.0.0.1:8000/api/v1/code-post",

        method: "POST",

        data: {
            "csrfmiddlewaretoken": "{{ csrf_token }}",
            "language": $("#languages").val(),
            "code": editor.getSession().getValue(),
            "problem_id": 1,
            "user_id": 1,
        },

        success: function(response) {
            $(".output").text(response)
        }
    })
}