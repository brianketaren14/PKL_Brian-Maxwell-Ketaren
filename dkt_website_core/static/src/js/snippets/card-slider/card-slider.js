class CardSlider {
    constructor(containerId, cardClass) {
        this.sliderContainer = document.getElementById(containerId);
        this.slider = this.sliderContainer.querySelector('.slider');
        this.prevBtn = this.sliderContainer.querySelector('.prev-btn');
        this.nextBtn = this.sliderContainer.querySelector('.next-btn');
        this.cardWidth = this.sliderContainer.querySelector(`.${cardClass}`).offsetWidth + 15; // Card width + gap
        this.autoSlideInterval = null;
        this.isHovered = false;
        this.isSwiping = false;
        this.startX = 0;
        this.endX = 0;
        this.numCards = this.sliderContainer.querySelectorAll(`.${cardClass}`).length;
        this.init();
    }

    init() {
        this.startAutoSlide();
        this.prevBtn.addEventListener('click', () => this.handlePrev());
        this.nextBtn.addEventListener('click', () => this.handleNext());

        this.sliderContainer.addEventListener('mouseenter', () => this.handleMouseEnter());
        this.sliderContainer.addEventListener('mouseleave', () => this.handleMouseLeave());

        this.sliderContainer.addEventListener('mousedown', (e) => this.handleTouchStart(e));
        this.sliderContainer.addEventListener('mouseup', () => this.handleTouchEnd());
        this.sliderContainer.addEventListener('mousemove', (e) => this.handleTouchMove(e));

        this.sliderContainer.addEventListener('touchstart', (e) => this.handleTouchStart(e));
        this.sliderContainer.addEventListener('touchend', () => this.handleTouchEnd());
        this.sliderContainer.addEventListener('touchmove', (e) => this.handleTouchMove(e));
    }

    moveNext() {
        this.slider.style.transition = "transform 0.3s ease-in-out";
        this.slider.style.transform = `translateX(-${this.cardWidth}px)`;

        setTimeout(() => {
            this.slider.style.transition = "none";
            this.slider.appendChild(this.slider.firstElementChild);
            this.slider.style.transform = "translateX(0)";
        }, 300);
    }

    movePrev() {
        this.slider.style.transition = "none";
        this.slider.prepend(this.slider.lastElementChild);
        this.slider.style.transform = `translateX(-${this.cardWidth}px)`;

        setTimeout(() => {
            this.slider.style.transition = "transform 0.3s ease-in-out";
            this.slider.style.transform = "translateX(0)";
        }, 10);
    }

    startAutoSlide() {
        if (!this.isHovered && !this.isSwiping) {
            this.autoSlideInterval = setInterval(() => this.moveNext(), 3000);
        }
    }

    stopAutoSlide() {
        clearInterval(this.autoSlideInterval);
    }

    handleNext() {
        this.stopAutoSlide();
        this.moveNext();
        this.startAutoSlide();
    }

    handlePrev() {
        this.stopAutoSlide();
        this.movePrev();
        this.startAutoSlide();
    }

    handleMouseEnter() {
        this.isHovered = true;
        this.stopAutoSlide();
        this.prevBtn.style.display = 'block';
        this.nextBtn.style.display = 'block';


    }

    handleMouseLeave() {
        this.isHovered = false;
        this.startAutoSlide();
        this.prevBtn.style.display = 'none';
        this.nextBtn.style.display = 'none';

    }

    handleTouchStart(e) {
        this.isSwiping = true;
        this.startX = e.clientX || e.touches[0].clientX;
        this.stopAutoSlide();
    }

    handleTouchEnd() {
        if (this.isSwiping) {
            this.isSwiping = false;
            this.startAutoSlide();
        }
    }

    handleTouchMove(e) {
        if (this.isSwiping) {
            this.endX = e.clientX || e.touches[0].clientX;
            if (this.startX - this.endX > 100) {
                this.moveNext();
                this.isSwiping = false;
                this.startAutoSlide();
            } else if (this.endX - this.startX > 100) {
                this.movePrev();
                this.isSwiping = false;
                this.startAutoSlide();
            }
        }
    }
}