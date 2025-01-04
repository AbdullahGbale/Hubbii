document.addEventListener('DOMContentLoaded', () => {
    const sidebar = document.querySelector('.sidebar');
    const toggleButton = document.querySelector('.toggle-btn');

    if (sidebar && toggleButton) {
        toggleButton.addEventListener('click', () => {
            sidebar.classList.toggle('collapsed');
            document.body.classList.toggle('sidebar-collapsed');

            // Accessibility enhancement
            const isCollapsed = sidebar.classList.contains('collapsed');
            toggleButton.setAttribute('aria-expanded', !isCollapsed);
        });
    } else {
        console.error('Sidebar or toggle button not found. Ensure the HTML structure matches the script.');
    }
});
