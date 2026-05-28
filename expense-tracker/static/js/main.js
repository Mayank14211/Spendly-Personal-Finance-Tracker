// Profile dropdown toggle
(function() {
    const profileBtn = document.getElementById('profileBtn');
    const profileMenu = document.getElementById('profileMenu');

    if (profileBtn && profileMenu) {
        profileBtn.addEventListener('click', function(e) {
            e.stopPropagation();
            profileMenu.classList.toggle('is-open');
        });

        // Close dropdown when clicking outside
        document.addEventListener('click', function() {
            profileMenu.classList.remove('is-open');
        });

        // Close on escape key
        document.addEventListener('keydown', function(e) {
            if (e.key === 'Escape') {
                profileMenu.classList.remove('is-open');
            }
        });
    }
})();
