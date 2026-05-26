const menuToggle = document.querySelector('.menu-toggle');
const siteNav = document.querySelector('.site-nav, .subpage-nav');
const navLinks = siteNav ? siteNav.querySelectorAll('a') : [];
const currentYear = document.getElementById('currentYear');

if (currentYear) {
    currentYear.textContent = new Date().getFullYear();
}

if (menuToggle && siteNav) {
    menuToggle.addEventListener('click', () => {
        const isOpen = siteNav.classList.toggle('is-open');
        menuToggle.setAttribute('aria-expanded', String(isOpen));
    });
}

navLinks.forEach((link) => {
    link.addEventListener('click', () => {
        if (siteNav) {
            siteNav.classList.remove('is-open');
        }
        if (menuToggle) {
            menuToggle.setAttribute('aria-expanded', 'false');
        }
    });
});

const sections = siteNav && siteNav.classList.contains('site-nav')
    ? [...document.querySelectorAll('main section[id]')]
    : [];
const setActiveLink = () => {
    if (!sections.length) {
        return;
    }

    const scrollPosition = window.scrollY + 120;

    sections.forEach((section) => {
        const start = section.offsetTop;
        const end = start + section.offsetHeight;
        const link = document.querySelector(`.site-nav a[href="#${section.id}"]`);

        if (!link) return;

        if (scrollPosition >= start && scrollPosition < end) {
            navLinks.forEach((navLink) => navLink.classList.remove('is-active'));
            link.classList.add('is-active');
        }
    });
};

window.addEventListener('scroll', setActiveLink);
window.addEventListener('load', setActiveLink);
