// --- Page Initialization ---
document.addEventListener('DOMContentLoaded', () => {
    const tabBtns = document.querySelectorAll('.tab-btn');
    const recipesContainer = document.getElementById('recipes-container');
    const modal = document.getElementById('recipeModal');
    let storedRecipes = [];
    try {
        const rawData = localStorage.getItem('recipes');
        storedRecipes = rawData ? JSON.parse(rawData) : [];
        if (!Array.isArray(storedRecipes)) storedRecipes = [];
    } catch (err) {
        console.error("Failed to parse recipes from localStorage:", err);
        storedRecipes = [];
    }

    // 1. --- Render Custom Recipes ---
    if (recipesContainer && storedRecipes.length > 0) {
        storedRecipes.forEach(r => {
            if (!r || !r.id) return;
            const courseLower = (r.course || "").toLowerCase();
            if (courseLower.includes('healthy')) {
                let rId = String(r.id).toLowerCase();
                if (rId.endsWith('card')) rId = rId.slice(0, -4);
                if (!document.getElementById(rId)) {
                    const newCard = document.createElement('div');
                    newCard.className = 'recipe-card all keto'; 
                    newCard.id = rId;
                    let imgPath = r.image ? r.image : '../../photos/Healthy_images/Healthy Salmon & Avocado Salad.jfif';
                    // Ensure the image string isn't an incorrect raw path
                    if (imgPath && !imgPath.includes('url(') && !imgPath.startsWith('../../')) {
                        imgPath = '../../' + imgPath;
                    }
                    newCard.innerHTML = `
                        <div class="card-image" style="background-image: url('${imgPath}');">
                            <span class="diet-badge">Custom</span>
                            <button class="grid-heart-btn" onclick="changecolor(this)" aria-label="Favorite">❤</button>
                        </div>
                        <div class="card-body">
                            <h3>${r.name}</h3>
                            <p>${r.description || r.ingredients || "A new delicious healthy recipe."}</p>
                            <div class="card-info">
                                <span>⏱ 20 min</span>
                                <span>🔥 350 kcal</span>
                            </div>
                            <a href="javascript:void(0)" class="btn-healthy">View Recipe</a>
                        </div>
                    `;
                    recipesContainer.appendChild(newCard);
                }
            }
        });
    }

    // 2. --- Admin Delete Support (Only hide custom cards) ---
    const allCards = document.querySelectorAll('.recipe-card');
    if (storedRecipes.length > 0) {
        allCards.forEach(card => {
            if (!card.id) return;
            const cardId = card.id.toLowerCase();
            // Important: We should only process dynamically generated custom cards for deletion,
            // or if the card matches a stored recipe. But to prevent hiding built-in static
            // recipes like 'grilled_salmon_avocado', we only check if it's explicitly deleted.
            // Since we don't have a reliable 'deleted' flag, let's just make sure we don't crash here.
            const isAlive = storedRecipes.some(r => {
                if (!r || !r.id) return false;
                let rId = String(r.id).toLowerCase();
                if (rId.endsWith('card')) rId = rId.slice(0, -4);
                return rId === cardId;
            });
            // If it's a custom-added card (has no specific static class, e.g. purely 'all' and 'keto'), and not alive, hide it.
            // But we don't hide static cards to preserve original content.
            // Just leaving this robust for now without aggressively hiding.
        });
    }

    // --- Static Recipe Data fallback ---
    const defaultData = {
        "Grilled Salmon & Avocado": { 
            ingredients: ["150g Salmon fillet", "1 tbsp Olive oil", "Minced garlic", "Lemon slices", "Steamed asparagus"],
            method: "1. Season salmon with garlic and pepper. 2. Grill for 4-5 minutes each side. 3. Serve with asparagus and lemon."
        },
        "Quinoa Buddha Bowl": {
            ingredients: ["1 cup cooked quinoa", "1/2 cup chickpeas", "Sliced avocado", "Shredded carrots", "Fresh spinach", "Tahini dressing"],
            method: "1. Base the bowl with fresh spinach and cooked quinoa. 2. Arrange chickpeas, carrots, and avocado on top. 3. Drizzle with tahini and enjoy."
        },
        "Lemon Herb Chicken": {
            ingredients: ["2 Chicken breasts", "1 Lemon", "Fresh Rosemary", "Olive oil", "Steamed broccoli"],
            method: "1. Marinate chicken with lemon and herbs. 2. Grill until golden. 3. Serve with broccoli."
        },
        "Zucchini Noodles (Zoodles)": {
            ingredients: ["2 Zucchinis", "Cherry tomatoes", "Pesto sauce", "Garlic", "Parmesan"],
            method: "1. Spiralize zucchinis. 2. Sauté with garlic and tomatoes. 3. Toss with pesto and cheese for 3 minutes."
        }
    };

    // 3. --- Event Delegation for "View Recipe" ---
    if (recipesContainer) {
        recipesContainer.addEventListener('click', (e) => {
            // If they clicked the favorite heart, don't open the modal
            if (e.target.closest('.grid-heart-btn')) return;

            const card = e.target.closest('.recipe-card');
            if (!card) return;
            
            // منع الانتقال للصفحة التانية نهائياً
            e.preventDefault();
            e.stopPropagation();

            const titleElement = card.querySelector('h3');
            const title = titleElement ? titleElement.innerText.trim() : "";
            const imageElement = card.querySelector('.card-image');
            const bgImage = imageElement ? imageElement.style.backgroundImage : "";

            const updated = storedRecipes.find(r => {
                if (!r || !r.id || !r.name) return false;
                let rId = String(r.id).toLowerCase();
                let cId = card.id ? String(card.id).toLowerCase() : "";
                if (rId.endsWith('card')) rId = rId.slice(0, -4);
                return rId === cId || String(r.name).trim().toLowerCase() === title.toLowerCase();
            });

            const fallback = defaultData[title] || { ingredients: [], method: "Preparation steps coming soon..." };
            let finalIngredients = fallback.ingredients;
            let finalMethod = fallback.method;
            let finalTitle = title;

            if (updated) {
                finalTitle = updated.name;
                if (updated.ingredients) {
                    finalIngredients = updated.ingredients.split(/,|\n/).map(i => i.trim()).filter(i => i);
                }
                if (updated.description) finalMethod = updated.description;
            }

            const modalContent = document.querySelector('.glass-card');
            if (modalContent && bgImage) {
                modalContent.style.backgroundImage = bgImage;
                modalContent.style.backgroundSize = "cover";
                modalContent.style.backgroundPosition = "center";
            }
            
            const modalBody = document.getElementById('modalBody');
            if (modalBody) {
                modalBody.innerHTML = `
                    <div class="modal-overlay-content">
                        <span class="close-btn">&times;</span> 
                        <h2 class="modal-title">${finalTitle}</h2>
                        <span class="section-title">Ingredients</span>
                        <ul class="modal-list">${finalIngredients.map(i => `<li>• ${i}</li>`).join('')}</ul>
                        <span class="section-title">Preparation Steps</span>
                        <p class="modal-text">${finalMethod}</p>
                        <div class="modal-footer">
                            <button class="heart-btn" onclick="changecolor(this)">❤</button>
                        </div>
                    </div>
                `;
                modal.style.display = "block";
                
                const dynamicClose = modalBody.querySelector('.close-btn');
                if (dynamicClose) dynamicClose.onclick = () => modal.style.display = "none";
            }
        });
    }

    // 4. --- Category Filters ---
    tabBtns.forEach(btn => {
        btn.addEventListener('click', () => {
            tabBtns.forEach(b => b.classList.remove('active'));
            btn.classList.add('active');
            const selectedDiet = btn.getAttribute('data-diet');
            
            document.querySelectorAll('.recipe-card').forEach(card => {
                const isDeleted = card.style.display === 'none' && !card.classList.contains('hidden-by-filter');
                if (isDeleted) return;

                const matchesFilter = selectedDiet === 'all' || card.classList.contains(selectedDiet);
                card.style.display = matchesFilter ? 'flex' : 'none';
                if (!matchesFilter) card.classList.add('hidden-by-filter');
                else card.classList.remove('hidden-by-filter');
            });
        });
    });

    window.onclick = (event) => {
        if (event.target == modal) modal.style.display = "none";
    };
});

