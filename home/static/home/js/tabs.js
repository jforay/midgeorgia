const tabVideos = {
    'welcome': `
        <div class="yt-embed-holder">
            <iframe width="560" height="315"
                src="https://www.youtube.com/embed/F3i04XHN0Qg?si=sSXKT0_V-Z4dzvlg&autoplay=1&mute=1&loop=1&controls=0&color=white&modestbranding=0&rel=0&playsinline=1&enablejsapi=1&playlist=F3i04XHN0Qg"
                title="YouTube video player"
                frameborder="0"
                allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share"
                referrerpolicy="strict-origin-when-cross-origin"
                allowfullscreen>
            </iframe>
        </div>
    `,
    'how-it-works': `
        <div class="yt-embed-holder">
            <iframe width="560" height="315"
                src="https://www.youtube.com/embed/TMDQG8rzOhc?si=sSXKT0_V-Z4dzvlg&autoplay=1&mute=1&loop=1&controls=0&color=white&modestbranding=0&rel=0&playsinline=1&enablejsapi=1&playlist=TMDQG8rzOhc"
                title="YouTube video player"
                frameborder="0"
                allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share"
                referrerpolicy="strict-origin-when-cross-origin"
                allowfullscreen>
            </iframe>
        </div>
    `
};

function showTab(tabId) {
    const contents = document.querySelectorAll('.tab-content');
    contents.forEach(content => {
        content.style.display = 'none';
        content.innerHTML = '';
    });

    const buttons = document.querySelectorAll('.tab-button');
    buttons.forEach(button => button.classList.remove('active'));

    const selectedTab = document.getElementById(tabId);
    selectedTab.style.display = 'block';
    selectedTab.innerHTML = tabVideos[tabId];

    const clickedButton = document.querySelector(`.tab-button[onclick="showTab('${tabId}')"]`);
    if (clickedButton) {
        clickedButton.classList.add('active');
    }
}

document.addEventListener('DOMContentLoaded', function () {
    showTab('welcome');
});