// --- Page Initialization ---
document.addEventListener('DOMContentLoaded', () => {
    const tabBtns = document.querySelectorAll('.tab-btn');
    const recipesContainer = document.getElementById('recipes-container');
    const modal = document.getElementById('recipeModal');

    // 1. --- Category Filters (التحكم في ظهور الكروت بناءً على نوع الدايت) ---
    tabBtns.forEach(btn => {
        btn.addEventListener('click', () => {
            // تغيير شكل الزرار النشط
            tabBtns.forEach(b => b.classList.remove('active'));
            btn.classList.add('active');

            const selectedDiet = btn.getAttribute('data-diet');
            
            // الفلترة بتحصل هنا بناءً على الـ Class اللي جاي من Django
            document.querySelectorAll('.recipe-card').forEach(card => {
                if (selectedDiet === 'all' || card.classList.contains(selectedDiet)) {
                    card.style.display = 'flex';
                } else {
                    card.style.display = 'none';
                }
            });
        });
    });

    // 2. --- Close Modal Logic (قفل النافذة) ---
    window.onclick = (event) => {
        if (event.target == modal) {
            modal.style.display = "none";
        }
    };
});

// 3. --- AJAX Function: Fetch Recipe Details ---
// دي الدالة اللي بتجيب البيانات من السيرفر بدون تحميل الصفحة
function openRecipeModal(recipeId) {
    const modal = document.getElementById('recipeModal');
    const modalBody = document.getElementById('modalBody');

    // بننادي على الرابط اللي عملناه في urls.py[cite: 3]
    fetch(`/recipe-api/${recipeId}/`)
        .then(response => {
            if (!response.ok) throw new Error('Recipe not found');
            return response.json();
        })
        .then(data => {
            // بنحقن البيانات الحقيقية جوه الـ HTML[cite: 11, 12]
            modalBody.innerHTML = `
                <div class="modal-overlay-content">
                    <span class="close-btn" onclick="closeModal()">&times;</span> 
                    <h2 class="modal-title">${data.title}</h2>
                    
                    <span class="section-title">Ingredients</span>
                    <ul class="modal-list">
                        ${data.ingredients.map(i => `<li>• ${i.trim()}</li>`).join('')}
                    </ul>
                    
                    <span class="section-title">Preparation Steps</span>
                    <p class="modal-text">${data.method}</p>
                    
                    <div class="modal-footer">
                        <div class="stats">
                            <span>🔥 ${data.calories} kcal</span>
                            <span>⏱ ${data.prep_time} min</span>
                        </div>
                        <button class="heart-btn" onclick="changecolor(this, '${data.title}')">❤</button>
                    </div>
                </div>
            `;
            
            // تغيير خلفية الـ Modal لصورة الوجبة[cite: 11]
            const modalContent = document.querySelector('.glass-card');
            if (modalContent) {
                modalContent.style.backgroundImage = `url('${data.image_url}')`;
                modalContent.style.backgroundSize = "cover";
                modalContent.style.backgroundPosition = "center";
            }

            modal.style.display = "block";
        })
        .catch(err => console.error("Error fetching recipe:", err));
}

function closeModal() {
    document.getElementById('recipeModal').style.display = "none";
}

// 4. --- Favorites Logic (القلب الأحمر) ---
function changecolor(heartIcon, recipeTitle) {
    heartIcon.classList.toggle('active');
    
    if (heartIcon.classList.contains('active')) {
        heartIcon.style.color = "#e74c3c"; 
        // ممكن لاحقاً نربط دي بـ Backend لحفظ المفضلة
        console.log("Added to favorites:", recipeTitle);
    } else {
        heartIcon.style.color = "";
    }
}