
function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

function onClick() {
    window.scrollBy({
        top: 740,
        behavior: 'smooth'
    });
}

//==============================  heart button  ==================================
function changecolor(heartIcon) {
    const recipeId = heartIcon.getAttribute('data-id');
    
    if (!recipeId) {
        // Fallback for hardcoded recipes if they don't have a data-id yet
        heartIcon.classList.toggle('active');
        heartIcon.style.color = heartIcon.classList.contains('active') ? "red" : "white";
        return;
    }

    // Django AJAX Toggle Favorite
    fetch(`/toggle-favorite/${recipeId}/`, {
        method: 'POST',
        headers: {
            'X-CSRFToken': getCookie('csrftoken'),
            'Content-Type': 'application/json',
        },
    })
    .then(response => response.json())
    .then(data => {
        if (data.status === 'success') {
            if (data.is_favorite) {
                heartIcon.classList.add('active');
                heartIcon.style.color = "red";
                heartIcon.title = "Added to Favorites! ✨";
            } else {
                heartIcon.classList.remove('active');
                heartIcon.style.color = "white";
                heartIcon.title = "Add to Favorites";
            }
        } else {
            alert("Please login to save favorites!");
        }
    })
    .catch(error => {
        console.error('Error:', error);
    });
}

// =================================== OPEN CARD==============================================
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

window.onclick = function (event) {
    if (currentCard && currentCard.style.display === "block") {
        if (!currentCard.contains(event.target)) {
            currentCard.style.display = "none";
            currentCard = null;
        }
    }
}

//================================Go Back=========================================
document.addEventListener("DOMContentLoaded", () => {
    const backBtn = document.getElementById("backbutton");
    if (backBtn) {
        backBtn.onclick = function(event) {
            event.preventDefault();
            if (window.history.length > 1) {
                window.history.back();
            } else {
                window.location.href = "/"; 
            }
        };
    }
});

//================================Admin Features =========================================      
window.addEventListener("load", function() {
    let recipeId = window.location.hash.substring(1);
    if (recipeId && recipeId.endsWith('card')) {
        recipeId = recipeId.replace('card', '');
    }
    if (recipeId) {
        setTimeout(function() {
            const detailsCardId = recipeId + 'card';
            const detailsCard = document.getElementById(detailsCardId);
            if (detailsCard) {
                if (currentCard) currentCard.style.display = "none";
                detailsCard.style.display = "block";
                currentCard = detailsCard;
                const element = document.getElementById(recipeId);
                if (element) {
                    element.scrollIntoView({ behavior: 'smooth', block: 'center' });
                    element.style.transition = "all 0.3s ease";
                    element.style.transform = "translateY(-10px)";
                    element.style.boxShadow = "0 5px 15px rgba(0,0,0,0.3)";
                    setTimeout(function() {
                        element.style.transform = "";
                        element.style.boxShadow = "";
                    }, 1000);
                }
            }
        }, 500);
    }
});
