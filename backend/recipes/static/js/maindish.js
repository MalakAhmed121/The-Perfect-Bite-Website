function onClick() {
    window.scrollBy({
        top: 740,
        behavior: 'smooth'
    });
}

// ============================== HEART BUTTON ==============================
function changecolor(heartIcon) {
    heartIcon.classList.toggle('active');

    const card = heartIcon.closest('.recipe-content-box');
    const title = card ? card.querySelector('h2').innerText : null;

    let favorites = JSON.parse(localStorage.getItem('myFavorites')) || [];

    if (heartIcon.classList.contains('active')) {
        heartIcon.style.color = "red";

        if (title) {
            const recipe = {
                id: title.toLowerCase().replace(/\s/g, '-'),
                title: title
            };

            if (!favorites.some(fav => fav.title === title)) {
                favorites.push(recipe);
                localStorage.setItem('myFavorites', JSON.stringify(favorites));
            }
        }

    } else {
        heartIcon.style.color = "white";

        // remove from favorites
        if (title) {
            favorites = favorites.filter(fav => fav.title !== title);
            localStorage.setItem('myFavorites', JSON.stringify(favorites));
        }
    }
}

// ============================== OPEN CARD ==============================
let currentCard = null;

function openCard(event, cardId) {
    if (event && event.stopPropagation) {
        event.stopPropagation();
    }

    if (currentCard) {
        currentCard.style.display = "none";
    }

    const targetCard = document.getElementById(cardId);

    if (targetCard) {
        targetCard.style.display = "block";
        currentCard = targetCard;
    }
}

// ============================== CLOSE OUTSIDE CARD ==============================
window.onclick = function (event) {
    if (currentCard && currentCard.style.display === "block") {
        if (!currentCard.contains(event.target)) {
            currentCard.style.display = "none";
            currentCard = null;
        }
    }
};

// ============================== GO BACK ==============================
document.addEventListener("DOMContentLoaded", () => {
    const backBtn = document.getElementById("backbutton");

    if (backBtn) {
        backBtn.onclick = function (event) {
            event.preventDefault();

            if (window.history.length > 1) {
                window.history.back();
            } else {
                window.location.href = "home.html";
            }
        };
    }
});

// ============================== ADMIN FEATURES ==============================
window.addEventListener("load", function () {
    let recipeId = window.location.hash.substring(1);

    if (recipeId && recipeId.endsWith('card')) {
        recipeId = recipeId.replace('card', '');
    }

    if (recipeId) {
        setTimeout(function () {
            const detailsCardId = recipeId + 'card';
            const detailsCard = document.getElementById(detailsCardId);

            if (detailsCard) {
                if (currentCard) {
                    currentCard.style.display = "none";
                }

                detailsCard.style.display = "block";
                currentCard = detailsCard;

                const element = document.getElementById(recipeId);

                if (element) {
                    element.scrollIntoView({ behavior: 'smooth', block: 'center' });

                    element.style.transition = "all 0.3s ease";
                    element.style.transform = "translateY(-10px)";
                    element.style.boxShadow = "0 5px 15px rgba(0,0,0,0.3)";

                    setTimeout(function () {
                        element.style.transform = "";
                        element.style.boxShadow = "";
                    }, 1000);
                }
            } else {
                console.log("Card not found:", detailsCardId);
            }
        }, 500);
    }
});