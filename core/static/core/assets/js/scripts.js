function validateEmail(email) {
    const re = /^(([^<>()[\]\\.,;:\s@\"]+(\.[^<>()[\]\\.,;:\s@\"]+)*)|(\".+\"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;
    return re.test(email);
};

$("#btn-send").on("click", function() {
    var name = $("#name").val();
    if (name) {
        if (name.length <= 2) {
            swal({
                title: "Invalid Data!",
                text: "Please Enter Valid Name!",
                icon: "error",
            });
            return;
        }
    } else {
        swal({
            title: "Invalid Data!",
            text: "Please Enter Name!",
            icon: "error",
        });
        return;
    }
    var email = $("#email").val();
    if (!validateEmail(email)) {
        swal({
            title: "Invalid Data!",
            text: "Please Enter Valid Email!",
            icon: "error",
        });
        return;
    }
    var con_num = $("#contact_num").val();
    if (con_num) {
        if (con_num.length >= 10) {
            if (/^\d{10}$/.test(con_num)) {
                $.ajax({
                    type: "GET",
                    url: "/send-inquiry/",
                    method: "POST",
                    data: {
                        "name": $("#name").val(),
                        "contact_num": $("#contact_num").val(),
                        "email": $("#email").val(),
                        "content": $("#content").val(),
                        "subject": $("#subject").val(),
                    },
                    success: function(response) { // I guess the mistake is here
                        if (response['sended'] == '1') {
                            $('#contact_num').attr('disabled', 'disabled');
                            $('#name').attr('disabled', 'disabled');
                            $('#email').attr('disabled', 'disabled');
                            $('#btn-send').attr('disabled', 'disabled');
                            $('#contact_num').val('');
                            $('#name').val('');
                            $('#email').val('');
                            $('#content').val('');
                            swal({
                                title: "Good Job!",
                                text: "We will contact you soon!",
                                icon: "success",
                            });
                        } else {
                            swal({
                                title: "Server Issue!",
                                text: "Please try our email or contact number to contact us!",
                                icon: "error",
                            });
                        }
                    }
                });

            } else {
                swal({
                    title: "Invalid Data!",
                    text: "Please Enter Valid Number!",
                    icon: "error",
                });
                return false;
            }
        } else {
            swal({
                title: "Invalid Data!",
                text: "Please Enter Valid Number!",
                icon: "error",
            });
        }
    } else {
        swal({
            title: "Invalid Data!",
            text: "Please Enter Number!",
            icon: "error",
        });
    }
});