$('#storePerson').on('click', function(){
    var button = $(this)
    var route = button.data('route')
    var student_name = button.parent().parent().find('.student_name')
    var rollnumber = button.parent().parent().find('.rollnumber')
    var student_class = button.parent().parent().find('.student_class')
    var student_age = button.parent().parent().find('.student_age')
    var avatar = button.parent().parent().find('.avatar')
    var token = $('[name=csrfmiddlewaretoken]')
    var editRoute = button.data('editroute')
    var deleteRoute = button.data('deleteroute')
    var showRoute = button.data('showroute')
    var formData = new FormData();
    formData.append('avatar', avatar.files);
    var context = {
        customer: customer.val(),
        service: service.val(),
        student_class: student_class.val(),
        student_age: student_age.val(),
        student_date: student_date.val()
    }

    // $.each(avatar.files, function(i, file) {
    //     formData.append('avatar[]', file);

    // });
    $.ajax({
        url: route,
        type: 'POST',
        // contentType: false,
        // processData: false,
        headers: {
            'X-CSRFToken': token.val()
        },
        context: {
            context
        },  
        success:function(data){
            context = JSON.parse(context)
            $('#closeModal').click()
            customer.val('')
            service.val('')
            $('#personsTable').find('tbody').append(
                '<tr>'+
                '<td>'+ context['customer'] +'</td>'+
                '<td>'+ context['service'] +'</td>'+

                '<td>'  +
                '<div class="d-flex justify-content-center">'+
                    '<div class="col-md-3">'+
                        '<a href="'+ showRoute + context['id'] +'" class="btn btn-secondary"><i class="fa fa-eye"></i></a>'+
                    '</div>'+
                    '<div class="col-md-3">'+
                        '<a class="btn btn-warning" href="'+ editRoute + data['id'] +'"><i class="fa fa-edit"></i></button></a>'+
                    '</div>'+
                    '<div class="col-md-3">'+
                        '<button class="btn btn-danger deletePerson" onclick="deletePerson(this)" data-route="'+deleteRoute + data['id'] +'/"><i class="fa fa-trash"></i></button>'+
                    '</div>'+
                '</div>'+
                '</td>'+
                '</tr>'
            )
        },
        error:function(data){
            console.log('ne ok')
            $('html').html(data['responseText'])
        }
    })
})

$('.deletePerson').on('click', function(){
    deletePerson(this)
})
    
function deletePerson (person) {
    if(confirm('Вы уверены?')){
        var button = $(person)
        var route = button.data('route')
        var tr = button.parent().parent().parent().parent()
        var token = $('[name=csrfmiddlewaretoken]')

        $.ajax({
            url: route,
            type: 'POST',
            // contentType: false,
            // processData: false,
            headers: {
                'X-CSRFToken': token.val()
            },  
            success:function(data){
                $('#deleteAlert').css('top', '0')
                setTimeout(function(){
                    $('#deleteAlert').css('top', '-300px')
                }, 3000)
                tr.hide('slow', function(){ tr.remove(); });
            },
            error:function(data){
                console.log('ne ok')
                $('html').html(data['responseText'])
            }
        })
    }
}
    // function checkParams(){
    //     var name = $('#name').val();
    //     var roll = $('#roll').val();
    //     var age = $('#age').val();
         
    //     if(name.length != 0 && roll.length != 0 && age.length != 0) {
    //         $('#submit').removeAttr('disabled');
    //     } 
    //     else {
    //         $('#submit').attr('disabled', 'disabled');
    //     }
    // }

    $(document).ready(function(){

        var checkedCheckboxes = [];
    
        $('button').click(function(){
            $('input').each(function(){
                if ($(this).is(':checked')) {
                    checkedCheckboxes.push($(this).val())  
                }
            });
    
        // Now we have an array
        console.log('JS Array: ');
        console.log(checkedCheckboxes);
    
        // Convert array to standard Javascript Object Literal
        var checkedCheckboxesObject = $.extend({}, checkedCheckboxes);
        console.log('JS Object: ');
        console.log(checkedCheckboxesObject);
    
        // Convert Object Literal to JSON
        var checkedCheckboxesJSON = JSON.stringify(checkedCheckboxesObject);
        console.log('JSON: ');
        console.log(checkedCheckboxesJSON);
    
        });
    });


