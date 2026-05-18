function changecolor(el) { toggleFavorite({ stopPropagation: () => {} }, el); }

function toggleFavorite(event, element) {
    event.stopPropagation();

    const recipeId = element.dataset.id;

    fetch(`/toggle-favorite/${recipeId}/`, {
        method: "POST",
        headers: {
            "X-CSRFToken": getCookie("csrftoken"),
            "X-Requested-With": "XMLHttpRequest",
        },
    })
        .then(res => res.json())
        .then(data => {
            if (!data.is_favorite) {
                const card = document.getElementById(`recipe-${recipeId}`);
                if (card) card.remove();

                const details = document.getElementById(`recipe-${recipeId}-card`);
                if (details) details.remove();

                const remaining = document.querySelectorAll(".recipe-card");

                if (remaining.length === 0) {
                    document.getElementById("favorites-view").innerHTML = `
                    <h1 class="fav" style="margin-top:20px">MY FAVORITES</h1>
                    <div id="empty-state">
                        <img class="favimg" src="/static/bakeryimages/favorite.png" width="400">
                        <h2 class="fav">Your favorites haven't arrived yet...</h2>
                        <p class="P-fav">
                            Your personal collection of recipes is ready to grow.<br>
                            Start saving the recipes you love and build your delicious collection!
                        </p>
                        <a href="/recipes/" style="text-decoration:none">
                            <span class="favbutton">DISCOVER DELIGHTFUL RECIPES</span>
                        </a>
                    </div>
                `;
                }
            }
        });
}
window.openCard = function (event, cardId) {
    event.stopPropagation();

    const card = document.getElementById(cardId);

    if (!card) return;

    document.querySelectorAll(".details-card").forEach(c => {
        c.style.display = "none";
    });

    card.style.display = "block";
};

function getCookie(name) {
    let cookieValue = null;

    document.cookie.split(";").forEach(c => {
        c = c.trim();
        if (c.startsWith(name + "=")) {
            cookieValue = decodeURIComponent(c.split("=")[1]);
        }
    });

    return cookieValue;
}

document.addEventListener("click", function () {
    document.querySelectorAll(".details-card").forEach(card => {
        card.style.display = "none";
    });
});