// Initializing various Materialize components when the document is ready
$(document).ready(function () {
    $(".sidenav").sidenav({ edge: "right" });
    $('select').formSelect();
    $('.collapsible').collapsible();
    $('.dropdown-trigger').dropdown();
    $(".datepicker").datepicker({
        format: "dd mmmm, yyyy",
        yearRange: 3,
        showClearBtn: true,
        i18n: {
            done: "Select"
        }
    });
});


//Footer collapsible
$(document).ready(function () {
    $('#filter-icon').click(function () {
        $('#showCollapsible').toggle();
    });
    // Sorting
    $('#alpha-order-items').click(function (event) {
        event.preventDefault();
        window.location.href = '/get_to_do_items?sort=alpha';
    });

    $('#alpha-order-categories').click(function (event) {
        event.preventDefault();
        window.location.href = '/get_categories?sort=alpha';
    });

    $('#category-filter').click(function (event) {
        event.preventDefault();
        window.location.href = '/get_to_do_items?category=true';
    });

    $('#user-filter').click(function (event) {
        event.preventDefault();
        window.location.href = '/get_categories?sort=created_by';
    });

    $('#imp-order').click(function (event) {
        event.preventDefault();
        window.location.href = '/get_to_do_items?sort=important';
    });
});


//credit to Tim Nelson (Code Institute)
$(document).ready(function () {
    validateMaterializeSelect();
});

function validateMaterializeSelect() {
    let classValid = { "border-bottom": "1px solid #ff69b4", "box-shadow": "0 1px 0 0 #ff69b4" };
    let classInvalid = { "border-bottom": "1px solid #800080", "box-shadow": "0 1px 0 0 #800080" };

    if ($("select.validate").prop("required")) {
        $("select.validate").css({ "display": "block", "height": "0", "padding": "0", "width": "0", "position": "absolute" });
    }

    $(".select-wrapper input.select-dropdown").on("focusin", function () {
        $(this).parent(".select-wrapper").on("change", function () {
            if ($(this).children("ul").children("li.selected:not(.disabled)").on("click", function () { })) {
                $(this).children("input").css(classValid);
            }
        });
    }).on("click", function () {
        if ($(this).parent(".select-wrapper").children("ul").children("li.selected:not(.disabled)").css("background-color") === "your selected item background color") {
            $(this).parent(".select-wrapper").children("input").css(classValid);
        } else {
            $(".select-wrapper input.select-dropdown").on("focusout", function () {
                if ($(this).parent(".select-wrapper").children("select").prop("required")) {
                    if ($(this).css("border-bottom") != "1px solid #ff69b4") {
                        $(this).parent(".select-wrapper").children("input").css(classInvalid);
                    }
                }
            });
        }
    });
}

//Confirmation dialogs for deleting items or categories

function confirmDeleteItem() {
    return confirm('Are you sure you want to delete this item?');
}

function confirmDeleteAllChecked() {
    return confirm('Are you sure you want to delete all checked items?');
}

function confirmDeleteCategory() {
    return confirm('Are you sure you want to delete this category?');
}

// Visibility of the search container
function toggleSearch() {
    const searchContainer = document.getElementById("search-container");
    searchContainer.classList.toggle("show");
}


