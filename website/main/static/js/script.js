document.addEventListener('DOMContentLoaded', function() {
    const sidebar = document.querySelector('.sidebar');
    const mainContent = document.querySelector('.main-content');
    const toggleButton = document.createElement('button');
    toggleButton.classList.add('sidebar-toggle');
    toggleButton.innerHTML = '<span>&#9776</span>'; // Hamburger icon

    sidebar.insertBefore(toggleButton, sidebar.firstChild);

    toggleButton.addEventListener('click', function() {
        sidebar.classList.toggle('collapsed');
        mainContent.classList.toggle('collapsed');
    });

    // Reaction buttons
    const reactionButtons = document.querySelectorAll('.react-button');
    reactionButtons.forEach(button => {
        button.addEventListener('click', () => {
            const reactionType = button.dataset.reaction;
            const projectId = "{{ project.id }}"; // Make sure project is defined in template
            fetch(`/project/${projectId}/react/${reactionType}/`, {
                method: 'POST',
                headers: {
                    'X-CSRFToken': '{{ csrf_token }}',
                    'Content-Type': 'application/json'
                }
            })
            .then(response => response.json())
            .then(data => {
                if (data.status === 'success') {
                    // Update UI if needed (e.g., show a message)
                    console.log('Reaction sent successfully');
                } else {
                    console.error('Error sending reaction:', data.message);
                }
            })
            .catch(error => {
                console.error('Error sending reaction:', error);
            });
        });
    });
});