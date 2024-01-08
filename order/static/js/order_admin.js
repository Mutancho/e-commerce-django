document.addEventListener('DOMContentLoaded', function () {
    // Function to update the subtotal for a given inline
    function updateSubtotal(priceInput, quantityInput, subtotalDisplay) {
        const price = parseFloat(priceInput.value) || 0;
        const quantity = parseInt(quantityInput.value) || 0;
        const subtotal = price * quantity;
        subtotalDisplay.textContent = subtotal.toFixed(2); // Assuming 2 decimal places for currency
    }

    // Function to update the total cost for all inlines
    function updateTotal() {
        let total = 0;
        document.querySelectorAll('.subtotal').forEach(function (element) {
            total += parseFloat(element.textContent) || 0;
        });
        // Update the total display, make sure to have an element with this ID in your HTML
        const totalDisplay = document.querySelector('#id_total_cost');
        if (totalDisplay) {
            totalDisplay.textContent = total.toFixed(2);
        }
    }

    // Function to fetch and update the price when a product is selected
    function fetchAndUpdatePrice(productSelect, priceInput, quantityInput, subtotalDisplay) {
        fetch(`/product/get-product-price/${productSelect.value}/`)
            .then(response => response.json())
            .then(data => {
                priceInput.value = data.price; // Update the price input
                updateSubtotal(priceInput, quantityInput, subtotalDisplay);
                updateTotal();
            })
            .catch(error => console.error('Error fetching product price:', error));
    }

    // Bind events for each inline on page load
    document.querySelectorAll('.dynamic-inline').forEach(function (inline, index) {
        // Adjust these selectors based on your actual form's structure
        const productSelect = inline.querySelector(`#id_items-${index}-product`);
        const priceInput = inline.querySelector(`#id_items-${index}-price`);
        const quantityInput = inline.querySelector(`#id_items-${index}-quantity`);
        const subtotalDisplay = inline.querySelector(`#id_items-${index}-subtotal`);

        // Bind the product selection change event
        if (productSelect) {
            productSelect.addEventListener('change', function () {
                fetchAndUpdatePrice(productSelect, priceInput, quantityInput, subtotalDisplay);
            });
        }

        // Bind the quantity change event
        if (quantityInput) {
            quantityInput.addEventListener('change', function () {
                updateSubtotal(priceInput, quantityInput, subtotalDisplay);
                updateTotal();
            });
        }
    });
});
