import os
import re

html_path = r"d:\web_course\The-Perfect-Bite-Website\backend\recipes\templates\recipes\index.html"
css_path = r"d:\web_course\The-Perfect-Bite-Website\backend\recipes\static\css\style.css"

with open(html_path, 'r', encoding='utf-8') as f:
    html_content = f.read()

# Replace the <main> and <section> with the new layout
new_body = """
    <main class="new-hero-section" style="background-image: url('{% static 'home-page.png' %}');">
        <div class="hero-content">
            <h1 class="hungry-title" style="font-size: 4.5rem; text-transform: uppercase; font-weight: 800; letter-spacing: 2px;">SHARPEN YOUR<br>KNIVES.</h1>
            <p class="hero-subtext" style="font-size: 1.3rem; margin-top: 20px; font-weight: 500;">Turn simple ingredients into pure magic, because every<br>great story starts with a sizzle.</p>
            <a href="{% url 'search' %}" class="btn-hero-pill" style="margin-top: 30px;">Explore Masterpieces</a>
        </div>
    </main>

    <div class="overlapping-cards-wrapper">
        <div class="overlapping-cards-container">
            <div class="feature-card" onclick="location.href='{% url 'recipes' %}'">
                <div class="icon-circle">
                    <svg width="28" height="28" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M12 2v20M17 5H9.5a3.5 3.5 0 0 0 0 7h5a3.5 3.5 0 0 1 0 7H6"/></svg>
                </div>
                <h3>Recipes</h3>
                <p>Discover the recipes that are breaking the internet this week.</p>
            </div>
            <div class="feature-card" onclick="location.href='{% url 'search' %}'">
                <div class="icon-circle">
                    <svg width="28" height="28" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="11" cy="11" r="8"/><path d="m21 21-4.3-4.3"/></svg>
                </div>
                <h3>Search</h3>
                <p>Gourmet meals ready in under 15 minutes for your busy nights.</p>
            </div>
            <div class="feature-card" onclick="location.href='{% url 'favorites' %}'">
                <div class="icon-circle">
                    <svg width="28" height="28" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M19 14c1.49-1.46 3-3.21 3-5.5A5.5 5.5 0 0 0 16.5 3c-1.76 0-3 .5-4.5 2-1.5-1.5-2.74-2-4.5-2A5.5 5.5 0 0 0 2 8.5c0 2.3 1.5 4.05 3 5.5l7 7Z"/></svg>
                </div>
                <h3>Favorites</h3>
                <p>Feeling cozy or adventurous? Find the perfect dish for your vibe.</p>
            </div>
        </div>
    </div>

    <section class="vibe-section">
        <div class="vibe-filter">
            <span class="vibe-label" style="font-weight: bold; color: var(--text-main);">What's Your Vibe?</span>
            <span class="vibe-separator">|</span>
            <a href="{% url 'main_dish' %}" class="vibe-link">Main Dishes</a>
            <span class="vibe-separator">|</span>
            <a href="{% url 'healthy' %}" class="vibe-link">Healthy Food</a>
            <span class="vibe-separator">|</span>
            <a href="{% url 'bakery' %}" class="vibe-link">Bakery</a>
            <span class="vibe-separator">|</span>
            <a href="{% url 'dessert' %}" class="vibe-link">Desserts</a>
            <span class="vibe-separator">|</span>
            <a href="{% url 'juices' %}" class="vibe-link">Juices</a>
            <span class="vibe-separator">|</span>
            <a href="{% url 'appetizers' %}" class="vibe-link">Appetizers</a>
        </div>

        <div class="bento-grid">
            <div class="bento-card tall" style="background-image: url('{% static 'maindish/main.jpg' %}');" onclick="location.href='{% url 'main_dish' %}'">
                <div class="bento-overlay"></div>
                <div class="bento-content">
                    <h3>Main Dishes</h3>
                    <button class="bento-btn">View Recipes</button>
                </div>
            </div>
            
            <div class="bento-card" style="background-image: url('{% static 'Healthy_images/healthy-food.jpg' %}');" onclick="location.href='{% url 'healthy' %}'">
                <div class="bento-overlay"></div>
                <div class="bento-content">
                    <h3>Healthy Food</h3>
                    <button class="bento-btn">View Recipes</button>
                </div>
            </div>
            
            <div class="bento-card tall" style="background-image: url('{% static 'bakeryimages/bakery12.png' %}');" onclick="location.href='{% url 'bakery' %}'">
                <div class="bento-overlay"></div>
                <div class="bento-content">
                    <h3>Bakery</h3>
                    <button class="bento-btn">View Recipes</button>
                </div>
            </div>
            
            <div class="bento-card" style="background-image: url('{% static 'dessertimages/background.jpg' %}');" onclick="location.href='{% url 'dessert' %}'">
                <div class="bento-overlay"></div>
                <div class="bento-content">
                    <h3>Desserts</h3>
                    <button class="bento-btn">View Recipes</button>
                </div>
            </div>

            <div class="bento-card" style="background-image: url('{% static 'juicesimg/juicesbg.jpeg' %}');" onclick="location.href='{% url 'juices' %}'">
                <div class="bento-overlay"></div>
                <div class="bento-content">
                    <h3>Juices</h3>
                    <button class="bento-btn">View Recipes</button>
                </div>
            </div>

            <div class="bento-card" style="background-image: url('{% static 'appetizersimgs/main1.jpg' %}');" onclick="location.href='{% url 'appetizers' %}'">
                <div class="bento-overlay"></div>
                <div class="bento-content">
                    <h3>Appetizers</h3>
                    <button class="bento-btn">View Recipes</button>
                </div>
            </div>
        </div>
    </section>
"""

