document.addEventListener('DOMContentLoaded', () => {

    // Modal functionality for viewing patient/doctor details
    const modal = document.getElementById('modal');
    const closeModal = document.getElementsByClassName('close')[0];

    // Open modal on button click
    document.querySelectorAll('.view-details').forEach(button => {
        button.addEventListener('click', (e) => {
            const modalContent = document.querySelector('.modal-content');
            const targetId = e.target.getAttribute('data-id');

            // Assuming you fetch patient/doctor data based on this ID
            // Use AJAX or Fetch API to get data dynamically

            modalContent.innerHTML = `
                <div class="modal-header">
                    Details for ${targetId}
                </div>
                <div class="modal-body">
                    <p>Some details about the patient/doctor/appointment/billing...</p>
                </div>
                <div class="modal-footer">
                    <button class="close-modal">Close</button>
                </div>
            `;
            modal.style.display = 'block';
        });
    });

    // Close modal on clicking 'X' or 'Close' button
    closeModal.addEventListener('click', () => {
        modal.style.display = 'none';
    });

    // Close modal on clicking outside the modal content
    window.onclick = function(event) {
        if (event.target == modal) {
            modal.style.display = 'none';
        }
    };

    // Show loading spinner on form submission
    document.querySelectorAll('form').forEach(form => {
        form.addEventListener('submit', (e) => {
            const spinner = document.createElement('div');
            spinner.className = 'spinner';
            spinner.innerHTML = '<div class="loader"></div>';
            form.appendChild(spinner);
        });
    });
});

// Example Spinner CSS
const spinnerStyles = document.createElement('style');
spinnerStyles.innerHTML = `
    .spinner {
        display: flex;
        justify-content: center;
        align-items: center;
        margin-top: 20px;
    }
    .loader {
        border: 16px solid #f3f3f3;
        border-radius: 50%;
        border-top: 16px solid #3498db;
        width: 60px;
        height: 60px;
        animation: spin 2s linear infinite;
    }
    @keyframes spin {
        0% { transform: rotate(0deg); }
        100% { transform: rotate(360deg); }
    }
`;
document.head.appendChild(spinnerStyles);
