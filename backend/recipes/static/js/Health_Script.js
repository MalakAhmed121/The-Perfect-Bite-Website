// ==========================================================================
// HEALTHY FOOD PAGE SCRIPT - FINAL COMPLETE VERSION
// ==========================================================================

// =========================
// PAGE INITIALIZATION
// =========================
document.addEventListener('DOMContentLoaded', () => {

    const tabBtns = document.querySelectorAll('.tab-btn');

    const modal = document.getElementById('recipeModal');

    // =========================================================
    // CATEGORY FILTERS
    // =========================================================
    tabBtns.forEach(btn => {

        btn.addEventListener('click', () => {

            // إزالة active من كل الأزرار
            tabBtns.forEach(b => b.classList.remove('active'));

            // إضافة active للزر الحالي
            btn.classList.add('active');

            const selectedDiet = btn.getAttribute('data-diet');

            // فلترة الكروت
            document.querySelectorAll('.recipe-card').forEach(card => {

                if (
                    selectedDiet === 'all' ||
                    card.classList.contains(selectedDiet)
                ) {

                    card.style.display = 'block';

                } else {

                    card.style.display = 'none';
                }
            });

        });

    });

    // =========================================================
    // CLOSE MODAL WHEN CLICKING OUTSIDE
    // =========================================================
    window.addEventListener('click', (event) => {

        if (event.target === modal) {

            closeModal();
        }
    });

});


// ==========================================================================
// OPEN RECIPE MODAL
// ==========================================================================
function openRecipeModal(recipeId) {

    const modal = document.getElementById('recipeModal');

    const modalBody = document.getElementById('modalBody');

    const modalContent = document.getElementById('recipeModalContent');

    // =========================================================
    // FETCH RECIPE DATA
    // =========================================================
    fetch(`/recipe-api/${recipeId}/`)

        .then(response => {

            if (!response.ok) {

                throw new Error('Recipe not found');
            }

            return response.json();
        })

        .then(data => {

            // =====================================================
            // INSERT MODAL CONTENT
            // =====================================================
            modalBody.innerHTML = `

                <div class="modal-overlay-content">

                    <!-- CLOSE BUTTON -->
                    <span
                        class="close-btn"
                        onclick="closeModal()"
                    >
                        &times;
                    </span>

                    <!-- TITLE -->
                    <h2 class="modal-title">
                        ${data.title}
                    </h2>

                    <!-- INGREDIENTS -->
                    <span class="section-title-modal">
                        Ingredients
                    </span>

                    <ul class="modal-list">

                        ${data.ingredients.map(item => `
                            <li>• ${item.trim()}</li>
                        `).join('')}

                    </ul>

                    <!-- PREPARATION -->
                    <span class="section-title-modal">
                        Preparation Steps
                    </span>

                    <p class="modal-text">
                        ${data.method}
                    </p>

                    <!-- FOOTER -->
                    <div class="modal-footer">

                        <div class="stats">

                            <span>
                                🔥 ${data.calories} kcal
                            </span>

                            |

                            <span>
                                ⏱ ${data.prep_time} min
                            </span>

                        </div>

                        <button
                            class="heart-btn ${data.is_favorite ? 'active' : ''}"
                            data-id="${data.id}"
                            onclick="changecolor(this, '${data.title}')"
                        >
                            ❤
                        </button>

                    </div>

                </div>
            `;

            // =====================================================
            // MODAL BACKGROUND IMAGE
            // =====================================================
            modalContent.style.backgroundImage = `
                linear-gradient(
                    rgba(255,255,255,0.90),
                    rgba(255,255,255,0.90)
                ),
                url('${data.image_url}')
            `;

            modalContent.style.backgroundSize = "cover";

            modalContent.style.backgroundPosition = "center";

            modalContent.style.backgroundRepeat = "no-repeat";

            // =====================================================
            // RESET SCROLL POSITION
            // =====================================================
            modalContent.scrollTop = 0;

            // =====================================================
            // SHOW MODAL
            // =====================================================
            modal.style.display = "flex";

            // =====================================================
            // PREVENT PAGE SCROLL
            // =====================================================
            document.body.style.overflow = "hidden";

        })

        .catch(error => {

            console.error("Error fetching recipe:", error);

            alert("Failed to load recipe details.");
        });

}


// ==========================================================================
// CLOSE MODAL
// ==========================================================================
function closeModal() {

    const modal = document.getElementById('recipeModal');

    modal.style.display = "none";

    // إعادة السكرول للصفحة
    document.body.style.overflow = "auto";
}


// Note: changecolor is now handled by bakery-java.js to avoid duplication
// and ensure AJAX favorites work across all pages.