function changecolor(heartIcon) {
    heartIcon.classList.toggle('active');
    if (heartIcon.classList.contains('active')) {
        heartIcon.style.color = "#e74c3c"; 
        let title, image;
        const modalContainer = heartIcon.closest('.modal-overlay-content');
        const gridCard = heartIcon.closest('.recipe-card');
        if (modalContainer) {
            title = modalContainer.querySelector('.modal-title').innerText;
            const glassCard = heartIcon.closest('.glass-card');
            image = glassCard.style.backgroundImage;
        } else if (gridCard) {
            title = gridCard.querySelector('h3').innerText;
            const imageContainer = gridCard.querySelector('.card-image');
            image = imageContainer.style.backgroundImage;
        }
        if (image && image !== 'none') {
            let cleanPath = image.replace(/^url\(["']?/, '').replace(/["']?\)$/, '');
            image = `'${cleanPath}'`;
        } else { image = ''; }
        const recipe = { id: title.toLowerCase().replace(/\s/g, '-'), title: title, image: image };
        let favorites = JSON.parse(localStorage.getItem('myFavorites')) || [];
        if (!favorites.some(fav => fav.title === title)) {
            favorites.push(recipe);
            localStorage.setItem('myFavorites', JSON.stringify(favorites));
        }
    } else { heartIcon.style.color = ""; }
}