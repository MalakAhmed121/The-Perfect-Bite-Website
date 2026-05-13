
document.addEventListener("DOMContentLoaded", () => {
    const sideMenu = document.getElementById("side-menu");
    const menuIcon = document.querySelector(".menu-icon");

    if (menuIcon && sideMenu) {
        menuIcon.addEventListener("click", (e) => {
            e.stopPropagation();
            sideMenu.classList.toggle("show");
        });

        document.addEventListener("click", (e) => {
            if (!sideMenu.contains(e.target) && !menuIcon.contains(e.target)) {
                sideMenu.classList.remove("show");
            }
        });
    }
});
