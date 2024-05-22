particlesJS.load('particles', 'static/particles.json', function() {
    console.log('callback - particles.js config loaded');
});

const next = document.querySelector(".next");
const hotEdge = document.querySelector('.hot-edge');
const wrapper = document.querySelector('section.wrapper');
const emptySection = document.querySelector('section.empty');

let open = false;

next.onclick = e => {
    document.querySelector('.wrapper').scrollIntoView({ behavior: 'smooth' });
    open = true;
};

hotEdge.addEventListener('mouseenter', function() {
    if (!open) return;
    wrapper.style.transform = 'translateY(20px)';
});

hotEdge.addEventListener('mouseleave', function() {
    if (!open) return;
    wrapper.style.transform = 'translateY(0)';
});

hotEdge.addEventListener('click', function() {
    if (!open) return;
    emptySection.scrollIntoView({ behavior: 'smooth' });
    open=false;
    setTimeout(() => {
        wrapper.style.transform = 'translateY(0)';
    }, 200);
});


document.querySelectorAll('.link').forEach(link => {
    link.addEventListener('click', function() {
        document.querySelectorAll('.link').forEach(link => link.classList.remove('fullscreen'));
        this.classList.add('fullscreen');
        this.classList.remove('nonfullscreen-link');
        setTimeout(() => {
            this.style.fontSize = 0;
            setTimeout(() => {
                window.location.replace(this.dataset.href);
            }, 200);
        }, 1300);
    });
})
