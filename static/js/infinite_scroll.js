$(document).ready(function () {
    let isLoading = false;
    let nextPage = 2;  // Start loading from the second page
    const loadMoreProductsUrl = $('#loading').data('load-more-products-url');  // Get URL from data attribute

    function loadMoreProducts() {
        if (isLoading) return; // Prevent multiple concurrent AJAX calls
        isLoading = true;
        $('#loading').show();

        $.ajax({
            url: loadMoreProductsUrl,  // Make sure this URL is correct
            type: 'GET',
            data: {'page': nextPage},  // Send the current page number to load
            success: function (data) {
                if (data.trim().length) { // Check if data is not just whitespace
                    $('#product-grid').append(data);
                    nextPage++;  // Prepare for the next page
                } else {
                    // No more products to load
                    $('#loading').text('No more products to show.').show();
                    $(window).off('scroll', onScroll); // Remove scroll handler
                }
                isLoading = false;
                $('#loading').hide();
            },
            error: function () {
                isLoading = false;
                $('#loading').hide();
                alert('Failed to load more products.');  // Error handling
            }
        });
    }

    // Scroll event handler
    function onScroll() {
        if ($(window).scrollTop() + $(window).height() > $(document).height() - 100) {
            loadMoreProducts();
        }
    }

    $(window).scroll(onScroll);
});
