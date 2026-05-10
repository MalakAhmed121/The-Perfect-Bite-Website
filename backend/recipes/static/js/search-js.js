function searchRecipes(type) {
    let query = document.getElementById("searchInput").value;

    console.log("Searching:", query, "Type:", type);

    fetch(`/ajax-search/?q=${encodeURIComponent(query)}&type=${encodeURIComponent(type)}`)
        .then(res => res.json())
        .then(data => {
            console.log("Response:", data);

            let container = document.getElementById("results");
            container.innerHTML = "";

            if (!data.results || data.results.length === 0) {
                container.innerHTML = `<p class="no-results">No recipes found</p>`;
                return;
            }

            data.results.forEach(recipe => {
                container.innerHTML += `
                    <div class="recipe"
                        style="background-image:url('${recipe.image}')">

                        <h2>${recipe.title}</h2>
                        <p>${(recipe.description || "").slice(0, 80)}...</p>

                        <a class="btn-main" href="/recipe/${recipe.slug}/">
                            View Recipe
                        </a>
                    </div>
                `;
            });
        })
        .catch(err => console.error("Fetch error:", err));
}