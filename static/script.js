window.confetti = function () {
    // Add minimalist confetti effect (example only)
    let duration = 1100;
    let end = Date.now() + duration;
    (function frame() {
        // Insert your preferred confetti library or simple effect here
        if (Date.now() < end) { requestAnimationFrame(frame); }
    })();
};
