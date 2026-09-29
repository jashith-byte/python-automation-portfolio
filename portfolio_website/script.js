document.addEventListener("DOMContentLoaded", () => {

    // =========================
    // NAVBAR SCROLL EFFECT
    // =========================

    const navbar = document.querySelector(".navbar");

    window.addEventListener("scroll", () => {

        if (window.scrollY > 40) {

            navbar.style.background =
                "rgba(7, 11, 20, 0.96)";

        } else {

            navbar.style.background =
                "rgba(7, 11, 20, 0.85)";
        }

    });


    // =========================
    // REVEAL ANIMATION
    // =========================

    const revealElements =
        document.querySelectorAll(
            ".service-card, .project-card, .about-content, .tech-stack"
        );


    const observer = new IntersectionObserver(
        (entries) => {

            entries.forEach((entry) => {

                if (entry.isIntersecting) {

                    entry.target.classList.add("visible");

                    observer.unobserve(entry.target);

                }

            });

        },
        {
            threshold: 0.12
        }
    );


    revealElements.forEach((element) => {

        element.classList.add("reveal");

        observer.observe(element);

    });


    // =========================
    // CURRENT YEAR
    // =========================

    const footer =
        document.querySelector("footer p");

    if (footer) {

        const currentYear =
            new Date().getFullYear();

        footer.textContent =
            `© ${currentYear} Y Jashith. Built with HTML, CSS & JavaScript.`;

    }

});