 document.addEventListener('DOMContentLoaded', function() {
        // Animasi scroll halus untuk semua link
        document.querySelectorAll('a[href^="#"]').forEach(anchor => {
            anchor.addEventListener('click', function(e) {
                e.preventDefault();
                document.querySelector(this.getAttribute('href')).scrollIntoView({
                    behavior: 'smooth'
                });
            });
        });

        // Animasi saat elemen muncul di viewport
        const animateOnScroll = function() {
            const elements = document.querySelectorAll('.diabetes-card, .tip-card, .myth-fact-item, .conclusion');
            
            elements.forEach(element => {
                const elementPosition = element.getBoundingClientRect().top;
                const screenPosition = window.innerHeight / 1.2;
                
                if (elementPosition < screenPosition) {
                    element.style.opacity = '1';
                    element.style.transform = 'translateY(0)';
                }
            });
        };

        // Set initial styles for animated elements
        const animatedElements = document.querySelectorAll('.diabetes-card, .tip-card, .myth-fact-item, .conclusion');
        animatedElements.forEach(element => {
            element.style.opacity = '0';
            element.style.transform = 'translateY(30px)';
            element.style.transition = 'all 0.6s ease-out';
        });

        // Run animation on scroll
        window.addEventListener('scroll', animateOnScroll);
        animateOnScroll(); // Run once on load

        // Animasi hover untuk tombol CTA
        const ctaButton = document.querySelector('.cta-button');
        if (ctaButton) {
            ctaButton.addEventListener('mouseenter', function() {
                this.style.transform = 'translateY(-3px) scale(1.05)';
            });
            ctaButton.addEventListener('mouseleave', function() {
                this.style.transform = 'translateY(0) scale(1)';
            });
        }

        // Animasi untuk header saat di-scroll
        const articleHeader = document.querySelector('.article-header');
        window.addEventListener('scroll', function() {
            if (window.scrollY > 100) {
                articleHeader.style.transform = 'translateY(-10px)';
                articleHeader.style.opacity = '0.9';
            } else {
                articleHeader.style.transform = 'translateY(0)';
                articleHeader.style.opacity = '1';
            }
        });

        // Animasi untuk gambar utama saat muncul
        const featuredImage = document.querySelector('.featured-image');
        if (featuredImage) {
            featuredImage.style.opacity = '0';
            featuredImage.style.transform = 'scale(0.95)';
            featuredImage.style.transition = 'all 0.8s ease-out';
            
            setTimeout(() => {
                featuredImage.style.opacity = '1';
                featuredImage.style.transform = 'scale(1)';
            }, 300);
        }

        // Animasi teks intro
        const intro = document.querySelector('.intro');
        if (intro) {
            intro.style.opacity = '0';
            intro.style.transform = 'translateX(-20px)';
            intro.style.transition = 'all 0.6s ease-out';
            
            setTimeout(() => {
                intro.style.opacity = '1';
                intro.style.transform = 'translateX(0)';
            }, 600);
        }

        // Animasi untuk share buttons
        const shareButtons = document.querySelectorAll('.share-button');
        shareButtons.forEach((button, index) => {
            button.style.transform = 'scale(0)';
            button.style.transition = `all 0.3s ease-out ${index * 0.1}s`;
            
            setTimeout(() => {
                button.style.transform = 'scale(1)';
            }, 1000 + (index * 100));
        });
    });

    // Animasi untuk judul bagian saat di-scroll
    const headings = document.querySelectorAll('h2, h3');
    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.style.animation = 'fadeInUp 0.6s ease-out forwards';
            }
        });
    }, { threshold: 0.1 });

    headings.forEach(heading => {
        heading.style.opacity = '0';
        heading.style.transform = 'translateY(20px)';
        observer.observe(heading);
    });

    // Tambahkan style untuk keyframes animation
    const style = document.createElement('style');
    style.textContent = `
        @keyframes fadeInUp {
            from {
                opacity: 0;
                transform: translateY(20px);
            }
            to {
                opacity: 1;
                transform: translateY(0);
            }
        }
    `;
    document.head.appendChild(style);