$(document).ready(function () {
    console.log(1);

    if ($('.amazon-carousel').length > 0) {
        $('.amazon-carousel').slick();

        // get alert option selection
        $('.contact-method-options').on('change', function () {
            let alert_option = $('.contact-method-options').find(':selected').val()

            if (alert_option == 'phone') {
                $('.contact-by > input').toggleClass('hidden');
                $('.contact-by input.phone-number').prop('required', true);
                $('.contact-by input.email-address').prop('required', false);
                console.log('phone')
            } else if (alert_option == 'email') {
                $('.contact-by > input').toggleClass('hidden');
                $('.contact-by input.phone-number').prop('required', false);
                $('.contact-by input.email-address').prop('required', true);
                console.log('email')
            }


        })
    }

    $('.zen-card').click(function () {
        console.log('click');
        $(this).toggleClass('active');
        // let volume = $(this).find('audio')[0].volume;
        if ($(this).hasClass("active")) {
            console.log('active');
            $(this).find('audio')[0].play();
            // console.log(volume);

        } else {
            console.log('Not Active');
            $(this).find('audio')[0].pause();
        }



    });

    // $('.zen-card .controls input').on('input change', $(this), function (e) {
    //     e.stopPropagation();
    //     let slider = $(this).find('input').val() / 100;
    //     console.log(slider);
    // })

    $('.zen-card .controls input').on('input', function (e) {
        e.stopPropagation();
        let slider = $(this).val() / 100;
        // let volume = $(this).parents('.zen-card').find('audio')[0].volume;
        let volume = $(this).parents('.zen-card').find('audio');
        // console.log(volume);
        // console.log(slider);
        volume.prop('volume', slider);
        let vol_icon = $(this).parents('.controls').find('i');
        let mute = 'fa-solid fa-volume-xmark';
        let vol_low = 'fa-solid fa-volume-low'
        let vol_high = 'fa-solid fa-volume-high'
        if (slider <= 0.01) {
            // console.log(vol_icon);
            vol_icon.removeClass();
            vol_icon.addClass(mute);
        } else if (slider <= 0.5) {
            vol_icon.removeClass();
            vol_icon.addClass(vol_low);
        } else {
            vol_icon.removeClass();
            vol_icon.addClass(vol_high);
        }
        // volume = slider;
    })


    $('.zen-card .controls').click(function (e) {
        e.stopPropagation();
    })

    $('.zen-page .shuffle').click(function () {
        // Shuffle the array of divs
        $('.zen-card.active').trigger('click');
        var shuffledDivs = select_random_three($('.zen-card'));
        // console.log(shuffledDivs);
        // Select the first three divs after shuffling
        var selectedDivs = shuffledDivs.slice(0, 3);

        // Add a class or apply any other action to the selected divs
        selectedDivs.trigger("click");
    })




    function select_random_three(array) {
        for (var i = array.length - 1; i > 0; i--) {
            var j = Math.floor(Math.random() * (i + 1));
            var temp = array[i];
            array[i] = array[j];
            array[j] = temp;
        }
        return array;
    }


}) // End doc ready