# Extract the navbar and scripts
nav_start = html_content.find('<div id="navbar">')
nav_end = html_content.find('</div>', html_content.find('</nav>')) + 6
scripts_start = html_content.rfind('<script')

if nav_start != -1 and nav_end != -1 and scripts_start != -1:
    header_part = html_content[:nav_end]
    footer_part = html_content[scripts_start:]
    final_html = header_part + new_body + footer_part
    with open(html_path, 'w', encoding='utf-8') as f:
        f.write(final_html)

new_css = """

/* ============================================================
   NEW HOMEPAGE DESIGN
   ============================================================ */

.new-hero-section {
    min-height: 85vh;
    background-size: cover;
    background-position: center;
    background-attachment: fixed;
    display: flex;
    justify-content: center;
    align-items: center;
    text-align: center;
    color: white;
    position: relative;
    padding-bottom: 80px; /* Space for overlapping cards */
}

.new-hero-section::before {
    content: '';
    position: absolute;
    inset: 0;
    background: linear-gradient(to bottom, rgba(0,0,0,0.3) 0%, rgba(0,0,0,0.1) 100%);
}

.hero-content {
    position: relative;
    z-index: 2;
    max-width: 800px;
    padding: 0 20px;
}

.btn-hero-pill {
    display: inline-block;
    background-color: rgba(169, 143, 111, 0.85); /* Brownish pill */
    backdrop-filter: blur(5px);
    color: white;
    padding: 15px 40px;
    border-radius: 50px;
    font-size: 1.1rem;
    font-weight: 600;
    text-decoration: none;
    transition: all 0.3s ease;
    border: 1px solid rgba(255, 255, 255, 0.3);
}

.btn-hero-pill:hover {
    transform: translateY(-3px);
    background-color: rgba(169, 143, 111, 1);
    box-shadow: 0 10px 20px rgba(0,0,0,0.2);
    color: white;
}

/* Feature Cards Overlapping */
.overlapping-cards-wrapper {
    max-width: 1200px;
    margin: -80px auto 40px auto;
    position: relative;
    z-index: 10;
    padding: 0 20px;
}

.overlapping-cards-container {
    display: flex;
    justify-content: space-between;
    gap: 20px;
}

.feature-card {
    background: white;
    border-radius: 20px;
    padding: 40px 30px;
    flex: 1;
    text-align: center;
    box-shadow: 0 15px 35px rgba(0,0,0,0.05);
    cursor: pointer;
    transition: transform 0.3s ease, box-shadow 0.3s ease;
}

.feature-card:hover {
    transform: translateY(-10px);
    box-shadow: 0 20px 40px rgba(0,0,0,0.1);
}

.icon-circle {
    width: 60px;
    height: 60px;
    margin: 0 auto 20px auto;
    color: var(--text-main);
    display: flex;
    justify-content: center;
    align-items: center;
}

.feature-card h3 {
    color: var(--text-main);
    font-size: 1.4rem;
    margin-bottom: 15px;
    font-weight: bold;
}

.feature-card p {
    color: var(--text-muted);
    font-size: 1rem;
    line-height: 1.5;
}

/* Vibe Section */
.vibe-section {
    max-width: 1200px;
    margin: 60px auto;
    padding: 0 20px;
}

.vibe-filter {
    text-align: center;
    margin-bottom: 40px;
    font-size: 1.1rem;
}

.vibe-link {
    color: var(--text-muted);
    text-decoration: none;
    margin: 0 10px;
    transition: color 0.3s ease;
}

.vibe-link:hover {
    color: var(--text-main);
}

.vibe-separator {
    color: #ccc;
    margin: 0 5px;
}

/* Bento Grid */
.bento-grid {
    display: grid;
    grid-template-columns: repeat(4, 1fr);
    grid-template-rows: repeat(2, 250px);
    gap: 20px;
}

.bento-card {
    position: relative;
    border-radius: 25px;
    overflow: hidden;
    background-size: cover;
    background-position: center;
    cursor: pointer;
    box-shadow: 0 10px 20px rgba(0,0,0,0.1);
    transition: transform 0.3s ease, box-shadow 0.3s ease;
}

.bento-card:hover {
    transform: translateY(-5px);
    box-shadow: 0 15px 30px rgba(0,0,0,0.2);
}

.bento-card:hover .bento-overlay {
    background: linear-gradient(to top, rgba(0,0,0,0.9), rgba(0,0,0,0.2));
}

.bento-overlay {
    position: absolute;
    inset: 0;
    background: linear-gradient(to top, rgba(0,0,0,0.7), rgba(0,0,0,0.1));
    transition: background 0.3s ease;
}

.bento-content {
    position: absolute;
    bottom: 30px;
    left: 0;
    right: 0;
    text-align: center;
    z-index: 2;
    padding: 0 15px;
}

.bento-content h3 {
    color: white;
    font-size: 1.6rem;
    margin-bottom: 15px;
    text-shadow: 0 2px 5px rgba(0,0,0,0.5);
    font-weight: 600;
}

.bento-btn {
    background-color: rgba(169, 143, 111, 0.7);
    backdrop-filter: blur(5px);
    color: white;
    border: none;
    padding: 10px 25px;
    border-radius: 50px;
    font-size: 1rem;
    font-weight: 500;
    cursor: pointer;
    transition: all 0.3s ease;
}

.bento-btn:hover {
    background-color: white;
    color: #4b1f11;
}

.bento-card.tall {
    grid-row: span 2;
}

@media (max-width: 900px) {
    .overlapping-cards-container {
        flex-direction: column;
    }
    .overlapping-cards-wrapper {
        margin-top: -40px;
    }
    .bento-grid {
        grid-template-columns: repeat(2, 1fr);
        grid-template-rows: auto;
    }
    .bento-card.tall {
        grid-row: span 1;
        height: 250px;
    }
    .bento-card {
        height: 250px;
    }
    .vibe-filter {
        line-height: 2;
    }
}
@media (max-width: 600px) {
    .bento-grid {
        grid-template-columns: 1fr;
    }
    .new-hero-section h1 {
        font-size: 3rem !important;
    }
}
"""

with open(css_path, 'a', encoding='utf-8') as f:
    f.write(new_css)

print("Updated HTML and CSS.")
