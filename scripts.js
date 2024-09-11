document.addEventListener('DOMContentLoaded', function() {
    // Fetch and display novels
    fetch('fetch_novels.php')
        .then(response => response.json())
        .then(data => {
            const novelGrid = document.querySelector('.novel-grid');
            data.forEach(novel => {
                const novelItem = document.createElement('div');
                novelItem.className = 'novel-item';
                novelItem.innerHTML = `
                    <img src="${novel.cover_image_url}" alt="${novel.title}">
                    <h3>${novel.title}</h3>
                    <p>${novel.description}</p>
                `;
                novelGrid.appendChild(novelItem);
            });
        });

    // Search functionality
    const searchForm = document.getElementById('search-form');
    const searchInput = document.getElementById('search-input');

    searchForm.addEventListener('submit', function(e) {
        e.preventDefault();
        const query = searchInput.value.toLowerCase();

        document.querySelectorAll('.novel-item').forEach(function(item) {
            const title = item.querySelector('h3').textContent.toLowerCase();
            if (title.includes(query)) {
                item.style.display = 'block';
            } else {
                item.style.display = 'none';
            }
        });
    });
});