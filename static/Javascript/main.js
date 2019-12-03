$('#contact-form').submit(function(e) {
    e.preventDefault()
    const name = $('input[name=name]').val()
    const email = $('input[name=email]').val()
    const telephone = $('input[name=telephone]').val()
    const subject = $('input[name=subject]').val()
    const message = $('input[name=message]').val()

    const token = jQuery("[name=csrfmiddlewaretoken]").val();

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