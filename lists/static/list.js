jQuery(document).ready(function ($) {
    $('body').on('input', 'keypress', function () {
        $('.has-error').hide();
    });
});
