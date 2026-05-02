

        function onClick() {
            window.scrollBy({
                top: 740,
                behavior: 'smooth'
            });
        }
//==============================  heart button==================================
       function changecolor(heartIcon) {
    // 1. Toggle the visual look (red color)
    heartIcon.classList.toggle('active');
    
    if (heartIcon.classList.contains('active')) {
        heartIcon.style.color = "red";
        
        // 2. Find the recipe details near the clicked heart
        const card = heartIcon.closest('.recipe-content-box');
        const title = card.querySelector('h2').innerText;
        
        // Create a recipe object
        const recipe = {
            id: title.toLowerCase().replace(/\s/g, '-'),
            title: title,
            // You can add an image path here if you want images in favorites too
        };

        // 3. Save to localStorage
        let favorites = JSON.parse(localStorage.getItem('myFavorites')) || [];
        
        // Only add if it's not already there
        if (!favorites.some(fav => fav.title === title)) {
            favorites.push(recipe);
            localStorage.setItem('myFavorites', JSON.stringify(favorites));
        }
    } else {
        heartIcon.style.color = "white"; // Or your default color
        
    }
}


       

// =================================== OPEN CARD==============================================
          let currentCard = null;

          function openCard(event, cardId) {
               // Prevent the click event from bubbling up to the 'window' object,
               // otherwise the window.onclick listener would immediately close the card we just opened.
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
          /**
           * Global click listener to detect clicks outside the active card.
           */
          window.onclick = function (event) {
               // Check if the clicked element is NOT the card itself 
               // AND is NOT a child element inside the card
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

                              // Check if there is actually a page to go back to in this tab
                              if (window.history.length > 1) {
                                   window.history.back();
                              } else {
                         
                                   window.location.href = "index.html"; 
                              }
                         };
                    }
           });

 //================================Admin Features=========================================      

// هذا الكود يعمل فور تحميل الصفحة
window.addEventListener("load", function() {
    // Get the recipe ID from the URL hash (everything after #)
    let recipeId = window.location.hash.substring(1);
    
    // Remove 'card' suffix if present (clean the ID)
    if (recipeId && recipeId.endsWith('card')) {
        recipeId = recipeId.replace('card', '');
    }

    if (recipeId) {
        // Add a longer delay to ensure the DOM is fully ready
        setTimeout(function() {
            // Try to open the details card
            const detailsCardId = recipeId + 'card';
            const detailsCard = document.getElementById(detailsCardId);
            
            if (detailsCard) {
                // Close any open card first
                if (currentCard) {
                    currentCard.style.display = "none";
                }
                
                // Open the card
                detailsCard.style.display = "block";
                currentCard = detailsCard;
                
                // Find and scroll to the recipe card
                const element = document.getElementById(recipeId);
                if (element) {
                    element.scrollIntoView({ behavior: 'smooth', block: 'center' });
                    
                    // Add highlight effect
                    element.style.transition = "all 0.3s ease";
                    element.style.transform = "translateY(-10px)";
                    element.style.boxShadow = "0 5px 15px rgba(0,0,0,0.3)";
                    
                    setTimeout(function() {
                        element.style.transform = "";
                        element.style.boxShadow = "";
                    }, 1000);
                }
            } else {
                console.log("Card not found:", detailsCardId);
            }
        }, 500); // Increased delay to 500ms
    }
});
 

     

