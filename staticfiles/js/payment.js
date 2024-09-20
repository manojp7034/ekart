document.addEventListener('DOMContentLoaded', function() {
    const form = document.getElementById('payment-form');

    form.addEventListener('submit', function(event) {
        event.preventDefault();
        // Here you would typically send the payment data securely to your server for processing
        // Example: You can use fetch API to send data to the server
        // Replace '/process_payment' with your actual backend endpoint
        fetch('/process_payment', {
            method: 'POST',
            body: new FormData(form)
        })
        .then(response => {
            if (!response.ok) {
                throw new Error('Network response was not ok');
            }
            return response.json(); // Assuming your backend returns JSON response
        })
        .then(data => {
            // Handle successful payment response from server
            alert('Payment successful!');
            form.reset(); // Optional: Reset the form after successful payment
        })
        .catch(error => {
            // Handle errors from server or network issues
            console.error('Error:', error);
            alert('Payment failed. Please try again later.');
        });
    });
});
