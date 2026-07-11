import re

html_path = 'gowwee-landing.html'
with open(html_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Let's see if the counter logic is exactly as I expect.
# We will just write a small test html file.
html_test = '''
<html>
<body>
    <div class="counter" data-target="4.9" data-decimals="1" data-suffix="/5">0.0/5</div>
    <div class="counter" data-target="10" data-decimals="0" data-suffix="RB+">0RB+</div>
    <div class="counter" data-target="21" data-decimals="0" data-suffix="">0</div>
    <script>
        function animateCounter(el) {
            const target = parseFloat(el.dataset.target);
            const decimals = parseInt(el.dataset.decimals || '0', 10);
            const suffix = el.dataset.suffix || '';
            const duration = 1800;
            const startTime = performance.now();
            function step(now) {
                const progress = Math.min((now - startTime) / duration, 1);
                const eased = 1 - Math.pow(1 - progress, 3);
                const current = target * eased;
                el.textContent = current.toFixed(decimals) + suffix;
                if (progress < 1) {
                    requestAnimationFrame(step);
                } else {
                    el.textContent = target.toFixed(decimals) + suffix;
                }
            }
            requestAnimationFrame(step);
        }
        document.querySelectorAll('.counter').forEach(animateCounter);
    </script>
</body>
</html>
'''
with open('test_counter.html', 'w', encoding='utf-8') as f:
    f.write(html_test)
print("Test file created")
