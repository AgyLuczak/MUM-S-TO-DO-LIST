

$(document).ready(function () {
    $(".sidenav").sidenav({ edge: "right" });
    $(".collapsible").collapsible();
    $('select').formSelect();
    $(".datepicker").datepicker({
        format: "dd mmmm, yyyy",
        yearRange: 3,
        showClearBtn: true,
        i18n: {
            done: "Select"
        }
    });
});

