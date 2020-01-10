$('#contact-form').submit(function(e) {
    e.preventDefault()
    const name = $('input[name=name]').val();
    const email = $('input[name=email]').val();
    const telephone = $('input[name=telephone]').val();
    const message = $('textarea[name=message]').val();
    const select = $('select[name=subject]');
    const subject = select[0].value;
    const token = jQuery("[name=csrfmiddlewaretoken]").val();
    console.log(message);

    $.ajax({
        type: 'POST',
        url: '/contato/',
        data: {
            'csrfmiddlewaretoken': token,
            'name': name,
            'email': email,
            'telephone' : telephone,
            'subject': subject,
            'message': message
        },
        success: function(data){
            alert('E-mail enviado com sucesso, obrigado pelo seu tempo!')
        },
        error: function(data){
            alert('Algo deu errado, o E-mail não pôde ser enviado')
        }
    })
});